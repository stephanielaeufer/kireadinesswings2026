# Auswertungsbericht GARI-DE-0.1: Datenprüfung, Berechnung und Maßnahmen

**Datenart: SYNTHETIC_DEMO.** Alle Zahlen in diesem Bericht beschreiben künstliche Testdatensätze. Sie sind kein empirischer Befund über Beschäftigte, ein Unternehmen oder eine Berufsgruppe.

## 0. Kurzfassung

- Die gelieferte Datei `antworten.json` passt formal zu Fragebogen und Codebuch GARI-DE-0.1 (Datei- und Personenebene, 34 IDs je Person, keine doppelten Kürzel).
- Der reguläre Lauf von `auswertung/score.py` ist **abgebrochen (Exitstatus 2)**. Grund: `DEMO01/U03` enthält den Wert 12. Die Skala ABILITY_0_10 erlaubt nur ganze Zahlen von 0 bis 10.
- **Status des regulären Ergebnisses für die gelieferte Datei: NICHT_BERECHNET.** Ich habe den Wert nicht korrigiert.
- Damit die eindeutig auswertbaren Teile trotzdem bearbeitet werden, habe ich zwei offen gekennzeichnete Arbeitskopien gerechnet (Abschnitt 4). Diese Teilauswertung ist **kein reguläres Ergebnis** der gelieferten Datei. Sie bleibt vorläufig, bis U03 für DEMO01 geklärt ist.
- L01–L03 und W03 haben bei allen drei Datensätzen keine gültige Antwort (je 3 × KEINE_ANGABE). Teilbereich L ist deshalb fehlend (`null`), nicht 0.
- Die Maßnahmenmatrix (Abschnitt 6) zeigt nur, wie die Planungslogik des Codebuchs mit solchen Daten arbeitet. Sie ist keine Empfehlung für eine reale Organisation.

## 1. Ziel, Kontext und Annahmen

| Angabe | Inhalt |
|---|---|
| Betriebsart | AUSWERTEN (ausdrücklich angegeben) |
| Auftrag | Datenprüfung, Berechnung und Maßnahmenbericht |
| Fragebogenversion | GARI-DE-0.1 (Itembank vom 29.09.2026) |
| Codebuch | `instrument/Codebuch.md`, Projektpaket 0.2, Stand 29.09.2026, redaktionell fortgeschrieben 17.10.2026 |
| Promptversion | Masterprompt 0.5 vom 17.10.2026 |
| Datenart | SYNTHETIC_DEMO (Feld `data_kind` der Datei) |
| Herkunft der synthetischen Daten | NICHT_DOKUMENTIERT. Die Datei sagt nicht, ob es sich um von Hand konstruierte Rechentestfälle oder um LLM-Persona-Antworten (LLM_PERSONA) handelt. Es gibt kein Herkunftsfeld, keinen Erzeugungsprompt und kein Formularprotokoll. |
| Zielpopulation, Unternehmen, Tätigkeitsbereiche | Für diesen Datensatz nicht anwendbar. Kein Briefing beigefügt. Ich ergänze keine Unternehmensmerkmale. |
| Antwortoberfläche | Unbekannt. Für synthetische Daten gibt es keine Erhebungsoberfläche, deren NB-/KA-Verfügbarkeit ich prüfen könnte. |
| Datum des Laufs | 18. Oktober 2026 |
| System und Modell | Claude (Anthropic), Modellbezeichnung laut Systemangabe: Claude Opus 5.5, Kennung `claude-opus-5-5`. Weitere Systemparameter (z. B. Temperatur): NICHT_VERFUEGBAR. Gleiche Prompts garantieren keine identischen Ausgaben. |
| Laufzeit | Python 3.13.16, keine Zusatzpakete |
| Quellenstand | `Quellen_APA.md`, Stand 17.10.2026; Quellenregister in der Itembank |

Annahme: Da kein Briefing vorliegt, verstehe ich den Auftrag als technische Demonstration der Auswertungskette (Prüfung, Berechnung, Ableitung). Das ist eine eigene Einordnung.

## 2. Quellen- und Konstruktgrundlage mit Evidenzgrenzen

Ich habe in diesem Lauf keine Originalquellen eingesehen. Die folgenden Angaben stammen aus der Itembank (`source_register`, Itemfelder) und aus `Quellen_APA.md`. Sie geben den dort dokumentierten Prüfstand wieder, keine eigene Neuprüfung.

