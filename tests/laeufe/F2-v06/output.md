# Auswertungsbericht GARI-DE-0.1 · Datensatz antworten.json

**DEMONSTRATION MIT SYNTHETISCHEN DATEN (data_kind = SYNTHETIC_DEMO). Alle Zahlen in diesem Bericht beschreiben drei künstliche Testfälle. Sie sind kein empirischer Befund über Beschäftigte, kein Pretestergebnis und kein Unternehmensprofil.**

| Angabe | Wert |
|---|---|
| Datum | 18. Oktober 2026 |
| System und Modell | Claude; Modellkennung laut Systemangabe claude-opus-5-5. Weitere Systemparameter (Temperatur, Sampling, Kontextlänge): NICHT_VERFUEGBAR |
| Promptversion | Masterprompt Version 0.6 vom 18. Oktober 2026 |
| Betriebsart | AUSWERTEN (ausdrücklich angegeben) |
| Fragebogenversion | GARI-DE-0.1 (Itembank vom 29. September 2026) |
| Codebuch | Codebuch GARI-DE-0.1, Revision 0.6, Stand 18. Oktober 2026 |
| Auswertungsskript | auswertung/score.py (auf GARI-DE-0.1 festgelegt, Revision-0.6-Kommentar) |
| Quellenstand | Quellen_APA.md, Stand 17. Oktober 2026 |
| Datenart | SYNTHETIC_DEMO; Herkunft (von Hand konstruiert oder LLM_PERSONA): NICHT_DOKUMENTIERT |
| Laufzeit | Python 3.13.16 |
| Berechnungsstatus | Erster Lauf: abgebrochen (Exit 2). Zweiter Lauf nach dokumentierter Umkodierung: BERECHNET (Exit 0) |

Gleiche Prompts garantieren keine identischen LLM-Ausgaben. Die Zahlen unten stammen ausschließlich aus der Ausgabedatei des Skripts, nicht aus freier Formulierung.

---

## 1 Ziel, Datenbasis und Annahmen

**Ziel.** Datenprüfung, Berechnung und Maßnahmenbericht für die beigefügten Antwortdaten zum Fragebogen GARI-DE-0.1.

**Zielgruppe des Instruments.** Mitarbeitende aller Tätigkeitsbereiche, ausdrücklich auch Personen ohne bisherige Nutzung generativer KI (laut Itembank und Codebuch).

**Datenbasis.** Drei Datensätze (DEMO01, DEMO02, DEMO03), Datei- und Personenversion GARI-DE-0.1, data_kind SYNTHETIC_DEMO.

**Getroffene Annahmen und Grenzen.**

- Die Daten sind laut Pflichtfeld synthetisch. Ich behandle sie durchgehend als Demonstration. Ob sie von Hand konstruiert oder von einer KI-Persona erzeugt wurden, ist nicht dokumentiert (NICHT_DOKUMENTIERT).
- Die drei Demonstrationsfälle sind nicht die drei realen Pretestpersonen, die das Codebuch in seiner Fortschreibung vom 17. Oktober 2026 erwähnt. Die Kürzel DEMO01 bis DEMO03 und data_kind sprechen dagegen. Eine Verwechslung muss ausgeschlossen bleiben.
- Die tatsächlich verwendete Antwortoberfläche ist nicht beigefügt. Deshalb ist offen, ob NB und KA dort auswählbar waren. Die Itembank (eingefrorener Befragtentext) sieht NB und KA für alle 0–10- und 1–7-Items vor.
- Ein Unternehmensbriefing liegt nicht vor und wird für AUSWERTEN laut Masterprompt auch nicht benötigt. Unternehmensmerkmale werden nicht ergänzt.
- Ein Forschungsmodell mit Hypothesen ist nicht Teil der Eingaben. In AUSWERTEN wird keines erfunden. Hypothesen wären ohnehin erst mit ausreichend großen SURVEY-Daten und einer vorab festgelegten Analyse prüfbar.

---

## 2 Quellen- und Evidenzgrenzen (übernommen aus Itembank und Quellen_APA.md)

In dieser Sitzung wurden keine Primärquellen eingesehen. Die folgenden Angaben geben ausschließlich den Prüfstand wieder, den Itembank, Codebuch und Quellen_APA.md selbst dokumentieren.

| Teilbereich | Herkunft laut Bank | Status | Dokumentierte Evidenzgrenze |
|---|---|---|---|
| C01–C06 | Eigenentwicklung | NEU_ENTWICKELT | Noch nicht empirisch geprüft. Einzelitems, keine Skala. |
| U01–U06, K01–K06, L01–L03 | MAILS, deutscher Autorenfragebogen, Items 1–12 und 26–28 (Carolus et al., 2023) | ADAPTIERT | Auf generative KI und Arbeitskontext eingegrenzt; NB/KA ergänzt; Originalanker beibehalten. Ursprüngliche Evidenz betrifft allgemeine KI, Selbstbericht, 300 deutschsprachige Erwachsene. Im Projekt nicht empirisch geprüft. Die Vollständigkeitsregel für Mittelwerte ist eine eigene Projektregel, keine MAILS-Vorschrift. |
| G01–G03 | Eigenentwicklung | NEU_ENTWICKELT | Drei Einzelitems, ausdrücklich kein G-Mittelwert. |
| A01–A04, I01–I03 | Wichmann et al. (2025), bereitgestellte Itemsammlung Questionnaire 2 / PowerPilot | ADAPTIERT | Übersetzt, Technologie, Arbeitskontext und Zeitraum (drei Monate) geändert. Der OSF-Originalanhang war nicht abrufbar; die Gleichheit des Wortlauts mit dessen Fassung bleibt offen. Ursprünglicher Kontext: Energie-Monitoring-Anwendungen. |
| W01–W03 | Eigenentwicklung | NEU_ENTWICKELT | Noch nicht empirisch geprüft. |

