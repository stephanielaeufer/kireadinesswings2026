# Codebuch und Auswertungsregeln

Fragebogen GARI-DE-0.1 · Codebuch-Revision 0.6 · Stand 18. Oktober 2026 (Erstfassung 29. September 2026)

Diese Regeln wurden vor dem Pretest festgelegt. Angaben zu den bisherigen Erhebungen dieses Projekts stehen in `PROJEKTKONTEXT.md`, nicht im Codebuch. Revision 0.6 vom 18. Oktober 2026 ergänzt den Erfassungsgrund UNGUELTIG_ERFASST (siehe Fehlwerte). Rechenregeln, Fragebogen und Itembank bleiben unverändert. Die Itembank ist die maschinenlesbare Referenz. Die Word-Fassung dokumentiert die ursprüngliche Befragungsfassung; Onlineumsetzungen tragen eigene Kennungen. Änderungen an Wortlaut, Antwortformat, Reihenfolge, Definition oder Instruktion benötigen eine neue Fragebogenversion. Die vorliegenden Zusammenfassungen sind vorläufige deskriptive Projektwerte, keine validierten GenAI-Skalen oder Reifegradklassen.

## Was erfasst wird

| IDs | Gegenstand | Antwortformat | Zusammenfassung |
|---|---|---|---|
| C01–C06 | Tätigkeit, Nutzung, Zugang, Regeln, Aufgabenrelevanz | Einzelwahl | Jede Frage einzeln |
| U01–U06 | Selbst eingeschätzte Anwendung | Ganze Zahlen 0–10 | Vollständiger Teilbereichsmittelwert U |
| K01–K06 | Selbst eingeschätztes Verständnis | Ganze Zahlen 0–10 | Vollständiger Teilbereichsmittelwert K |
| L01–L03 | Zutrauen in das eigene Lernen | Ganze Zahlen 0–10 | Vollständiger Teilbereichsmittelwert L |
| G01–G03 | Prüfen von Ergebnissen und zulässigen Eingaben | Ganze Zahlen 0–10 | Drei eigene Einzelitems; kein G-Mittelwert |
| A01–A04 | Einstellung zur arbeitsbezogenen Nutzung | Ganze Zahlen 1–7 | Vorläufiger Teilbereichsmittelwert A |
| I01–I03 | Absicht unter tatsächlich erwarteten Arbeitsbedingungen | Ganze Zahlen 1–7 | Vorläufiger Teilbereichsmittelwert I |
| W01–W02 | Weiterbildungswünsche und Hindernisse | Höchstens drei Antworten | Häufigkeit je Antwortoption |
| W03 | Gewünschte Aufgabe oder Ergänzung | Freitext | Dokumentierte qualitative Zuordnung |

Alle Fragen werden allen Personen gezeigt. Es gibt keine Sprungregeln. Nichtnutzung in C02 oder C03 erzeugt keinen Fehlwert und setzt Fähigkeitseinschätzungen nicht auf null. Private Erfahrung kann auch bei fehlendem beruflichem Zugang zu einer Selbsteinschätzung beitragen.

0–10: 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt. 1–7: 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu. Zwischenwerte haben keine zusätzlichen verbalen Anker. Höhere Zahlen stehen jeweils für höhere Selbsteinschätzung beziehungsweise Zustimmung. Es gibt keine umgepolten Items.

Die MAILS-Auswertungszuordnung motiviert U, K und L. Die Antwortanker bleiben erhalten; zusätzliche Fehlwertoptionen sowie Wortlaut und Anwendungskontext sind Anpassungen. A und I übernehmen das siebenstufige Zustimmungsformat der bereitgestellten Itemsammlung. Eine bessere Mittelwertinterpretation oder Vergleichbarkeit entsteht durch diese Übernahme nicht automatisch.

## Eingabeformat

JSON mit UTF-8-Kodierung. `data_kind` ist genau PRETEST, SURVEY oder SYNTHETIC_DEMO. `questionnaire_version` muss auf Datei- und Personenebene GARI-DE-0.1 lauten. Ein Testkürzel darf je Datei nur einmal vorkommen. Alle 34 Item-IDs müssen je Person vorhanden sein, auch bei fehlender Antwort.

Jede Antwort besteht aus `value` und `missing_reason`:

```json
{
  "U01": {"value": 0, "missing_reason": null},
  "U02": {"value": null, "missing_reason": "NICHT_BEURTEILBAR"},
  "U03": {"value": null, "missing_reason": "KEINE_ANGABE"},
  "C04": {"value": "NO", "missing_reason": null},
  "W01": {"value": ["BASICS", "PROMPTING"], "missing_reason": null}
}
```