| Teilbereich / Items | Herkunft laut Itembank | Status | Evidenzgrenze |
|---|---|---|---|
| U01–U06, K01–K06, L01–L03 | MAILS, deutscher Autorenfragebogen (Carolus et al., 2023), Items 1–6, 7–12, 26–28 | ADAPTIERT | Original betrifft allgemeine KI und 300 deutschsprachige Erwachsene. Eingrenzung auf generative KI und zusätzliche NB/KA-Optionen sind Anpassungen. Die Regel „nur vollständige Antworten“ ist eine eigene Projektregel, keine MAILS-Vorschrift. |
| G01–G03 | Eigenentwicklung | NEU_ENTWICKELT | Drei Einzelitems, keine Skala, kein G-Mittelwert. Noch nicht empirisch geprüft. |
| A01–A04, I01–I03 | Bereitgestellte Itemsammlung zu Wichmann et al. (2025), PowerPilot | ADAPTIERT | Übersetzt, Technologie, Arbeitskontext und Zeitraum geändert. Geprüft anhand der bereitgestellten Itemsammlung. **Der direkte Vergleich mit dem OSF-Anhang (https://doi.org/10.17605/OSF.IO/GEBK9) bleibt offen.** |
| C01–C06, W01–W03 | Eigenentwicklung | NEU_ENTWICKELT | Kontext-, Wunsch- und Hindernisfragen, keine Skalen. |

Keine der Zusammenfassungen U, K, L, A, I ist als GenAI-Skala validiert. Es gibt keine psychometrische Validierung der Kombination (vgl. Boateng et al., 2018, zur Trennung von Itementwicklung und Prüfung der Messqualität).

## 3. Datenprüfung

### 3.1 Eingesetzte Dateien und Prüfsummen (SHA-256)

| Datei | SHA-256 |
|---|---|
| `antworten.json` | `3fa736848c84a83b08eab11e88d26ce31516c2d20df90b8d80777817503673f5` |
| `instrument/Itembank_GARI_DE_0.1.json` (Datei) | `12582782e64397d3460e88c2f4b2425b062f1f1c33725fc2d9953f5067afd050` |
| Itembank, kanonischer Hash laut `score.py` (`bank_sha256`) | `c2e7eb3ba5f7505a9418ac1cd21b1847ae7e84f4cdd799db3ccfc8107c2ec080` |
| `auswertung/score.py` | `cccab0a8e9c2b55b40302a14ca8dbd2acd4493c821a8171df47788d41f8686c5` |

### 3.2 Regulärer Lauf von score.py

Befehl (im Ordner `input/`):

```bash
python3 auswertung/score.py antworten.json ../work/ergebnis.json
```

Tatsächliche Ausgabe:

```text
Datenprüfung fehlgeschlagen: DEMO01/U03: Ungültiger Skalenwert.
```

Exitstatus: **2**. Es wurde keine Ergebnisdatei erzeugt. `score.py` bricht beim ersten Fehler ab. Deshalb habe ich zusätzlich ein eigenes, nur lesendes Prüfskript (`work/pruefung.py`) mit denselben Regeln laufen lassen, das alle Auffälligkeiten sammelt statt abzubrechen. Es fand **genau einen** blockierenden Fehler.

### 3.3 Prüfbericht

| Prüfpunkt | Ergebnis |
|---|---|
| `data_kind` | SYNTHETIC_DEMO, zulässig |
| `questionnaire_version` Dateiebene | GARI-DE-0.1, passt zur Bank |
| `questionnaire_version` Personenebene | 3 × GARI-DE-0.1, passt |
| Anzahl Datensätze | 3 (DEMO01, DEMO02, DEMO03) |
| Doppelte Testkürzel | keine |
| Inhaltlich identische Datensätze | keine |
| Item-IDs je Person | alle 34 vorhanden, keine unbekannten IDs |
| Struktur `value` / `missing_reason` | bei allen 102 Antworten korrekt |
| Widerspruch Wert und Fehlwertgrund | keiner |
| Fehlwertgründe | nur NICHT_BEURTEILBAR und KEINE_ANGABE; keine unzulässigen Gründe (kein NICHT_ZUTREFFEND, kein UEBERSPRUNGEN) |
| Einzelwahl C01–C06 | alle Kategorien zulässig |
| Mehrfachwahl W01, W02 | nichtleere Listen, höchstens 3, keine Doppelungen, exklusive Optionen (NONE, UNKNOWN) jeweils allein gewählt |
| Freitext W03 | 3 × KEINE_ANGABE, kein Inhalt zu prüfen |
| Ganzzahlige Skalenwerte | **1 Fehler: DEMO01/U03 = 12, zulässig 0–10** |
| Filter | GARI-DE-0.1 hat keine Filter. Keine widersprüchlichen Filter möglich. |

**Fehler F-01: DEMO01/U03 = 12.** Der Wert liegt außerhalb der Skala. Ich kann nicht erkennen, was gemeint war (z. B. Tippfehler für 1 oder 2, absichtlich eingebauter Prüffall oder etwas anderes). Laut Codebuch wird nichts still repariert und nie selbst eine Antwort ausgewählt. Ich setze deshalb **keinen Ersatzwert** ein. Die Klärung braucht die Person, die die Daten erzeugt hat.

### 3.4 Weitere Auffälligkeiten (keine Fehler, nicht verändert)

| ID | Auffälligkeit | Einordnung |
|---|---|---|
| P-01 | L01–L03: bei allen 3 Datensätzen KEINE_ANGABE (9 von 9 Zellen) | Kein Personenwert L möglich. Kann bei synthetischen Daten gewollt sein. Bei realen Daten wäre zuerst zu prüfen, ob der Block angezeigt, ausgefüllt und korrekt exportiert wurde. Ein Motiv wird nicht ergänzt. |
| P-02 | W03: bei allen 3 Datensätzen KEINE_ANGABE | Keine qualitative Zuordnung möglich. |
| P-03 | C01–C06 bei allen drei Datensätzen identisch: OFFICE, D0, YES, NO, NOT_KNOWN, UNKNOWN | Keine Variation im Kontext. Gruppenvergleiche nach Tätigkeit oder Zugang sind nicht möglich. |
| P-04 | Gleichförmige Antwortblöcke: DEMO01 hat 20 von 25 numerischen Antworten = 3; DEMO02 hat 14 × 8 und 6 × 6; DEMO03 hat 15 × 0 und 7 × 1 | Hinweis auf schematisch konstruierte Antworten. Keine automatische Entfernung. Bei realen Daten wäre das ein Prüfhinweis, kein Ausschlussgrund ohne vorab festgelegte Regel. |
| P-05 | DEMO02: C04 = NO (kein Zugang), aber I01 = 6 und I03 = 6 | Von `score.py` ausgegebener Prüfhinweis (siehe 4.5). Keine Korrektur. |
| P-06 | DEMO01: C04 = NO und C05 = NOT_KNOWN, aber W02 = NONE („Derzeit nichts“ erschwert den Einsatz) | Kein Widerspruch im Sinne der Regeln. Fehlender Zugang muss nicht als Hindernis erlebt werden, etwa wenn kein Bedarf besteht (C06 = UNKNOWN). Nur als Nachfragepunkt notiert. |
| P-07 | DEMO02: C02 = D0 (keine berufliche Nutzung), aber U-Werte 8 | Laut Codebuch zulässig. Private Erfahrung (C03 = YES) kann zur Selbsteinschätzung beitragen. |
| P-08 | DEMO01: U01 = 0, die übrigen gültigen U-Werte = 3 | Nur notiert. Keine Plausibilitätsregel im Codebuch. |
| P-09 | NB-Antworten: 1 von 54 Zellen der Fähigkeitsitems U, K, L, G (DEMO02/U01); über alle 75 numerischen Zellen ebenfalls 1 | Bei synthetischen Daten sagt die Zahl nichts darüber, ob NB auf einer Oberfläche wählbar war. |
| P-10 | Keine Zeitstempel | Keine Aussage zur Bearbeitungsdauer möglich. |

## 4. Berechnung

### 4.1 Vorgehen bei der Teilauswertung (Abweichung, offen ausgewiesen)

Der Masterprompt verlangt, die übrigen eindeutig auswertbaren Teile zu bearbeiten. Das Codebuch erlaubt keine Reparatur. Ich habe deshalb die Originaldatei unverändert gelassen und zwei Arbeitskopien in `work/` gerechnet. Beide Läufe nutzen das unveränderte `score.py` mit der unveränderten Bank.

| Variante | Änderung gegenüber `antworten.json` | Zweck | Exitstatus | Prüfsumme der Kopie |
|---|---|---|---|---|
| B (Hauptdarstellung) | Nur DEMO01/U03: Wert 12 ausgeklammert. Technisch als `value: null` mit `missing_reason: "KEINE_ANGABE"` eingetragen, weil das Datenformat keinen Grund „ungültiger Wert“ kennt. | Alle übrigen 101 Antworten bleiben in der Auswertung. | 0, „3 Fälle berechnet (SYNTHETIC_DEMO)“ | `1224939dcd63008f4034aa1c708d94691924794d998ebdab4d0c278ad740aec6` |
| A (Kontrolle) | Datensatz DEMO01 vollständig entfernt | Zeigt, wie stark die Werte an DEMO01 hängen. | 0, „2 Fälle berechnet (SYNTHETIC_DEMO)“ | `a8f3dee65c7ac9ead969b4c3be992c453dd1afbfdfd1c626a168b3c855088c07` |

Wichtig zu Variante B: Der Eintrag KEINE_ANGABE ist ein **technischer Platzhalter**. Inhaltlich bedeutet er „ungültiger Wert 12, ausgeklammert“. In allen Tabellen unten weise ich diesen Fall deshalb gesondert als „ungültig“ aus und nicht als echte KA. Diese Ausklammerung ist keine Korrektur der Daten. Sie ersetzt keine Klärung nach Codebuch (Korrekturprotokoll). Sobald der richtige Wert feststeht, muss der reguläre Lauf mit der korrigierten Originaldatei wiederholt werden. Ändert sich U03 für DEMO01, ändern sich die Verteilung von U03 und möglicherweise Teilbereich U.

Rechenregeln laut Codebuch, unverändert angewandt: Personenwert = arithmetisches Mittel nur bei vollständigen gültigen Antworten im Teilbereich. Gruppenwert = Mittel der gültigen Personenwerte. Keine Imputation. Keine Umkodierung (keine umgepolten Items). Kein Gesamtwert. 0–10 und 1–7 werden nicht verglichen.

Alle Zahlen in 4.2 bis 4.5 stammen aus `work/ergebnis_B_U03_KA.json` bzw. `work/ergebnis_A_ohne_DEMO01.json`. Die von mir gerundeten Werte (eine Nachkommastelle bei Prozent, zwei bei Mittelwerten) sind Rundungen dieser Ausgabe.

### 4.2 Kontextfragen C01–C06 (Variante B, n = 3)

| Item | Gültig | KA | Verteilung |
|---|---|---|---|
| C01 Tätigkeit | 3 | 0 | OFFICE 3; OTHER_WORK 0; MIXED 0 |
| C02 Berufliche Nutzungstage, 4 Wochen | 3 | 0 | D0 3; D1_3 0; D4_9 0; D10_15 0; D16_PLUS 0; UNKNOWN 0 |
| C03 Private Nutzung jemals | 3 | 0 | YES 3; NO 0; UNKNOWN 0 |
| C04 Aktueller Zugang | 3 | 0 | YES 0; NO 3; UNKNOWN 0 |
| C05 Kenntnis betrieblicher Regeln | 3 | 0 | KNOWN 0; PARTLY 0; NOT_KNOWN 3; EXISTENCE_UNKNOWN 0 |
| C06 Sinnvolle Tätigkeiten vorhanden | 3 | 0 | YES 0; NO 0; UNKNOWN 3 |

Die Unsicherheitsoptionen (z. B. C06 UNKNOWN) sind laut Codebuch reguläre Antwortkategorien und hier mitgezählt.

### 4.3 Numerische Items: Verteilungen (Variante B)

Skala 0–10 für U, K, L, G; Skala 1–7 für A, I. Nicht genannte Skalenwerte haben die Häufigkeit 0.

| Item | Gültig | NB | KA | Ungültig ausgeklammert | Verteilung (Wert: Anzahl) |
|---|---|---|---|---|---|
| U01 | 2 | 1 | 0 | 0 | 0: 2 |
| U02 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| U03 | 2 | 0 | 0 | 1 (DEMO01, Wert 12) | 0: 1; 8: 1 |
| U04 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| U05 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| U06 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| K01 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| K02 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| K03 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| K04 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| K05 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| K06 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| L01 | 0 | 0 | 3 | 0 | keine gültigen Werte |
| L02 | 0 | 0 | 3 | 0 | keine gültigen Werte |
| L03 | 0 | 0 | 3 | 0 | keine gültigen Werte |
| G01 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| G02 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| G03 | 3 | 0 | 0 | 0 | 0: 1; 3: 1; 8: 1 |
| A01 | 3 | 0 | 0 | 0 | 1: 1; 3: 1; 6: 1 |
| A02 | 3 | 0 | 0 | 0 | 1: 1; 3: 1; 6: 1 |
| A03 | 3 | 0 | 0 | 0 | 1: 1; 3: 1; 6: 1 |
| A04 | 3 | 0 | 0 | 0 | 1: 1; 3: 1; 6: 1 |
| I01 | 3 | 0 | 0 | 0 | 1: 1; 3: 1; 6: 1 |
| I02 | 2 | 0 | 1 | 0 | 1: 1; 3: 1 |
| I03 | 3 | 0 | 0 | 0 | 1: 1; 3: 1; 6: 1 |

Hinweis zu U03: `score.py` zählt den ausgeklammerten Fall in Variante B technisch unter KEINE_ANGABE (1). In dieser Tabelle steht er korrekt als „ungültig“.

### 4.4 Vorläufige Teilbereichswerte U, K, L, A, I

Nur für die im Codebuch zugelassenen fünf Teilbereiche. G01–G03 sind Einzelitems (Verteilungen in 4.3). Für G, C und W sowie über alle Bereiche gibt es keinen Wert.

**Variante B (3 Datensätze, DEMO01/U03 ausgeklammert):**

| Teilbereich | Spanne | Vollständig | Unvollständig | Mittelwert der Personenwerte | Min | Max |
|---|---|---|---|---|---|---|
| U Selbst eingeschätzte Anwendung | 0–10 | 1 | 2 | 0,00 | 0 | 0 |
| K Selbst eingeschätztes Verständnis | 0–10 | 3 | 0 | 3,67 | 0 | 8 |
| L Zutrauen in das eigene Lernen | 0–10 | 0 | 3 | fehlend (`null`) | – | – |
| A Einstellung zur Nutzung | 1–7 | 3 | 0 | 3,33 | 1 | 6 |
| I Berichtete Nutzungsabsicht | 1–7 | 2 | 1 | 2,00 | 1 | 3 |

Gründe für unvollständige Fälle:

- U: DEMO01 (U03 ungültig, ausgeklammert), DEMO02 (U01 = NICHT_BEURTEILBAR). Der U-Wert beruht damit auf **einem** Datensatz (DEMO03).
- L: alle drei wegen KEINE_ANGABE auf L01–L03.
- I: DEMO02 (I02 = KEINE_ANGABE). Der I-Mittelwert enthält DEMO02 deshalb nicht, obwohl DEMO02 bei I01 und I03 jeweils 6 angibt.

Personenwerte aus der Arbeitsdatei (nur weil synthetisch; ein realer Bericht würde nur aggregieren):

| Datensatz | U | K | L | A | I |
|---|---|---|---|---|---|
| DEMO01 | fehlend | 3 | fehlend | 3 | 3 |
| DEMO02 | fehlend | 8 | fehlend | 6 | fehlend |
| DEMO03 | 0 | 0 | fehlend | 1 | 1 |

**Kontrollvariante A (ohne DEMO01, 2 Datensätze):**

| Teilbereich | Vollständig | Unvollständig | Mittelwert | Min | Max |
|---|---|---|---|---|---|
| U | 1 | 1 | 0,00 | 0 | 0 |
| K | 2 | 0 | 4,00 | 0 | 8 |
| L | 0 | 2 | fehlend (`null`) | – | – |
| A | 2 | 0 | 3,50 | 1 | 6 |
| I | 1 | 1 | 1,00 | 1 | 1 |

Lesart: Bei drei bzw. zwei Fällen hängen die Mittelwerte vollständig an einzelnen Datensätzen. Der I-Mittelwert springt je nach Variante zwischen 2,00 und 1,00, weil nur ein oder zwei Personenwerte eingehen. Die Mittelwerte sind deshalb kaum aussagekräftig. Die Einzelverteilungen bleiben die primäre Darstellung. Die Mittelwerte setzen gleichabständige Antwortzahlen voraus. Das ist eine transparente Projektannahme, keine geprüfte Eigenschaft.

### 4.5 Mehrfachantworten W01, W02 und Freitext W03 (Variante B)

Bezugsgröße: Personen mit gültiger Antwort auf das jeweilige Item (n = 3). Jede Option zählt höchstens einmal je Person. Die Anteile können zusammen über 100 Prozent liegen (hier: 133,3 Prozent, weil DEMO02 zwei Optionen gewählt hat).

**W01 Weiterbildungswünsche** (gültig 3, KA 0)

| Option | Anzahl | Anteil an gültigen (n = 3) |
|---|---|---|
| BASICS Grundlagen generativer KI | 1 | 33,3 % |
| USE_CASES Passende Einsatzmöglichkeiten | 0 | 0 % |
| PROMPTING Klare Eingaben formulieren und Ergebnisse verbessern | 1 | 33,3 % |
| VERIFY Antworten und Quellen überprüfen | 0 | 0 % |
| DATA_RULES Betriebliche Regeln und zulässige Dateneingaben | 0 | 0 % |
| KEEP_CURRENT Auf dem Laufenden bleiben | 0 | 0 % |
| OTHER Anderes Thema | 0 | 0 % |
| NONE Derzeit kein Weiterbildungswunsch | 1 | 33,3 % |
| UNKNOWN Bedarf noch nicht einschätzbar | 1 | 33,3 % |

Zuordnung: BASICS und PROMPTING stammen beide von DEMO02. NONE von DEMO01, UNKNOWN von DEMO03.

**W02 Hindernisse** (gültig 3, KA 0)

| Option | Anzahl | Anteil an gültigen (n = 3) |
|---|---|---|
| ACCESS Kein Zugang zu einem freigegebenen Werkzeug | 1 | 33,3 % |
| RULES Unklare betriebliche Regeln | 1 | 33,3 % |
| TIME Zu wenig Zeit | 0 | 0 % |
| KNOWLEDGE Fehlendes Wissen über die Nutzung | 0 | 0 % |
| TASK_FIT Kein passender Einsatz erkennbar | 0 | 0 % |
| RELIABILITY Unsicherheit über Verlässlichkeit | 0 | 0 % |
| OTHER Etwas anderes | 0 | 0 % |
| NONE Derzeit nichts | 1 | 33,3 % |
| UNKNOWN Noch nicht einschätzbar | 1 | 33,3 % |

Zuordnung: ACCESS und RULES von DEMO02. NONE von DEMO01, UNKNOWN von DEMO03.

**W03 Freitext:** 0 gültige Antworten, 3 × KEINE_ANGABE. Keine Themenzuordnung möglich.

**Prüfhinweis aus score.py:** DEMO02, Items C04, I01, I02, I03: „Kein aktueller Zugang und Zustimmung 6 oder 7 zur künftigen Nutzung: erwartete Zugangsänderung prüfen; keine automatische Korrektur.“ Regel: eigener Plausibilitätshinweis, keine Readiness-Grenze. Ich habe nichts verändert.

### 4.6 Was die Zahlen nicht zeigen

- Keine Aussage über eine Belegschaft. Die Daten sind künstlich (`interpretation_limit` laut Skript: „Künstliche Testdaten; keinerlei empirischer Befund.“).
- Keine Reliabilität, keine Faktorenstruktur, keine Signifikanz, keine Wirkung. Bei drei künstlichen Fällen wären solche Berechnungen sinnlos.
- Keine Kompetenzgrenzen, keine Einstufung als „bereit“ oder „nicht bereit“, kein Gesamtwert (`total_score: null`, „Nicht vorgesehen.“).
- Selbsteinschätzungen (U, K, G) sind keine objektive Leistung. Die Unterschiede zwischen DEMO01, DEMO02 und DEMO03 sind beim Erzeugen der Daten festgelegt worden. Sie belegen nicht, dass der Fragebogen Personen trennen kann.

## 5. Befundliste

Befund-IDs für die Rückverweise in Abschnitt 6. Datenbasis jeweils: SYNTHETIC_DEMO, Variante B, n = 3, sofern nicht anders angegeben.

| Befund-ID | Items | Befund (Anzahl / Bezugsgröße) | Art |
|---|---|---|---|
| B-01 | C04, W02 | C04 = NO bei 3 von 3. W02 = ACCESS bei 1 von 3 (DEMO02). | Organisatorische Bedingung |
| B-02 | C05, W02, W01 | C05 = NOT_KNOWN bei 3 von 3. W02 = RULES bei 1 von 3 (DEMO02). W01 = DATA_RULES bei 0 von 3. | Orientierung / Organisation |
| B-03 | C06, W01, W02 | C06 = UNKNOWN bei 3 von 3. W02 = TASK_FIT bei 0 von 3. W01 = USE_CASES bei 0 von 3. | Offene Frage zur Aufgabenpassung |
| B-04 | W01 | BASICS 1 von 3, PROMPTING 1 von 3 (beide DEMO02). | Geäußerter Lernwunsch |
| B-05 | W01, W02 | W01 NONE 1 von 3 (DEMO01), UNKNOWN 1 von 3 (DEMO03). W02 NONE 1 von 3 (DEMO01), UNKNOWN 1 von 3 (DEMO03). | Kein bzw. noch nicht einschätzbarer Bedarf |
| B-06 | G01–G03, W01, W02 | Je Item 0: 1, 3: 1, 8: 1. VERIFY (W01) 0 von 3, RELIABILITY (W02) 0 von 3. | Selbsteinschätzung ohne passenden Lernwunsch |
| B-07 | U01–U06, K01–K06, W01 | DEMO03: alle gültigen U- und K-Werte 0, W01 = UNKNOWN, C03 = YES. | Möglicher Lernbedarf nur als Hypothese |
| B-08 | C04, I01–I03 | Prüfhinweis DEMO02: C04 = NO, I01 = 6, I03 = 6, I02 = KA. | Plausibilitätshinweis |
| B-09 | L01–L03 | 0 gültige von 3, je 3 × KA. Teilbereich L fehlend. | Datenlücke |
| B-10 | W03 | 0 gültige von 3. | Datenlücke |
| B-11 | U03 | DEMO01/U03 = 12, außerhalb 0–10. | Datenfehler |
| B-12 | U01 | NB 1 von 3 (DEMO02). Über alle 54 Zellen der Fähigkeitsitems U, K, L, G: 1 NB. | Einschätzbarkeit |

## 6. Maßnahmenmatrix (Demonstration der Planungslogik)

Die Zuordnung folgt der Tabelle „Vom Befund zur Maßnahme“ im Codebuch. Diese ist eine eigene, überprüfbare Planungslogik des Projekts, keine validierte Entscheidungsregel. Weil die Daten synthetisch sind, zeigen die Zeilen nur, wie eine Empfehlung aufgebaut wäre. Sie gelten für keine reale Organisation. Für keine Maßnahme ist in den bereitgestellten Unterlagen eine Wirksamkeit belegt.

| Nr. | Befund-ID / Items | Typ | Interpretationsregel (Codebuch) | Thema und Zielgruppe | Ziel | Praktikable Maßnahme | Unsicherheit | Erfolgskontrolle |
|---|---|---|---|---|---|---|---|---|
| M-01 | B-01 / C04, W02 | Organisatorischer Handlungsbedarf | C04 = NO oder W02 = ACCESS → Zugang klären, keine Kompetenzlücke behaupten | Zugang; alle Befragten ohne Zugang (3 von 3) | Klären, ob und welches freigegebene Werkzeug es gibt bzw. geben soll | Zuständige Stelle benennen; vorhandene oder geplante Freigaben erheben und mitteilen | Synthetische Daten. Ob fehlender Zugang gewollt ist (z. B. Datenschutz, kein Bedarf), ist unbekannt. | Bei Folgeerhebung C04-Verteilung und W02 = ACCESS vergleichen; Freigabeentscheidung dokumentiert ja/nein |
| M-02 | B-02 / C05, W02 | Organisatorischer Handlungsbedarf, Orientierung | C05 = NOT_KNOWN → Regeln verständlich bereitstellen; Zuständigkeit und tatsächliches Vorhandensein klären | Betriebliche Regeln; 3 von 3 kennen keine Regeln | Klären, ob Regeln existieren; wenn ja, verständlich zugänglich machen | Bestand an Regeln prüfen; kurze, auffindbare Regelübersicht mit Ansprechperson | Ob Regeln existieren, sagt C05 = NOT_KNOWN nicht. Nur 1 von 3 nennt unklare Regeln als Hindernis. | C05 bei Folgeerhebung; Anteil KNOWN/PARTLY; Rückfragen an die Ansprechperson |
| M-03 | B-03 / C06, W01, W02 | Offene Frage | Für C06 = UNKNOWN gibt es im Codebuch keine eigene Zeile. Eigene Ableitung analog zu C06 = NO: Bedarf und Anwendungsfälle prüfen; Nutzung kann sachlich unnötig sein. | Aufgabenpassung; 3 von 3 können noch nicht beurteilen, ob GenAI sinnvoll wäre | Klären, ob es passende Aufgaben gibt, bevor geschult wird | Kurze Bedarfsklärung je Tätigkeitsbereich (z. B. Gespräch mit Führungskraft und Team) | Eigene methodische Ableitung, im Codebuch nicht ausdrücklich vorgesehen. UNKNOWN ist keine Ablehnung. | Anteil C06 = YES/NO statt UNKNOWN bei Folgeerhebung; Liste geprüfter Anwendungsfälle |
| M-04 | B-04 / W01 BASICS | Geäußerter Lernwunsch | W01 = BASICS → Einführung anbieten; Vorkenntnisse und Aufgaben prüfen | Grundlagen; 1 von 3 (DEMO02) | Grundverständnis generativer KI | Optionale Einführung; vorab Aufgabenbezug klären | Ein Fall. DEMO02 schätzt K bereits mit 8 ein. Wunsch und Selbsteinschätzung passen nicht offensichtlich zusammen; Ursache offen. | Teilnahme; Rückmeldung zur Passung; bei Folgeerhebung W01 und K beschreiben, ohne Kausalbehauptung |
| M-05 | B-04, B-01 / W01 PROMPTING, C04 | Geäußerter Lernwunsch mit Voraussetzung | W01 = PROMPTING → Übung zu Eingaben und Überarbeitung; passendes Werkzeug voraussetzen | Eingaben formulieren; 1 von 3 (DEMO02) | Übung an Arbeitsbeispielen | **Erst nach M-01**, weil DEMO02 keinen Zugang hat (C04 = NO, W02 = ACCESS) | Ein Fall. Ohne Zugang keine arbeitsnahe Übung möglich. | Erst planbar, wenn Zugang geklärt ist |
| M-06 | B-05 / W01, W02 | Offene Frage | NONE und UNKNOWN sind reguläre Antworten; keine Codebuchzeile verlangt eine Maßnahme | Kein Wunsch (1 von 3) bzw. Bedarf nicht einschätzbar (1 von 3) | Kein Schulungsziel ableiten | Keine Pflichtmaßnahme. Für UNKNOWN: Orientierung über M-02 und M-03 anbieten | Kein Wunsch ist kein Defizit. | Bei Folgeerhebung Verschiebung von UNKNOWN beobachten |
| M-07 | B-06, B-07 / G01–G03, U, K, W01 | Aus Selbsteinschätzung abgeleiteter möglicher Lernbedarf (Hypothese) | „Bestimmte Fähigkeitsantworten und passender Lernwunsch“ → nur dann Hypothese. Hier fehlt der passende Wunsch (VERIFY/RELIABILITY 0 von 3; DEMO03 W01 = UNKNOWN). | Ergebnis- und Quellenprüfung, Grundanwendung | Keine Maßnahme festlegen; offene Frage | Praktische Aufgabe zur Abklärung **anbieten**, nicht verordnen; erst nach M-01 bis M-03 sinnvoll | Niedrige Selbsteinschätzung (DEMO03 überall 0) ist kein Kompetenznachweis. Kein Grenzwert vorhanden. | Freiwillige Teilnahme; Ergebnis der praktischen Aufgabe separat dokumentieren |
| M-08 | B-08 / C04, I01–I03 | Offene Frage | Prüfhinweis, keine Korrektur | DEMO02 | Klären, ob Zugang erwartet wird | Bei realen Daten: neutrale Nachfrage zu erwarteten Bedingungen in den nächsten drei Monaten | Persona bzw. Konstruktion unbekannt | Entfällt bei synthetischen Daten |
| M-09 | B-09, B-10, B-11 / L01–L03, W03, U03 | Verfahrensprüfung | Keine Maßnahme aus fehlenden oder ungültigen Daten ableiten | Datenqualität | Vollständiger, regelkonformer Datensatz | U03 klären und regulären Lauf wiederholen; Ursache der durchgehenden KA bei L und W03 klären | Synthetisch: möglicherweise absichtlich eingebaut | Exitstatus 0 im regulären Lauf mit der korrigierten Originaldatei |
| M-10 | B-12 / U01 | Keine Maßnahme | „Viele NB“ → Frageverständnis prüfen. Hier 1 NB von 3 bei U01, 1 von 54 Fähigkeitszellen insgesamt. | U01 | Keine | Keine eigene Maßnahme; bei realen Daten Anzahl weiter berichten | Ein Einzelfall begründet keine Aussage zur Verständlichkeit | Entfällt |

**Priorisierung (begründete Planungsentscheidung, keine validierte Regel):** M-09 zuerst, weil ohne korrekte Daten keine reguläre Auswertung vorliegt. Danach M-01 und M-02, weil fehlender Zugang und unbekannte Regeln alle drei Datensätze betreffen und Voraussetzung für arbeitsnahe Lernangebote sind. Dann M-03. Lernangebote (M-04, M-05, M-07) erst danach und nur als Angebot, weil Wünsche nur von einem Datensatz kommen.

## 7. Offene Rückfragen

Ich habe alles erledigt, was ohne Antwort möglich war. Drei Punkte kann nur die Person klären, die die Daten erzeugt hat:

1. **DEMO01/U03 = 12:** Welcher Wert war vorgesehen? Ist es ein absichtlich eingebauter Prüffall? Wenn kein Wert eindeutig feststellbar ist: Soll U03 nach Codebuch als KEINE_ANGABE mit Eintrag im Korrekturprotokoll geführt werden?
2. **Herkunft der Daten:** Handelt es sich um von Hand konstruierte Rechentestfälle oder um LLM-Persona-Antworten (dann zusätzlich LLM_PERSONA mit Prompt, Formular, System und Modell)? Sind die durchgehenden KEINE_ANGABE bei L01–L03 und W03 gewollt?
3. **Verwendungszweck:** Soll diese Auswertung in der Hausarbeit als Demonstration der Auswertungskette erscheinen, oder liegt zusätzlich ein realer SURVEY-Datensatz vor, der ausgewertet werden soll?

## 8. Änderungsprotokoll dieses Laufs

| Nr. | Schritt | Datei | Bemerkung |
|---|---|---|---|
| 1 | Regulärer Lauf `score.py` | `input/antworten.json` | Exitstatus 2, keine Ausgabe. Eingabedatei nicht verändert. |
| 2 | Vollständige Prüfung ohne Abbruch | `work/pruefung.py` | Eigenes Hilfsskript, nur lesend, gleiche Prüfregeln wie `score.py`. Ein Fehler, keine weiteren. |
| 3 | Arbeitskopie Variante B | `work/variante_B_U03_KA.json` | Nur DEMO01/U03 von 12 auf `null` / KEINE_ANGABE (technischer Platzhalter für „ungültig“). |
| 4 | Arbeitskopie Variante A | `work/variante_A_ohne_DEMO01.json` | DEMO01 entfernt. |
| 5 | Läufe `score.py` auf beiden Kopien | `work/ergebnis_B_U03_KA.json`, `work/ergebnis_A_ohne_DEMO01.json` | Jeweils Exitstatus 0. |

Keine Änderung an Itembank, Codebuch, `score.py` oder Originaldaten. Keine Änderung von Versionsangaben.

## 9. Literatur

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114

Hinweis: Die Inhaltsangaben zu diesen Quellen stammen aus der Projektdokumentation (`Quellen_APA.md`, Itembank). Ich habe die Originale in diesem Lauf nicht eingesehen. Die DOIs ersetzen keine Prüfung des Inhalts.

## 10. Status

| Bereich | Stand |
|---|---|
| Datenprüfung | **Erstellt und ausgeführt.** Ein blockierender Fehler (DEMO01/U03 = 12), zehn dokumentierte Auffälligkeiten. |
| Reguläre Berechnung der gelieferten Datei | **NICHT_BERECHNET** (score.py Exitstatus 2). |
| Teilauswertung | **Berechnet** mit unverändertem `score.py` auf offen gekennzeichneten Arbeitskopien (Variante B, Kontrolle A). Vorläufig, kein reguläres Ergebnis. |
| Datenart | SYNTHETIC_DEMO. Kein empirischer Befund. Herkunft NICHT_DOKUMENTIERT. |
| Maßnahmenmatrix | Erstellt als Demonstration der Codebuchlogik. Keine Empfehlung für eine reale Organisation. Keine Wirksamkeitsbelege. |
| Nicht geprüft | Originalquellen (nicht eingesehen), Antwortoberfläche, Bearbeitungsdauer, psychometrische Eigenschaften. POWERPILOT_2025: Vergleich mit dem OSF-Anhang offen. |
| Fehlt für einen regulären Lauf | Geklärter Wert oder Korrekturprotokoll für DEMO01/U03; danach erneuter Lauf mit der korrigierten Originaldatei. |
| Fehlt für eine inhaltliche Auswertung | Ein realer SURVEY-Datensatz mit Erhebungsinformation, Teilnahmeumfang und festgelegten Gruppenberichten. |
