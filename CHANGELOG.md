# Änderungsprotokoll

## Projektversion 0.6 vom 18. Oktober 2026

Auslöser: Erstmalige Evaluation des Masterprompts mit 16 Läufen am 18. Oktober 2026 (`tests/Masterprompt_Evaluation_2026-10-18.md`). Die Änderungen wurden von der Erstellerin freigegeben.

| Befund der Evaluation | Änderung | Betroffene Dateien |
|---|---|---|
| In 5 von 5 Masterprompt-Anwendungsläufen wurden Pretestrunden und Projektdateien in fiktive Unternehmen übertragen | Alle projektbezogenen Abschnitte aus dem Masterprompt entfernt und in `PROJEKTKONTEXT.md` ausgelagert. Neuer Abschnitt „Umgang mit Eingabedateien“: nur Eingaben der Sitzung, keine Projektunterlagen nachfordern | MASTERPROMPT.md, PROJEKTKONTEXT.md (neu) |
| Masterprompt-Entwicklungsläufe lieferten keinen ausdrücklichen Theorievorschlag und keine Hypothesen; die Prüfungsaufgabe verlangt einen Theorievorschlag | Neue Phase 1a: Theorievorschlag, Abgrenzung Theorie/Instrument/Methode, Forschungsmodell, nummerierte Hypothesen mit Quelle und Prüfbarkeit, Zuordnung zu Itemblöcken. Pflichtteil in ENTWICKELN und GESAMTPROZESS; Itemregister nennt Konstrukt und Hypothesen | MASTERPROMPT.md |
| Ungültiger Wert musste im Fehlerfall F2 hilfsweise als KEINE_ANGABE geführt werden | Erfassungsgrund UNGUELTIG_ERFASST mit Korrekturprotokoll. Für alle Items in `score.py` zugelassen; Itembank bleibt unverändert (Hash identisch). Neuer Test | instrument/Codebuch.md (Revision 0.6), auswertung/score.py, tests/test_scoring.py, beispiele/synthetisches_rechenergebnis.json |
| Baseline ergänzte betriebsspezifische Kontextfragen als Modul; Masterprompt ließ das offen | Regeln für ein gekennzeichnetes Zusatzmodul in ANWENDEN: eigenes ID-Präfix Z, eigene Modulversion, NEU_ENTWICKELT, keine Einrechnung in Kernwerte, Mindestgruppengröße | MASTERPROMPT.md |
| Briefing nennt drei Monate Rückblick, C02 vier Wochen | Regel: Bei Abweichung zwischen Briefing und Bank gilt in ANWENDEN die Bank, Abweichung benennen | MASTERPROMPT.md |
| ENTWICKELN erzeugte aus identischen Eingaben drei verschiedene Instrumente | Hinweis im Masterprompt: Entwicklungsergebnisse sind Entwürfe; Vergleichbarkeit erst nach Einfrieren einer Referenzbank | MASTERPROMPT.md |

Zusätzlich: Prüfung, ob Items einer bereitgestellten Itemsammlung geplanten Eigenitems nahekommen (Phase 1b). KI-Systemtabelle in PROJEKTKONTEXT.md.

Nachtrag 18. Oktober 2026: Plattformprüfung in NotebookLM dokumentiert (Evaluationsprotokoll Abschnitt 11). Abschnitt 6 des Protokolls präzisiert, weil die Gegenprüfung die Gütekriterien-Zuordnung zu Recht als überzeichnet bewertete. Bedienregel für NotebookLM in README, Notebook-Links in PROJEKTKONTEXT.md. Masterprompt selbst nicht geändert; drei Kandidaten für v0.7 im Protokoll.

Nachtrag 18. Oktober 2026, abends: Menschlicher Abgleich durch die Erstellerin als Abschnitt 12 im Evaluationsprotokoll, ausgefüllter Bewertungsbogen beigelegt. Repositoryfassung zusammengestellt: v0.5- und v0.6-Dateien zusammengeführt, öffentliche Laufausgaben unter `tests/laeufe/`, Pfade in `check_runs.py` relativ gemacht.

Unverändert: Itembank GARI-DE-0.1, Fragebogen, Itemregister, Rechenregeln. Nachprüfung der Änderungen mit den Läufen M-S2, E-M1 und F2 unter v0.6 im Evaluationsprotokoll.

## Projektversion 0.5 vom 17. Oktober 2026