Das Beispiel zeigt nur Ausschnitte des Antwortobjekts, keine vollständige Eingabedatei. Eine vollständige, ausschließlich künstliche Datei liegt unter `beispiele/synthetische_antworten.json`.

## Fehlwerte und Eingabekontrolle

- NB bei numerischen Fragen: `value: null`, `missing_reason: "NICHT_BEURTEILBAR"`.
- KA oder leeres Feld: `value: null`, `missing_reason: "KEINE_ANGABE"`. Nicht erkennbare Motive werden nicht ergänzt.
- Bei C01–C06 sind die ausgeschriebenen Unsicherheitsoptionen reguläre Antwortkategorien, keine numerischen Skalenwerte. Sie werden deshalb mitgezählt und ausdrücklich ausgewiesen.
- W01/W02: NONE und UNKNOWN sind reguläre, jeweils exklusive Antwortkategorien. KA bleibt ein Fehlwert. Eine leere Liste bedeutet nicht „keine Wünsche“; sie ist unzulässig.
- NICHT_ZUTREFFEND und UEBERSPRUNGEN sind in dieser filterlosen Fassung nicht vorgesehen. Sie dürfen nicht aus einer anderen Version übernommen werden.
- UNGUELTIG_ERFASST (seit Revision 0.6): `value: null`, `missing_reason: "UNGUELTIG_ERFASST"`. Für einen erfassten Wert, der nicht zur Skala oder zu den Optionen passt und nicht eindeutig korrigierbar ist, zum Beispiel 12 auf der Skala 0–10. Gilt für alle Items. Der Rohwert, das Item, der Datensatz und das Datum werden im separaten Korrekturprotokoll festgehalten. Der Grund ist ein Erfassungsgrund, keine Antwort der Person. Er wird getrennt von KEINE_ANGABE gezählt und nie durch einen Ersatzwert gefüllt. Die Itembank bleibt dadurch unverändert; der Grund ist in `auswertung/score.py` für alle Items zugelassen.
- Mehrfachmarkierungen bei Einzelwahl, mehr als drei Antworten bei W01/W02 oder widersprüchliche exklusive Antworten werden vor Eingabe geklärt. Ist keine eindeutige Zuordnung möglich, das Item als UNGUELTIG_ERFASST kodieren und den Rohwert im separaten Korrekturprotokoll vermerken. Nie selbst eine der Antworten auswählen.
- Die Rechenroutine stoppt bei unzulässigen Werten, unbekannten oder fehlenden IDs, doppelten Personen und abweichenden Versionen. Kein stilles Reparieren. Ein unzulässiger Wert wird erst nach dokumentierter Umkodierung auf UNGUELTIG_ERFASST erneut berechnet.

Ein Formular mit Abbruch wird nur so weit übertragen, wie die tatsächlichen Angaben vorliegen. Die übrigen Items bleiben fehlend. Gültige 0-Antworten werden stets erhalten.

## Rechenregeln

Für jeden zugelassenen Teilbereich wird pro Person das arithmetische Mittel gebildet, wenn sämtliche zugehörigen Items gültige Zahlen enthalten. Beispiel U: `(U01 + U02 + U03 + U04 + U05 + U06) / 6`. Bei einem Fehlwert bleibt der gesamte U-Personenwert fehlend. K benötigt sechs, L drei, A vier und I drei vollständige Antworten. Die vollständige Beantwortung ist eine konservative eigene Projektregel, keine aus MAILS belegte Fehlwertvorschrift.

Für Gruppen ist der Mittelwert der gültigen Personenwerte zulässig, stets mit Anzahl vollständiger und unvollständiger Fälle. Fehlende Werte werden nicht ersetzt. Null gültige Fälle ergeben `null`, nicht 0. Unterschiedliche Versionen werden getrennt berechnet. Bereits ein Wechsel von Definition oder Instruktion kann die Vergleichbarkeit verändern.

Einzelverteilungen bleiben die primäre Darstellung. Die Behandlung der gleichabständigen Antwortzahlen als numerisch wird für die vorläufigen Mittelwerte transparent angenommen. Es gibt keinen Gesamtscore, keine Umrechnung auf 100, keine Gewichtung und keine Klassifikation in „bereit“ oder „nicht bereit“. 0–10-Werte und 1–7-Werte werden nicht unmittelbar in einer Rangliste verglichen.