Gesamtstatus laut Bank: „Für erste Pretestrunde festgehalten; inhaltliche Quellenprüfung mit dokumentierter Grenze bei POWERPILOT_2025; keine psychometrische Validierung.“ Die Teilbereichsmittelwerte sind laut Codebuch „vorläufige deskriptive Projektwerte, keine validierten GenAI-Skalen oder Reifegradklassen“. Diese Grenze gilt für jede Zahl in Abschnitt 4. Übersetzung, Kürzung und Kontextänderung übertragen keine Validierungsaussage der Originalinstrumente (vgl. Boateng et al., 2018, laut Quellen_APA.md als Grundlage für die Trennung von Itementwicklung, Pretest und Prüfung der Messqualität geführt).

---

## 3 Prüfbericht

### 3.1 Versions- und Strukturprüfung

| Prüfpunkt | Ergebnis |
|---|---|
| data_kind vorhanden und zulässig | Ja: SYNTHETIC_DEMO |
| questionnaire_version Datei | GARI-DE-0.1, passt zu Bank und Codebuch |
| questionnaire_version je Person | 3 von 3 GARI-DE-0.1 |
| Doppelte Testkürzel | Keine |
| Alle 34 Item-IDs je Person, keine unbekannten IDs | Ja, bei allen drei Datensätzen |
| Jede Antwort mit value und missing_reason | Ja |
| Widerspruch Wert plus Fehlwertgrund | Keiner |
| Einzelwahl-Kategorien C01–C06 | Alle zulässig |
| Mehrfachwahl W01/W02 (höchstens 3, keine Dopplung, exklusive Optionen allein) | Alle zulässig |
| Fehlwertgründe | Nur KEINE_ANGABE und NICHT_BEURTEILBAR, jeweils für das Item zugelassen |
| Skalenwerte 0–10 und 1–7 | **Ein Wert außerhalb der Skala: DEMO01 / U03 = 12** |
| Filter | Die Fassung hat keine Sprungregeln; widersprüchliche Filter sind daher nicht möglich |

Prüfwerkzeuge: Erstens das mitgelieferte Skript score.py. Es bricht beim ersten Fehler ab. Zweitens ein eigenes Prüfskript (work/pruefung.py), das alle Datensätze vollständig durchläuft und alle Auffälligkeiten sammelt. Beide fanden übereinstimmend genau einen unzulässigen Wert.

### 3.2 Erster Skriptlauf mit den Originaldaten

```
python3 input/auswertung/score.py input/antworten.json work/ergebnis_roh.json
Datenprüfung fehlgeschlagen: DEMO01/U03: Ungültiger Skalenwert.
Exitstatus: 2
```

Es wurde keine Ergebnisdatei erzeugt. Das Skript arbeitet wie im Codebuch beschrieben: kein stilles Reparieren.

### 3.3 Behandlung des unzulässigen Werts

Das Codebuch sieht seit Revision 0.6 den Erfassungsgrund UNGUELTIG_ERFASST für alle Items vor: „für einen erfassten Wert, der nicht zur Skala oder zu den Optionen passt und nicht eindeutig korrigierbar ist, zum Beispiel 12 auf der Skala 0–10“. Der Wert 12 ist nicht eindeutig korrigierbar. Denkbar wären etwa 1, 2 oder 10. Deshalb wird kein Wert geschätzt oder ersetzt.

**Korrekturprotokoll** (auch maschinenlesbar in work/korrekturprotokoll.json):

| Korrektur-ID | Datum | Datensatz | Item | Rohwert | Zulässiger Bereich | Neuer Eintrag | Grundlage |
|---|---|---|---|---|---|---|---|
| KP-01 | 18.10.2026 | DEMO01 | U03 | 12 | 0–10 (ABILITY_0_10) | value: null, missing_reason: UNGUELTIG_ERFASST | Codebuch Revision 0.6, Abschnitt „Fehlwerte und Eingabekontrolle“ |

Die Originaldatei input/antworten.json bleibt unverändert (SHA-256 3fa73684…3673f5). Die umkodierte Arbeitsfassung liegt unter work/antworten_korrigiert.json (SHA-256 c1803605…f55f739). UNGUELTIG_ERFASST ist keine Antwort der Person. Der Grund wird getrennt von KEINE_ANGABE gezählt.

**Hinweis zur zeitlichen Gültigkeit der Regel.** Das Codebuch beschreibt sich als „vor dem Pretest festgelegt“. Der Erfassungsgrund UNGUELTIG_ERFASST kam aber erst mit Revision 0.6 am 18. Oktober 2026 hinzu. Wann die vorliegenden Daten erzeugt wurden, ist nicht dokumentiert. Die Ergänzung ändert weder Rechenregeln noch Bedeutung gültiger Antworten. Sie regelt nur, wie ein unzulässiger Rohwert geführt wird. Bei realen Daten müsste trotzdem offen ausgewiesen werden, dass diese Regel nachträglich zur ursprünglichen Fassung ergänzt wurde.

