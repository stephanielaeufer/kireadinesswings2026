"""Deterministische Beschreibung von GARI-DE-0.1. Python 3.10+, keine Pakete.

Aufruf: python auswertung/score.py beispiele/synthetische_antworten.json ergebnis.json
Kein Gesamtwert, keine Kompetenzgrenzen, keine automatische Maßnahmenentscheidung.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from statistics import mean

BANK = Path(__file__).resolve().parents[1] / 'instrument' / 'Itembank_GARI_DE_0.1.json'
# Codebuch-Revision 0.6: Erfassungsgrund für Werte, die nicht zur Skala oder zu den
# Optionen passen. Gilt für alle Items, ändert die eingefrorene Bank nicht.
CAPTURE_REASONS = ('UNGUELTIG_ERFASST',)

def fail(message):
    raise ValueError(message)

def evaluate(payload, bank=None):
    bank = bank or json.loads(BANK.read_text(encoding='utf-8'))
    if not isinstance(payload, dict):
        fail('Die Eingabe muss ein JSON-Objekt sein.')
    if payload.get('data_kind') not in {'PRETEST', 'SURVEY', 'SYNTHETIC_DEMO'}:
        fail('data_kind fehlt oder ist unzulässig.')
    if payload.get('questionnaire_version') != bank['version']:
        fail('Fragebogen- und Codebuchversion passen nicht zusammen.')
    records = payload.get('records')
    if not isinstance(records, list):
        fail('records muss eine Liste sein.')
    lookup = {i['item_id']: i for i in bank['items']}
    ids, person_scores = set(), []
    warnings = []
    for rec in records:
        if not isinstance(rec, dict):
            fail('Jeder Datensatz muss ein Objekt sein.')
        pid = rec.get('participant_id')
        if not isinstance(pid, str) or not pid.strip() or pid in ids:
            fail('Testkürzel fehlt oder kommt mehrfach vor.')
        ids.add(pid)
        if rec.get('questionnaire_version') != bank['version']:
            fail(f'{pid}: Abweichende oder fehlende Fragebogenversion.')
        answers = rec.get('answers')
        if not isinstance(answers, dict) or set(answers) != set(lookup):
            fail(f'{pid}: Item-IDs sind unvollständig oder enthalten unbekannte IDs.')
        for id, spec in lookup.items():
            a = answers[id]
            if not isinstance(a, dict) or set(a) != {'value', 'missing_reason'}:
                fail(f'{pid}/{id}: value und missing_reason erforderlich.')
            value, missing = a['value'], a['missing_reason']
            if value is None:
                if missing not in tuple(spec['missing_allowed']) + CAPTURE_REASONS:
                    fail(f'{pid}/{id}: Fehlwertgrund fehlt oder ist nicht zugelassen.')
                continue
            if missing is not None:
                fail(f'{pid}/{id}: Wert und Fehlwertgrund widersprechen sich.')
            if spec['type'] == 'integer':
                sc = bank['scales'][spec['scale_id']]
                if type(value) is not int or not sc['min'] <= value <= sc['max']:
                    fail(f'{pid}/{id}: Ungültiger Skalenwert.')
            elif spec['type'] == 'single':
                if not isinstance(value, str) or value not in dict(spec['options']):
                    fail(f'{pid}/{id}: Unbekannte Antwortkategorie.')
            elif spec['type'] == 'multi':
                if not isinstance(value, list) or not value or any(not isinstance(v, str) for v in value):
                    fail(f'{pid}/{id}: Mehrfachantwort als nichtleere Liste erforderlich.')
                if len(value) != len(set(value)) or len(value) > spec['max_selections']:
                    fail(f'{pid}/{id}: Doppelte oder zu viele Antworten.')
                if not set(value) <= set(dict(spec['options'])):
                    fail(f'{pid}/{id}: Unbekannte Antwortkategorie.')
                if set(value) & set(spec['exclusive_options']) and len(value) != 1:
                    fail(f'{pid}/{id}: Exklusive Antwort kombiniert.')
            elif spec['type'] == 'text':
                if not isinstance(value, str) or not value.strip():
                    fail(f'{pid}/{id}: Leeren Freitext als Fehlwert kodieren.')
        scores = {}
        for name, domain in bank['domains'].items():
            vals = [answers[id]['value'] for id in domain['items']]
            scores[name] = mean(vals) if all(v is not None for v in vals) else None
        person_scores.append({'participant_id': pid, 'scores': scores})
        # Nur ein Prüfhinweis; subjektive Erwartungen können diesen Fall erklären.
        intention = [answers[id]['value'] for id in bank['domains']['I']['items']]
        if answers['C04']['value'] == 'NO' and any(v is not None and v >= 6 for v in intention):
            warnings.append({'participant_id': pid, 'items': ['C04','I01','I02','I03'],
                             'message': 'Kein aktueller Zugang und Zustimmung 6 oder 7 zur künftigen Nutzung: erwartete Zugangsänderung prüfen; keine automatische Korrektur.',
                             'rule': 'Eigener Plausibilitätshinweis, keine Readiness-Grenze.'})
    summaries = {}
    for id, spec in lookup.items():
        answers = [r['answers'][id] for r in records]
        valid = [a['value'] for a in answers if a['value'] is not None]
        missing = Counter(a['missing_reason'] for a in answers if a['value'] is None)
        s = {'n_valid': len(valid), 'n_missing': len(answers)-len(valid),
             'missing_by_reason': {k: missing[k] for k in tuple(spec['missing_allowed']) + CAPTURE_REASONS}}
        if spec['type'] != 'text':
            if spec['type'] == 'integer':
                scale = bank['scales'][spec['scale_id']]
                keys = list(range(scale['min'], scale['max']+1))
            else:
                keys = list(dict(spec['options']))
            counts = Counter(v for row in valid for v in row) if spec['type']=='multi' else Counter(valid)
            s['distribution'] = {str(k): {'n': counts[k], 'percent_valid': 100*counts[k]/len(valid) if valid else None} for k in keys}
            s['denominator'] = 'Personen mit gültiger Antwort auf dieses Item; bei Mehrfachantworten sind mehr als 100 Prozent insgesamt möglich.'
        else:
            s['note'] = 'Freitext wird nicht in den numerischen Bericht kopiert. Gesondert pseudonymisiert und inhaltlich prüfen.'
        summaries[id] = s
    domains = {}
    for key, domain in bank['domains'].items():
        values = [p['scores'][key] for p in person_scores if p['scores'][key] is not None]
        domains[key] = {'label': domain['label'], 'n_complete': len(values),
                        'n_incomplete': len(records)-len(values), 'mean': mean(values) if values else None,
                        'min': min(values) if values else None, 'max': max(values) if values else None,
                        'range': domain['range']}
    labels = {'PRETEST': 'Nur Beschreibung der Testfälle; kein Unternehmensprofil.',
              'SURVEY': 'Beschreibung der tatsächlich Befragten; keine automatische Repräsentativität.',
              'SYNTHETIC_DEMO': 'Künstliche Testdaten; keinerlei empirischer Befund.'}
    return {'data_kind': payload['data_kind'], 'questionnaire_version': bank['version'],
            'interpretation_limit': labels[payload['data_kind']], 'n_records': len(records),
            'calculation_status': 'BERECHNET', 'items': summaries, 'domains': domains,
            'individual_scores': person_scores, 'review_flags': warnings,
            'total_score': None, 'total_score_reason': 'Nicht vorgesehen.',
            'bank_sha256': hashlib.sha256(json.dumps(bank, ensure_ascii=False, sort_keys=True).encode()).hexdigest()}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path); parser.add_argument('output', type=Path)
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error('Eingabe und Ausgabe müssen unterschiedliche Dateien sein.')
    try:
        raw = args.input.read_bytes()
        result = evaluate(json.loads(raw))
    except (ValueError, OSError, TypeError) as exc:
        parser.exit(2, f'Datenprüfung fehlgeschlagen: {exc}\n')
    result['input_sha256'] = hashlib.sha256(raw).hexdigest()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8')
    print(f"{result['n_records']} Fälle berechnet ({result['data_kind']}). Ausgabe: {args.output}")

if __name__ == '__main__':
    main()
