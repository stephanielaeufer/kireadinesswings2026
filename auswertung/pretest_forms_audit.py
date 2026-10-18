"""Prüft einen Google-Forms-XLSX-Export gegen GARI-DE-0.1; erzeugt keine Scores.

Aufruf: python auswertung/pretest_forms_audit.py export.xlsx audit.json
Nur Python-Standardbibliothek. Das Ergebnis enthält reale Angaben und bleibt privat.
Der Adapter prüft Datenwerte, nicht die historische Formularoberfläche.
"""
import collections
import hashlib
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def read_export(path):
    with zipfile.ZipFile(path) as z:
        sheets = [n for n in z.namelist() if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", n)]
        if len(sheets) != 1:
            raise ValueError("Der Adapter erwartet genau ein Tabellenblatt; Auswahl vorher klären.")
        strings = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            strings = ["".join(t.text or "" for t in x.findall(".//m:t", NS)) for x in root]
        root = ET.fromstring(z.read(sheets[0]))
        rows = []
        for r in root.findall(".//m:sheetData/m:row", NS):
            values = {}
            for c in r.findall("m:c", NS):
                col = re.sub(r"\d", "", c.attrib["r"])
                v = c.find("m:v", NS)
                text = "" if v is None else v.text or ""
                if c.attrib.get("t") == "s":
                    text = strings[int(text)]
                elif c.attrib.get("t") == "inlineStr":
                    text = "".join(t.text or "" for t in c.findall(".//m:t", NS))
                values[col] = text
            if any(v.strip() for v in values.values()):
                rows.append((int(r.attrib["r"]), values))
    if len(rows) < 2:
        raise ValueError("Kein auswertbarer Datensatz mit Kopfzeile und Antworten.")
    return rows


def audit(source, bank):
    rows = read_export(source)
    headers = rows[0][1]
    columns = {}
    for col, h in headers.items():
        m = re.match(r"^([CUKLGAIW]\d{2})\s+", h.strip())
        if m:
            if m[1] in columns:
                raise ValueError("Mehrdeutige Item-ID in den Spalten: " + m[1])
            columns[m[1]] = col
    items = {i["item_id"]: i for i in bank["items"]}
    if set(columns) != set(items):
        raise ValueError("Item-IDs stimmen nicht mit der Referenzbank überein.")
    numeric = {k: v for k, v in items.items() if v["type"] == "integer"}
    feedback_cols = [c for c in headers if c not in columns.values() and c not in ("A", "B")]
    header_diffs = []
    for item_id, col in columns.items():
        actual = re.sub(r"^[A-Z]\d{2}\s+", "", headers[col].strip())
        if actual != items[item_id]["text"]:
            header_diffs.append({"item_id": item_id, "column": col, "export_header": actual,
                                 "reference_text": items[item_id]["text"]})
    issues, records = [], []
    option_counts = {i: collections.Counter() for i in ("W01", "W02")}
    valid_multi_n = {i: 0 for i in option_counts}
    for n, (row_number, values) in enumerate(rows[1:], 1):
        person = f"P{n:02d}"
        valid = 0
        for item_id, item in numeric.items():
            raw = values.get(columns[item_id], "").strip()
            try:
                number = float(raw)
                low, high = (1, 7) if item["scale_id"] == "AGREEMENT_1_7" else (0, 10)
                if not number.is_integer() or not low <= number <= high:
                    raise ValueError
                valid += 1
            except ValueError:
                issues.append({"person": person, "item_id": item_id, "raw": raw,
                               "issue": "LEER_ODER_NICHT_GUELTIG_NUMERISCH"})
        for item_id in option_counts:
            raw = values.get(columns[item_id], "").strip()
            # Diese konkrete Bank enthält keine Kommas innerhalb der W01/W02-Labels.
            mapping = {label: code for code, label in items[item_id]["options"]}
            if any("," in label for label in mapping):
                raise ValueError("Komma im Optionslabel: Importregel muss explizit angepasst werden.")
            if raw in ("", "Keine Angabe"):
                continue
            labels = [v.strip() for v in raw.split(",")]
            codes = [mapping.get(v) for v in labels]
            invalid = (None in codes or len(codes) > items[item_id]["max_selections"]
                       or len(codes) != len(set(codes))
                       or (len(codes) > 1 and any(c in items[item_id]["exclusive_options"] for c in codes)))
            if invalid:
                issues.append({"person": person, "item_id": item_id, "raw": raw,
                               "issue": "MEHRFACHAUSWAHL_PRUEFEN"})
                continue
            valid_multi_n[item_id] += 1
            option_counts[item_id].update(codes)
        records.append({
            "analysis_id": person, "source_row": row_number,
            "numeric_valid_n": valid,
            "context": {i: values.get(columns[i], "") for i in items if i.startswith("C")},
            "training": {i: values.get(columns[i], "") for i in ("W01", "W02", "W03")},
            "feedback": {c: {"question": headers[c], "answer": values.get(c, "")} for c in feedback_cols},
        })
    filled = sum(bool(r["feedback"][c]["answer"].strip()) for r in records for c in feedback_cols)
    return {
        "data_kind": "PRETEST", "analysis_date": "2026-10-17",
        "reference_bank": bank["version"],
        "implementation_id": "GARI-DE-0.1-FORMS-R1",
        "implementation_id_note": "Nachträglich vergebene Analysebezeichnung; Originalexport ohne Versionsfeld.",
        "source_file": source.name, "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "respondents_n": len(records), "core_items_n": len(columns),
        "numeric_items_per_person": len(numeric),
        "numeric_valid_total": sum(r["numeric_valid_n"] for r in records),
        "feedback_fields_per_person": len(feedback_cols),
        "feedback_nonempty_total": filled,
        "feedback_empty_total": len(records) * len(feedback_cols) - filled,
        "id_to_column": columns,
        "header_differences_requiring_ui_review": header_diffs,
        "multi_counts": {i: {"valid_n": valid_multi_n[i], "counts": dict(c)} for i, c in option_counts.items()},
        "issues": issues, "records": records,
        "scoring_status": "NICHT_DURCHGEFUEHRT_ABWEICHENDE_UMSETZUNG_UND_PRETESTZWECK",
        "limits": ["Keine Prüfung von Verständnis, historischer Pflichtfeldkonfiguration oder Abbrüchen aus Zellvollständigkeit.",
                   "Keine Personenidentifikation oder Prüfung auf Mehrfachteilnahme möglich.",
                   "NB und KA waren bei den numerischen Items der separat geprüften Oberfläche nicht verfügbar."]
    }


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Aufruf: python pretest_forms_audit.py export.xlsx audit.json")
    source, target = map(Path, sys.argv[1:])
    bank_path = Path(__file__).resolve().parents[1] / "instrument" / "Itembank_GARI_DE_0.1.json"
    result = audit(source, json.loads(bank_path.read_text(encoding="utf-8")))
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("respondents_n", "core_items_n", "numeric_valid_total", "feedback_nonempty_total", "feedback_empty_total", "issues")}, ensure_ascii=False))
