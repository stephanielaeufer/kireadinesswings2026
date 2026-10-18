"""Bestandsprüfung ausdrücklich synthetischer Forms-Antworten, keine Scores.

Aufruf: python auswertung/audit_synthetic_forms.py export.xlsx ausgabe.json
Nur für die von der Erstellerin als Claude-Personas deklarierten R2-Daten.
Die Personenreihenfolge ist eine Zeilenzuordnung, kein Identitätsnachweis.
"""
import collections
import hashlib
import json
from pathlib import Path
import re
import sys

from pretest_forms_audit import read_export


def audit(source, bank):
    rows = read_export(source)
    headers = rows[0][1]
    items = {i['item_id']: i for i in bank['items']}
    columns, feedback = {}, {}
    for col, title in headers.items():
        m = re.match(r'^([CUKLGAIW]\d{2})\s+', title.strip())
        f = re.match(r'^(PF\d{2})\s+', title.strip())
        if m:
            if m[1] in columns:
                raise ValueError('Doppelte Item-ID: ' + m[1])
            columns[m[1]] = col
        if f:
            if f[1] in feedback:
                raise ValueError('Doppelte Feedback-ID: ' + f[1])
            feedback[f[1]] = col
    if set(columns) != set(items):
        raise ValueError('Die 34 Referenz-IDs sind nicht vollständig und eindeutig vorhanden.')
    records, issues = [], []
    for index, (source_row, row) in enumerate(rows[1:], 1):
        record = {'case_id': f'SYN{index:02}', 'source_row': source_row,
                  'data_kind': 'SYNTHETIC_DEMO', 'numeric_counts': collections.Counter(),
                  'core_answers': {}, 'feedback': {}, 'empty_core_items': []}
        for item_id, item in items.items():
            col = columns[item_id]
            raw = row.get(col, '')
            value, missing = None, None
            if not raw.strip():
                missing = 'KEINE_ANGABE'
                record['empty_core_items'].append(item_id)
            elif raw.strip() in ('NB', 'Nicht beurteilbar (NB)'):
                missing = 'NICHT_BEURTEILBAR'
            elif raw.strip() in ('KA', 'Keine Angabe', 'Keine Angabe (KA)'):
                missing = 'KEINE_ANGABE'
            elif item['type'] == 'integer':
                try:
                    num = float(raw)
                    lo, hi = (1, 7) if item['scale_id'] == 'AGREEMENT_1_7' else (0, 10)
                    if not num.is_integer() or not lo <= num <= hi:
                        raise ValueError
                    value = int(num)
                except ValueError:
                    issues.append({'case_id': record['case_id'], 'item_id': item_id,
                                   'issue': 'UNGUELTIGER_ZAHLENWERT', 'raw': raw})
            elif item['type'] == 'multi':
                mapping = {label: code for code, label in item['options']}
                if any(',' in label for label in mapping):
                    raise ValueError('Komma im Antwortlabel: Importregel muss geändert werden.')
                value = [mapping.get(label.strip()) for label in raw.split(',')]
                if (None in value or len(value) != len(set(value))
                        or len(value) > item['max_selections']
                        or (len(value) > 1 and any(c in item['exclusive_options'] for c in value))):
                    issues.append({'case_id': record['case_id'], 'item_id': item_id,
                                   'issue': 'MEHRFACHAUSWAHL_PRUEFEN', 'raw': raw})
            elif item['type'] == 'text':
                value = raw
            else:
                mapping = {label: code for code, label in item['options']}
                value = mapping.get(raw.strip())
                if value is None:
                    issues.append({'case_id': record['case_id'], 'item_id': item_id,
                                   'issue': 'UNBEKANNTE_KATEGORIE', 'raw': raw})
            if missing and missing not in item['missing_allowed']:
                issues.append({'case_id': record['case_id'], 'item_id': item_id,
                               'issue': 'NICHT_ERLAUBTER_FEHLWERTGRUND', 'raw': raw})
            record['core_answers'][item_id] = {'source_cell': col + str(source_row),
                                              'raw': raw, 'value': value, 'missing_reason': missing}
            if item['type'] == 'integer':
                status = ('NUMBER' if value is not None else
                          'NB' if missing == 'NICHT_BEURTEILBAR' else
                          'EMPTY' if not raw.strip() else
                          'KA' if missing == 'KEINE_ANGABE' else 'INVALID')
                record['numeric_counts'][status] += 1
        for field_id, col in feedback.items():
            record['feedback'][field_id] = {'source_cell': col + str(source_row),
                                           'question': headers[col], 'raw': row.get(col, '')}
        records.append(record)
    totals = collections.Counter()
    for record in records:
        totals.update(record['numeric_counts'])
    return {'data_kind': 'SYNTHETIC_DEMO', 'synthetic_origin': 'LLM_PERSONA',
            'source_declaration': 'Erstellerin: zwei fiktive Personas mit Claude im Browser.',
            'system': 'Claude', 'model_version': 'NICHT_DOKUMENTIERT',
            'questionnaire_version': 'GARI-DE-0.1-FORMS-R2', 'reference_bank': bank['version'],
            'source_file': source.name, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'case_n': len(records), 'core_item_n': len(items),
            'numeric_item_n': sum(i['type'] == 'integer' for i in items.values()),
            'numeric_totals': dict(totals), 'feedback_field_n': len(feedback),
            'feedback_nonempty_n': sum(bool(f['raw'].strip()) for r in records for f in r['feedback'].values()),
            'id_to_column': columns, 'issues': issues, 'records': records,
            'scoring_status': 'NICHT_BERECHNET',
            'interpretation_limits': ['Keine realen Testpersonen.',
                                     'Keine Imputation aus Persona-Prompts oder späteren Freitexten.',
                                     'Keine Skalenberechnung und keine Behauptung gleichwertiger Fassungen.',
                                     'Keine Prüfung der Browseraktionen von Claude ohne zugehöriges Protokoll.']}


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('Aufruf: python audit_synthetic_forms.py export.xlsx ausgabe.json')
    source, target = map(Path, sys.argv[1:])
    bank_path = Path(__file__).resolve().parents[1] / 'instrument' / 'Itembank_GARI_DE_0.1.json'
    result = audit(source, json.loads(bank_path.read_text(encoding='utf-8')))
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ['data_kind', 'case_n', 'core_item_n', 'numeric_totals', 'feedback_nonempty_n', 'issues']}, ensure_ascii=False))
