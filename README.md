# GenAI-Readiness und Weiterbildungsbedarf: ein Masterprompt nach Design Science Research

Projektpaket 0.6 · Masterprompt 0.6 · Referenzfragebogen GARI-DE-0.1 · Codebuch-Revision 0.6 · Stand 18. Oktober 2026

Stephanie Renner, MSc · Hausarbeit im Praxisseminar, Master Digital Commerce, Marketing & Psychology, WINGS / Hochschule Wismar · Abgabe 1. November 2026

## Worum es geht

Das Artefakt ist ein **Masterprompt**: Leitlinien für ein großes Sprachmodell. Mit ihnen erstellt das Modell aus einer Datenbasis und bereitgestellten Studien Fragebögen zur Readiness von Mitarbeitenden für generative KI, wendet sie in einem Unternehmen an, wertet Antworten aus und leitet Hinweise auf Weiterbildungsbedarf ab. Entwickelt wurde es nach Design Science Research (Peffers et al., 2007).

Status quo, selbst eingeschätzte Fähigkeiten, Einstellung, Nutzungsabsicht, Lernwünsche und betriebliche Voraussetzungen werden getrennt beschrieben. Es gibt keinen Gesamtscore. Das Ergebnis ist ein geprüfter Prototyp. Seine Messqualität ist nicht nachgewiesen.

## Für die Prüfenden: Schnellzugriff

| Was | Wo |
|---|---|
| Artefakt | [`MASTERPROMPT.md`](MASTERPROMPT.md) |
| Referenzfragebogen (34 Fragen) | [`instrument/Itembank_GARI_DE_0.1.json`](instrument/Itembank_GARI_DE_0.1.json), Herkunft je Frage in [`instrument/Itemregister.md`](instrument/Itemregister.md) |
| Rechen- und Interpretationsregeln | [`instrument/Codebuch.md`](instrument/Codebuch.md), [`auswertung/score.py`](auswertung/score.py) |
| Evaluation des Masterprompts (16 Läufe, Version 0.6, NotebookLM, menschlicher Abgleich) | [`tests/Masterprompt_Evaluation_2026-10-18.md`](tests/Masterprompt_Evaluation_2026-10-18.md) |
| Pretest des Fragebogens (R1 bis R3) | [`pretest/Abschluss_Evaluation_R3.md`](pretest/Abschluss_Evaluation_R3.md) |
| Änderungen je Version | [`CHANGELOG.md`](CHANGELOG.md) |
| Eingesetzte KI-Systeme und Chatverläufe | [`PROJEKTKONTEXT.md`](PROJEKTKONTEXT.md), [`ki-verlaeufe/`](ki-verlaeufe/README.md) |

### NotebookLM

Der Masterprompt wurde in Google NotebookLM demonstriert und das Projektpaket dort unabhängig geprüft. Die Notebooks enthalten die Lehrunterlagen des Moduls als Quellen. Sie sind deshalb nur für die Prüfenden freigegeben, nicht öffentlich.

| Notebook | Inhalt | Link |
|---|---|---|
| A1 Demonstration | Anwendung in einem fiktiven Betrieb (ANWENDEN, Szenario S1) | https://notebook.google.com/notebook/7878dd69-19e2-4c85-9413-c8b47fd455d4 |
| A2 Demonstration | Entwicklung aus der Datenbasis: Theorievorschlag, Modell, Hypothesen, Itementwurf | https://notebook.google.com/notebook/b93af67b-ce85-44c9-9c8b-fad06d719475 |
| B Prüfung | Unabhängige Prüfung des Gesamtpakets | https://notebook.google.com/notebook/20cd88dc-d11e-4a0c-a2d8-98d687ac4ed1 |

Die verwendeten Prompts stehen in [`tests/notebooklm/ANLEITUNG_NotebookLM.md`](tests/notebooklm/ANLEITUNG_NotebookLM.md), die Rohantworten in `tests/notebooklm/N-A1.md` bis `N-B2.md`.

## Einstieg

1. **In einem Unternehmen anwenden:** `MASTERPROMPT.md` als Anweisung, dazu ein ausgefülltes Briefing (Vorlage `beispiele/briefing.json`), `instrument/Itembank_GARI_DE_0.1.json` und `instrument/Codebuch.md`. Betriebsart ANWENDEN angeben.
2. **Neues Instrument entwickeln:** `MASTERPROMPT.md`, Briefing, Studien und Itemsammlung. Betriebsart ENTWICKELN. Ergebnis ist ein Entwurf, der vor wiederholtem Einsatz als Referenzbank eingefroren wird.
3. **Antworten auswerten:** Betriebsart AUSWERTEN mit Daten im Format des Codebuchs, Bank, Codebuch und `auswertung/score.py`.

Jedes System, das Dateien lesen kann, ist geeignet. Python-Ausführung verbessert die Auswertung. Erprobt wurde der Masterprompt mit Claude Opus 5.5 und in Google NotebookLM.

