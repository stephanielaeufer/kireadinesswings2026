# Verläufe mit KI-Systemen

Diese Übersicht zeigt, wo die Verläufe jedes eingesetzten KI-Systems liegen. Die Systeme selbst sind in `PROJEKTKONTEXT.md` beschrieben.

| System | Einsatz | Verlauf |
|---|---|---|
| GPT-6 Astra Max (OpenAI) | Vorarbeit September bis 17. Oktober 2026: Literaturauswahl, Itembank, Codebuch, Masterprompt bis 0.5 | `ChatGPT_Verlauf.md`: direkt aus ChatGPT kopierter Text, Links zu Formularen und Antworttabellen entfernt. Eine von ChatGPT erzeugte PDF ist ein Teil-Export mit Lücken und wird nicht veröffentlicht |
| Gemini in Google Forms | Umsetzung des Fragebogens in die Formularfassungen R1 und R2 | Kein Chatverlauf vorhanden. Die Funktion „Hilf mir, ein Formular zu erstellen“ speichert keinen Verlauf. Der verwendete Erzeugungsprompt steht in `pretest/GoogleForms_Runde2_Anleitung.md`, Abschnitt 4 |
| Claude Opus 5.5 im Browser | Zwei synthetische Persona-Durchläufe R2, je ein eigener Chat | Prompts wortgleich in `pretest/Claude_Persona_Testprotokoll.md`. Die Antworten liegen als Formularexport R2 vor, der nicht veröffentlicht wird; geprüft mit `auswertung/audit_synthetic_forms.py` |
| Claude Opus 5.5 (claude-opus-5-5) | Prüfbericht, 16 Evaluationsläufe, Masterprompt 0.6, NotebookLM-Auswertung, Hausarbeit | `Claude_Hauptverlauf_2026-10-18.md` und `Claude_Teilagenten_2026-10-18.md` |
| Google NotebookLM | Demonstration A1 bis A3, Prüfung B1 und B2 | Prompts in `tests/notebooklm/ANLEITUNG_NotebookLM.md`, Antworten wortgleich in `tests/notebooklm/N-A1.md` bis `N-B2.md`. Es wurden keine weiteren Eingaben gemacht. Die Notebooks selbst sind in der README verlinkt |

## Hinweise zu den Claude-Exporten

- Enthalten sind alle Nachrichten der Erstellerin, alle Antworttexte von Claude und je Werkzeugaufruf eine Zeile mit Werkzeug und Zweck.
- Nicht enthalten sind die Werkzeugergebnisse. Sie enthalten Volltexte der Lehrunterlagen und Studien, die nicht veröffentlicht werden dürfen.
- Systemhinweise der Plattform und die E-Mail-Adresse wurden entfernt. Meldungen über abgeschlossene Teilagenten erscheinen als „Systemmeldung“.
- An einer Stelle hat die Plattform den Gesprächskontext technisch zusammengefasst. Die Stelle ist markiert.
- Der Hauptverlauf endet mit der Bereitstellung dieser Verläufe am 18. Oktober 2026.
- Die Teilagenten sind eigene, neu gestartete Sitzungen ohne Gesprächsverlauf, vor allem die 16 Evaluationsläufe und die Nachprüfungen.
