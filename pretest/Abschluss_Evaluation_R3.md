# Abschluss der formativen Evaluation und technische Nachprüfung von R3

Stand 17. Oktober 2026 · Projektpaket und Masterprompt 0.5

## Abschließender Umfang

Drei reale Testpersonen beantworteten R1. Zwei KI-generierte Personas beantworteten R2. Weitere reale Personen sind nach ausdrücklicher Entscheidung der Erstellerin nicht vorgesehen. R3 ist eine nachfolgende technische Korrektur; es liegen keine neuen menschlichen Verständlichkeitsdaten dazu vor.

Die Claude-Angabe lautet wörtlich „Claude Opus Mittel 5.5“. Beide Personas wurden nach Auskunft der Erstellerin in getrennten Chats im Browser bearbeitet. Die Rollenprompts waren bewusst offen gestaltet. Die bekannte Vorgabe und der Interpretationsspielraum bleiben dokumentiert; hinzugefügte Rolleneigenschaften werden als Modellannahmen geführt.

## Prüfung der zuletzt bereitgestellten Oberfläche

Die sichtbare Formularüberschrift lautet „Fragebogen zum Umgang mit generativer KI - GARI-DE-0.1-FORMS-R3“. Die nachfolgende Prüfung erfolgte interaktiv in der Antwortoberfläche. Es wurde keine Antwort abgesendet und kein neuer Datensatz erzeugt. Die frühere Bezeichnung R2.1 war nur eine vorgeschlagene Versionskennung.

| Prüfaspekt | Beobachtung | Reichweite |
|---|---|---|
| Numerische Fragen | 25 vorhanden; U/K/L/G je 13 Optionen, A/I je 9, jeweils einschließlich NB und KA | Antwortangebot technisch sichtbar |
| Freiwilligkeit | Seiten mit numerischen Sachfragen konnten ohne Zahlenantworten passiert werden; W03 blieb leer | Kein vollständiger Test jeder möglichen Antwortkombination |
| Zehn schriftliche Prüffragen | PF01–PF10 entsprechen im Fragetext der vorgesehenen Einzelliste | Rückmeldungen echter Personen zu R3 liegen nicht vor |
| W01 Höchstzahl | Vier gewählte Optionen erzeugten „Wählen Sie höchstens 3 Optionen aus.“ | Seitenwechsel blockiert |
| W02 Höchstzahl | Vier gewählte Optionen erzeugten dieselbe Meldung | Seitenwechsel blockiert |
| Zulässige Auswahl | Nach Reduktion auf drei Optionen je Frage gelang der Wechsel zur Nachbefragung | Endgültiges Absenden nicht geprüft |
| Digitale Anleitung bei L/G | „Wählen Sie pro Aussage eine Antwort“ vorhanden | Alter Einkreis-Hinweis dort ersetzt |

Die Höchstzahlregel prüft nicht automatisch die Exklusivität von „keine Angabe“, „derzeit nichts“ oder vergleichbaren Kategorien. Deren Kombination mit inhaltlichen Optionen wurde in diesem Durchlauf nicht funktional getestet. Eine weitergehende Bestätigung wird nicht behauptet.

## Verbleibende redaktionelle und methodische Punkte

- Auf der Startseite steht noch „Beim Gespräch weiß ich, wer Sie sind“, in der Einleitung „Im anschließenden Gespräch“ und „Beim begleiteten Test“. Für eine spätere rein schriftliche Durchführung sind diese Hinweise anzupassen. Die tatsächlich bereits durchgeführte R1-Nachbefragung bleibt schriftlich dokumentiert.
- W02 nennt weiterhin „höchstens drei Themen“ statt „höchstens drei Antworten“. Der Begriff „exklusive Antwort“ ist zusätzlich in den W-Fragen vorhanden; die Abschnittsbeschreibung erläutert die gemeinten Optionen konkreter.
- Bei PF05 wird C02 samt Vierwochenzeitraum eingeblendet. Die Prüffrage ist zwar einzeln umgesetzt, eine spätere Antwort könnte sich dadurch am eingeblendeten Hinweis orientieren. Für die Untersuchung spontaner Erinnerung wäre dieser Hinweis wegzulassen. Es liegen keine R3-Antworten vor, die deshalb neu auszuwerten wären.

Diese Punkte bleiben sichtbar dokumentiert. Sie lösen im abgeschlossenen Umfang keine neue Runde mit Testpersonen aus. Die Oberfläche wird nicht als vollständig geprüft oder psychometrisch validiert bezeichnet.

## Evidenzbilanz

- R1: drei reale Personen; 75 numerische Antworten im zulässigen Bereich; 23 nichtleere und vier leere schriftliche Felder. NB/KA fehlten als Auswahlmöglichkeiten. Alle drei Personen berichteten bereits Nutzungserfahrung.
- R2: zwei synthetische Fälle; 46 numerische Werte und vier NB-Antworten; drei leere Kontextfelder im ersten Fall. Keine Imputation und keine Readiness-Scores.
- R3: technische Bestätigung der oben genannten Korrekturen, ohne neue Teilnahme.
- Rechenroutine: die dokumentierten Tests vom 29. September 2026 bestehen fort. Code und Kernbank wurden in 0.5 nicht verändert; kein erneuter Testlauf wird behauptet.
- Kontrollierter Masterpromptvergleich: 18 Ausgaben und sechs Prompt-Fehlerfälle geplant, nicht durchgeführt. Kein Nachweis vergleichender Überlegenheit, systemübergreifender Stabilität oder universeller Verwendbarkeit.

## Nächste Arbeitsschritte

Hausarbeitsentwurf, aktuelle README und Quellenstatus fertigstellen. Für GitHub eine konkrete Repositoryadresse und Abgabeversion festhalten. Vor einer öffentlichen Bereitstellung adaptierter Instrumenttexte deren Nachnutzbarkeit sowie den noch ausstehenden direkten Originalabgleich klären. Für einen späteren operativen Einsatz wäre ein passender Importweg für die tatsächlich freigegebene Formularfassung erforderlich. Es wird keine neue Befragung innerhalb dieser Hausarbeit vorausgesetzt.

> Nachtrag 18. Oktober 2026: Der hier als nicht durchgeführt genannte Masterpromptvergleich wurde am 18. Oktober 2026 in reduziertem Umfang mit 16 Läufen durchgeführt. Siehe `tests/Masterprompt_Evaluation_2026-10-18.md`.