- Erhebungsumfang nach Entscheidung der Erstellerin mit drei realen Personen und zwei synthetischen Fällen abgeschlossen; keine weitere reale Runde vorgesehen.
- Modellangabe „Claude Opus Mittel 5.5“, getrennte Chats und bewusst offene Persona-Prompts dokumentiert.
- Sichtbare neue Formularversion R3 übernommen; R2.1 bleibt nur historische Planung. Claude-Daten bleiben R2.
- R3 technisch geprüft: zehn einzelne Rückfragen, vollständige NB-/KA-Angebote, Blockierung bei vier und Weitergehen bei drei W01-/W02-Auswahlen. Keine Antwort abgesendet.
- Gesprächshinweise, W02-Formulierung und der Erinnerungshinweis bei PF05 als verbleibende Punkte festgehalten.
- Masterprompt, README, Projektgrundlage und Evaluationsstand auf den abgeschlossenen Umfang abgestimmt. Unausgeführte kontrollierte Vergleiche bleiben als solche kenntlich.
- Zehnseitiger Hausarbeitsentwurf mit zusätzlichem Literaturverzeichnis separat erstellt. Noch keine externe GitHub-Veröffentlichung.
- Kernbank und Rechenprogramme unverändert; Codebuch nur redaktionell hinsichtlich des Pretestumfangs angepasst.

## Projektversion 0.4 vom 17. Oktober 2026

- Bestätigung der Erstellerin dokumentiert: R1 blieb zwischen den drei echten Teilnahmen und der ersten Oberflächenprüfung unverändert.
- Sämtliche Abschnitte der neuen Forms-Fassung R2 geprüft. NB/KA bei 25 Zahlenfragen und die Freiwilligkeit der Sachfragen festgestellt. Keine zusätzliche Antwort abgesendet.
- Verbleibende gebündelte PF-Fragen, unpassende Hinweise und den möglichen Seitenwechsel mit vier W01-/W02-Auswahlen dokumentiert.
- Zwei von Claude erzeugte Persona-Antworten als SYNTHETIC_DEMO eingeordnet; 46 gültige Zahlenwerte, vier NB und drei leere Kontextfelder geprüft. Echte Testpersonen weiterhin n = 3.
- Persona-Prompts und offene Modell-/Sitzungsangaben protokolliert. Fehlende Zellen unverändert belassen; keine Readiness-Scores berechnet.
- Masterprompt 0.4 um Prüfung von Datenherkunft, funktionierenden Eingaberegeln und exakt übernommenen Prüffragen ergänzt. Der Kopierprompt enthält die zehn Prüffragen nun vollständig.
- Nacharbeit R2.1 konkretisiert; methodische Literatur zur synthetischen Befragung ergänzt.

## Projektversion 0.3 vom 17. Oktober 2026

- Export mit drei echten Pretestantworten eingelesen; 34 IDs, 75 zulässige Zahlenwerte sowie 23 nichtleere und vier leere schriftliche Rückmeldungsfelder festgestellt.
- Alle Abschnitte des bereitgestellten Google-Forms-Formulars gegen die Referenz geprüft. Keine Antwort abgesendet und keine Liveänderung vorgenommen.
- Fehlende NB-/KA-Auswahl, einzelne Pflichtfelder und unklare mehrteilige Prüffragen dokumentiert.
- Tatsächliche Methode als schriftliche Nachbefragung dokumentiert; keine nachträgliche Behauptung geführter Interviews.
- Masterprompt 0.3 um Prüfung der tatsächlichen Oberfläche, Umsetzungskennungen und Behandlung mehrdeutiger Rückmeldungen ergänzt.
- Runde-2-Anleitung mit konkreten Forms-Einstellungen, Erzeugungsprompt, zehn einzelnen Prüffragen und offener Abnahme vorbereitet.
- Separates Python-Skript für die Bestandsprüfung des echten Exports ausgeführt. Keine Readiness-Scores berechnet.

## Projektversion 0.2 vom 29. September 2026

- Publizierte MAILS-Fassung, deutscher Autorenfragebogen und Validierungs-/Kurzfassungsstudie von 2024 geprüft; Itemnummern und Auswertungszuordnung dokumentiert.
- 34 Fragen in GARI-DE-0.1 festgelegt, mit stabilen IDs, Quellenstatus, Anpassungen und fünf getrennten vorläufigen Teilbereichswerten.
- Word-Fragebogen, Pretestleitfaden mit Notizbogen, Itemregister, JSON-Bank und Codebuch erstellt.
- Masterprompt 0.2 an die konkrete Bank und die Datenregeln gebunden.
- Python-Auswertung mit ausschließlich künstlichen Daten ausgeführt. Fünf Testmethoden einschließlich 16 Fehlervarianten bestanden.

## Version 0.1 vom 18. September 2026

- Projektumfang auf generative KI, Mitarbeitende aller Tätigkeitsbereiche sowie Status quo und Weiterbildungsbedarf festgelegt.
- Thema, Forschungsfrage, Messmodell als Arbeitsentwurf und Zehn-Seiten-Gliederung formuliert.
- Masterprompt mit Betriebsarten für Entwicklung, Anwendung, Pretest, Auswertung und Gesamtprozess geschrieben.
- Baselinevergleich, Szenarien, Fehlerfälle und Pretest in zwei Runden mit insgesamt fünf Personen geplant.

Die „Noch offen“-Listen der Versionen 0.1 bis 0.4 sind historisch und wurden gekürzt. Ihr vollständiger Wortlaut steht im CHANGELOG des Projektpakets 0.5.