**Bedienregel für NotebookLM:** Masterprompt als Quelle hochladen, nicht in das Anweisungsfeld. Vor jedem Lauf in der Quellenliste nur die Quellen auswählen, die der Prompt nennt. NotebookLM setzt einen Quellenausschluss im Prompt nicht zuverlässig um (Evaluationsprotokoll, Abschnitt 11). Lange Ausgaben in Abschnitten anfordern.

## Rechenregeln nachvollziehen

Python 3.10 oder neuer, keine Zusatzpakete. Im Projektordner:

```bash
python -m unittest discover -s tests -v
python auswertung/score.py beispiele/synthetische_antworten.json ergebnis.json
```

Die Ausgabe enthält Einzelverteilungen und fünf getrennte vorläufige Teilbereichswerte. Gültige Nullwerte und Fehlwerte werden unterschieden. Ein Personenwert verlangt vollständige Antworten des jeweiligen Teilbereichs. `score.py` akzeptiert ausschließlich GARI-DE-0.1.

## Dateien

| Datei oder Ordner | Zweck | Stand |
|---|---|---|
| `MASTERPROMPT.md` | Arbeitsanweisung für alle Betriebsarten | 0.6 |
| `PROJEKTKONTEXT.md` | Projektangaben, Erhebungsumfang, eingesetzte KI-Systeme, Notebook-Links | 0.6 |
| `CHANGELOG.md` | Änderungen je Version | 0.6 |
| `Quellen_APA.md` | Literatur und Prüfstatus der Quellen | 0.5 |
| `Projektgrundlage.md`, `Evaluation.md` | Ursprüngliche Planung und datierte Fortschreibungen | historisch |
| `instrument/` | Itembank, Itemregister, Codebuch, Word-Fassung des Fragebogens | GARI-DE-0.1, Codebuch 0.6 |
| `auswertung/` | `score.py` sowie Bestandsprüfungen der Formularexporte R1 und R2 | 0.6 |
| `beispiele/` | Fiktives Briefing, Registervorlage, synthetische Rechentestfälle und Ergebnis | 0.6 |
| `pretest/` | Formularanleitung, Persona-Protokoll, Abschlussprüfung R3, Pretestleitfaden | 0.5 |
| `tests/test_scoring.py`, `tests/Pruefprotokoll.md` | Tests der Rechenroutine | 0.6 |
| `tests/Masterprompt_Evaluation_2026-10-18.md` | Evaluation des Masterprompts | 0.6 |
| `tests/laeufe/` | Auftrag und Rohausgabe je Evaluationslauf, mechanische Prüfung | 18. Oktober 2026 |
| `tests/notebooklm/` | Prompts und Rohantworten aus NotebookLM | 18. Oktober 2026 |
| `tests/Bewertungsbogen_Erstellerin*.md` | Leerer und ausgefüllter Bogen des menschlichen Abgleichs | 18. Oktober 2026 |
| `ki-verlaeufe/` | Verläufe mit allen eingesetzten KI-Systemen, Übersicht in `ki-verlaeufe/README.md` | 18. Oktober 2026 |

## Was nicht in diesem Repository liegt und warum

- **Lehrunterlagen des Moduls** (Prüfungsaufgabe, Study Guide, Foliensatz, Bewertungsbogen, Itemsammlung `Datensatz_v1`) und **Volltexte der fünf Studien**. Sie dürfen laut Study Guide nicht veröffentlicht werden.
- **Eingabe- und Arbeitsordner der Evaluationsläufe** sowie die **Ausgaben der Entwicklungsläufe E-B1, E-M1, E-M1-v06 und E-M2**. Sie geben Textstellen und Itemwortlaute aus den Lehrunterlagen in größerem Umfang wieder. Das vollständige Archiv wird den Prüfenden auf Anfrage bereitgestellt.
- **Personenbezogene Pretestdaten** (Formularexporte R1 und R2, Auswertungsbericht Runde 1). Die Prüfskripte in `auswertung/` liegen bei, die Rohdaten nicht.

## Rechte und Zitation

Der Fragebogen enthält Anpassungen fremder Items. Sie sind je Frage mit Quelle und Änderung im Itemregister ausgewiesen:

- U01 bis U06, K01 bis K06, L01 bis L03: adaptiert aus dem deutschen Autorenfragebogen der Meta AI Literacy Scale (Carolus et al., 2023). Rechte an den Originalitems liegen bei den Autor:innen.
- A01 bis A04, I01 bis I03: adaptiert aus der Itemsammlung zu Wichmann et al. (2025).

Code (`auswertung/`, `tests/`) und eigene Texte stammen von der Verfasserin. Eine Nachnutzung über die Prüfung hinaus bitte vorher abstimmen.

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (S. 961–970). https://doi.org/10.24251/HICSS.2025.114

Vollständige Literatur in `Quellen_APA.md` und im Literaturverzeichnis der Hausarbeit.
