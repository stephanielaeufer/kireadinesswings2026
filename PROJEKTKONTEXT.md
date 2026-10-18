# Projektkontext zur Hausarbeit

Stand 18. Oktober 2026 · Gehört zu Projektpaket 0.6 · Nicht Teil des Masterprompts

Diese Datei enthält alle Angaben, die nur dieses Projekt betreffen. Sie stand bis Version 0.5 im Masterprompt selbst. Die Evaluation vom 18. Oktober 2026 zeigte, dass das Modell diese Angaben in fiktive Unternehmen übertrug: In 5 von 5 Anwendungsläufen verwies es auf Pretestrunden oder Projektdateien. Deshalb wurden sie ausgelagert. Wer den Masterprompt in einem Unternehmen einsetzt, braucht diese Datei nicht.

## Referenzfassung dieses Projekts

- Referenzbank: `instrument/Itembank_GARI_DE_0.1.json`, Fragebogenversion GARI-DE-0.1, 34 IDs. Die Bank enthält in `frozen_participant_text` Definition und alle Instruktionen. Die Fragebogenversion ist unabhängig von der Promptversion.
- Codebuch: `instrument/Codebuch.md`. Zugelassene vorläufige Teilbereichswerte: U, K, L, A, I. G01 bis G03 sind Einzelitems. Für G, C und W sowie über alle Bereiche entsteht kein Gesamtwert.
- Alle Fragen werden allen Personen angezeigt. NICHT_ZUTREFFEND und UEBERSPRUNGEN sind in GARI-DE-0.1 keine erlaubten Fehlwertgründe. UNGUELTIG_ERFASST ist seit Codebuch-Revision 0.6 als Erfassungsgrund zulässig.
- Auswertung: `auswertung/score.py`, an GARI-DE-0.1 gebunden. Tests: `tests/test_scoring.py`.
- Quellengrenze: POWERPILOT_2025 (A01 bis A04, I01 bis I03) ist an der bereitgestellten Itemsammlung geprüft. Der direkte Vergleich mit dem OSF-Anhang bleibt offen.
- Die Word-Fassung des Fragebogens war für einen begleiteten Pretest vorgesehen. Jede Onlineumsetzung braucht einen eigenen Abgleich und bei Abweichungen eine eigene Kennung.

## Erhebungsumfang und Abschlussregeln

- Drei reale Pretestfälle der Formularfassung GARI-DE-0.1-FORMS-R1.
- Zwei synthetische Claude-Personas der Fassung R2. Modellangabe der Erstellerin: Claude Opus 5.5 im Browser, Einstellung „Mittel“, getrennte Chats, bewusst offene Rollenprompts.
- Letzte Formularfassung: R3, technisch nachgeprüft, ohne neue Teilnahmen.
- Weitere reale Personen sind nicht vorgesehen. Das ist eine Abweichung vom ursprünglichen Plan mit fünf realen Personen. Die synthetischen Fälle ersetzen keine menschliche zweite Runde.
- Daten bleiben bei ihrer tatsächlich verwendeten Fassung. Die Rechenroutine für GARI-DE-0.1 darf R1, R2 oder R3 nicht durch Umbenennen der Versionsangabe akzeptieren.
- Abschluss der Erhebung bedeutet keine Freigabe oder Validierung des Instruments.

## Projektdateien zu Pretest und Evaluation

| Datei | Inhalt |
|---|---|
| `pretest/Abschluss_Evaluation_R3.md` | Aktueller Stand der Formularprüfung |
| `pretest/GoogleForms_Runde2_Anleitung.md` | Historische Umsetzungsanleitung für R2/R2.1 |
| `pretest/Claude_Persona_Testprotokoll.md` | Persona-Prompts und Grenzen |
| `pretest/Pretestleitfaden_und_Notizbogen.docx` | Ursprünglicher Plan für begleitete Gespräche |
| `tests/Masterprompt_Evaluation_2026-10-18.md` | 16 Läufe zu v0.5 und Nachprüfung v0.6 |
| `Evaluation.md` | Ursprünglicher Evaluationsplan und datierte Fortschreibungen |

## Eingesetzte KI-Systeme

| System | Version laut Anbieter oder Erstellerin | Zweck | Phase |
|---|---|---|---|
| GPT-6 Astra Max | Angabe der Erstellerin | Vorarbeit: Literaturauswahl, Itembank, Codebuch, Masterprompt bis v0.5, Prüfberichte | September bis 17. Oktober 2026 |
| Gemini in Google Forms („Hilf mir, ein Formular zu erstellen“) | Version nicht angezeigt | Erzeugung der Formularfassungen R1 und R2 aus Word-Fassung und Anleitung | Oktober 2026 |
| Claude Opus 5.5, claude.ai im Browser | Angabe der Erstellerin, Einstellung „Mittel“ | Zwei synthetische Persona-Durchläufe R2 | 17. Oktober 2026 |
| Claude Opus 5.5 (claude-opus-5-5) | technische Modell-ID | Prüfbericht, 16 Evaluationsläufe, Masterprompt v0.6, Nachprüfung, Auswertung der NotebookLM-Läufe | 18. Oktober 2026 |
| Google NotebookLM (Workspace Business Standard) | Anzeige „Pro“, keine weitere Angabe | Demonstration des Masterprompts (A1 bis A3) und unabhängige Prüfung des Pakets (B1, B2) | 18. Oktober 2026 |

## NotebookLM-Notebooks

Freigegeben nur für bestimmte Personen, nicht öffentlich, weil Lehrunterlagen und Studien als Quellen enthalten sind. Zuordnung von der Erstellerin am 18. Oktober 2026 bestätigt.

| Notebook | Inhalt | Link |
|---|---|---|
| A1 Demonstration | Anwendung, Szenario S1 | https://notebook.google.com/notebook/7878dd69-19e2-4c85-9413-c8b47fd455d4 |
| A2 Demonstration | Entwicklung aus der Datenbasis, Phase 1 und Itementwurf | https://notebook.google.com/notebook/b93af67b-ce85-44c9-9c8b-fad06d719475 |
| B Prüfung | Unabhängige Prüfung des Gesamtpakets | https://notebook.google.com/notebook/20cd88dc-d11e-4a0c-a2d8-98d687ac4ed1 |
