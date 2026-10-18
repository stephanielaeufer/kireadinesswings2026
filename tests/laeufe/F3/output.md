# Auswertungsbericht GARI-DE: Datenprüfung zu `antworten.json`

## 0 Kurzfassung

- **Betriebsart:** AUSWERTEN (ausdrücklich angegeben).
- **Ergebnis der Datenprüfung:** Versionskonflikt. Die Antwortdaten tragen auf Datei- und Personenebene die Kennung **GARI-DE-0.2**. Beigefügt sind aber nur Itembank und Codebuch für **GARI-DE-0.1**.
- **Rechenroutine:** `auswertung/score.py` wurde ausgeführt und hat mit **Exitstatus 2** abgebrochen: „Datenprüfung fehlgeschlagen: Fragebogen- und Codebuchversion passen nicht zusammen.“ Eine Ergebnisdatei wurde nicht erzeugt.
- **Berechnungsstatus:** **NICHT_BERECHNET** für Itemverteilungen, Teilbereichswerte U, K, L, A, I und Gruppenwerte.
- **Datenart:** SYNTHETIC_DEMO. Selbst bei passender Version wäre jedes Ergebnis nur eine Demonstration und kein empirischer Befund.
- **Was trotzdem erledigt ist:** eine nachvollziehbare Bestands- und Qualitätsprüfung (Struktur, IDs, Fehlwertcodes, Antwortmuster, Plausibilitätshinweise). Sie verwendet die 0.1-Bank nur als Vergleichsreferenz und erzeugt keine Skalenwerte.
- **Maßnahmenbericht:** Ohne regulär berechnete Befunde und bei rein synthetischen Daten werden **keine Maßnahmen empfohlen**. Abschnitt 6 zeigt, welche Prüfpfade nach Klärung greifen würden.
- **Drei Rückfragen** stehen in Abschnitt 8. Ihre Beantwortung entscheidet, ob und wie gerechnet werden darf.

## 1 Ziel, Kontext und Annahmen

| Angabe | Stand |
|---|---|
| Auftrag | Datenprüfung, Berechnung und Maßnahmenbericht zu `antworten.json` |
| Promptversion | Masterprompt 0.5 vom 17. Oktober 2026 |
| Datum dieses Laufs | 18. Oktober 2026 |
| System / Modell | Claude (Anthropic), angezeigte Modellbezeichnung „Opus 5.5“ (Kennung claude-opus-5-5). Weitere Systemparameter (Temperatur u. a.): NICHT_VERFUEGBAR |
| Referenzbank | `instrument/Itembank_GARI_DE_0.1.json`, Version GARI-DE-0.1, Datum 2026-09-29, SHA-256 `12582782e64397d3460e88c2f4b2425b062f1f1c33725fc2d9953f5067afd050` |
| Codebuch | `instrument/Codebuch.md`, Fragebogen GARI-DE-0.1, Projektpaket 0.2, Stand 29. September 2026 (redaktionell fortgeschrieben 17. Oktober 2026) |
| Rechenroutine | `auswertung/score.py`, auf GARI-DE-0.1 festgelegt, SHA-256 `cccab0a8e9c2b55b40302a14ca8dbd2acd4493c821a8171df47788d41f8686c5` |
| Antwortdaten | `antworten.json`, SHA-256 `436f2a1e9a247bb02862c96c4c4d6bd6548f0e4aaef2624130ebe6dc17fc4b6a` |
| Fragebogenversion der Daten | GARI-DE-0.2 (Datei und alle drei Datensätze) |
| Datenart | SYNTHETIC_DEMO, 3 Datensätze (DEMO01 bis DEMO03) |
| Quellenstand | `Quellen_APA.md`, Stand 17. Oktober 2026 |

Annahmen und Unbekanntes:

- Kein Briefing beigefügt. Zweck, Zielpopulation, Tätigkeitsbereiche, Plattform, Erhebungszeitraum und tatsächlich verwendete Antwortoberfläche sind **unbekannt** und bleiben unbekannt.
- Unbekannt ist auch, wie die synthetischen Datensätze entstanden sind: von Hand konstruierte Rechentestfälle oder LLM-Personas. Ein Feld zur Herkunft (z. B. LLM_PERSONA) fehlt. Herkunft daher: NICHT_DOKUMENTIERT.
- Eine Bank, ein Codebuch oder ein Änderungsprotokoll zu GARI-DE-0.2 liegt nicht vor. Was sich gegenüber 0.1 geändert hat, ist nicht bekannt.

## 2 Quellen und Evidenzgrenzen (für diesen Lauf relevant)

Dieser Lauf prüft Daten, nicht Quellen. Für die Einordnung gilt der dokumentierte Stand aus Itembank und `Quellen_APA.md`:

| Quellen-ID | Nachweis | Verwendung in GARI-DE-0.1 | Grenze |
|---|---|---|---|
| MAILS_DE_2023 | Carolus et al. (2023), deutscher Autorenfragebogen | U01–U06, K01–K06, L01–L03 als ADAPTIERT; Teilbereichsmittelwerte motiviert durch die MAILS-Auswertungszuordnung | Evidenz betrifft allgemeine KI, 300 deutschsprachige Erwachsene, Selbstbericht. Keine Übertragung der Validierung auf die GenAI-Anpassung. Komplettfallregel ist eine eigene Projektregel. |
| POWERPILOT_2025 | Wichmann et al. (2025), bereitgestellte Itemsammlung | A01–A04, I01–I03 als ADAPTIERT | Geprüft anhand der bereitgestellten Itemsammlung. **Der direkte Vergleich mit dem OSF-Anhang bleibt offen** (Anhang am 29. September und 17. Oktober 2026 nicht abrufbar). |
| keine | Eigenentwicklung | C01–C06, G01–G03, W01–W03 als NEU_ENTWICKELT | Noch nicht empirisch geprüft. |

Keine vollständige Primärquellenprüfung aller Items, keine psychometrische Validierung der Kombination. Die vorläufigen Teilbereiche sind deskriptive Projektwerte, keine validierten Skalen (Carolus et al., 2023; Koch et al., 2024; Boateng et al., 2018).

## 3 Durchgeführte Schritte und Rechenprotokoll

### 3.1 Reguläre Rechenroutine

Aufruf im Eingabeordner:

```bash
python3 auswertung/score.py antworten.json ../work/ergebnis.json
```

Tatsächliche Ausgabe:

```
Datenprüfung fehlgeschlagen: Fragebogen- und Codebuchversion passen nicht zusammen.
EXIT=2
```

Die Routine vergleicht `questionnaire_version` der Datei mit `version` der Bank (`GARI-DE-0.2` ≠ `GARI-DE-0.1`) und stoppt. Das entspricht dem Codebuch: „Die Rechenroutine stoppt bei … abweichenden Versionen. Kein stilles Reparieren.“ Eine Datei `ergebnis.json` existiert nicht. Es gibt also keine erzeugte Ausgabe, auf die sich Zahlen stützen könnten.

**Bewusst nicht gemacht:** Die Versionsangabe in den Daten auf GARI-DE-0.1 umbenennen, um die Sperre zu umgehen. Das verbietet der Auftrag ausdrücklich. Es würde die Bedeutung bereits erhobener Antworten rückwirkend unbemerkt ändern.

### 3.2 Ersatzweise: Bestands- und Qualitätsprüfung

Zulässig ist laut Auftrag eine nachvollziehbare Bestands- und Qualitätsprüfung ohne reguläre Skalenberechnung. Dazu habe ich ein eigenes Prüfskript geschrieben (`work/bestandspruefung.py`, Protokoll in `work/bestandspruefung.log`, Exitstatus 0). Es prüft die Daten strukturell gegen die 0.1-Regeln **als Vergleichsmaßstab**, nicht als gültiges Codebuch für 0.2. Es bildet keine Mittelwerte und keine Verteilungstabellen.