### 3.4 Zweiter Skriptlauf

```
python3 input/auswertung/score.py work/antworten_korrigiert.json work/ergebnis.json
3 Fälle berechnet (SYNTHETIC_DEMO). Ausgabe: work/ergebnis.json
Exitstatus: 0
```

Ausgabe: calculation_status BERECHNET, total_score null („Nicht vorgesehen.“), interpretation_limit „Künstliche Testdaten; keinerlei empirischer Befund.“, bank_sha256 (kanonisierte Bank laut Skript) c2e7eb3b…2ec080, input_sha256 c1803605…f55f739.

Die mitgelieferten Unittests (laut Codebuch unter tests/) sind nicht Teil der Eingaben und wurden nicht ausgeführt. Sie würden ohnehin nur die Rechenroutine prüfen, nicht diesen Bericht.

### 3.5 Weitere Auffälligkeiten (nicht verändert, nur dokumentiert)

| ID | Auffälligkeit | Betroffene Stellen | Einordnung |
|---|---|---|---|
| P01 | Der gesamte Block L (L01–L03) ist bei allen drei Datensätzen KEINE_ANGABE | L01–L03, 3 von 3 | Kein L-Personenwert möglich. Mögliche Ursachen (Darstellung, Verständnis, bewusste Konstruktion der Demo) sind aus den Daten nicht ableitbar. Nicht als geringes Lernzutrauen werten. |
| P02 | Durchgehend identische Antworten innerhalb der Fähigkeits- und Zustimmungsblöcke | DEMO01: 0–10-Items überwiegend 3, 1–7-Items alle 3; DEMO02: 0–10-Items alle 8, 1–7-Items alle 6; DEMO03: 0–10-Items alle 0, 1–7-Items alle 1 | Typisch für konstruierte Testfälle. Bei realen Daten wäre ein solches Muster ein Hinweis zur Prüfung des Antwortverhaltens, kein Grund zum Ausschluss ohne vorab festgelegte Regel. |
| P03 | DEMO01: U01 = 0, alle anderen gültigen U-Items = 3 | U01–U06 | Nur beschrieben, keine Korrektur. |
| P04 | DEMO02: U01 (Bedienen) NICHT_BEURTEILBAR, U02–U06 jeweils 8 | U01–U06 | Inhaltlich auffällig, weil Bedienen eher Voraussetzung der übrigen Einschätzungen ist. Möglicher Prüfpunkt zum Itemverständnis von U01. Ohne Rückmeldung keine Deutung. |
| P05 | DEMO02: C04 = NO, I01 = 6 und I03 = 6 | C04, I01–I03 | Prüfhinweis des Skripts (siehe 4.4). Keine Korrektur. |
| P06 | Alle drei Fälle haben identische Kontextangaben C01–C06 | C01–C06 | Keine Variation, daher auch keine Gruppenunterscheidung möglich. |
| P07 | W03 bei allen drei Fällen KEINE_ANGABE | W03 | Kein Freitext vorhanden; keine qualitative Zuordnung möglich. |
| P08 | Antwortoberfläche nicht dokumentiert | alle numerischen Items | Ob NB/KA auswählbar waren, ist offen. „0 Fälle NB“ bei einem Item bedeutet daher nicht, dass alle urteilen konnten. Vollständige numerische Zellen belegen kein Verständnis. Bearbeitungszeiten liegen nicht vor. |

---

## 4 Auswertungsbericht (DEMONSTRATION, SYNTHETIC_DEMO, n = 3)

Alle Werte stammen aus work/ergebnis.json. Bei n = 3 genügen laut Codebuch absolute Zahlen. Prozentangaben beziehen sich auf Personen mit gültiger Antwort auf das jeweilige Item.

### 4.1 Kontextfragen C01–C06 (Einzelwahl, jede Frage einzeln)

| Item | Gültig | Fehlend | Verteilung (nur besetzte Kategorien) | Unbesetzte Kategorien |
|---|---|---|---|---|
| C01 Tätigkeit | 3 | 0 | OFFICE (Büro/Bildschirm): 3 | OTHER_WORK, MIXED |
| C02 Nutzungstage berufl., letzte 4 Wochen | 3 | 0 | D0 (an keinem Tag): 3 | D1_3, D4_9, D10_15, D16_PLUS, UNKNOWN |
| C03 Private Nutzung jemals | 3 | 0 | YES: 3 | NO, UNKNOWN |
| C04 Aktueller Zugang, Nutzung erlaubt | 3 | 0 | NO: 3 | YES, UNKNOWN |
| C05 Betriebliche Regeln bekannt | 3 | 0 | NOT_KNOWN (Nein): 3 | KNOWN, PARTLY, EXISTENCE_UNKNOWN |
| C06 Sinnvolle Tätigkeiten im Aufgabenbereich | 3 | 0 | UNKNOWN (kann ich noch nicht beurteilen): 3 | YES, NO |