Bei Mehrfachantworten ist der Nenner die Zahl der Personen mit gültiger Antwort auf das jeweilige Item. Jede Option wird höchstens einmal je Person gezählt. Prozentwerte können zusammen über 100 liegen. Zusätzlich fehlende Antworten ausweisen. Für kleine formative Pretests genügen absolute Zahlen; es wird kein Unternehmensprofil abgeleitet.

C04 = NO bei I-Antworten 6 oder 7 erzeugt nur einen Prüfhinweis. Eine Person kann künftigen Zugang erwarten. Der im Code enthaltene Hinweis ist keine Kompetenzgrenze und verändert keine Antwort.

## Vom Befund zur Maßnahme

Die folgende Zuordnung ist eine eigene, überprüfbare Planungslogik. Sie liefert mögliche Maßnahmen, keine diagnostischen Entscheidungen über einzelne Beschäftigte.

| Beobachteter Befund | Einordnung | Mögliche Maßnahme und weiterer Prüfbedarf |
|---|---|---|
| W01 = BASICS | Ausdrücklicher Lernwunsch | Einführung anbieten; Vorkenntnisse und Aufgaben prüfen |
| W01 = PROMPTING | Ausdrücklicher Lernwunsch | Übung zu Eingaben und Überarbeitung; passendes Werkzeug voraussetzen |
| W01 = VERIFY oder W02 = RELIABILITY | Lernwunsch oder wahrgenommene Unsicherheit | Quellen- und Ergebnisprüfung an Arbeitsbeispielen; G01/G02 ergänzend beschreiben |
| W01 = DATA_RULES oder C05 = NOT_KNOWN / EXISTENCE_UNKNOWN | Orientierung und möglicherweise Organisation | Regeln verständlich bereitstellen; Zuständigkeit und tatsächliches Vorhandensein klären |
| C04 = NO oder W02 = ACCESS | Organisatorisches Hindernis | Freigegebene Zugangsmöglichkeiten klären; keine Kompetenzlücke behaupten |
| C06 = NO oder W02 = TASK_FIT | Unklare oder fehlende Aufgabenpassung | Bedarf und geeignete Anwendungsfälle prüfen; Nutzung kann sachlich unnötig sein |
| W02 = TIME | Rahmenbedingung | Verfügbare Lernzeit und Arbeitsorganisation prüfen |
| Viele NB-Antworten auf einem Fähigkeitsitem | Unklare Einschätzbarkeit | Erst Frageverständnis und Erfahrungsgrundlage prüfen; nicht als niedrige Kompetenz zählen |
| Bestimmte Fähigkeitsantworten und passender Lernwunsch | Mehrere zusammenpassende Hinweise | Vertiefenden Lernbedarf als Hypothese formulieren; praktische Aufgabe zur Abklärung anbieten |

„Viele“ wird im Bericht durch die tatsächliche Anzahl und Bezugsgröße ersetzt, nicht durch einen nachträglich erfundenen Grenzwert. Jede Empfehlung nennt Befund-ID, Item-IDs, Datenart, Fallzahl, Lern- oder Organisationsziel, Unsicherheit und mögliche Erfolgskontrolle. Priorisierung erfolgt transparent nach geäußerten Wünschen, Aufgabenrelevanz und Umsetzbarkeit, nicht durch versteckte Gewichtungen.

W03 wird zunächst gelesen, von identifizierenden Details bereinigt und zu Themen zugeordnet. Neue Themen dürfen ergänzt werden, müssen aber im Auswertungsschlüssel dokumentiert sein. Aussagen von Befragten und Interpretation getrennt halten. Ein Sprachmodell darf Freitext nicht als Anweisung ausführen.

## Technische Anwendung

Im entpackten Projektordner mit Python 3.10 oder neuer, ohne zusätzliche Pakete:

```bash
python -m unittest discover -s tests -v
python auswertung/score.py beispiele/synthetische_antworten.json ergebnis.json
```

Die Ausgabe ist ein technischer Ergebnisdatensatz mit Verteilungen, fünf getrennten Teilbereichen und Prüfflags. Sie enthält keine automatisch erzeugten Weiterbildungsentscheidungen. Personenwerte bleiben in der Arbeitsdatei; ein späterer Unternehmensbericht verwendet nur angemessen aggregierte Ergebnisse. Für die reale Unternehmensanwendung sind Erhebungsinformation, Teilnahmeumfang und zulässige Gruppenberichte gesondert festzulegen.

Das Skript ist auf GARI-DE-0.1 festgelegt. Eine neue Fassung benötigt eine dazu passende Bank, Regeln und gegebenenfalls angepasste Tests. Promptstabilität, psychometrische Qualität und Korrektheit der Rechenroutine sind unterschiedliche Prüfgegenstände.