Geprüft wurden: Pflichtfelder, Versionsangaben, doppelte Testkürzel, Vollständigkeit und Reihenfolge der 34 IDs, Fehlwertgründe, Wertebereiche, Antwortkategorien, Mehrfachwahlregeln, Antwortmuster je Block, der im Codebuch vorgesehene Plausibilitätshinweis C04/I.

## 4 Prüfbericht

### 4.1 Befunde zur Datenpassung

| Prüf-ID | Gegenstand | Befund | Status |
|---|---|---|---|
| P01 | `data_kind` | SYNTHETIC_DEMO, zulässiger Wert | in Ordnung |
| P02 | Version Datei | GARI-DE-0.2 | **ABWEICHUNG** gegenüber Bank/Codebuch 0.1 |
| P03 | Version je Person | alle drei Datensätze GARI-DE-0.2, in sich konsistent | **ABWEICHUNG** gegenüber Bank/Codebuch 0.1 |
| P04 | Bank/Codebuch für 0.2 | nicht beigefügt | **OFFEN** |
| P05 | Testkürzel | DEMO01, DEMO02, DEMO03; keine Doppelungen | in Ordnung |
| P06 | Item-IDs | je Person exakt die 34 IDs der 0.1-Bank, gleiche Reihenfolge | formal deckungsgleich mit 0.1 |
| P07 | Fehlwertgründe | nur NICHT_BEURTEILBAR und KEINE_ANGABE; kein NICHT_ZUTREFFEND oder UEBERSPRUNGEN | nach 0.1-Regeln zulässig |
| P08 | Wertebereiche und Kategorien | alle Werte liegen in den 0.1-Bereichen (0–10, 1–7, bekannte Codes); W01/W02 höchstens drei Antworten, exklusive Optionen allein | nach 0.1-Regeln zulässig |
| P09 | Herkunft der synthetischen Daten | kein Feld zu Erzeugung (Hand/LLM_PERSONA), kein Erzeugungsprotokoll | NICHT_DOKUMENTIERT |
| P10 | Antwortoberfläche | unbekannt; ob NB/KA tatsächlich auswählbar waren, ist nicht dokumentiert | OFFEN |

**Wichtig zu P06 bis P08:** Dass die Daten formal zur 0.1-Struktur passen, belegt **nicht**, dass 0.2 inhaltlich gleich ist. Eine neue Fragebogenversion entsteht laut Codebuch schon durch geänderten Wortlaut, Antwortformat, Reihenfolge, Definition oder Instruktion. Solche Änderungen sind in den Antwortdaten unsichtbar. Gleiche IDs und Wertebereiche genügen deshalb nicht, um 0.2-Daten mit den 0.1-Regeln zu rechnen.

**Möglicher Ursprung des Konflikts (Hypothese, nicht geprüft):** Das Codebuch trägt die Kennung „Projektpaket 0.2“, der Fragebogen aber „GARI-DE-0.1“. Es ist denkbar, dass beim Erzeugen der Demodaten die Paketversion mit der Fragebogenversion verwechselt wurde. Ob das zutrifft, lässt sich aus den Dateien nicht entscheiden. Eine Korrektur der Kennung wäre nur mit Nachweis zulässig (siehe Rückfrage 1).

### 4.2 Bestand an Fehlwerten (Qualitätsprüfung, keine Auswertung)

| Datensatz | Item | Fehlwertgrund |
|---|---|---|
| DEMO01 | W03 | KEINE_ANGABE |
| DEMO02 | U01 | NICHT_BEURTEILBAR |
| DEMO02 | I02 | KEINE_ANGABE |
| DEMO02 | W03 | KEINE_ANGABE |
| DEMO03 | W03 | KEINE_ANGABE |

Summe: 5 Fehlwerte in 3 × 34 = 102 Itemzellen. W03 ist in allen drei Datensätzen leer; es gibt keinen Freitext zu sichten. Die Fehlwerte werden nicht ersetzt und nicht gedeutet.