KEINE_ANGABE und UNGUELTIG_ERFASST: jeweils 0. Die Unsicherheitskategorien (UNKNOWN, EXISTENCE_UNKNOWN) sind reguläre Antworten und werden mitgezählt.

### 4.2 Fähigkeitsselbsteinschätzungen 0–10 (U, K, L, G)

0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt. Zwischenwerte ohne verbale Anker. Werte 1, 2, 4–7, 9 und 10 kamen in keinem Item vor.

| Item | Gültig | NB | KA | UNGUELTIG_ERFASST | Verteilung |
|---|---|---|---|---|---|
| U01 | 2 | 1 | 0 | 0 | 0: 2 |
| U02 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| U03 | 2 | 0 | 0 | 1 | 0: 1 · 8: 1 |
| U04 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| U05 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| U06 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| K01 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| K02 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| K03 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| K04 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| K05 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| K06 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| L01 | 0 | 0 | 3 | 0 | keine gültigen Werte |
| L02 | 0 | 0 | 3 | 0 | keine gültigen Werte |
| L03 | 0 | 0 | 3 | 0 | keine gültigen Werte |
| G01 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| G02 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |
| G03 | 3 | 0 | 0 | 0 | 0: 1 · 3: 1 · 8: 1 |

Hinweis zu C02 = D0: Alle drei Fälle berichten keine berufliche Nutzung in den letzten vier Wochen, aber private Nutzung (C03 = YES). Laut Codebuch kann private Erfahrung zu einer Selbsteinschätzung beitragen. Nichtnutzung setzt Fähigkeitswerte nicht auf null.

### 4.3 Zustimmungsitems 1–7 (A, I)

1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu. Werte 2, 4, 5 und 7 kamen nicht vor.

| Item | Gültig | NB | KA | UNGUELTIG_ERFASST | Verteilung |
|---|---|---|---|---|---|
| A01 vorteilhaft | 3 | 0 | 0 | 0 | 1: 1 · 3: 1 · 6: 1 |
| A02 zufriedenstellend | 3 | 0 | 0 | 0 | 1: 1 · 3: 1 · 6: 1 |
| A03 wichtig | 3 | 0 | 0 | 0 | 1: 1 · 3: 1 · 6: 1 |
| A04 angenehm | 3 | 0 | 0 | 0 | 1: 1 · 3: 1 · 6: 1 |
| I01 plane Nutzung | 3 | 0 | 0 | 0 | 1: 1 · 3: 1 · 6: 1 |
| I02 Absicht | 2 | 0 | 1 | 0 | 1: 1 · 3: 1 |
| I03 werde auf jeden Fall nutzen | 3 | 0 | 0 | 0 | 1: 1 · 3: 1 · 6: 1 |

A erfasst laut Bank eine bedingte Bewertung („wäre“), keine tatsächliche Nutzungsabsicht. I erfasst die Absicht unter tatsächlich erwarteten Arbeitsbedingungen in den nächsten drei Monaten.

### 4.4 Zugelassene Teilbereichsmittelwerte (vorläufige deskriptive Projektwerte)

Regel laut Codebuch: Personenwert nur bei vollständig gültigen Antworten auf alle Items des Teilbereichs. Gruppenwert = Mittel der gültigen Personenwerte. Keine Imputation. Null gültige Fälle ergeben null. G hat ausdrücklich keinen Mittelwert. Es gibt keinen Gesamtwert, keine Gewichtung, keine Klassifikation. 0–10- und 1–7-Werte werden nicht in eine Rangfolge gebracht.

| Teilbereich | Skala | Vollständig | Unvollständig | Mittelwert | Min | Max |
|---|---|---|---|---|---|---|
| U Selbst eingeschätzte Anwendung | 0–10 | 1 | 2 | 0,00 | 0 | 0 |
| K Selbst eingeschätztes Verständnis | 0–10 | 3 | 0 | 3,67 | 0 | 8 |
| L Zutrauen in das eigene Lernen | 0–10 | 0 | 3 | nicht bestimmbar (null) | – | – |
| A Einstellung zur Nutzung | 1–7 | 3 | 0 | 3,33 | 1 | 6 |
| I Berichtete Nutzungsabsicht | 1–7 | 2 | 1 | 2,00 | 1 | 3 |

Gerundet auf zwei Nachkommastellen; Rohwerte im Skript: K 3,6666…, A 3,3333…

**Lesehinweise.**

- **U = 0,00 beruht auf einem einzigen Fall.** DEMO01 (U03 UNGUELTIG_ERFASST) und DEMO02 (U01 NICHT_BEURTEILBAR) fallen durch die Vollständigkeitsregel heraus. Beide haben auf den übrigen U-Items höhere Werte (3 bzw. 8). Der U-Gruppenwert bildet also nur DEMO03 ab und steht im Widerspruch zum Bild der Itemverteilungen. Daran zeigt sich, warum laut Codebuch die Einzelverteilungen die primäre Darstellung bleiben.
- **I = 2,00 beruht auf zwei Fällen.** DEMO02 fehlt wegen KA bei I02. Gerade dieser Fall hat auf I01 und I03 jeweils 6.
- **L ist nicht bestimmbar**, weil kein Fall gültige L-Antworten hat. Das Ergebnis bleibt fehlend und ist nicht 0.
- Personenwerte bleiben laut Codebuch in der Arbeitsdatei (work/ergebnis.json) und werden hier nicht berichtet.

