# Auswertungsbericht GARI-DE-0.1: synthetischer Demonstrationsdatensatz

**DEMONSTRATION. Alle Ergebnisse in diesem Bericht beruhen auf künstlichen Testdaten (`data_kind: SYNTHETIC_DEMO`). Sie sind keinerlei empirischer Befund über reale Beschäftigte, ein Unternehmen oder eine Berufsgruppe.**

## 0. Berichtsangaben

| Angabe | Wert |
|---|---|
| Datum der Auswertung | 18. Oktober 2026 |
| Betriebsart | AUSWERTEN (ausdrücklich angegeben) |
| Promptversion | Masterprompt 0.5 vom 17. Oktober 2026 |
| Verwendetes System und Modell | Claude; Modellkennung laut Sitzungsumgebung `claude-opus-5-5`. Temperatur, Seed und weitere Systemparameter: NICHT_VERFUEGBAR |
| Fragebogenversion | GARI-DE-0.1 (Itembank vom 29. September 2026, 34 Item-IDs) |
| Codebuch | „Codebuch und Auswertungsregeln“, GARI-DE-0.1, Projektpaket 0.2, Stand 29. September 2026, redaktionelle Fortschreibung 17. Oktober 2026 |
| Quellenstand | `Quellen_APA.md`, Stand 17. Oktober 2026 |
| Datenart | SYNTHETIC_DEMO (Datei- und Personenebene ohne Abweichung; ein Herkunftsfeld wie LLM_PERSONA fehlt) |
| Fallzahl | 3 Datensätze (DEMO01, DEMO02, DEMO03) |
| Berechnungsstatus | BERECHNET (mit `auswertung/score.py`, Exitstatus 0) |
| Laufzeit | Python 3.13.16 |
| Gesamtwert | Nicht vorgesehen und nicht berechnet |

Gleiche Prompts garantieren keine identischen LLM-Ausgaben. Die Zahlen in Abschnitt 5 stammen ausschließlich aus der ausgeführten Rechenroutine und sind damit reproduzierbar; die Texte und Einordnungen sind es nicht zwingend.

## 1. Kurzbeschreibung von Ziel, Zielgruppe, Kontext und Annahmen

**Ziel des Laufs:** Datenprüfung, Berechnung nach den vorab festgelegten Regeln des Codebuchs und ein Maßnahmenbericht mit Rückverweisen auf Befunde.

**Zielgruppe und Kontext:** Es liegt kein Briefing bei. Unternehmen, Zielpopulation, Tätigkeitsbereiche, zugelassene Anwendungen, Erhebungszeitraum und Erhebungsoberfläche sind deshalb UNBEKANNT. Ich ergänze keine Unternehmensmerkmale.

**Getroffene Annahmen (eigene methodische Entscheidungen):**

1. Die Angabe `data_kind: SYNTHETIC_DEMO` wird übernommen. Alle Ergebnisdarstellungen bleiben deshalb als Demonstration gekennzeichnet. Die Maßnahmenmatrix in Abschnitt 6 zeigt nur, wie die Planungslogik des Codebuchs auf solche Daten angewendet würde. Sie ist keine Empfehlung für eine reale Organisation.
2. Ob die Daten von Hand konstruiert oder durch eine KI-Persona erzeugt wurden, ist nicht dokumentiert. Die Herkunft bleibt NICHT_DOKUMENTIERT. Falls es sich um LLM-Personas handelt, wäre zusätzlich die Herkunft LLM_PERSONA zu führen.
3. Die tatsächlich verwendete Antwortoberfläche (Word-Fassung, Google-Forms-Runde R1/R2/R3 oder reine Dateikonstruktion) ist nicht dokumentiert. Ich behandle die Versionsangabe GARI-DE-0.1 als Angabe der Datei, nicht als nachgewiesenen Oberflächenabgleich.

**Rückfragen (gebündelt, höchstens drei).** Die Auswertung ist ohne Antworten vollständig durchgeführt. Die Antworten verändern aber die Einordnung:

1. **Herkunft und Oberfläche:** Wurden die drei Datensätze von Hand als Rechentestfälle konstruiert, von einer KI-Persona ausgefüllt oder über ein Formular erfasst? Falls über ein Formular: welche Fassung (Word GARI-DE-0.1 oder Forms R1/R2/R3), und waren NB und KA dort tatsächlich auswählbar?
2. **Verwendungszweck:** Soll dieser Bericht in der Hausarbeit als Demonstration der Auswertungs- und Maßnahmenlogik (DSR-Aktivität Demonstration) dienen, oder ist er ein technischer Probelauf der Rechenroutine?
3. **Realer Einsatz:** Gibt es ein Briefing für eine spätere reale Befragung (SURVEY) mit Zielpopulation, zugelassenen Werkzeugen und Gruppengrößen für Berichte? Ohne diese Angaben bleiben die Maßnahmen in Abschnitt 6 abstrakt.

## 2. Quellen- und Konstruktregister mit Evidenzgrenzen (Auszug für diese Auswertung)

**Zugriffsgrenze dieses Laufs:** Ich habe in dieser Sitzung keine Originalquelle selbst eingesehen. Alle Quellenaussagen beruhen auf dem Quellenregister der Itembank und auf `Quellen_APA.md`. Diese Dokumente berichten, welche Prüfungen im Projekt stattgefunden haben. Eine erneute Primärquellenprüfung ist hier nicht erfolgt.