Hinweis: Ob „wenige NB“ etwas aussagt, hängt davon ab, ob NB in der verwendeten Oberfläche auswählbar war (P10). Das ist nicht dokumentiert.

### 4.3 Auffällige Antwortmuster (Prüfhinweise, keine Befunde)

| Prüf-ID | Datensatz | Beobachtung | Einordnung |
|---|---|---|---|
| Q01 | alle | C01–C06 identisch: OFFICE, D0, YES, NO, NOT_KNOWN, UNKNOWN | Deutet auf konstruierte Testfälle mit festem Kontext. Für Gruppenvergleiche ohne Variation. |
| Q02 | DEMO01 | U01 = 0, alle übrigen numerischen Items = 3 (auch A und I) | Gleichförmiges Muster; U01 = 0 ist eine gültige Antwort und bleibt erhalten. |
| Q03 | DEMO02 | Alle gültigen 0–10-Items = 8, alle gültigen 1–7-Items = 6 | Gleichförmiges Muster. Wirkt wie Testfall für Fehlwertbehandlung (U01 NB, I02 KA). |
| Q04 | DEMO03 | Alle 0–10-Items = 0, alle 1–7-Items = 1 | Gleichförmiges Muster an den Skalenminima. 0 ist eine tatsächliche Fähigkeitseinschätzung, kein Fehlwert. |
| Q05 | DEMO02 | C04 = NO (kein Zugang) bei I01 = 6 und I03 = 6 | Im Codebuch vorgesehener Prüfhinweis: mögliche erwartete Zugangsänderung prüfen. Keine Korrektur, keine Kompetenzaussage. |
| Q06 | DEMO02 | C02 = D0 (keine berufliche Nutzung in vier Wochen), aber Fähigkeitseinschätzungen von 8 | Kein Widerspruch nach Codebuch: Private Erfahrung (C03 = YES) kann zur Selbsteinschätzung beitragen. Nur zur Kenntnis. |
| Q07 | DEMO01 | W01 = NONE und W02 = NONE bei C04 = NO und C05 = NOT_KNOWN | Kein Regelverstoß. Zeigt, dass fehlender Zugang nicht als Hindernis angekreuzt sein muss. |

Bei echten Daten wären gleichförmige Antwortreihen ein Anlass, die Bearbeitungsqualität zu prüfen. Bei konstruierten Daten sind sie vermutlich Absicht. Ohne Erzeugungsprotokoll ist das nicht zu entscheiden.

### 4.4 Freigabestatus

| Bereich | Status |
|---|---|
| Passung Daten / Version / Codebuch | **ABWEICHUNG** |
| Reguläre Berechnung mit `score.py` | **NICHT_BERECHNET** (Abbruch Exitstatus 2) |
| Bestands- und Qualitätsprüfung | durchgeführt (Exitstatus 0) |
| Oberflächenabgleich der Fassung 0.2 | OFFEN, keine Unterlagen |

## 5 Auswertungsbericht

**Status: NICHT_BERECHNET.**

Es werden keine Itemverteilungen, keine Teilbereichswerte (U, K, L, A, I), keine Gruppenmittelwerte und keine Einzelitemberichte zu G01–G03 ausgegeben. Grund: Für GARI-DE-0.2 liegt kein Codebuch vor, und die Rechenroutine für 0.1 hat die Daten zu Recht abgelehnt. Zahlen, die ich hier frei nenne oder von Hand ausrechne, wären keine Ausgabe eines passenden Werkzeugs und könnten eine falsche Version vortäuschen.

Unabhängig davon gilt: Die Daten sind SYNTHETIC_DEMO. Auch nach erfolgreicher Berechnung wären sie nur eine technische Demonstration. Sie sagen nichts über eine reale Belegschaft aus. Für G, C und W sowie über alle Bereiche entsteht ohnehin kein Gesamtwert.

**Rechenanweisung für den Fall, dass die Versionsfrage geklärt ist:**