**Prüfhinweis des Skripts** (review_flags): DEMO02, Items C04, I01–I03: „Kein aktueller Zugang und Zustimmung 6 oder 7 zur künftigen Nutzung: erwartete Zugangsänderung prüfen; keine automatische Korrektur.“ Regel laut Skript: „Eigener Plausibilitätshinweis, keine Readiness-Grenze.“ Die Antworten bleiben unverändert. Die Person kann künftigen Zugang erwarten.

### 4.5 Weiterbildungswünsche und Hindernisse (W01, W02; höchstens drei Antworten)

Bezugsgröße: Personen mit gültiger Antwort (je 3). Jede Option zählt höchstens einmal je Person. Summen über 100 Prozent sind möglich und kommen hier vor (4 Nennungen bei 3 Personen je Item). KEINE_ANGABE: je 0.

| W01 Weiterbildungsthema | n | % von 3 |
|---|---|---|
| BASICS Grundlagen generativer KI | 1 | 33,3 |
| USE_CASES Passende Einsatzmöglichkeiten | 0 | 0 |
| PROMPTING Klare Eingaben formulieren, Ergebnisse verbessern | 1 | 33,3 |
| VERIFY Antworten und Quellen überprüfen | 0 | 0 |
| DATA_RULES Betriebliche Regeln, zulässige Dateneingaben | 0 | 0 |
| KEEP_CURRENT Auf dem Laufenden bleiben | 0 | 0 |
| OTHER Anderes Thema | 0 | 0 |
| NONE Derzeit kein Weiterbildungswunsch | 1 | 33,3 |
| UNKNOWN Bedarf noch nicht einschätzbar | 1 | 33,3 |

| W02 Hindernis | n | % von 3 |
|---|---|---|
| ACCESS Kein Zugang zu freigegebenem Werkzeug | 1 | 33,3 |
| RULES Unklare betriebliche Regeln | 1 | 33,3 |
| TIME Zu wenig Zeit | 0 | 0 |
| KNOWLEDGE Fehlendes Wissen über die Nutzung | 0 | 0 |
| TASK_FIT Kein passender Einsatz erkennbar | 0 | 0 |
| RELIABILITY Unsicherheit über Verlässlichkeit | 0 | 0 |
| OTHER Etwas anderes | 0 | 0 |
| NONE Derzeit nichts | 1 | 33,3 |
| UNKNOWN Noch nicht einschätzbar | 1 | 33,3 |

BASICS und PROMPTING stammen von derselben Person; ebenso ACCESS und RULES. Je eine Person wählte NONE beziehungsweise UNKNOWN (exklusiv).

### 4.6 Freitext W03

Gültig 0, KEINE_ANGABE 3. Es gibt keinen Text zum Lesen, Bereinigen oder Zuordnen. Thematische Aussagen sind nicht möglich.

### 4.7 Was diese Auswertung nicht leistet

Keine Reliabilitäts-, Faktoren-, Signifikanz- oder Wirkungsaussagen. Keine Prüfung von Hypothesen. Keine Readiness-Klassen, keine Kompetenzgrenzen, kein Gesamtwert. Keine Aussage über Verständlichkeit des Fragebogens: Dafür fehlen Pretestnotizen, und synthetische Antworten belegen kein Verständnis (vgl. Bisbee et al., 2024, laut Quellen_APA.md zu den Grenzen der Gleichsetzung von LLM-Personas mit realen Befragten).

---

## 5 Maßnahmenmatrix (DEMONSTRATION der Planungslogik)

Grundlage ist die Zuordnungstabelle „Vom Befund zur Maßnahme“ im Codebuch. Sie ist laut Codebuch eine eigene, überprüfbare Planungslogik und liefert mögliche Maßnahmen, keine diagnostischen Entscheidungen über einzelne Beschäftigte. Wo ich über die Tabelle hinausgehe, ist das als eigene Zuordnung gekennzeichnet. Datenart aller Befunde: SYNTHETIC_DEMO, n = 3. Bei realen Daten müssten Teilnahmeumfang, Reichweite und eine Mindestgruppengröße für Berichte festgelegt sein.

### 5.1 Befundliste

| Befund-ID | Typ | Items | Beobachtung (Anzahl / Bezugsgröße) |
|---|---|---|---|
| B01 | Organisatorischer Handlungsbedarf | C04, W02 | C04 = NO: 3/3. W02 = ACCESS: 1/3 |
| B02 | Organisatorischer Handlungsbedarf, Orientierung | C05, W02 | C05 = NOT_KNOWN: 3/3. W02 = RULES: 1/3 |
| B03 | Offene Frage, Aufgabenpassung | C06, W02 | C06 = UNKNOWN: 3/3. W02 = TASK_FIT: 0/3 |
| B04 | Geäußerter Lernwunsch | W01 | BASICS: 1/3. PROMPTING: 1/3 (dieselbe Person) |
| B05 | Kein bzw. noch unklarer Lernwunsch | W01, W02 | W01 NONE: 1/3, UNKNOWN: 1/3. W02 NONE: 1/3, UNKNOWN: 1/3 |
| B06 | Offene Frage, Datenlage | L01–L03 | KEINE_ANGABE: 3/3 je Item; L-Wert für 0 Fälle |
| B07 | Offene Frage, Einschätzbarkeit | U01 | NICHT_BEURTEILBAR: 1/3; Fall hat U02–U06 je 8 |
| B08 | Aus Selbsteinschätzung abgeleiteter möglicher Lernbedarf (Hypothese) | U, K, G, W01 | Je Item 0–10 eine Person bei 0, eine bei 3, eine bei 8. Kein Fall wünscht VERIFY; W02 RELIABILITY: 0/3 |
| B09 | Prüfhinweis | C04, I01–I03 | 1 Fall: kein Zugang, I01 und I03 je 6 |
| B10 | Offene Frage, Ablehnung oder fehlende Grundlage | A01–A04, I01–I03, W01, W02 | A-Items je 1/3 mit Wert 1; I01, I02, I03 je 1/3 mit Wert 1 |