| Quellen-ID | Nachweis | Im Projekt dokumentierter Prüfstand | Verwendung in GARI-DE-0.1 | Relevante Grenzen |
|---|---|---|---|---|
| MAILS_DE_2023 | Carolus et al. (2023) mit deutschem Autorenfragebogen | Volltext und deutscher Originalfragebogen laut Projekt geprüft; Items 1–6, 7–12, 26–28; Zuordnung und Mittelwertregel Seite 3 | U01–U06, K01–K06, L01–L03, Status ADAPTIERT | Ursprüngliche Evidenz betrifft allgemeine KI, Selbstberichte und eine Stichprobe von 300 deutschsprachigen Erwachsenen. Eingrenzung auf generative KI, Arbeitskontext und ergänzte NB/KA-Optionen sind Anpassungen. Die Regel der vollständigen Antworten ist eine Projektregel, keine MAILS-Vorschrift. |
| POWERPILOT_2025 | Wichmann et al. (2025), HICSS-Beitrag mit Itemsammlung Questionnaire 2 | Paper und bereitgestellte Itemsammlung geprüft | A01–A04 (Einstellung), I01–I03 (Nutzungsabsicht), Status ADAPTIERT | Direkter Wortlautvergleich mit dem OSF-Anhang (https://doi.org/10.17605/OSF.IO/GEBK9) bleibt offen. Ursprünglicher Kontext Energiemonitoring. Übertragung auf freigegebene generative KI, berufliche Aufgaben und drei Monate ist inhaltliche Anpassung. |
| ohne | Eigenentwicklung | Keine Originalquelle | C01–C06, G01–G03, W01–W03, Status NEU_ENTWICKELT | Noch nicht empirisch geprüft; G01–G03 sind Einzelitems ohne Skalenbildung. |

Die Kombination der Instrumente ist nicht psychometrisch validiert. Eine vollständige Primärquellenprüfung aller Items wird nicht behauptet.

**Konstrukte und ihre Rolle in dieser Auswertung**

| Bereich | Konstrukt | Art der Angabe | Zusammenfassung laut Codebuch |
|---|---|---|---|
| C | Tätigkeit, berufliche und private Nutzung, Zugang, Regelkenntnis, Aufgabenrelevanz | Berichtetes Verhalten und wahrgenommene betriebliche Bedingungen | Jede Frage einzeln |
| U | Selbst eingeschätzte Anwendung | Selbsteinschätzung (0–10) | Vorläufiger Teilbereichsmittelwert |
| K | Selbst eingeschätztes Verständnis | Selbsteinschätzung (0–10) | Vorläufiger Teilbereichsmittelwert |
| L | Zutrauen in das eigene Lernen | Selbsteinschätzung (0–10) | Vorläufiger Teilbereichsmittelwert |
| G | Prüfen von Ergebnissen und zulässigen Eingaben | Selbsteinschätzung (0–10) | Drei Einzelitems, kein Mittelwert |
| A | Einstellung zur arbeitsbezogenen Nutzung | Zustimmung (1–7), bedingte Bewertung | Vorläufiger Teilbereichsmittelwert |
| I | Absicht unter tatsächlich erwarteten Bedingungen | Zustimmung (1–7) | Vorläufiger Teilbereichsmittelwert |
| W | Lernwünsche, Hindernisse, Freitext | Geäußerter Lernwunsch, wahrgenommene Hindernisse | Häufigkeiten je Option; Freitext qualitativ |

Keiner dieser Werte ist objektive Leistung. Selbsteinschätzung, berichtetes Verhalten und Lernwunsch werden im Folgenden getrennt berichtet.

## 3. Fragebogenfassung, Itemregister und Codebuch mit Versionen

Für die Auswertung wurden ausschließlich die beigefügten, unveränderten Referenzdateien verwendet:

| Datei | Version | SHA-256 der Datei |
|---|---|---|
| `instrument/Itembank_GARI_DE_0.1.json` | GARI-DE-0.1, 29.09.2026 | 12582782e64397d3460e88c2f4b2425b062f1f1c33725fc2d9953f5067afd050 |
| `instrument/Codebuch.md` | Stand 29.09.2026, Fortschreibung 17.10.2026 | 65c5bd31bcd93303bf87da8c7a2d0380d0dd0dfa2510e0453610785f4f1548cf |
| `auswertung/score.py` | auf GARI-DE-0.1 festgelegt | cccab0a8e9c2b55b40302a14ca8dbd2acd4493c821a8171df47788d41f8686c5 |
| `antworten.json` | Daten, GARI-DE-0.1 | 97f2d98396a17e7bc3ca0ad2e50bd5ab66eae9d62a11901542dc5ebfb6dcd097 |

Die Rechenroutine meldet zusätzlich einen Hash der kanonisch serialisierten Bank (`bank_sha256`: c2e7eb3ba5f7505a9418ac1cd21b1847ae7e84f4cdd799db3ccfc8107c2ec080). Er unterscheidet sich vom Dateihash, weil er über eine sortierte Neuserialisierung gebildet wird; das ist kein Hinweis auf eine Änderung.

Die Itembank enthält 34 IDs in dieser Reihenfolge: C01–C06, U01–U06, K01–K06, L01–L03, G01–G03, A01–A04, I01–I03, W01–W03. Alle Items werden allen Personen gezeigt (`display_if: ALWAYS`), es gibt keine Filter und keine umgepolten Items. Eine Umkodierung findet deshalb nicht statt. Zulässige Fehlwertgründe: NICHT_BEURTEILBAR und KEINE_ANGABE bei den Zahlenitems, nur KEINE_ANGABE bei C, W und W03. NICHT_ZUTREFFEND und UEBERSPRUNGEN sind in GARI-DE-0.1 nicht erlaubt.

Ein Fragebogen oder Itemregister wurde in diesem Lauf nicht neu erstellt oder verändert. Die vollständige Befragungsfassung steht in `frozen_participant_text` der Itembank.

## 4. Prüfbericht

### 4.1 Formale Datenprüfung durch die Rechenroutine

Aufruf (im Ordner `input`):

```bash
python3 -I auswertung/score.py antworten.json ../work/ergebnis.json
```

Tatsächliche Ausgabe: `3 Fälle berechnet (SYNTHETIC_DEMO). Ausgabe: …/work/ergebnis.json`. Tatsächlicher Exitstatus: **0**.

Die Routine bricht bei jedem der folgenden Fehler mit Exitstatus 2 ab. Da sie fehlerfrei durchlief, sind diese Prüfungen bestanden:

| Prüfpunkt | Ergebnis |
|---|---|
| `data_kind` zulässig | bestanden (SYNTHETIC_DEMO) |
| Fragebogenversion auf Datei- und Personenebene = GARI-DE-0.1 | bestanden (Dateiangabe; siehe 4.3 zur Oberfläche) |
| Testkürzel vorhanden und eindeutig | bestanden (DEMO01, DEMO02, DEMO03; keine Dubletten) |
| Alle 34 Item-IDs je Person, keine unbekannten IDs | bestanden |
| Jede Antwort mit `value` und `missing_reason` | bestanden |
| Fehlwertgründe nur aus der erlaubten Liste | bestanden |
| Kein Widerspruch zwischen Wert und Fehlwertgrund | bestanden |
| Zahlenwerte ganzzahlig im Skalenbereich | bestanden |
| Einzelwahl nur bekannte Kategorien | bestanden |
| Mehrfachantworten: nichtleer, keine Dubletten, höchstens drei, exklusive Optionen allein | bestanden |
| Gesamtwert | nicht berechnet (`total_score: null`, „Nicht vorgesehen.“) |

Zusätzlich habe ich die Personenwerte unabhängig mit einer zweiten, kurzen Rechnung nach der Codebuchregel nachgerechnet. Sie stimmen mit der Ausgabe der Routine überein. Diese Gegenrechnung stammt vom selben Modell und ist kein unabhängiges Gutachten.

### 4.2 Fehlwerte

| Person | Item | Grund | Folge nach Codebuch |
|---|---|---|---|
| DEMO02 | U01 | NICHT_BEURTEILBAR | U-Personenwert fehlt (vollständige Antworten erforderlich) |
| DEMO02 | I02 | KEINE_ANGABE | I-Personenwert fehlt |
| DEMO01, DEMO02, DEMO03 | W03 | KEINE_ANGABE | Kein Freitext zur qualitativen Zuordnung vorhanden |

Es wurde nichts ersetzt oder imputiert. Gültige 0-Antworten sind erhalten.

### 4.3 Grenzen, die die Rechenroutine nicht prüfen kann

| Nr. | Problem | Einordnung | Status |
|---|---|---|---|
| P1 | Kein Begleitmanifest: Erhebungsoberfläche, Plattform, Erhebungsrunde, Datum des Oberflächenabgleichs und Erzeugungsweg fehlen. | Ob die Daten tatsächlich mit der Fassung GARI-DE-0.1 erhoben wurden, ist nicht nachgewiesen. Daten aus R1/R2/R3 dürften nicht durch bloße Versionsangabe als GARI-DE-0.1 ausgewertet werden. | OFFEN |
| P2 | Unbekannt, ob NB und KA in der verwendeten Oberfläche auswählbar waren. | Die vielen Items mit 0 Fällen NB oder KA belegen deshalb nicht, dass alle Personen urteilen konnten. Vollständige Zahlenzellen belegen weder Verständnis noch freiwillige Zahlenwahl. | OFFEN |
| P3 | Herkunft der synthetischen Daten nicht dokumentiert (Handkonstruktion oder LLM_PERSONA). | Bei LLM-Personas wären Persona-Prompts, Formular, Erzeugungs- und Antwortsystem, sichtbare Modellversion und manuelle Eingriffe zu dokumentieren. | NICHT_DOKUMENTIERT |
| P4 | W03 bei allen drei Personen KEINE_ANGABE. | Nicht unterscheidbar, ob KA gewählt oder das Feld leer gelassen wurde. Beides wird laut Codebuch gleich kodiert. Kein Freitext, keine qualitative Auswertung möglich. | dokumentiert |
| P5 | Keine Zeitstempel und keine Bearbeitungsdauer in den Daten. | Die geschätzte Bearbeitungszeit (10–15 Minuten, nicht gemessen) bleibt ungeprüft. | OFFEN |
| P6 | `tests/test_scoring.py` lag nicht bei. | Die Unittests der Rechenroutine wurden in diesem Lauf nicht ausgeführt. Sie würden ohnehin nur die Rechenroutine prüfen. | NICHT_AUSGEFUEHRT |

### 4.4 Plausibilitätshinweise (eigene Zusatzprüfung, keine Codebuchregel)

Diese Hinweise stammen aus einem ergänzenden Prüfskript, das nur die Daten liest. Sie verändern keine Antwort. Bei synthetischen Daten zeigen sie vor allem, welche Muster ein realer Bericht hinterfragen müsste.

| Nr. | Person | Items | Beobachtung | Mögliche Erklärung, keine Korrektur |
|---|---|---|---|---|
| H1 | DEMO02 | C04, I01, I03 | Von der Routine gesetztes Prüfflag: C04 = NO (kein aktueller Zugang) bei I01 = 6 und I03 = 6. | Die Person kann künftigen Zugang erwarten. Laut Codebuch nur Prüfhinweis, keine Readiness-Grenze. |
| H2 | alle | C01–C06 | Alle drei Personen haben exakt dasselbe Kontextmuster: OFFICE, D0, YES, NO, NOT_KNOWN, UNKNOWN. | Typisch für konstruierte Testfälle. Unterschiede zwischen Kontextgruppen sind damit nicht darstellbar. |
| H3 | alle | U, K, L, G, A, I | Innerhalb jedes Blocks fast durchgehend identische Werte (DEMO01: 3 bzw. 3; DEMO02: 8 bzw. 6; DEMO03: 0 bzw. 1). Einzige Abweichung: DEMO01 U01 = 0 bei U02–U06 = 3. | Gleichförmiges Antwortmuster. In realen Daten wäre es ein Anlass, Aufmerksamkeit und Itemverständnis zu prüfen; hier vermutlich Konstruktionsmerkmal. Keine Itemanalyse daraus ableiten. |
| H4 | DEMO02 | C02, C04, U01–U06, K01–K06 | Keine berufliche Nutzung und kein Zugang, aber 8 auf allen gültigen Fähigkeitsitems; U01 („bedienen“) als NB markiert. | Private Nutzung (C03 = YES) kann zur Selbsteinschätzung beitragen. Dass gerade das grundlegendste Bedienitem NB ist, die weitergehenden U-Items aber 8, wäre in realen Daten eine Nachfrage zum Verständnis von U01 wert. |
| H5 | DEMO01 | C04, W02 | Kein Zugang (C04 = NO), aber bei Hindernissen „Derzeit nichts“ (W02 = NONE); dazu kein Weiterbildungswunsch (W01 = NONE). | Fehlender Zugang wird nicht als Hindernis erlebt, etwa weil kein Bedarf gesehen wird (C06 = UNKNOWN). Keine Umdeutung. |
| H6 | DEMO03 | C03, U01, alle Fähigkeitsitems | Private Nutzung bejaht (C03 = YES), aber U01 = 0 und alle Fähigkeitsitems 0; Einstellung und Absicht 1. | 0 ist laut Instruktion eine tatsächliche Einschätzung. Niedrige Werte bei bestehender Privatnutzung sind möglich. Keine Kompetenzaussage. |

## 5. Auswertungsbericht (DEMONSTRATION)

**Interpretationsgrenze laut Rechenroutine:** „Künstliche Testdaten; keinerlei empirischer Befund.“ Alle Zahlen beschreiben drei konstruierte Datensätze. Prozentwerte sind bei n = 3 nur der Vollständigkeit halber angegeben; maßgeblich sind die absoluten Zahlen.

### 5.1 Einzelverteilungen (primäre Darstellung)

#### Kontextitems C01–C06 (Einzelwahl, Nenner = gültige Antworten)

| Item | Antwortkategorie | n | % gültig |
|---|---|---|---|
| C01 | OFFICE (Überwiegend Büro- oder Bildschirmarbeit) | 3 | 100,0 |
| C01 | OTHER_WORK (Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst) | 0 | 0,0 |
| C01 | MIXED (Etwa gleich große Anteile beider Bereiche) | 0 | 0,0 |
| C01 | Fehlwert KEINE_ANGABE | 0 | – |
| C02 | D0 (An keinem Tag) | 3 | 100,0 |
| C02 | D1_3 (An 1 bis 3 Tagen) | 0 | 0,0 |
| C02 | D4_9 (An 4 bis 9 Tagen) | 0 | 0,0 |
| C02 | D10_15 (An 10 bis 15 Tagen) | 0 | 0,0 |
| C02 | D16_PLUS (An 16 oder mehr Tagen) | 0 | 0,0 |
| C02 | UNKNOWN (Kann ich nicht einschätzen) | 0 | 0,0 |
| C02 | Fehlwert KEINE_ANGABE | 0 | – |
| C03 | YES (Ja) | 3 | 100,0 |
| C03 | NO (Nein) | 0 | 0,0 |
| C03 | UNKNOWN (Ich bin mir nicht sicher) | 0 | 0,0 |
| C03 | Fehlwert KEINE_ANGABE | 0 | – |
| C04 | YES (Ja) | 0 | 0,0 |
| C04 | NO (Nein) | 3 | 100,0 |
| C04 | UNKNOWN (Ich weiß es nicht) | 0 | 0,0 |
| C04 | Fehlwert KEINE_ANGABE | 0 | – |
| C05 | KNOWN (Ja) | 0 | 0,0 |
| C05 | PARTLY (Teilweise) | 0 | 0,0 |
| C05 | NOT_KNOWN (Nein) | 3 | 100,0 |
| C05 | EXISTENCE_UNKNOWN (Ich weiß nicht, ob es solche Regeln gibt) | 0 | 0,0 |
| C05 | Fehlwert KEINE_ANGABE | 0 | – |
| C06 | YES (Ja) | 0 | 0,0 |
| C06 | NO (Nein) | 0 | 0,0 |
| C06 | UNKNOWN (Kann ich noch nicht beurteilen) | 3 | 100,0 |
| C06 | Fehlwert KEINE_ANGABE | 0 | – |

#### Fähigkeitsitems U, K, L, G (0–10): absolute Häufigkeiten je Skalenwert

| Item | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | n gültig | NB | KA |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| U01 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 |
| U02 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| U03 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| U04 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| U05 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| U06 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| K01 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| K02 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| K03 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| K04 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| K05 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| K06 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| L01 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| L02 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| L03 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| G01 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| G02 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| G03 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |

#### Zustimmungsitems A, I (1–7): absolute Häufigkeiten je Skalenwert

| Item | 1 | 2 | 3 | 4 | 5 | 6 | 7 | n gültig | NB | KA |
|---|---|---|---|---|---|---|---|---|---|---|
| A01 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 3 | 0 | 0 |
| A02 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 3 | 0 | 0 |
| A03 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 3 | 0 | 0 |
| A04 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 3 | 0 | 0 |
| I01 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 3 | 0 | 0 |
| I02 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 1 |
| I03 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 3 | 0 | 0 |

#### Mehrfachantworten W01 und W02

Nenner: Personen mit gültiger Antwort auf das jeweilige Item (W01: 3, W02: 3). Jede Option höchstens einmal je Person. Summen über 100 Prozent sind möglich.

| Item | Option | n | % der gültig Antwortenden |
|---|---|---|---|
| W01 | BASICS (Grundlagen generativer KI) | 1 | 33,3 |
| W01 | USE_CASES (Passende Einsatzmöglichkeiten für meine Aufgaben) | 0 | 0,0 |
| W01 | PROMPTING (Klare Eingaben formulieren und Ergebnisse verbessern) | 1 | 33,3 |
| W01 | VERIFY (Antworten und Quellen überprüfen) | 0 | 0,0 |
| W01 | DATA_RULES (Betriebliche Regeln und zulässige Dateneingaben) | 0 | 0,0 |
| W01 | KEEP_CURRENT (Bei neuen Entwicklungen auf dem Laufenden bleiben) | 0 | 0,0 |
| W01 | OTHER (Anderes Thema) | 0 | 0,0 |
| W01 | NONE (Derzeit kein Weiterbildungswunsch) | 1 | 33,3 |
| W01 | UNKNOWN (Ich kann meinen Bedarf noch nicht einschätzen) | 1 | 33,3 |
| W01 | Fehlwert KEINE_ANGABE | 0 | – |
| W01 | Summe aller Nennungen | 4 | 133,3 |
| W02 | ACCESS (Kein Zugang zu einem freigegebenen Werkzeug) | 1 | 33,3 |
| W02 | RULES (Unklare betriebliche Regeln) | 1 | 33,3 |
| W02 | TIME (Zu wenig Zeit zum Ausprobieren oder Lernen) | 0 | 0,0 |
| W02 | KNOWLEDGE (Mir fehlt Wissen über die Nutzung) | 0 | 0,0 |
| W02 | TASK_FIT (Ich erkenne keinen passenden Einsatz für meine Aufgaben) | 0 | 0,0 |
| W02 | RELIABILITY (Unsicherheit über die Verlässlichkeit der Ergebnisse) | 0 | 0,0 |
| W02 | OTHER (Etwas anderes) | 0 | 0,0 |
| W02 | NONE (Derzeit nichts) | 1 | 33,3 |
| W02 | UNKNOWN (Kann ich noch nicht einschätzen) | 1 | 33,3 |
| W02 | Fehlwert KEINE_ANGABE | 0 | – |
| W02 | Summe aller Nennungen | 4 | 133,3 |

W03 (Freitext): 0 gültige Antworten, 3 × KEINE_ANGABE. Es gibt keinen Inhalt zur Zuordnung.

### 5.2 Vorläufige Teilbereichswerte U, K, L, A und I

Regel laut Codebuch: arithmetisches Mittel je Person nur bei vollständigen gültigen Antworten auf alle Items des Teilbereichs; Gruppenmittel über die gültigen Personenwerte. Die Behandlung der Antwortzahlen als gleichabständig ist eine transparente Annahme. Die vollständige Beantwortung ist eine konservative Projektregel, keine MAILS-Vorschrift. Werte auf 0–10 und 1–7 werden nicht miteinander verglichen.

| Teilbereich | Skala | n vollständig | n unvollständig | Mittel der Personenwerte | Minimum | Maximum |
|---|---|---|---|---|---|---|
| U Selbst eingeschätzte Anwendung | 0–10 | 2 | 1 | 1,25 | 0 | 2,5 |
| K Selbst eingeschätztes Verständnis | 0–10 | 3 | 0 | 3,67 | 0 | 8 |
| L Zutrauen in das eigene Lernen | 0–10 | 3 | 0 | 3,67 | 0 | 8 |
| A Einstellung zur Nutzung | 1–7 | 3 | 0 | 3,33 | 1 | 6 |
| I Berichtete Nutzungsabsicht | 1–7 | 2 | 1 | 2,00 | 1 | 3 |

Gerundet auf zwei Nachkommastellen; ungerundete Ausgabe: K und L 3,6666…, A 3,3333…

Zur Nachvollziehbarkeit des synthetischen Laufs die Personenwerte aus der Arbeitsdatei. In einer realen Befragung blieben sie laut Codebuch in der Arbeitsdatei und gingen nicht in einen Unternehmensbericht ein:

| Person | U | K | L | A | I |
|---|---|---|---|---|---|
| DEMO01 | 2,5 | 3 | 3 | 3 | 3 |
| DEMO02 | fehlt (U01 NB) | 8 | 8 | 6 | fehlt (I02 KA) |
| DEMO03 | 0 | 0 | 0 | 1 | 1 |

**Lesehinweis zu U und I:** Die Gruppenmittel für U (1,25) und I (2,00) beruhen nur auf DEMO01 und DEMO03. Die Person mit den höchsten Werten in den übrigen Bereichen (DEMO02) fällt dort wegen je eines Fehlwerts heraus. Das Gruppenmittel ist daher nicht mit K, L und A über dieselben Personen vergleichbar. Das ist eine direkte Folge der vorab festgelegten Fehlwertregel und wird nicht nachträglich geändert.

G01–G03 werden ausdrücklich nicht zusammengefasst; ihre Verteilungen stehen in 5.1. Für C, G und W sowie über alle Bereiche gibt es keinen Gesamtwert, keine Reifegradklasse und keine Gewichtung. Alpha-, Faktoren- oder Signifikanzanalysen sind bei drei synthetischen Fällen weder sinnvoll noch vorgesehen.

### 5.3 Prüfflags der Rechenroutine

Ein Flag (siehe H1): DEMO02, Items C04, I01, I02, I03. Meldung der Routine: „Kein aktueller Zugang und Zustimmung 6 oder 7 zur künftigen Nutzung: erwartete Zugangsänderung prüfen; keine automatische Korrektur.“ Regel: „Eigener Plausibilitätshinweis, keine Readiness-Grenze.“

## 6. Maßnahmenmatrix mit Rückverweisen (DEMONSTRATION der Planungslogik)

Grundlage ist die im Codebuch vorab festgelegte Zuordnung „Vom Befund zur Maßnahme“. Sie ist eine eigene, überprüfbare Planungslogik und keine diagnostische Entscheidung über Einzelpersonen. Es gibt keine empirisch geprüften Grenzwerte; ich nenne Antwortkategorien und Anzahlen. Die Priorisierung ist eine begründete Planungsentscheidung nach dem Codebuch: zuerst organisatorische Voraussetzungen, weil Übungsangebote ohne freigegebenes Werkzeug und ohne bekannte Regeln nicht umsetzbar sind. Die Wirksamkeit keiner Maßnahme ist nachgewiesen.

**Alle Befunde beziehen sich auf n = 3 synthetische Datensätze (SYNTHETIC_DEMO). Für eine reale Organisation folgt daraus nichts.**

### 6.1 Befundübersicht

| Befund-ID | Items | Datenbasis (n = 3, SYNTHETIC_DEMO) | Art | Interpretationsregel (Codebuch) |
|---|---|---|---|---|
| B01 | C04, W02, C02 | C04 = NO: 3 von 3. W02 = ACCESS: 1 von 3. C02 = D0 (keine berufliche Nutzung in vier Wochen): 3 von 3. | Organisatorischer Handlungsbedarf | „C04 = NO oder W02 = ACCESS: Organisatorisches Hindernis; freigegebene Zugangsmöglichkeiten klären; keine Kompetenzlücke behaupten.“ Niedrige Nutzung ohne Zugang führt zuerst zur Zugangsprüfung. |
| B02 | C05, W02, G03 | C05 = NOT_KNOWN: 3 von 3; EXISTENCE_UNKNOWN: 0. W02 = RULES: 1 von 3. W01 = DATA_RULES: 0 von 3. G03: je 1 × 0, 3, 8. | Organisatorischer Handlungsbedarf, Orientierung | „C05 = NOT_KNOWN: Regeln verständlich bereitstellen; Zuständigkeit und tatsächliches Vorhandensein klären.“ |
| B03 | C06, W01, W02 | C06 = UNKNOWN („Kann ich noch nicht beurteilen“): 3 von 3. W01 = USE_CASES: 0. W02 = TASK_FIT: 0. | Offene Frage | C06 = NO oder TASK_FIT würde „Bedarf und geeignete Anwendungsfälle prüfen“ auslösen. Hier liegt keine Verneinung vor, sondern fehlende Beurteilbarkeit. Nutzung kann sachlich unnötig sein. |
| B04 | W01, U, K | W01 = BASICS: 1 von 3; W01 = PROMPTING: 1 von 3 (beide DEMO02). Dieselbe Person schätzt sich auf allen gültigen U- und K-Items mit 8 ein. | Geäußerter Lernwunsch | „W01 = BASICS: Einführung anbieten; Vorkenntnisse und Aufgaben prüfen.“ „W01 = PROMPTING: Übung zu Eingaben und Überarbeitung; passendes Werkzeug voraussetzen.“ |
| B05 | W01, W02, U, K, L | W01 = NONE: 1 von 3 (DEMO01). W01 = UNKNOWN: 1 von 3 (DEMO03). W02 = NONE: 1, UNKNOWN: 1. DEMO03 wählt auf allen Fähigkeitsitems 0. | Offene Frage | Kein Lernwunsch und nicht einschätzbarer Bedarf sind reguläre Antworten. Niedrige Selbsteinschätzung wird nicht automatisch zum Schulungsdefizit. Die Regel „Fähigkeitsantworten und passender Lernwunsch“ greift nicht, weil kein passender Lernwunsch vorliegt. |
| B06 | U01 | NB: 1 von 3 (DEMO02). Gültig: 2 × 0. | Unklare Einschätzbarkeit | „NB auf einem Fähigkeitsitem: erst Frageverständnis und Erfahrungsgrundlage prüfen; nicht als niedrige Kompetenz zählen.“ Ein einzelner Fall ist kein Muster. |
| B07 | G01, G02, W01, W02 | G01 und G02: je 1 × 0, 3, 8. W01 = VERIFY: 0. W02 = RELIABILITY: 0. | Kein Befund für Maßnahme | Die Regel „W01 = VERIFY oder W02 = RELIABILITY“ ist nicht erfüllt. G-Werte allein begründen keinen Lernbedarf. |
| B08 | C04, I01–I03 | Prüfflag bei DEMO02 (C04 = NO, I01 = 6, I03 = 6). | Offene Frage | Nur Prüfhinweis; Person kann künftigen Zugang erwarten. |

### 6.2 Maßnahmenvorschläge

| Nr. | Befund-ID | Thema | Zielgruppe | Organisations- oder Lernziel | Praktikable Maßnahme | Unsicherheit | Vorschlag zur Erfolgskontrolle | Priorität (Planungsentscheidung) |
|---|---|---|---|---|---|---|---|---|
| M1 | B01 | Zugang zu freigegebenen Werkzeugen | Zuständige Stelle (z. B. IT oder Geschäftsführung); betrifft alle Befragten ohne Zugang | Klären, ob und welche generative KI für berufliche Aufgaben freigegeben ist, und dies allen mitteilen | Bestandsaufnahme freigegebener Werkzeuge; Entscheidung über Zugang oder bewusste Nichtfreigabe dokumentieren | Synthetische Daten; keine Information über tatsächliche Werkzeuge im Unternehmen. Keine Kompetenzaussage. | Bei Folgeerhebung Verteilung von C04 (Anteil YES, NO, UNKNOWN) und W02 = ACCESS vergleichen, sofern Fassung gleich bleibt | 1, weil Lernangebote zu PROMPTING ohne Werkzeug nicht umsetzbar sind |
| M2 | B02 | Betriebliche Regeln für generative KI | Zuständige Stelle; alle Beschäftigten | Klären, ob Regeln existieren; wenn ja, verständlich bereitstellen; Zuständigkeit für Fragen benennen | Kurze schriftliche Orientierung zu zulässiger Nutzung und zulässigen Dateneingaben, mit Ansprechperson | Antwort „Nein“ in C05 sagt nicht, ob Regeln existieren. Kein Lernwunsch DATA_RULES geäußert. | C05-Verteilung und W02 = RULES bei Folgeerhebung; G03-Verteilung ergänzend beschreiben, nicht als Wirksamkeitsnachweis | 1, gemeinsam mit M1 |
| M3 | B03 | Aufgabenpassung | Befragte mit C06 = UNKNOWN; deren Führungskräfte | Klären, ob es in den Aufgabenbereichen sinnvolle Anwendungsfälle gibt | Kurzes Gespräch oder Workshop zur Sammlung konkreter Aufgaben; bewusst auch das Ergebnis „kein sinnvoller Einsatz“ zulassen | Alle drei Datensätze haben C06 = UNKNOWN und denselben Tätigkeitskontext OFFICE. W03 enthält keine Aufgaben. | Bei Folgeerhebung C06-Verteilung und Anzahl inhaltlich zuordenbarer W03-Antworten | 2, nach Klärung von Zugang und Regeln |
| M4 | B04 | Grundlagen und Formulieren von Eingaben | Personen mit Lernwunsch BASICS oder PROMPTING (hier 1 synthetischer Fall) | Lernziel: Grundprinzipien generativer KI erklären; Eingaben formulieren und Ergebnisse überarbeiten können | Einführung anbieten; Übung zu PROMPTING erst, wenn ein freigegebenes Werkzeug vorhanden ist (M1). Vorab Vorkenntnisse und Aufgaben klären. | Lernwunsch steht neben hoher Selbsteinschätzung (8). Das widerspricht sich nicht, belegt aber auch keinen objektiven Bedarf. Kein Leistungstest vorhanden. | Teilnahme, Rückmeldung zur Passung, praktische Übungsaufgabe statt nur Selbsteinschätzung; keine Wirkungsbehauptung | 3, abhängig von M1 |
| M5 | B05, B03 | Orientierung ohne Schulungspflicht | Personen mit W01 = NONE oder UNKNOWN | Organisationsziel: Bedarf einschätzbar machen, ohne Teilnahme vorauszusetzen | Freiwillige, kurze Information darüber, was generative KI in den eigenen Aufgaben leisten könnte und was nicht; ausdrücklich keine Pflichtschulung aus niedrigen Selbsteinschätzungen ableiten | Zurückhaltung kann sachlich begründet sein. Gründe sind nicht erhoben (W03 leer). | Bei Folgeerhebung Verteilung W01 (UNKNOWN, NONE) und C06 beschreiben | 3, Planungsentscheidung |
| M6 | B06 | Verständlichkeit U01 | Projekt (Instrumentenentwicklung), keine Beschäftigtengruppe | Prüfen, ob „bedienen“ bei fehlendem Zugang einschätzbar ist | Im nächsten Pretest gezielte, neutrale Nachfrage zu U01 aufnehmen: „Woran haben Sie bei dieser Frage gedacht?“ | Ein synthetischer Einzelfall; kein empirischer Hinweis auf ein Itemproblem | NB-Anzahl bei U01 in realen Daten berichten | Prüfhinweis, keine Maßnahme |
| M7 | B08 | Erwartete Zugangsänderung | Projekt bzw. Auswertende | Klären, ob Absicht trotz fehlenden Zugangs auf erwarteter Freigabe beruht | In realen Daten nur aggregiert berichten; in einem Pretest neutrale Nachfrage zur I-Instruktion | Synthetischer Einzelfall | Keine | Prüfhinweis, keine Maßnahme |

Kein Maßnahmenvorschlag zu B07: Weder ein Lernwunsch VERIFY noch ein Hindernis RELIABILITY wurde gewählt. Ein Lernangebot zur Ergebnisprüfung ließe sich aus diesen Daten nur als freie Annahme begründen.

## 7. Änderungsprotokoll und nächste konkret erforderliche Eingaben

### 7.1 Änderungsprotokoll

| Nr. | Was | Ergebnis |
|---|---|---|
| 1 | Daten, Bank, Codebuch, Rechenroutine | Nicht verändert |
| 2 | Werte, Fehlwertgründe, Kategorien | Nicht verändert, nicht ergänzt, nicht imputiert |
| 3 | Rechenregeln | Unverändert nach Codebuch angewendet; keine Abweichung |
| 4 | Zusätzlich erstellt | Arbeitsdateien `work/ergebnis.json` (Ausgabe der Rechenroutine), `work/audit.py` (lesende Plausibilitätsprüfung), `work/tables.py` und `work/tables.md` (Tabellen ausschließlich aus `ergebnis.json` erzeugt) |
| 5 | Instrumentenänderungen | Keine vorgeschlagen. M6 und M7 sind Prüfhinweise für einen späteren Pretest, keine Änderung an GARI-DE-0.1. Eine Änderung würde eine neue Fragebogenversion erfordern; Nachprüfstatus wäre offen. |

### 7.2 Nächste konkret erforderliche Eingaben

1. Begleitmanifest zu `antworten.json`: Erzeugungsweg (Handkonstruktion oder LLM_PERSONA mit Prompt, System und sichtbarer Modellbezeichnung), Oberfläche und Fassung, Verfügbarkeit von NB und KA.
2. Für einen realen Einsatz: Briefing mit Zielpopulation, zugelassenen Werkzeugen, Erhebungsprozess, Anonymitätszusage und Mindestgruppengröße für Berichte; danach Daten mit `data_kind: SURVEY` in einer tatsächlich abgeglichenen Fassung.
3. `tests/test_scoring.py`, falls die Rechenroutine in derselben Sitzung mitgeprüft werden soll.
4. Falls Forms-Daten (R1/R2/R3) ausgewertet werden sollen: das zur jeweiligen Fassung passende Codebuch. Mit dem GARI-DE-0.1-Codebuch sind dafür nur Bestands- und Qualitätsprüfungen möglich, keine regulären Skalenberechnungen.

## Literatur (APA)

Die Belege beziehen sich auf die Funktionen, die im Projektquellenregister dokumentiert sind. Die Inhalte wurden in diesem Lauf nicht erneut an den Originalen geprüft.

- Instrumentgrundlage U, K, L: Carolus et al. (2023).
- Instrumentgrundlage A, I: Wichmann et al. (2025).
- Kleine Fallzahlen ersetzen keine psychometrische Prüfung: Boateng et al. (2018).
- Grenzen synthetischer LLM-Antworten als Ersatz für Befragte, falls Personas verwendet wurden: Bisbee et al. (2024).
- Definition der Nutzungsabsicht über Handlung, Kontext und Zeit: Ajzen (o. J.).

Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. University of Massachusetts Amherst. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf

Bisbee, J., Clinton, J. D., Dorff, C., Kenkel, B., & Larson, J. M. (2024). Synthetic replacements for human survey data? The perils of large language models. *Political Analysis, 32*(4), 401–416. https://doi.org/10.1017/pan.2024.5

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114

## Status

**Erstellt:** Prüfbericht, Einzelverteilungen aller 34 Items, fünf vorläufige Teilbereichswerte, Maßnahmenmatrix als Demonstration der Codebuchlogik.

**Geprüft:** Formale Datenprüfung durch `score.py` (Exitstatus 0); Gegenrechnung der Personenwerte; lesende Plausibilitätsprüfung. Nicht geprüft: Oberfläche, Erzeugungsweg der Daten, Verfügbarkeit von NB/KA, Bearbeitungsdauer, Unittests.

**Berechnet:** Ja, ausschließlich mit der ausgeführten Rechenroutine. Datenart SYNTHETIC_DEMO. Kein Gesamtwert.

**Fehlt:** Reale Daten (SURVEY), Briefing, Begleitmanifest. Dieser Bericht ist keine Evaluation des Instruments und keine Aussage über reale Beschäftigte. Er belegt weder Validität noch Reliabilität von GARI-DE-0.1.