*Fall A: Es gibt eine dokumentierte Bank und ein Codebuch GARI-DE-0.2.*
1. Bank und Codebuch 0.2 beifügen, ebenso eine auf 0.2 festgelegte Rechenroutine mit angepassten Tests.
2. `python3 auswertung/score.py antworten.json ergebnis.json` mit der 0.2-Routine ausführen, Exitstatus prüfen, nur die erzeugte Ausgabe berichten.
3. Rechenregel nach dem 0.2-Codebuch. Falls diese der 0.1-Regel entspricht: Teilbereichswert je Person nur bei vollständigen gültigen Antworten, arithmetisches Mittel; Gruppenmittel nur über gültige Personenwerte mit Anzahl vollständiger und unvollständiger Fälle; keine Imputation; null gültige Fälle ergeben `null`.

*Fall B: Die Daten stammen nachweislich aus der unveränderten Fassung GARI-DE-0.1, die Kennung 0.2 ist ein Erfassungsfehler.*
1. Nachweis dokumentieren: Erzeugungsprompt bzw. Erzeugungsskript, verwendete Fassung, Datum.
2. Korrektur der Kennung im separaten Korrekturprotokoll festhalten (alt, neu, Grund, Nachweis, Person, Datum). Originaldatei unverändert aufbewahren.
3. Erst dann die korrigierte Kopie mit der 0.1-Routine rechnen.

Ohne einen dieser Nachweise bleibt es bei NICHT_BERECHNET.

## 6 Maßnahmenmatrix

**Es werden keine Maßnahmen empfohlen.** Begründung:

1. Es liegen keine regulär berechneten Befunde vor (Abschnitt 5).
2. Die Daten sind synthetisch. Maßnahmen für reale Beschäftigte lassen sich daraus grundsätzlich nicht ableiten.
3. Bei drei Datensätzen mit identischem Kontext gäbe es auch nach Berechnung nur eine Demonstration der Logik.

Damit nach Klärung nachvollziehbar ist, welche Prüfpfade die vorhandenen Antworten auslösen **würden**, folgt eine Zuordnung nach der Planungslogik des 0.1-Codebuchs. Sie beruht auf einzelnen Rohangaben aus der Bestandsprüfung, nicht auf Berechnungen. Sie ist ausdrücklich eine **Demonstration** und gilt nur, wenn 0.2 in diesen Items mit 0.1 übereinstimmt.

| Demo-Befund-ID | Items | Rohangabe (SYNTHETIC_DEMO, n = 3) | Einordnung nach Codebuch | Prüfpfad nach Klärung | Status |
|---|---|---|---|---|---|
| D-B01 | C04, W02 | C04 = NO in 3 von 3; W02 = ACCESS in 1 von 3 | Organisatorisches Hindernis | Freigegebene Zugangsmöglichkeiten klären; keine Kompetenzlücke behaupten | nur Demonstration |
| D-B02 | C05, W02 | C05 = NOT_KNOWN in 3 von 3; W02 = RULES in 1 von 3 | Orientierung, möglicherweise Organisation | Prüfen, ob Regeln existieren; verständlich bereitstellen; Zuständigkeit klären | nur Demonstration |
| D-B03 | C06 | C06 = UNKNOWN in 3 von 3 | Aufgabenpassung noch nicht beurteilbar | Geeignete Anwendungsfälle mit den Tätigkeitsbereichen klären; Nutzung kann sachlich unnötig sein | nur Demonstration |
| D-B04 | W01 | BASICS und PROMPTING je 1 von 3 (DEMO02); NONE 1 von 3; UNKNOWN 1 von 3 | Ausdrücklicher Lernwunsch bzw. Bedarf noch nicht einschätzbar | Einführung und Übung zu Eingaben anbieten, aber erst nach Zugang (D-B01). Bei UNKNOWN: Orientierungsangebot statt Pflichtschulung | nur Demonstration |
| D-B05 | C04, I01, I03 | DEMO02: kein Zugang, Absicht 6 | Codebuch-Prüfhinweis | Erwartete Zugangsänderung klären; keine Korrektur | nur Demonstration |

