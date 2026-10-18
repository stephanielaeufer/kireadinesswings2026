# Technisches Prüfprotokoll

## Lauf vom 18. Oktober 2026 · Projektversion 0.6 · GARI-DE-0.1

`python -m unittest discover -s tests -v`: sechs Testmethoden bestanden. Neu ist `test_invalid_capture_is_missing_not_imputed` für den Erfassungsgrund UNGUELTIG_ERFASST (Codebuch-Revision 0.6).

| Prüfung | Erwartung | Ergebnis |
|---|---|---|
| UNGUELTIG_ERFASST bei U03 | Wird als Fehlwert akzeptiert, getrennt von KEINE_ANGABE gezählt; U-Personenwert fehlt; zulässig auch bei Items ohne NB (C01) | Erfüllt |
| Alle fünf bisherigen Prüfungen einschließlich 16 Fehlervarianten | wie 29. September 2026 | Erfüllt |

Die Itembank ist unverändert (kanonischer SHA-256 `c2e7eb3ba5f7505a9418ac1cd21b1847ae7e84f4cdd799db3ccfc8107c2ec080`). `beispiele/synthetisches_rechenergebnis.json` wurde neu erzeugt. Die Teilbereichswerte sind identisch mit dem Stand vom 29. September (U 1,25; K 3,67; L 3,67; A 3,33; I 2,0). Neu ist nur der zusätzliche Zähler UNGUELTIG_ERFASST mit Wert 0 je Item.

Vor diesem Lauf wurde Version 0.5 am selben Tag mit der hash-identischen Bank erneut geprüft: fünf Tests bestanden, Ergebnis identisch mit der gespeicherten Ausgabe.

## Lauf vom 29. September 2026 · Projektversion 0.2 · GARI-DE-0.1

`python -m unittest discover -s tests -v`: fünf Testmethoden bestanden. Eine Methode prüft zusätzlich 16 Varianten unzulässiger Eingaben. Die Testdaten sind vollständig künstlich.

| Prüfung | Erwartung | Ergebnis |
|---|---|---|
| Nullwerte und ein NB-Fehlwert | U01: zwei gültige Nullwerte, ein NB; U-Gruppenmittel 1,25 bei zwei vollständigen Fällen | Erfüllt |
| Mehrfachantworten | Jede Option geteilt durch drei gültig antwortende Personen | Erfüllt |
| Leerer Datensatz | Fehlende Mittelwerte und Prozentwerte statt erfundener Nullen | Erfüllt |
| Ausschließlich fehlende Antworten | Kein Personenwert für einen Teilbereich | Erfüllt |
| 16 Fehlerfälle | Ungültige Art/Version, doppelte Person, fehlende/falsche IDs, unzulässige Werte, widersprüchliche Fehlwerte und Mehrfachantworten zurückweisen | Erfüllt |

Beide Word-Dateien wurden damals gerendert und visuell kontrolliert. Die 34 Itemformulierungen im Fragebogen wurden mit der JSON-Bank abgeglichen.

## Reichweite

Die Prüfungen belegen das Verhalten der Rechenroutine in den ausgewählten Fällen. Sie belegen weder psychometrische Validität noch Stabilität eines Sprachmodells. Die Prüfung der Sprachmodellausgaben steht in `tests/Masterprompt_Evaluation_2026-10-18.md`.