### 5.2 Empfehlungen

Priorisierung ist eine begründete Planungsentscheidung, keine validierte Entscheidungsregel. Logik: Zuerst kommen Voraussetzungen, die alle Fälle betreffen und ohne die Lernangebote ins Leere laufen (Zugang, Regeln). Dann folgen ausdrücklich geäußerte Wünsche. Abgeleitete Hypothesen und offene Fragen kommen danach. Für keine Maßnahme ist eine Wirksamkeit belegt.

**M01 · Zugang klären** (Priorität 1)
- Befundgrundlage: B01 (C04 = NO 3/3; W02 = ACCESS 1/3).
- Interpretationsregel: Codebuch-Zeile „C04 = NO oder W02 = ACCESS → Organisatorisches Hindernis. Freigegebene Zugangsmöglichkeiten klären; keine Kompetenzlücke behaupten.“
- Organisatorisches Ziel: Es ist geklärt und kommuniziert, ob und welches freigegebene Werkzeug für welche Tätigkeiten verfügbar ist.
- Zielgruppe: alle Befragten ohne Zugang (hier 3/3).
- Maßnahme: Bestandsaufnahme vorhandener oder geplanter freigegebener Anwendungen; Zuständigkeit benennen; Ergebnis allen Beschäftigten mitteilen.
- Unsicherheit: C04 erfasst die Wahrnehmung der Befragten. Ob tatsächlich kein Zugang besteht oder er nur unbekannt ist, zeigen die Daten nicht. Synthetische Daten.
- Erfolgskontrolle: Bei einer Folgebefragung mit derselben Version C04 erneut betrachten; zusätzlich prüfen, ob eine schriftliche Zugangsinformation vorliegt.

**M02 · Regeln verständlich bereitstellen und Zuständigkeit klären** (Priorität 1)
- Befundgrundlage: B02 (C05 = NOT_KNOWN 3/3; W02 = RULES 1/3).
- Interpretationsregel: Codebuch-Zeile „W01 = DATA_RULES oder C05 = NOT_KNOWN / EXISTENCE_UNKNOWN → Orientierung und möglicherweise Organisation“. W02 = RULES steht nicht in der Tabelle; die Zuordnung zu diesem Befund ist meine eigene, gestützt auf die Masterprompt-Regel „Unklare Regeln führen zu Orientierung und Zuständigkeitsklärung“.
- Organisatorisches Ziel: Beschäftigte wissen, ob Regeln existieren, wo sie stehen und wen sie fragen können.
- Zielgruppe: alle (hier 3/3).
- Maßnahme: Erst prüfen, ob betriebliche Regeln tatsächlich vorhanden sind. Falls ja: kurze, verständliche Fassung und Ansprechperson. Falls nein: Erarbeitung anstoßen. G03 (zulässige Eingaben) kann ergänzend beschrieben werden (0: 1, 3: 1, 8: 1), ist aber kein Wissensnachweis.
- Unsicherheit: „Nein“ in C05 unterscheidet nicht, ob Regeln fehlen oder unbekannt sind. Synthetische Daten.
- Erfolgskontrolle: C05 in einer Folgeerhebung; Verfügbarkeit und Auffindbarkeit der Regel dokumentieren.

**M03 · Aufgabenpassung gemeinsam klären** (Priorität 2)
- Befundgrundlage: B03 (C06 = UNKNOWN 3/3; TASK_FIT 0/3; W01 USE_CASES 0/3).
- Interpretationsregel: Die Codebuch-Zeile nennt nur C06 = NO oder TASK_FIT. UNKNOWN ist dort nicht zugeordnet. Eigene Zuordnung als offene Frage: Die Daten zeigen weder Passung noch fehlende Passung. Nutzung kann sachlich unnötig sein.
- Organisatorisches Ziel: Für die vertretenen Tätigkeiten (hier nur OFFICE) ist geklärt, ob es sinnvolle und zulässige Anwendungsfälle gibt.
- Zielgruppe: Tätigkeitsbereiche mit C06 = UNKNOWN.
- Maßnahme: Kurzer Austausch mit Fachbereichen über konkrete Aufgaben, erst nach M01 und M02, damit Beispiele zu tatsächlich erlaubten Werkzeugen passen. Kein Schulungsangebot vor dieser Klärung.
- Unsicherheit: Ohne Freitext (W03 0/3) keine Hinweise auf konkrete Aufgaben.
- Erfolgskontrolle: Dokumentierte Liste geprüfter Anwendungsfälle; C06 und W03 in einer Folgeerhebung.