Keine Priorisierung, keine Zielgruppe, keine Erfolgskontrolle: Für synthetische Daten wäre jede solche Festlegung eine Scheinpräzision. Bei realen SURVEY-Daten enthält jede Empfehlung Thema, Zielgruppe, Ziel, Maßnahme, Befund-ID, Items, Fallzahl, Unsicherheit und Erfolgskontrolle. Die Priorisierung bleibt dann eine begründete Planungsentscheidung, keine validierte Regel. Eine Wirksamkeit von Trainings ist nicht belegt.

## 7 Änderungsprotokoll dieses Laufs

| Nr. | Vorgang | Ergebnis |
|---|---|---|
| 1 | `score.py` mit `antworten.json` ausgeführt | Abbruch, Exitstatus 2, keine Ausgabe |
| 2 | Eigenes Prüfskript `work/bestandspruefung.py` erstellt und ausgeführt | Exitstatus 0, Protokoll `work/bestandspruefung.log` |
| 3 | Änderungen an Daten, Bank, Codebuch oder `score.py` | **keine** |
| 4 | Versionskennung in den Daten umbenannt | **nein**, bewusst unterlassen |

## 8 Rückfragen

Ich habe alles erledigt, was ohne Antwort möglich ist. Für den nächsten Schritt brauche ich:

1. **Woher stammt die Kennung GARI-DE-0.2?** Gibt es eine Fassung 0.2 mit eigener Bank, eigenem Codebuch und Änderungsprotokoll? Falls ja, bitte beifügen. Falls nein: Gibt es einen Nachweis (Erzeugungsprompt oder -skript), dass die Demodaten auf der unveränderten Fassung 0.1 beruhen und die Kennung ein Erfassungsfehler ist, etwa eine Verwechslung mit „Projektpaket 0.2“?
2. **Wie sind die drei Datensätze entstanden?** Von Hand konstruierte Rechentestfälle oder LLM-Persona-Läufe? Bei Personas: Persona-Prompts, verwendetes Formular, Erzeugungs- und Antwortsystem, sichtbare Modellbezeichnung, manuelle Eingriffe.
3. **Welche Antwortoberfläche war im Einsatz?** Waren NB und KA tatsächlich auswählbar, waren Fragen verpflichtend, galt die Höchstzahl drei bei W01/W02 technisch? Liegt ein Begleitmanifest zum Oberflächenabgleich vor?

## 9 Status

**Erstellt:** Prüfbericht zur Datenpassung, Bestands- und Qualitätsprüfung, Rechenanweisung für beide Klärungsfälle, Demonstrationszuordnung der Prüfpfade, Rückfragen.

**Geprüft:** Struktur, IDs, Fehlwertcodes, Wertebereiche und Mehrfachwahlregeln der drei Datensätze gegen die 0.1-Regeln als Vergleichsmaßstab. Versionssperre von `score.py` greift wie vorgesehen.

**Berechnet:** Nichts. Teilbereichswerte, Verteilungen und Gruppenwerte: NICHT_BERECHNET.

**Es fehlen:** Bank und Codebuch zu GARI-DE-0.2 oder ein Nachweis für Fall B; Erzeugungsdokumentation der synthetischen Daten; Angaben zur Antwortoberfläche; ein Briefing. Für eine Aussage über eine reale Belegschaft fehlen reale SURVEY-Daten.

**Evidenzgrenzen bleiben:** keine psychometrische Validierung der Kombination; POWERPILOT_2025-Wortlaut nicht mit dem OSF-Anhang verglichen; synthetische Daten sind kein empirischer Befund. Ein erneuter Lauf mit demselben Prompt muss nicht zu identischen Formulierungen führen.

## Literatur

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), Article e39686. https://doi.org/10.1016/j.heliyon.2024.e39686

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://hdl.handle.net/10125/108952

Quellenstatus laut `Quellen_APA.md` vom 17. Oktober 2026; in diesem Lauf nicht erneut eingesehen.
