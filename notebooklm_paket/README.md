# Dateien für NotebookLM

NotebookLM nimmt keine `.json`-Dateien an. Dieser Ordner enthält deshalb dieselben Dateien wie das Projektpaket, die JSON-Dateien mit der Endung `.txt`. Der Inhalt ist unverändert. Mit genau diesen Dateien liefen die Demonstrationen A1 bis A3.

| Datei | Entspricht | Wofür |
|---|---|---|
| `01_MASTERPROMPT_v0.6.md` | `MASTERPROMPT.md` | Immer |
| `02_Referenzbank_GARI_DE_0.1.json.txt` | `instrument/Itembank_GARI_DE_0.1.json` | ANWENDEN, AUSWERTEN |
| `03_Codebuch_Rev0.6.md` | `instrument/Codebuch.md` | ANWENDEN, AUSWERTEN |
| `04_Briefing_S1_fiktiv.json.txt` | Briefing eines fiktiven Betriebs mit 40 Beschäftigten | ANWENDEN, als Beispiel oder Vorlage |
| `05_Briefing_Entwicklung_fiktiv.json.txt` | Briefing für die Neuentwicklung | ENTWICKELN |

## In einem Unternehmen anwenden

1. Neues Notebook anlegen. Die Dateien 01 bis 04 als Quellen hochladen. Den Masterprompt nicht in das Anweisungsfeld kopieren.
2. Für einen echten Betrieb: Datei 04 kopieren, im Texteditor Betriebsgröße, Tätigkeitsbereiche, Zugang zu KI und Zweck anpassen, als `.txt` speichern und statt 04 hochladen.
3. In der Quellenliste nur diese vier Quellen auswählen.
4. Prompt A1 aus `tests/notebooklm/ANLEITUNG_NotebookLM.md` verwenden.

Prüfen: Alle 34 Kernfragen wortgleich wie in der Referenzbank, kein Gesamtscore, Zusatzfragen nur mit Präfix Z, am Ende Manifest und Freigabestatus.

## Neu entwickeln

Datei 01, Datei 05, die Studien und die Itemsammlung als Quellen hochladen. Referenzbank und Codebuch dabei **nicht** auswählen, sonst übernimmt NotebookLM sie (Evaluationsprotokoll, Abschnitt 11). Prompt A2 aus der Anleitung verwenden. Studien und Itemsammlung liegen nicht in diesem Repository.