**M04 · Einführung und Übung zu Eingaben für Personen mit diesem Wunsch** (Priorität 2, abhängig von M01)
- Befundgrundlage: B04 (BASICS 1/3; PROMPTING 1/3, dieselbe Person).
- Interpretationsregel: Codebuch-Zeilen „W01 = BASICS → Einführung anbieten; Vorkenntnisse und Aufgaben prüfen“ und „W01 = PROMPTING → Übung zu Eingaben und Überarbeitung; passendes Werkzeug voraussetzen“.
- Lernziel: Teilnehmende können erklären, was generative KI leistet und wo ihre Grenzen liegen, und an einer eigenen Arbeitsaufgabe eine Eingabe formulieren und das Ergebnis überarbeiten.
- Zielgruppe: Personen, die BASICS oder PROMPTING wählen (hier 1 von 3).
- Maßnahme: Kurze Einführung; Übungsteil erst, wenn ein freigegebenes Werkzeug verfügbar ist (C04 = NO bei allen Fällen).
- Unsicherheit: Dieselbe Person schätzt U02–U06 und K01–K06 jeweils mit 8 ein und wünscht trotzdem Grundlagen. Das widerspricht sich nicht zwingend, ist aber ohne Rückmeldung nicht deutbar. Selbsteinschätzungen sind kein objektiver Kompetenznachweis.
- Erfolgskontrolle: Praktische Übungsaufgabe mit vorher festgelegten Kriterien; Rückmeldung der Teilnehmenden; keine Rückschlüsse aus einer Wiederholung derselben Selbsteinschätzungsitems allein.

**M05 · Lernzutrauen (L) nicht interpretieren, Ursache klären** (Priorität 3)
- Befundgrundlage: B06 (L01–L03 KA 3/3).
- Interpretationsregel: Masterprompt Phase 6, offene Frage: Die Daten liefern keine Erklärung. KA ist keine niedrige Ausprägung.
- Ziel: Klären, ob der L-Block angezeigt, verstanden und beantwortbar war.
- Zielgruppe: Projektteam beziehungsweise Erhebungsverantwortliche.
- Maßnahme: Antwortoberfläche und Erfassungsprozess für L01–L03 prüfen. Bei realen Daten im nächsten Pretest gezielte, neutrale Nachfrage zu diesem Block. Keine Maßnahme für Befragte daraus ableiten.
- Unsicherheit: Bei synthetischen Daten kann das Muster bewusst konstruiert sein.
- Erfolgskontrolle: Dokumentierter Oberflächenabgleich; Anteil KA in L bei der nächsten Erhebung.

**M06 · Einschätzbarkeit von U01 beobachten** (Priorität 3)
- Befundgrundlage: B07 (U01 NB 1/3).
- Interpretationsregel: Codebuch-Zeile „Viele NB-Antworten auf einem Fähigkeitsitem → Erst Frageverständnis und Erfahrungsgrundlage prüfen; nicht als niedrige Kompetenz zählen.“ Hier: 1 NB bei 3 Fällen. Ob das „viele“ sind, wird nicht über einen Grenzwert entschieden.
- Ziel: Verstehen, ob „bedienen“ bei Personen ohne beruflichen Zugang eindeutig ist.
- Maßnahme: Im Pretestleitfaden eine neutrale Nachfrage zu U01 vorsehen. Keine Itemänderung ohne Pretestbefund und neue Version.
- Unsicherheit: Ein synthetischer Fall.
- Erfolgskontrolle: NB-Anzahl und Pretestnotizen zu U01.

**M07 · Abgeleiteter Lernbedarf zur Ergebnisprüfung als Hypothese** (Priorität 3)
- Befundgrundlage: B08 (G01, G02: je eine Person 0, eine 3, eine 8; VERIFY 0/3; RELIABILITY 0/3).
- Interpretationsregel: Codebuch-Zeile „Bestimmte Fähigkeitsantworten und passender Lernwunsch → Vertiefenden Lernbedarf als Hypothese formulieren“. Ein passender Lernwunsch liegt hier nicht vor. Deshalb wird kein Lernbedarf festgestellt, nur eine Hypothese festgehalten.
- Lernziel (falls später bestätigt): Antworten generativer KI an Arbeitsbeispielen gegen unabhängige Quellen prüfen.
- Zielgruppe: Offen. Es gibt keine empirisch geprüften Grenzwerte; niedrige Selbsteinschätzungen machen niemanden „nicht kompetent“.
- Maßnahme: Bei späterem Zugang eine freiwillige praktische Prüfaufgabe zur Abklärung anbieten.
- Unsicherheit: Hoch. Selbsteinschätzung, n = 3, synthetisch.
- Erfolgskontrolle: Ergebnis der praktischen Aufgabe nach vorab festgelegten Kriterien.

**M08 · Zurückhaltung und Prüfhinweis nicht als Defizit werten** (offene Fragen)
- Befundgrundlage: B05, B09, B10.
- Interpretationsregel: Masterprompt Phase 6: „Eine kritisch begründete Ablehnung wird nicht automatisch zum Schulungsdefizit.“ Codebuch: C04 = NO mit I 6 oder 7 erzeugt nur einen Prüfhinweis.
- Beobachtung: Ein Fall antwortet bei allen A- und I-Items mit 1, bei allen Fähigkeitsitems mit 0 und bei W01/W02 mit UNKNOWN. Ein Fall wählt bei W01 und W02 NONE. Ein Fall plant trotz fehlenden Zugangs Nutzung (I01, I03 je 6).
- Maßnahme: Keine personenbezogene Maßnahme. Gründe sind ohne Freitext unbekannt; Ablehnung, fehlende Aufgabenpassung und fehlender Zugang sind nicht unterscheidbar. Erst M01 bis M03 umsetzen, dann bei einer realen Erhebung erneut betrachten.
- Unsicherheit: Hoch.
- Erfolgskontrolle: Nicht sinnvoll festlegbar, solange die Ursache offen ist.

Nicht angesetzte Maßnahmen: TIME (0/3), KNOWLEDGE (0/3), USE_CASES (0/3), KEEP_CURRENT (0/3), DATA_RULES (0/3) wurden nicht gewählt. Daraus folgt nur, dass diese drei Demonstrationsfälle sie nicht genannt haben.

---

## 6 Änderungsprotokoll dieses Laufs

| Nr. | Schritt | Datei | Art |
|---|---|---|---|
| 1 | Skriptlauf mit Originaldaten, Exit 2 | input/antworten.json | Nur gelesen |
| 2 | Vollständige eigene Vorprüfung | work/pruefung.py | Neues Prüfskript |
| 3 | Umkodierung DEMO01/U03 von 12 auf UNGUELTIG_ERFASST | work/antworten_korrigiert.json | Arbeitskopie; Original unverändert |
| 4 | Korrekturprotokoll KP-01 | work/korrekturprotokoll.json | Neu |
| 5 | Skriptlauf, Exit 0 | work/ergebnis.json | Ergebnisdatei |

Keine Änderungen an Itembank, Codebuch, Skript oder Fragebogenversion. Keine Imputation, keine Umpolung (die Bank enthält keine umgepolten Items), keine nachträglich erfundenen Grenzwerte.

## 7 Rückfragen an die Auftraggeberin (gebündelt)

1. **Herkunft der Demonstrationsdaten:** Wurden die drei Fälle von Hand konstruiert oder durch eine KI-Persona erzeugt (dann LLM_PERSONA mit Persona-Prompt, Formular und Modell dokumentieren)? War der Wert 12 bei DEMO01/U03 ein absichtlich eingebauter Prüffall?
2. **Erfassung:** Auf welcher Oberfläche und an welchem Datum wurden die Werte erfasst, und waren NB und KA dort auswählbar? Davon hängt ab, wie die Fehlwerte, besonders der vollständig fehlende L-Block, zu lesen sind, und ob Revision 0.6 vor der Erfassung galt.
3. **Reale Anwendung:** Für einen Bericht mit SURVEY-Daten werden Erhebungsinformation, Teilnahmeumfang, Reichweite und eine Mindestgruppengröße für Gruppenberichte benötigt. Gibt es dazu schon Festlegungen?

Alle Teile, die ohne Antwort möglich sind, sind oben erledigt.

## 8 Nächste konkret erforderliche Eingaben

- Für eine echte Auswertung: Antwortdaten mit data_kind SURVEY (oder PRETEST), Version GARI-DE-0.1, plus Angaben zur Erhebung.
- Für die Deutung der Fehlwerte: Begleitmanifest der tatsächlich verwendeten Oberfläche mit Oberflächenabgleich.
- Für eine Prüfung der Rechenroutine: den Testordner tests/, falls diese Prüfung im Lauf gewünscht ist.

## 9 Literatur (APA; Inhalte nur laut Quellenstatus in Quellen_APA.md, in dieser Sitzung nicht im Original eingesehen)

Bisbee, J., Clinton, J. D., Dorff, C., Kenkel, B., & Larson, J. M. (2024). Synthetic replacements for human survey data? The perils of large language models. *Political Analysis, 32*(4), 401–416. https://doi.org/10.1017/pan.2024.5

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://hdl.handle.net/10125/108952

Ein DOI ersetzt keine Prüfung des behaupteten Inhalts. Die Zuordnungen zu Items stammen aus der Itembank.

---

## Status

- **Erstellt:** Prüfbericht, Korrekturprotokoll, Auswertungsbericht mit Itemverteilungen und zugelassenen Teilbereichswerten, Maßnahmenmatrix als Demonstration, Rückfragen.
- **Geprüft:** Version, IDs, Dubletten, Wertebereiche, Optionen, Mehrfachwahlregeln und Fehlwertgründe für alle 3 Datensätze und 34 Items, mit Skript und eigenem Prüfskript.
- **Berechnet:** Ja, mit score.py (Exit 0) auf der dokumentierten Arbeitskopie. Status BERECHNET, Datenart SYNTHETIC_DEMO.
- **Nicht geprüft oder nicht vorhanden:** Antwortoberfläche und Verfügbarkeit von NB/KA, Herkunft der synthetischen Daten, Unittests, Verständlichkeit der Items, jede psychometrische Eigenschaft, jede Hypothese.
- **Kein empirisches Ergebnis:** Dieser Bericht beschreibt künstliche Testdaten. Er belegt nichts über reale Beschäftigte und ersetzt weder Pretest noch Befragung.
