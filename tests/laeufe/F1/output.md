# Zusatzmodul „Sorge vor Veränderungen des eigenen Arbeitsplatzes durch generative KI“ zu GARI-DE-0.1

**Betriebsart:** ENTWICKELN (Zusatzmodul), Kern GARI-DE-0.1 nach den Regeln von ANWENDEN unverändert übernommen
**Kontext:** FIKTIVE_DEMONSTRATION (Szenario F1). Alle Unternehmensangaben stammen aus dem Briefing. Es gibt keine realen Daten.

| Angabe | Wert |
|---|---|
| Datum | 18. Oktober 2026 |
| System und Modell | Claude (Anthropic). Angezeigte Modellkennung: claude-opus-5-5. Weitere Systemparameter (Temperatur, Sitzungseinstellungen): NICHT_VERFUEGBAR |
| Promptversion | Masterprompt 0.5 vom 17. Oktober 2026 |
| Quellenstand | `Quellen_APA.md`, Stand 17. Oktober 2026. Brougham und Haar (2018) liegt **nicht** vor |
| Kernbank | `instrument/Itembank_GARI_DE_0.1.json`, Version GARI-DE-0.1, 34 IDs, SHA-256 `12582782e64397d3460e88c2f4b2425b062f1f1c33725fc2d9953f5067afd050` |
| Codebuch | `instrument/Codebuch.md`, GARI-DE-0.1, SHA-256 `65c5bd31bcd93303bf87da8c7a2d0380d0dd0dfa2510e0453610785f4f1548cf` |
| Neue Modulversion | GARI-DE-ZM-ARB-0.1 (Entwicklungsentwurf) |
| Datenart | Keine Antwortdaten. Nur zwei handkonstruierte Rechentestfälle (SYNTHETIC_DEMO) zur Prüfung des Modulskripts |
| Berechnungsstatus | Befragungsergebnisse: NICHT_BERECHNET (keine Daten). Verfahrensprüfungen: ausgeführt, Exitstatus dokumentiert (Abschnitt 4) |

Gleiche Prompts garantieren keine identischen LLM-Ausgaben. Eine erneute Ausführung kann andere Formulierungsvorschläge erzeugen.

---

## 1 Kurzbeschreibung, Kontext und Annahmen

### 1.1 Ziel

Der fiktive Dienstleistungsbetrieb (40 Beschäftigte) will den Status quo zu generativer KI beschreiben, Hinweise auf Weiterbildungsbedarf ableiten und betriebliche Voraussetzungen gesondert erfassen. Dafür wird der Kern GARI-DE-0.1 unverändert eingesetzt. Zusätzlich soll ein Modul entstehen, das die Sorge der Beschäftigten vor Veränderungen ihres eigenen Arbeitsplatzes durch generative KI erfasst.

### 1.2 Übernommene Briefingangaben

| Prüfpunkt | Angabe laut Briefing | Folge für diesen Entwurf |
|---|---|---|
| Zweck | Status quo, Weiterbildungshinweise, betriebliche Voraussetzungen getrennt | Modul dient der Beschreibung und der Planung von Kommunikation, nicht der Personalentscheidung |
| Zielpopulation | Mitarbeitende aller Tätigkeitsbereiche, auch ohne GenAI-Nutzung | Alle Modulfragen für alle Personen, keine Filter |
| Tätigkeitsbereiche | Verwaltung, Kundenkontakt, Operative Tätigkeit | C01 bildet diese drei Bereiche nicht ab (siehe 4.3, offener Punkt P5) |
| Sprache | Deutsch | Deutsch |
| Bezug | Generative KI | Definition aus dem Kern gilt auch für das Modul |
| Bisherige Nutzung | Unbekannt, wird erhoben | Wird über C02/C03 erfasst, nicht angenommen |
| Zugelassene Anwendung | Ein freigegebenes Chat-Werkzeug für Büroarbeitsplätze | Nicht in den Fragebogentext übernommen, weil der Kern keinen Platzhalter dafür vorsieht |
| Aufgabenbezug | Nicht näher angegeben | Unbekannt |
| Betrachtungszeitraum | Nicht angegeben | Kern: vier Wochen (C02), drei Monate (A/I). Modul: zwei Jahre als **eigene Annahme** (siehe 3.3) |
| Erhebungsweg | Onlineformular, Link, freiwillig | Formular existiert noch nicht. Oberflächenabgleich OFFEN |
| Art der Daten | Keine Antwortdaten | Keine empirische Auswertung möglich |
| Kernbank / Codebuch | GARI-DE-0.1 / GARI-DE-0.1 | Kern unverändert |

### 1.3 Getroffene Annahmen und eigene Entscheidungen

- **A1** Die Betriebsart ist ausdrücklich angegeben (ENTWICKELN, Zusatzmodul). Der Kern wird nicht neu entwickelt, sondern nach den Regeln von ANWENDEN wörtlich übernommen.
- **A2** Die gewünschte Grundlage, die STARA-Awareness-Skala nach Brougham und Haar (2018), liegt weder im Volltext noch im Itemwortlaut vor. Ich kann sie deshalb weder übersetzen noch adaptieren. Alle Modulitems sind **NEU_ENTWICKELT**. Sie sind **keine** STARA-Items und dürfen nicht so bezeichnet werden.
- **A3** Der Modulzeitraum „in den nächsten zwei Jahren“ ist eine eigene Entscheidung (Begründung in 3.3).
- **A4** Das Modul liefert in Version 0.1 nur Einzelverteilungen. Es gibt keinen Modulmittelwert.
- **A5** Die Pretest-Rahmentexte der Word-Fassung (Testkürzel, „Im anschließenden Gespräch …“, Abschlusssatz zum Gespräch) passen nicht zu einer Onlinebefragung. Sie werden in einer gesondert gekennzeichneten Erhebungsfassung ersetzt. Das erlaubt `frozen_text_note` der Bank ausdrücklich. Definition, Kerninstruktionen, Items, Optionen und Reihenfolge bleiben unverändert.
- **A6** Fehlende Angaben zum Betrieb (Betriebsrat, Mindestgruppengröße, Formularplattform, Kontaktstelle) werden nicht erfunden. Sie stehen als kenntlich gemachte Platzhalter im Text und als Rückfragen in Abschnitt 7.

---

## 2 Quellen- und Konstruktregister

### 2.1 Quellenregister

| Quellen-ID | Nachweis | Geprüfter Dokumentstand | Zugang | Fundstelle | Zielgruppe / Sprache | Funktion hier | Grenzen |
|---|---|---|---|---|---|---|---|
| STARA_2018 | Brougham und Haar (2018), STARA-Awareness-Skala. Vollständiger bibliografischer Nachweis: **im Projekt nicht vorhanden** | Keiner | **Nur Nennung im Briefing.** Kein Volltext, kein Itemwortlaut, keine Skala, keine Lizenzangabe | Keine | Unbekannt | Gewünschte Grundlage. Kann hier **nicht** als Quelle für Items, Skala, Faktorstruktur oder Validität dienen | Jede inhaltliche Aussage über die Skala wäre ungeprüft. Sie fehlt deshalb bewusst. Nicht im Literaturverzeichnis als geprüfte Quelle führen |
| MAILS_DE_2023 | Carolus et al. (2023), deutscher Autorenfragebogen | Laut Bank und `Quellen_APA.md` geprüft (Items 1–12, 26–28; Auswertung S. 3) | Vollständig (laut Projektdokumentation) | Siehe Kernregister 3.1 | 300 deutschsprachige Erwachsene; allgemeine KI | Grundlage U, K, L im Kern | Nicht für das Modul verwendet. Von mir in dieser Sitzung nicht erneut eingesehen |
| POWERPILOT_2025 | Wichmann et al. (2025) mit bereitgestellter Itemsammlung | Paper und Itemsammlung; OSF-Anhang nicht abrufbar | Auszugsweise | Siehe Kernregister 3.1 | Energie-Monitoring-App, Deutschland | Grundlage A, I im Kern | **Direkter Vergleich mit dem OSF-Anhang bleibt offen.** Diese Grenze gilt auch für diesen Einsatz |
| AJZEN_TPB | Ajzen (o. J.) | Siebenseitiges Originaldokument (laut `Quellen_APA.md`) | Vollständig (laut Projektdokumentation) | Gesamtdokument | Methodenanleitung | Begründet, dass Ziel, Handlung, Kontext und Zeit einer Aussage eindeutig sein sollen. Hier genutzt für den festen Zeitbezug der Modulitems | Es handelt sich um eine Anleitung für Verhaltensfragebögen. Für ein Sorgekonstrukt nur sinngemäß übertragbar (eigene Entscheidung) |
| BOATENG_2018 | Boateng et al. (2018) | Volltext (laut `Quellen_APA.md`) | Vollständig | Gesamtdokument | Methodenprimer | Trennung von Itementwicklung, Pretest und Prüfung der Messqualität | Ein kleiner Pretest ersetzt keine Validierungsstudie |
| NCHS_2024 | National Center for Health Statistics (2024) | Methodenbeschreibung (laut `Quellen_APA.md`) | Vollständig | Webseite | Methodenbeschreibung | Orientierung für die kognitive Prüfung der neuen Items | Begründet keine bestimmte Mindestanzahl von Personen |
| PEFFERS_2007 | Peffers et al. (2007) | Abschnitte zu den sechs Aktivitäten (laut `Quellen_APA.md`) | Auszugsweise geprüft | Abschnitte zu Aktivitäten, Demonstration, Evaluation | Methodik | Einordnung des Moduls als neues Artefakt im DSR-Zyklus | Keine Detailprüfung der Fallstudien |
| VENABLE_2016 | Venable et al. (2016) | Verlagsvolltext (laut `Quellen_APA.md`) | Vollständig | Gesamtdokument | Methodik | Begründung formativer Verfahrensprüfung vor empirischer Prüfung | Anzahl der Testfälle ist eigene Entscheidung |

Hinweis zu den Statusangaben: Ich habe in dieser Sitzung ausschließlich `briefing.json`, die Itembank, das Codebuch und `Quellen_APA.md` eingesehen. Die Angaben „geprüft“ zu MAILS, POWERPILOT, Ajzen, Boateng, NCHS, Peffers und Venable übernehme ich aus `Quellen_APA.md` und der Bank. Es ist **keine** eigene Primärquellenprüfung. Die übrigen in `Quellen_APA.md` genannten Studien (Wichmann et al., 2024, 2026; Paetow et al., 2026; Do Khac et al., 2025; Bisbee et al., 2024) werden für das Modul nicht benötigt. Die Anzahl vorhandener Studien ist kein Grund für weitere Module.

### 2.2 Folge der fehlenden STARA-Quelle

Der Auftrag lautet, das Modul auf die STARA-Awareness-Skala zu stützen. Das ist mit den vorliegenden Unterlagen nicht möglich, ohne gegen die Arbeitsregeln 1 bis 3 zu verstoßen. Titel, Autorennamen und Jahr reichen nicht als Nachweis des Originalwortlauts. Es gibt zwei saubere Wege:

| Weg | Vorgehen | Status von Items | Voraussetzung |
|---|---|---|---|
| **W-A (empfohlen, wenn STARA gewünscht bleibt)** | Originalartikel mit Itemwortlaut, Antwortskala, Zielgruppe und Nutzungsbedingungen beschaffen. Danach übersetzen bzw. auf generative KI adaptieren und mit Fundstelle dokumentieren | UEBERSETZT oder ADAPTIERT | Volltext und Klärung der Nutzungsrechte (Rückfrage R1) |
| **W-B (hier geliefert)** | Eigene Items zum benannten Konstrukt, ohne Bezug auf einen ungeprüften Wortlaut | NEU_ENTWICKELT | Keine. Inhaltliche Prüfung im Pretest und später ein Abgleich mit W-A |

Ich liefere W-B als Entwicklungsentwurf. Kommt der STARA-Volltext später hinzu, ist das Modul neu zu bewerten. Dann entsteht eine neue Modulversion (mindestens GARI-DE-ZM-ARB-0.2), egal ob STARA-Items die eigenen ersetzen oder ergänzen. Aussagen wie „angelehnt an STARA“ oder „in Anlehnung an Brougham und Haar (2018)“ sollten bis dahin **nicht** im Itemregister stehen. Sie würden eine inhaltliche Herkunft nahelegen, die nicht geprüft ist.

Außerdem geht der Konstruktname im Briefing („Sorge vor Veränderungen des eigenen Arbeitsplatzes“) über ein reines Bewusstsein oder Wahrnehmen von Technologie hinaus. Ob das STARA-Konstrukt eher Wahrnehmung oder Besorgnis erfasst, kann ich ohne Quelle nicht beurteilen. Auch diese Passung ist bei W-A zu prüfen.

### 2.3 Konstruktmatrix für das Zusatzmodul

| Konstrukt / Facette | Arbeitsdefinition (eigene) | Diagnosezweck | Theoretische Grundlage | Instrument | Überschneidung mit dem Kern | Platz |
|---|---|---|---|---|---|---|
| Erwartete Veränderung der eigenen Aufgaben (Z01) | Kognitive Einschätzung, ob generative KI die eigenen Arbeitsaufgaben im festgelegten Zeitraum verändert. Keine Bewertung, kein Gefühl | Trennt Erwartung von Sorge. Ohne diese Frage wäre geringe Sorge nicht von „erwartet keine Veränderung“ zu unterscheiden | Eigene Ableitung. Zeitbezug nach Ajzen (o. J.) sinngemäß | NEU_ENTWICKELT | Nahe an C06 (sinnvolle Tätigkeiten) und K05/K06 (Einsatzmöglichkeiten vorstellen). Unterschied: Z01 fragt nach erwarteter Veränderung, nicht nach Sinnhaftigkeit oder Fähigkeit | Modul, Position 1 |
| Sorge um Aufgabenverlust (Z02) | Besorgnis, dass generative KI Teile der eigenen Aufgaben übernimmt | Beschreibung einer möglichen Belastung | Eigene Ableitung | NEU_ENTWICKELT | Keine im Kern | Modul |
| Sorge um Arbeitsplatzverlust (Z03) | Besorgnis, dass der eigene Arbeitsplatz durch generative KI wegfällt | Beschreibung einer möglichen Belastung | Eigene Ableitung | NEU_ENTWICKELT | Keine im Kern | Modul |
| Sorge um Überforderung durch veränderte Anforderungen (Z04) | Besorgnis, veränderten Anforderungen nicht gewachsen zu sein | Hinweis, ob Unterstützung beim Lernen auch als Entlastung gebraucht wird | Eigene Ableitung | NEU_ENTWICKELT | **Teilweise mit L01–L03** (Zutrauen ins eigene Lernen) und W02 = KNOWLEDGE. Unterschied: Z04 erfasst Besorgnis, L erfasst Selbstwirksamkeit. Beide werden nicht verrechnet | Modul |
| Sorge um Bedeutungsverlust des Fachwissens (Z05) | Besorgnis, dass das eigene Fachwissen im Betrieb weniger zählt | Beschreibung einer möglichen Belastung | Eigene Ableitung | NEU_ENTWICKELT | Keine im Kern | Modul |
| Wahrgenommene Informiertheit über betriebliche Pläne (Z06) | Wahrgenommene betriebliche Bedingung: Fühlt sich die Person über die Pläne des Betriebs informiert? | Trennt persönliche Sorge von wahrgenommenem Informationsstand. Liefert organisatorische statt individueller Hinweise | Eigene Ableitung | NEU_ENTWICKELT | Nahe an C05 (Regeln bekannt). Unterschied: C05 betrifft Nutzungsregeln, Z06 betrifft Pläne für den Arbeitsbereich | Modul, letzte Position |

**Trennung persönlich und betrieblich:** Z01–Z05 sind persönliche Einschätzungen. Z06 ist eine wahrgenommene betriebliche Bedingung. Beide Arten werden nicht zusammengefasst.

**Bewusst weggelassen:**

- **Allgemeine Technikangst oder Einstellung zu KI in der Gesellschaft.** Der Auftrag betrifft den eigenen Arbeitsplatz. Eine allgemeine Einstellung würde A01–A04 doppeln und den Arbeitsbezug verlieren.
- **Wechselabsicht oder Arbeitsplatzunsicherheit allgemein.** Das sind eigene Konstrukte mit eigenen Instrumenten. Hier fehlt jede Quelle, und die Fragen wären im Betrieb mit 40 Personen besonders heikel.
- **Positive Erwartungen (Chance, Entlastung).** Werden teilweise durch A01–A04 abgedeckt. Ein zusätzliches Chancenitem würde ohne Quelle eine Gegenrichtung konstruieren, deren Messbedeutung ungeklärt ist.
- **Umgepolte Items.** Ohne Vorlage aus einer geprüften Skala erfinde ich keine Umpolung (Arbeitsregel 6 und Phase 5).

**Wichtig für die Interpretation:** Sorge ist **kein** Merkmal fehlender Readiness. Sachlich begründete Sorge kann eine realistische Einschätzung sein. Sie wird weder in U, K, L, A oder I eingerechnet noch automatisch als Schulungsbedarf gelesen.

---

## 3 Fragebogenfassung, Itemregister und Codebuch

### 3.1 Kernregister GARI-DE-0.1 (unverändert übernommen)

Diese Tabelle wurde per Skript direkt aus der Bank erzeugt. Wortlaut und Antwortoptionen stehen vollständig in der Befragtenfassung 3.2.

| ID | Teilbereich | Status | Quelle / Fundstelle | Skala | Fehlwertgründe | Rolle |
|---|---|---|---|---|---|---|
| C01 | C | NEU_ENTWICKELT | Eigenentwicklung | single | KEINE_ANGABE | FESTER_KERN |
| C02 | C | NEU_ENTWICKELT | Eigenentwicklung | single | KEINE_ANGABE | FESTER_KERN |
| C03 | C | NEU_ENTWICKELT | Eigenentwicklung | single | KEINE_ANGABE | FESTER_KERN |
| C04 | C | NEU_ENTWICKELT | Eigenentwicklung | single | KEINE_ANGABE | FESTER_KERN |
| C05 | C | NEU_ENTWICKELT | Eigenentwicklung | single | KEINE_ANGABE | FESTER_KERN |
| C06 | C | NEU_ENTWICKELT | Eigenentwicklung | single | KEINE_ANGABE | FESTER_KERN |
| U01 | U | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 1, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| U02 | U | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 2, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| U03 | U | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 3, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| U04 | U | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 4, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| U05 | U | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 5, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| U06 | U | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 6, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| K01 | K | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 7, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| K02 | K | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 8, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| K03 | K | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 9, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| K04 | K | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 10, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| K05 | K | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 11, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| K06 | K | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 12, Seite 1; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| L01 | L | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 26, Seite 2; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| L02 | L | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 27, Seite 2; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| L03 | L | ADAPTIERT | MAILS_DE_2023: Deutscher Autorenfragebogen, Item 28, Seite 2; Zuordnung und Mittelwertregel Seite 3. | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| G01 | G | NEU_ENTWICKELT | Eigenentwicklung | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| G02 | G | NEU_ENTWICKELT | Eigenentwicklung | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| G03 | G | NEU_ENTWICKELT | Eigenentwicklung | ABILITY_0_10 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| A01 | A | ADAPTIERT | POWERPILOT_2025: Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | AGREEMENT_1_7 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| A02 | A | ADAPTIERT | POWERPILOT_2025: Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | AGREEMENT_1_7 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| A03 | A | ADAPTIERT | POWERPILOT_2025: Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | AGREEMENT_1_7 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| A04 | A | ADAPTIERT | POWERPILOT_2025: Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 4; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | AGREEMENT_1_7 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| I01 | I | ADAPTIERT | POWERPILOT_2025: Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | AGREEMENT_1_7 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| I02 | I | ADAPTIERT | POWERPILOT_2025: Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | AGREEMENT_1_7 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| I03 | I | ADAPTIERT | POWERPILOT_2025: Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | AGREEMENT_1_7 | NICHT_BEURTEILBAR, KEINE_ANGABE | FESTER_KERN |
| W01 | W | NEU_ENTWICKELT | Eigenentwicklung | multi | KEINE_ANGABE | FESTER_KERN |
| W02 | W | NEU_ENTWICKELT | Eigenentwicklung | multi | KEINE_ANGABE | FESTER_KERN |
| W03 | W | NEU_ENTWICKELT | Eigenentwicklung | text | KEINE_ANGABE | FESTER_KERN |

Geltende Grenzen des Kerns: Für POWERPILOT_2025 (A01–A04, I01–I03) ist der Itemwortlaut nur an der bereitgestellten Itemsammlung geprüft. Der direkte Vergleich mit dem OSF-Anhang bleibt offen. Weder eine vollständige Primärquellenprüfung aller Items noch eine psychometrische Validierung der Kombination wird behauptet. U, K, L, A und I sind vorläufige Teilbereichswerte. G01–G03 bleiben Einzelitems. Für G, C, W und über alle Bereiche gibt es keinen Gesamtwert. NICHT_ZUTREFFEND und UEBERSPRUNGEN sind in GARI-DE-0.1 nicht erlaubt.

### 3.2 Befragtenfassung (Demonstration)

**Erhebungsfassung:** GARI-DE-0.1 + GARI-DE-ZM-ARB-0.1 / Onlinerahmen DEMO-F1 (Entwurf)

Teil A ist der Kern. Abschnittsüberschriften, Definition, Instruktionen, Items und Antwortoptionen sind zeichengleich aus `frozen_participant_text` übernommen. Ersetzt wurden ausschließlich die Rahmenzeilen 1, 2, 4 und 113 (gezählt ab 0). Zeile 5 (Testkürzel/Datum) entfällt. Diese Änderungen sind in Tabelle 3.2.1 dokumentiert. Die Papierformulierungen „Kreisen Sie …“ und „Bitte fahren Sie auf der nächsten Seite fort“ gehören zum eingefrorenen Kern und bleiben stehen. Für die Onlinefassung ist das ein offener Punkt (P3). Die Darstellung von □ und Zahlenreihen gibt die Bank wieder. Im Onlineformular braucht jede Antwortmöglichkeit einschließlich NB und KA eine auswählbare Option.

Platzhalter in eckigen Klammern müssen vor einem realen Einsatz befüllt werden. Für die Demonstration bleiben sie bewusst offen.

#### Teil A: Kern GARI-DE-0.1

```text
Fragebogen zum Umgang mit generativer KI

Befragungsfassung GARI-DE-0.1 mit Zusatzmodul GARI-DE-ZM-ARB-0.1 · Demonstration für einen fiktiven Betrieb · Stand 18. Oktober 2026

Dieser Fragebogen erfasst Ihre Erfahrungen, Einschätzungen und Weiterbildungswünsche zu generativer KI bei der Arbeit. Am Ende folgen einige Fragen dazu, wie Sie mögliche Veränderungen Ihres Arbeitsplatzes durch generative KI sehen. Es geht nicht um die Bewertung Ihrer Arbeitsleistung. Ergebnisse werden nur zusammengefasst berichtet, nie für einzelne Personen und nie für Gruppen mit weniger als [MINDESTGRUPPE] Antworten. Geschätzte Dauer: 11 bis 17 Minuten.

Generative KI erzeugt oder bearbeitet auf Eingaben hin Inhalte, zum Beispiel Texte, Bilder, Audio, Videos oder Programmcode. Gemeint sind sowohl eigenständige Anwendungen als auch entsprechende Funktionen in anderen Programmen.

Die Teilnahme ist freiwillig. Sie können einzelne Fragen auslassen oder die Befragung beenden. Bitte tragen Sie keine Namen, Personalnummern oder vertraulichen Informationen ein. [DATENSCHUTZHINWEIS: Wortlaut erst nach Prüfung des tatsächlichen Formulars einsetzen; ohne diese Prüfung keine Anonymität zusagen.]

Ihre Tätigkeit und bisherige Nutzung

Bitte wählen Sie pro Frage genau eine Antwort.

C01  Wie sieht Ihre hauptsächliche Tätigkeit aus?

□ Überwiegend Büro- oder Bildschirmarbeit    □ Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst    □ Etwa gleich große Anteile beider Bereiche    □ Keine Angabe

C02  An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt?

□ An keinem Tag    □ An 1 bis 3 Tagen    □ An 4 bis 9 Tagen    □ An 10 bis 15 Tagen    □ An 16 oder mehr Tagen    □ Kann ich nicht einschätzen    □ Keine Angabe

C03  Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt?

□ Ja    □ Nein    □ Ich bin mir nicht sicher    □ Keine Angabe

C04  Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen?

□ Ja    □ Nein    □ Ich weiß es nicht    □ Keine Angabe

C05  Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit?

□ Ja    □ Teilweise    □ Nein    □ Ich weiß nicht, ob es solche Regeln gibt    □ Keine Angabe

C06  Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre?

□ Ja    □ Nein    □ Kann ich noch nicht beurteilen    □ Keine Angabe

Anwendung und Verständnis

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

U01  Ich kann eine generative KI bedienen.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

U02  Ich kann mir berufliche Aufgaben durch generative KI erleichtern.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

U03  Ich kann generative KI gezielt für meine Arbeitsziele einsetzen.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

U04  Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

U05  Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

U06  Ich kann generativer KI verständlich mitteilen, was ich brauche.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

K01  Ich kenne die zentralen Konzepte generativer KI.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

K02  Ich kann erklären, was generative KI bedeutet.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

K03  Ich kann Chancen und Grenzen generativer KI einschätzen.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

K04  Ich kann Vor- und Nachteile generativer KI beurteilen.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

K05  Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

K06  Ich kann mir künftige Anwendungen generativer KI vorstellen.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

Lernen und Prüfen

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

L01  Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

L02  Ich kann mich über Neuerungen bei generativer KI informieren.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

L03  Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

G01  Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

G02  Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

G03  Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf.

0    1    2    3    4    5    6    7    8    9    10       NB       KA

Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.

Einstellung und geplante Nutzung

Wie sehr stimmen Sie den folgenden Aussagen zu? Gemeint ist die Nutzung für Ihre beruflichen Aufgaben in den kommenden drei Monaten. „Freigegeben“ bedeutet, dass Ihr Unternehmen die betreffende Nutzung erlaubt.

1 = stimme überhaupt nicht zu   ·   7 = stimme vollständig zu

NB = nicht beurteilbar   ·   KA = keine Angabe. Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein.

A01  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft.

1    2    3    4    5    6    7       NB       KA

A02  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend.

1    2    3    4    5    6    7       NB       KA

A03  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig.

1    2    3    4    5    6    7       NB       KA

A04  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm.

1    2    3    4    5    6    7       NB       KA

Für die folgenden drei Aussagen: Denken Sie an die Bedingungen, die Sie in den nächsten drei Monaten tatsächlich erwarten. Setzen Sie keinen gesicherten Zugang voraus, wenn dieser unklar ist. Fehlender Zugang bedeutet jedoch nicht automatisch, dass Sie nicht antworten können.

I01  Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

1    2    3    4    5    6    7       NB       KA

I02  Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

1    2    3    4    5    6    7       NB       KA

I03  Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen.

1    2    3    4    5    6    7       NB       KA

Weiterbildung und Unterstützung

Bei W01 und W02 sind jeweils höchstens drei Antworten möglich. „Kein Weiterbildungswunsch“, „derzeit nichts“, „kann ich noch nicht einschätzen“ und „keine Angabe“ dürfen innerhalb einer Frage nur allein gewählt werden.

W01  Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen.

□ Grundlagen generativer KI

□ Passende Einsatzmöglichkeiten für meine Aufgaben

□ Klare Eingaben formulieren und Ergebnisse verbessern

□ Antworten und Quellen überprüfen

□ Betriebliche Regeln und zulässige Dateneingaben

□ Bei neuen Entwicklungen auf dem Laufenden bleiben

□ Anderes Thema

□ Derzeit kein Weiterbildungswunsch

□ Ich kann meinen Bedarf noch nicht einschätzen

□ Keine Angabe

W02  Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen.

□ Kein Zugang zu einem freigegebenen Werkzeug

□ Unklare betriebliche Regeln

□ Zu wenig Zeit zum Ausprobieren oder Lernen

□ Mir fehlt Wissen über die Nutzung

□ Ich erkenne keinen passenden Einsatz für meine Aufgaben

□ Unsicherheit über die Verlässlichkeit der Ergebnisse

□ Etwas anderes

□ Derzeit nichts

□ Kann ich noch nicht einschätzen

□ Keine Angabe

W03  Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen.

□ Keine Angabe

________________________________________________________________________

________________________________________________________________________

________________________________________________________________________
```

#### Teil B: Zusatzmodul GARI-DE-ZM-ARB-0.1

Das Modul steht nach W03 und vor dem Abschlusstext. So kann es die Antworten im Kern nicht durch eine vorher angesprochene Sorge beeinflussen (eigene Begründung, nicht empirisch geprüft).

```text
Veränderungen Ihres Arbeitsplatzes

Zum Schluss geht es um mögliche Veränderungen Ihres eigenen Arbeitsplatzes durch generative KI. Denken Sie dabei an die nächsten zwei Jahre. Es gibt keine richtigen oder falschen Antworten. Auch diese Fragen können Sie auslassen. Geschätzte zusätzliche Dauer: ein bis zwei Minuten.

1 = stimme überhaupt nicht zu   ·   7 = stimme vollständig zu

NB = nicht beurteilbar   ·   KA = keine Angabe. Wählen Sie eine Zahl oder eine dieser beiden Antworten.

Z01  Ich erwarte, dass generative KI meine Arbeitsaufgaben in den nächsten zwei Jahren verändern wird.

1    2    3    4    5    6    7       NB       KA

Z02  Ich mache mir Sorgen, dass generative KI in den nächsten zwei Jahren Teile meiner Arbeitsaufgaben übernimmt.

1    2    3    4    5    6    7       NB       KA

Z03  Ich mache mir Sorgen, dass mein Arbeitsplatz in den nächsten zwei Jahren durch generative KI wegfällt.

1    2    3    4    5    6    7       NB       KA

Z04  Ich mache mir Sorgen, dass mich die durch generative KI veränderten Anforderungen an meine Arbeit in den nächsten zwei Jahren überfordern.

1    2    3    4    5    6    7       NB       KA

Z05  Ich mache mir Sorgen, dass mein Fachwissen in unserem Betrieb in den nächsten zwei Jahren durch generative KI an Bedeutung verliert.

1    2    3    4    5    6    7       NB       KA

Z06  Ich fühle mich ausreichend darüber informiert, ob unser Betrieb Veränderungen durch generative KI in meinem Arbeitsbereich plant.

1    2    3    4    5    6    7       NB       KA

Vielen Dank für Ihre Teilnahme. Fragen zur Befragung beantwortet [KONTAKTSTELLE].
```

#### 3.2.1 Änderungen am Rahmentext gegenüber `frozen_participant_text`

| Zeile | Wortlaut der Bank (gekürzt) | Neue Fassung | Begründung | Folge für die Vergleichbarkeit |
|---|---|---|---|---|
| 1 | „Fassung für den Verständlichkeitstest · GARI-DE-0.1 · 29. September 2026“ | Kennung der Erhebungsfassung mit Modul und Hinweis auf Demonstration | Onlineerhebung statt Verständlichkeitstest | Keine für Items |
| 2 | „… Im anschließenden Gespräch prüfen wir … 10 bis 15 Minuten.“ | Gespräch gestrichen. Hinweis auf das Modul, Berichtsregel mit Platzhalter, Dauer 11 bis 17 Minuten | Kein Gespräch vorgesehen. Befragte sollen vorher wissen, dass Fragen zum Arbeitsplatz kommen | Gering. Die angekündigte Sorgethematik kann trotzdem den Kern rahmen. Im Pretest beobachten |
| 4 | „… den Test beenden … Beim begleiteten Test kennt die durchführende Person Sie …“ | „Befragung beenden“. Datenschutzhinweis als Platzhalter | Kein begleiteter Test. Anonymität erst nach Prüfung des Formulars zusagen | Keine für Items |
| 5 | „Testkürzel: … Datum: …“ | Entfällt | Online vergibt das System eine Antwort-ID | Keine |
| 113 | „Vielen Dank. Im Gespräch …“ | Dank und Kontaktstelle als Platzhalter | Kein Gespräch. Wer Sorgen äußert, braucht eine Anlaufstelle | Keine |

Die Regel zum Auslassen von Fragen ist in Einleitung (Zeile 4), Kern (NB/KA, „Keine Angabe“) und Modulinstruktion gleich: Jede Frage darf ausgelassen werden. Keine Modulfrage ist verpflichtend.

Bearbeitungszeit: 10 bis 15 Minuten laut Bank (noch nicht gemessen) plus geschätzte 1 bis 2 Minuten für sechs Modulitems. Das ergibt 11 bis 17 Minuten. Das ist eine Schätzung, keine Messung.

### 3.3 Wissenschaftliches Itemregister für das Zusatzmodul

**Gemeinsame Felder aller Modulitems**

| Feld | Wert |
|---|---|
| dimension_id | Z |
| Status | NEU_ENTWICKELT |
| Originalquelle / Fundstelle | Keine. Eigenentwicklung zum im Briefing benannten Konstrukt |
| Originalwortlaut | Keiner. STARA-Wortlaut nicht eingesehen (source_wording_checked = false) |
| Ursprüngliche Antwortskala | Entfällt (keine Vorlage) |
| Verwendete Antwortskala | AGREEMENT_1_7 aus GARI-DE-0.1: ganze Zahlen 1–7, 1 = „stimme überhaupt nicht zu“, 7 = „stimme vollständig zu“, keine Zwischenanker. Zusätzlich NB = nicht beurteilbar, KA = keine Angabe |
| Begründung der Skala | Eigene Entscheidung. Ein im Fragebogen bereits eingeführtes Format senkt die Belastung. Die STARA-Antwortskala ist unbekannt und wird nicht nachgebildet. Bei W-A ist die Originalskala zu prüfen und die Abweichung zu begründen |
| Rolle | ZUSATZMODUL (nicht Teil des festen Kerns). Nicht in der Kernbank, eigene Versionsnummer |
| Anzeigebedingung | ALWAYS. Alle Personen, unabhängig von Nutzung und Zugang |
| Zielgruppe | Alle Beschäftigten. Personen ohne Nutzung können die Fragen beantworten, weil sie sich auf den eigenen Arbeitsplatz beziehen, nicht auf die eigene Nutzung |
| Auswertungsrichtung | Höhere Zahl = mehr Zustimmung. Keine Umkodierung |
| Fehlwerte | NICHT_BEURTEILBAR, KEINE_ANGABE. NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig (keine Filter) |
| Evidenzstatus | Noch nicht empirisch geprüft. Keine Messqualität bekannt |
| Prüfstatus | Formale Verfahrensprüfung bestanden (Abschnitt 4.1). Inhaltliche Fachprüfung, kognitive Prüfung und Quellenabgleich mit STARA: OFFEN |
| Version | GARI-DE-ZM-ARB-0.1, 18. Oktober 2026 |

**Einzelitems**

| item_id | Facette | Deutsche Befragungsformulierung | Zweck | Rolle im Modul | Begründung der Formulierung | Bekannte Risiken |
|---|---|---|---|---|---|---|
| Z01 | ERWARTUNG | Ich erwarte, dass generative KI meine Arbeitsaufgaben in den nächsten zwei Jahren verändern wird. | Erwartung ohne Bewertung | Kontextitem | Neutral formuliert: „verändern“ statt „ersetzen“ oder „erleichtern“. Ein Gegenstand, fester Zeitraum | „Verändern“ kann positiv oder negativ verstanden werden. Das ist gewollt. Im Pretest prüfen, ob Befragte das so lesen |
| Z02 | SORGE_AUFGABEN | Ich mache mir Sorgen, dass generative KI in den nächsten zwei Jahren Teile meiner Arbeitsaufgaben übernimmt. | Sorge um Aufgabenverlust | Sorgeitem | „Teile“ statt „meine Aufgaben“, damit die Frage nicht nur für Extremfälle passt | Wer eine Übernahme begrüßt, stimmt nicht zu. Das ist korrekt, weil Sorge gefragt ist. Im Pretest prüfen |
| Z03 | SORGE_ARBEITSPLATZ | Ich mache mir Sorgen, dass mein Arbeitsplatz in den nächsten zwei Jahren durch generative KI wegfällt. | Sorge um Arbeitsplatzverlust | Sorgeitem | Klarster Ausdruck des Konstrukts im Briefing | **Sensibel.** Kann Sorge erst auslösen oder sozial erwünscht beantwortet werden. Daher Kontaktstelle im Abschlusstext und strenge Berichtsregeln |
| Z04 | SORGE_ANFORDERUNGEN | Ich mache mir Sorgen, dass mich die durch generative KI veränderten Anforderungen an meine Arbeit in den nächsten zwei Jahren überfordern. | Sorge um Überforderung | Sorgeitem | Erfasst Besorgnis, nicht Lernfähigkeit (die liegt in L01–L03) | Überschneidung mit L und W02 = KNOWLEDGE. Satz relativ lang (21 Wörter). Im Pretest auf Verständlichkeit prüfen |
| Z05 | SORGE_FACHWISSEN | Ich mache mir Sorgen, dass mein Fachwissen in unserem Betrieb in den nächsten zwei Jahren durch generative KI an Bedeutung verliert. | Sorge um Bedeutungsverlust | Sorgeitem | Bezieht sich auf den Betrieb, nicht auf den Arbeitsmarkt allgemein | „Fachwissen“ kann bei operativer Tätigkeit anders verstanden werden als in der Verwaltung. Im Pretest gezielt prüfen |
| Z06 | INFORMIERTHEIT | Ich fühle mich ausreichend darüber informiert, ob unser Betrieb Veränderungen durch generative KI in meinem Arbeitsbereich plant. | Wahrgenommene betriebliche Information | Kontextitem (betriebliche Bedingung) | „ob … plant“ setzt keine Pläne voraus. Trennt Informationslage von persönlicher Sorge | Wer „ausreichend“ unterschiedlich versteht, antwortet unterschiedlich. Nicht mit Z02–Z05 verrechnen |

**Begründung des Zeitraums:** Die Kernitems A/I beziehen sich auf drei Monate, C02 auf vier Wochen. Veränderungen von Aufgaben und Arbeitsplätzen spielen sich nach meiner Einschätzung eher über längere Zeit ab. Daher zwei Jahre. Das ist eine eigene methodische Entscheidung ohne Quellenbeleg. Nach Ajzen (o. J.) sollen Ziel, Kontext und Zeit einer Aussage eindeutig sein. Deshalb steht der Zeitraum in jedem Item und in der Instruktion. Im Pretest ist zu prüfen, ob der Wechsel von drei Monaten (A/I) zu zwei Jahren (Modul) bemerkt wird.

**Bekannte Grenzen der Formulierung:**

- Z02–Z05 sind gleich gerichtet und beginnen mit demselben Stamm „Ich mache mir Sorgen, …“. Das erleichtert das Lesen, kann aber Zustimmungstendenz begünstigen. Ohne geprüfte Vorlage füge ich keine umgepolten Items hinzu.
- Die Facettenaufteilung ist ein Prüfvorschlag, keine belegte Faktorenstruktur (Boateng et al., 2018).

### 3.4 Codebuch-Ergänzung für GARI-DE-ZM-ARB-0.1

Das Codebuch GARI-DE-0.1 bleibt unverändert gültig. Diese Ergänzung gilt nur für das Modul.

| IDs | Gegenstand | Antwortformat | Zusammenfassung |
|---|---|---|---|
| Z01 | Erwartete Veränderung eigener Aufgaben | Ganze Zahlen 1–7 | Einzelverteilung |
| Z02–Z05 | Vier Facetten der Sorge | Ganze Zahlen 1–7 | **Jeweils Einzelverteilung. Kein Modulmittelwert in Version 0.1** |
| Z06 | Wahrgenommene Informiertheit über betriebliche Pläne | Ganze Zahlen 1–7 | Einzelverteilung |

**Datenformat**

- Die Moduldaten werden **in einer eigenen JSON-Datei** gespeichert und nicht in das Antwortobjekt der Kerndaten geschrieben. Grund: Laut Codebuch stoppt die Rechenroutine `auswertung/score.py` bei unbekannten IDs und ist auf GARI-DE-0.1 festgelegt. Z-Items in den Kerndaten würden den Kernlauf abbrechen. Die Kennung im Kerndatensatz anzupassen, um das zu umgehen, ist ausdrücklich unzulässig.
- Pflichtfelder auf Dateiebene: `data_kind` (genau PRETEST, SURVEY oder SYNTHETIC_DEMO), `module_version` = „GARI-DE-ZM-ARB-0.1“, `erhebungsfassung` (siehe Manifest 4.4).
- Pflichtfelder je Person: `respondent_code` (dieselbe technische Antwort-ID wie in den Kerndaten, keine Namen), `module_version`, `answers` mit allen sechs IDs Z01–Z06, auch bei fehlender Antwort.
- Jede Antwort besteht aus `value` und `missing_reason`:

```json
{
  "Z01": {"value": 5, "missing_reason": null},
  "Z03": {"value": null, "missing_reason": "NICHT_BEURTEILBAR"},
  "Z05": {"value": null, "missing_reason": "KEINE_ANGABE"}
}
```

Das Beispiel ist ein Ausschnitt und enthält keine Daten.

**Werte und Fehlwerte**

- Zulässige Werte: ganze Zahlen 1 bis 7. Es gibt keine 0. Eine 0 ist ein Fehler und wird nicht als Fehlwert umgedeutet.
- NB: `value: null`, `missing_reason: "NICHT_BEURTEILBAR"`.
- KA oder leeres Feld: `value: null`, `missing_reason: "KEINE_ANGABE"`. Motive werden nicht ergänzt.
- NICHT_ZUTREFFEND und UEBERSPRUNGEN sind nicht zulässig.
- Mehrfachmarkierung: vor Eingabe klären. Ist keine eindeutige Zuordnung möglich, KEINE_ANGABE kodieren und im Korrekturprotokoll vermerken.
- Bei Abbruch: nur vorhandene Angaben übertragen. Die übrigen Items bleiben KEINE_ANGABE und werden im Prüfbericht als „Abbruch vermutet“ nur dann ausgewiesen, wenn das Formular den Abbruch technisch belegt.

**Rechen- und Berichtsregeln (vor einer Erhebung festgelegt)**

1. Je Item: gültige Anzahl, Anzahl NB, Anzahl KA, Verteilung über 1–7 als absolute Zahlen. Prozentwerte nur mit Nenner (Personen mit gültiger Antwort).
2. Kein Modulmittelwert, kein Summenwert, keine Klassifikation („besorgt“/„nicht besorgt“), keine Grenzwerte. Eine spätere Zusammenfassung von Z02–Z05 braucht eine neue Version, eine Begründung und Daten aus einer größeren Erhebung.
3. Keine Verrechnung von Z-Items mit U, K, L, G, A, I, C oder W. Keine Rangliste zwischen 1–7- und 0–10-Werten.
4. Kreuztabellen mit Kernitems (zum Beispiel Z04 mit W01 oder Z06 mit C05) sind nur deskriptiv und nur, wenn jede berichtete Zelle die Mindestgruppengröße [MINDESTGRUPPE] erreicht. Sonst werden Kategorien zusammengefasst oder nicht berichtet.
5. **Keine Auswertung nach C01 für das Modul, solange eine Gruppe unter [MINDESTGRUPPE] liegt.** Bei 40 Beschäftigten und freiwilliger Teilnahme ist das wahrscheinlich. Wer in einer kleinen Gruppe Sorge um den Arbeitsplatz äußert, könnte sonst erkennbar werden.
6. Freitext gibt es im Modul nicht. Äußerungen zum Arbeitsplatz in W03 werden nach Codebuch GARI-DE-0.1 behandelt und für Berichte von identifizierenden Details bereinigt.
7. Für SYNTHETIC_DEMO wird jede Darstellung sichtbar als Demonstration gekennzeichnet. Für PRETEST stehen Verständlichkeit und Verfahrensprobleme im Bericht, kein Belegschaftsprofil. Nur SURVEY erlaubt einen Bericht über die befragte Belegschaft, begrenzt durch Teilnahmequote und Verteilung.

**Rechenwerkzeug:** `work/modul_verteilung.py` (siehe 4.2). Es prüft Version, `data_kind`, doppelte Personen, vollständige IDs und zulässige Werte. Bei Fehlern stoppt es mit Exitstatus 2 und repariert nichts.

---

## 4 Prüfbericht

### 4.1 Ausgeführte Verfahrensprüfung des Kerns und des Moduls

Skript: `/home/claude/eval/runs/F1/work/pruefung.py`, ausgeführt mit Python 3.13.16. **Exitstatus 0.** Ausgabe (gekürzt auf die Prüfergebnisse):

```text
SHA256 Kernbank: 12582782e64397d3460e88c2f4b2425b062f1f1c33725fc2d9953f5067afd050
Kern-IDs: 34 Modul-IDs: ['Z01', 'Z02', 'Z03', 'Z04', 'Z05', 'Z06']
Fehler: keine
Zeilen Befragtenfassung: 130 davon Kern: 114
```

| Prüfung | Ergebnis |
|---|---|
| Kernbank-Datei nicht verändert (SHA-256 vor und nach der Arbeit gleich) | Bestanden |
| 34 eindeutige Kern-IDs | Bestanden |
| Jede Kern-Itemzeile `ID  Wortlaut` steht zeichengleich in `frozen_participant_text` | Bestanden (34/34) |
| Reihenfolge der Items in Bank und Befragtentext gleich | Bestanden |
| Keine ID-Kollision zwischen Kern und Modul; Dimension Z im Kern unbelegt | Bestanden |
| Zeilen 6 bis 112 des eingefrorenen Texts (alle Abschnitte, Instruktionen, Items, Optionen) in Teil A unverändert enthalten | Bestanden (separater Abgleich, Ergebnis `True`) |

Was diese Prüfung **nicht** zeigt: Sie bestätigt formale Gleichheit von Texten und IDs. Sie sagt nichts über Verständlichkeit, Messqualität oder die spätere Umsetzung im Onlineformular. Sie ist eine Selbstprüfung desselben Systems, kein unabhängiges Gutachten.

### 4.2 Technischer Test der Modulroutine (nur synthetisch)

Daten: zwei **von Hand konstruierte Rechentestfälle** (`data_kind: SYNTHETIC_DEMO`, Herkunft HANDKONSTRUIERTER_RECHENTESTFALL). Keine LLM-Persona, keine realen Antworten. Sie prüfen nur, ob das Skript richtig zählt und Fehler erkennt.

| Testfall | Erwartung | Tatsächlicher Exitstatus | Ergebnis |
|---|---|---|---|
| Gültige Datei mit NB und KA | Zählung ohne Fehler | 0 | Bestanden. Z03: 1 gültig, 1 NB. Z05: 1 gültig, 1 KA. Z06: 1 gültig, 1 KA |
| Wert 0 bei Z02 | Abbruch | 2 („unzulässig“) | Bestanden |
| Doppelte Person und NICHT_ZUTREFFEND | Abbruch mit beiden Meldungen | 2 („doppelt: S1“, „unzulässig … NICHT_ZUTREFFEND“) | Bestanden |

Diese Zählungen sind **synthetisch** und kein Ergebnis über Beschäftigte. `tests/test_scoring.py` und `auswertung/score.py` des Kerns lagen in diesem Lauf nicht bei und wurden nicht ausgeführt.

### 4.3 Offene Probleme

| Nr. | Problem | Betroffene Stelle | Vorschlag | Status |
|---|---|---|---|---|
| P1 | STARA-Quelle fehlt. Das Modul erfüllt den Wunsch nach STARA-Grundlage nicht | Gesamtes Modul | Rückfrage R1, dann Weg W-A und neue Modulversion | OFFEN |
| P2 | Modulitems ungeprüft (inhaltlich und kognitiv) | Z01–Z06 | Fachliche Durchsicht durch eine zweite Person, danach kleiner kognitiver Pretest (Abschnitt 5) | OFFEN |
| P3 | Eingefrorene Kerninstruktionen enthalten Papierformulierungen („Kreisen Sie …“, „auf der nächsten Seite“) | Kern, Zeilen 21, 49, 64, 68 | Nicht stillschweigend ändern. Entweder Papierwortlaut online stehen lassen und im Pretest prüfen oder eine neue Kernversion mit Onlinewortlaut anlegen | OFFEN, Entscheidung durch Projektverantwortliche |
| P4 | Onlineformular existiert noch nicht. Abgleich von IDs, Wortlaut, Reihenfolge, NB/KA-Optionen, Höchstzahl bei W01/W02, Exklusivoptionen, Pflichtfeldern und Exporttyp fehlt | Umsetzung | Abgleich nach Abschnitt „Verbindlicher Abgleich“ des Masterprompts, mit ungesendeter Testsitzung | Freigabestatus **OFFEN** |
| P5 | C01 erfasst „Büro / andere Arbeit / gemischt“, nicht die drei Bereiche des Briefings (Verwaltung, Kundenkontakt, Operative Tätigkeit) | Kern C01 | Kern nicht ändern. Bei 40 Beschäftigten ist eine feinere Bereichsfrage wegen der Erkennbarkeit nicht zu empfehlen. Falls trotzdem gewünscht: eigenes, dokumentiertes Zusatzitem außerhalb des Kerns | OFFEN |
| P6 | Mindestgruppengröße, Anonymitätszusage und Kontaktstelle unbekannt | Rahmentext, Berichtsregeln | Rückfrage R2 | OFFEN |
| P7 | Die Ankündigung der Arbeitsplatzfragen in der Einleitung könnte die Antworten im Kern rahmen | Rahmentext Zeile 2 | Im Pretest beobachten. Alternative: Ankündigung erst vor Teil B | OFFEN |
| P8 | Zeitraumwechsel 3 Monate (A/I) zu 2 Jahren (Modul) | Teil B | Im Pretest gezielt nachfragen | OFFEN |
| P9 | Nutzungsrechte: bei W-A die STARA-Rechte; im Kern die offenen Rechte für MAILS-Anpassungen und POWERPILOT-Items | Quellenregister | Vor jeder öffentlichen Weitergabe klären | OFFEN |
| P10 | Sensibles Thema. Mögliche Mitbestimmungs- oder Datenschutzpflichten des Betriebs sind nicht bekannt | Einsatz im Betrieb | Vor einem realen Einsatz klären lassen. Ich treffe dazu keine rechtliche Aussage | OFFEN |

### 4.4 Begleitmanifest (Entwurf)

| Feld | Eintrag |
|---|---|
| Referenzbank | GARI-DE-0.1, `Itembank_GARI_DE_0.1.json`, SHA-256 siehe Kopf |
| Modul | GARI-DE-ZM-ARB-0.1, `work/Zusatzmodul_ZM_ARB_0.1.json`, SHA-256 `efa8fa1972abf19172632ad477b48501dfbb060908ffb9812e635dbc44c61af2` |
| Erhebungsfassung | GARI-DE-0.1 + GARI-DE-ZM-ARB-0.1 / Onlinerahmen DEMO-F1 (Entwurf) |
| `questionnaire_version` in Kerndaten | GARI-DE-0.1 (Kern und Kerninstruktionen unverändert, Modul danach). Ob die geänderte Einleitung die Vergleichbarkeit mit früheren Daten berührt, bleibt im Bericht zu nennen |
| Erhebungsrunde | Keine. Demonstration |
| Plattform | Nicht festgelegt |
| Datum Oberflächenabgleich | Nicht durchgeführt |
| Tatsächlich geprüfte Stellen | Nur Textebene (4.1). Keine Formularoberfläche |
| Offene Abweichungen | P3, P4, P5 |
| Erstellung | Masterprompt 0.5 mit Auftrag „Betriebsart: ENTWICKELN (Zusatzmodul)“. Eingabedateien: `briefing.json`, `instrument/Itembank_GARI_DE_0.1.json`, `instrument/Codebuch.md`, `Quellen_APA.md`. System: Claude, Modellkennung claude-opus-5-5. Manuelle Änderungen: keine |
| Freigabestatus | **OFFEN** |

---

## 5 Auswertungsbericht

**Status: NICHT_BERECHNET.** Es liegen keine Antwortdaten vor (`antwortdaten_vorhanden: false`). Es gibt deshalb keine Befunde zum Kern und keine zum Modul. Die Zahlen in 4.2 stammen aus zwei synthetischen Rechentestfällen und sind kein Ergebnis.

**Rechenanweisung für einen späteren Einsatz**

1. Kerndaten (GARI-DE-0.1, 34 IDs) wie im Codebuch vorgesehen mit `auswertung/score.py` auswerten, tatsächlichen Exitstatus prüfen und nur die erzeugte Ausgabe verwenden.
2. Moduldaten getrennt auswerten:

```bash
python3 modul_verteilung.py moduldaten.json modul_ergebnis.json
echo $?   # 0 = ausgewertet, 2 = Prüffehler (Meldungen lesen, nichts reparieren)
```

3. Kerndaten und Moduldaten nur über `respondent_code` verbinden. Prüfen, dass beide Dateien dieselbe `data_kind` und dieselbe Erhebungsfassung haben.
4. Berichtsregeln aus 3.4 anwenden, besonders die Mindestgruppengröße.

Quelltext von `modul_verteilung.py` (geprüft wie in 4.2):

```python
"""Verteilungen für Zusatzmodul GARI-DE-ZM-ARB-0.1. Kein Skalenwert, keine Imputation."""
import json, sys
VERSION = "GARI-DE-ZM-ARB-0.1"
IDS = ["Z01", "Z02", "Z03", "Z04", "Z05", "Z06"]
MISSING = {"NICHT_BEURTEILBAR", "KEINE_ANGABE"}
KINDS = {"PRETEST", "SURVEY", "SYNTHETIC_DEMO"}

def check(data):
    err = []
    if data.get("module_version") != VERSION: err.append("module_version abweichend")
    if data.get("data_kind") not in KINDS: err.append("data_kind unzulässig")
    seen = set()
    for r in data.get("responses", []):
        pid = r.get("respondent_code")
        if pid in seen: err.append(f"doppelt: {pid}")
        seen.add(pid)
        if r.get("module_version") != VERSION: err.append(f"{pid}: Version abweichend")
        a = r.get("answers", {})
        if set(a) != set(IDS): err.append(f"{pid}: IDs fehlen oder unbekannt")
        for k, v in a.items():
            val, mr = v.get("value"), v.get("missing_reason")
            if val is None and mr in MISSING: continue
            if mr is None and isinstance(val, int) and not isinstance(val, bool) and 1 <= val <= 7: continue
            err.append(f"{pid} {k}: unzulässig {v}")
    return err

def describe(data):
    out = {"module_version": VERSION, "data_kind": data["data_kind"], "n_records": len(data["responses"]), "items": {}}
    for i in IDS:
        d = {"valid_n": 0, "NICHT_BEURTEILBAR": 0, "KEINE_ANGABE": 0, "distribution": {str(k): 0 for k in range(1, 8)}}
        for r in data["responses"]:
            v = r["answers"][i]
            if v["value"] is None: d[v["missing_reason"]] += 1
            else: d["valid_n"] += 1; d["distribution"][str(v["value"])] += 1
        out["items"][i] = d
    return out

if __name__ == "__main__":
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    e = check(data)
    if e: print("\n".join(e)); sys.exit(2)
    json.dump(describe(data), open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
```

---

## 6 Maßnahmenmatrix (Planungslogik ohne Daten)

Es gibt noch keine Befunde. Die folgende Tabelle legt **vorab** fest, wie Modulergebnisse später gelesen werden. Sie ist eine eigene, überprüfbare Planungsregel, keine validierte Entscheidungsregel. Sie liefert Hinweise für Gruppen, nie Urteile über Einzelne. „Viele“ oder „wenige“ wird im Bericht immer durch Anzahl und Nenner ersetzt.

| Befund-ID (Platzhalter) | Beobachtung | Items | Einordnung | Mögliche Maßnahme | Unsicherheit | Erfolgskontrolle |
|---|---|---|---|---|---|---|
| ZB-01 | Zustimmung (6–7) zu Z02 oder Z03 bei einem Teil der Befragten | Z02, Z03, Z01 | Persönliche Sorge. **Kein Schulungsdefizit** | Organisatorisch: offene Information zu Plänen und Grenzen des KI-Einsatzes, Gesprächsangebot über Führung oder eine vertrauliche Anlaufstelle | Sorge kann sachlich begründet sein. Ursachen sind aus den Daten nicht ablesbar | Wiederholung von Z02/Z03 und Z06 in einer späteren Befragung mit gleicher Version. Veränderung nur beschreiben |
| ZB-02 | Ablehnung (1–2) bei Z06 | Z06, C05 | Organisatorischer Handlungsbedarf (Information) | Betrieb klärt und kommuniziert, ob und was für einzelne Arbeitsbereiche geplant ist. Zuständigkeit festlegen | „Ausreichend“ ist subjektiv. Fehlen Pläne, kann auch das kommuniziert werden | Z06 bei Wiederholung. Anzahl Rückfragen bei der Kontaktstelle |
| ZB-03 | Zustimmung zu Z04 zusammen mit W01-Wünschen oder W02 = KNOWLEDGE/TIME | Z04, W01, W02, L01–L03 | Möglicher Unterstützungsbedarf, als **Hypothese** | Lernangebot zu den in W01 gewählten Themen. Lernzeit klären, wenn W02 = TIME | Sorge und Lernbedarf sind nicht dasselbe. Keine Wirksamkeit eines Trainings belegt | Teilnahme, kurze Rückmeldung nach dem Angebot, Wiederholung von Z04 und W01 |
| ZB-04 | Zustimmung zu Z05 | Z05, C01 (nur bei ausreichender Gruppengröße) | Offene Frage | Gesprächsformat zur künftigen Rolle des Fachwissens. Kein Training ableiten | Kein Kernitem erklärt diesen Befund | Qualitative Nachfrage in einer späteren Runde |
| ZB-05 | Viele NB bei einem Z-Item | Z01–Z06 | Unklare Einschätzbarkeit | Erst Verständlichkeit und Informationslage prüfen. NB nicht als geringe Sorge lesen | NB ist nur aussagekräftig, wenn die Option online auswählbar war (P4) | Kognitive Nachprüfung des Items |
| ZB-06 | Geringe Zustimmung zu Z01 | Z01, C06 | Keine erwartete Veränderung | Keine Maßnahme nötig. Mit C06 lesen: Fehlende Aufgabenpassung ist kein Defizit | Erwartung kann sich ändern | Keine |

Priorisierung später transparent nach Anzahl betroffener Personen, Aufgabenrelevanz und Umsetzbarkeit, als Planungsentscheidung gekennzeichnet. Die Zuordnung der Kernbefunde folgt unverändert dem Codebuch GARI-DE-0.1.

---

## 7 Änderungsprotokoll, Pretestplan und nächste Eingaben

### 7.1 Änderungsprotokoll

| Nr. | Änderung | Stelle | Begründung | Folge für Vergleichbarkeit | Nachprüfung |
|---|---|---|---|---|---|
| Ä1 | Neues Zusatzmodul GARI-DE-ZM-ARB-0.1 mit Z01–Z06 | Nach W03 | Auftrag im Briefing | Kern unberührt. Modul nicht mit anderen Modulen oder STARA vergleichbar | OFFEN |
| Ä2 | Rahmentext für Onlinebefragung (Zeilen 1, 2, 4, 5, 113) | Einleitung, Abschluss | Kein Gespräch, kein begleiteter Test. Erlaubt durch `frozen_text_note` | Für Items keine. Mögliche Rahmung durch Ankündigung (P7) | OFFEN |
| Ä3 | Codebuch-Ergänzung, getrennte Moduldatei, Skript `modul_verteilung.py` | Datenhaltung | Versionssperre von `score.py` nicht umgehen | Keine für Kerndaten | Technisch synthetisch geprüft, Exitstatus dokumentiert |

Keine Änderung wurde als Verbesserung belegt. Alle Änderungen sind ungetestet.

### 7.2 Pretestplan für das Modul (noch nicht durchgeführt)

Zweck: begrenzte explorative Verständlichkeitsprüfung nach dem Ansatz kognitiver Interviews (National Center for Health Statistics, 2024). Sie belegt keine Messqualität und keine Vollständigkeit gefundener Probleme (Boateng et al., 2018).

- **Auswahl:** gezielt unterschiedliche Tätigkeiten (Verwaltung, Kundenkontakt, operative Tätigkeit) und unterschiedliche Nutzungserfahrung, auch Personen ohne Nutzung. Umfang nach dem vereinbarten Evaluationsplan.
- **Methode:** moderiertes Gespräch nach dem Ausfüllen. Falls nur schriftlich: als schriftliche Nachbefragung bezeichnen, nicht als Interview.
- **Einzelne Prüffragen (je ein Aspekt):**
  1. Z01: Was verstehen Sie hier unter „verändern“?
  2. Z01–Z06: Woran haben Sie bei „in den nächsten zwei Jahren“ gedacht?
  3. Z02: Was bedeutet für Sie „Teile meiner Arbeitsaufgaben“?
  4. Z03: Wie war es für Sie, diese Frage zu beantworten?
  5. Z04: Wie sind Sie zu Ihrer Antwort gekommen?
  6. Z05: Was zählt für Sie zu Ihrem „Fachwissen“?
  7. Z06: Woran haben Sie gedacht, als Sie „ausreichend informiert“ gelesen haben?
  8. Modul: Fehlte Ihnen eine Antwortmöglichkeit? Wenn ja, welche?
  9. Modul: Haben Sie bemerkt, dass sich der Zeitraum gegenüber den vorherigen Fragen geändert hat?
- **Protokoll je Befund:** Personenkürzel, Erhebungsfassung, Item-ID, wörtliches Zitat oder Paraphrase (kennzeichnen), Kategorie (Verständlichkeit, Erinnerbarkeit, Urteilsbildung, Antwortzuordnung, Aufgabenrelevanz).
- **Bearbeitungszeit** im Pretest messen, nicht aus Absendezeitstempeln ableiten.
- KI-Personas dürfen technisch erproben, ersetzen aber keine Testpersonen und begründen allein keine Itemänderung.

### 7.3 Rückfragen (gebündelt, höchstens drei)

- **R1 STARA-Grundlage:** Können Sie den Volltext von Brougham und Haar (2018) mit Itemwortlaut, Antwortskala und Nutzungsbedingungen bereitstellen? Ohne ihn bleibt das Modul eine Eigenentwicklung und darf nicht als STARA-basiert bezeichnet werden.
- **R2 Erhebungsrahmen:** Welche Mindestgruppengröße gilt für Berichte, wer sieht die Rohdaten, sammelt das Formular E-Mail-Adressen oder Anmeldedaten, und wer ist Kontaktstelle? Davon hängen Anonymitätshinweis und Auswertung nach C01 ab.
- **R3 Zeitraum und Ziel des Moduls:** Passt der Zeitraum von zwei Jahren? Soll das Modul später als Skala ausgewertet werden (dann ist eine größere Erhebung mit eigener Begründung nötig) oder bei Einzelitems bleiben?

### 7.4 Nächste erforderliche Eingaben

1. Antworten auf R1 bis R3.
2. Entscheidung zu P3 (Papierwortlaut in der Onlinefassung).
3. Das tatsächlich umgesetzte Onlineformular für den Oberflächenabgleich.
4. Fachliche Durchsicht der Modulitems durch eine zweite Person.
5. Pretestnotizen zur Modulfassung.
6. Erst danach: Antwortdaten mit `data_kind` und Versionsangaben.

---

## Literaturverzeichnis

Nur Quellen, die im Text verwendet werden und in `Quellen_APA.md` mit Prüfstatus dokumentiert sind. Brougham und Haar (2018) ist bewusst nicht aufgenommen, weil kein geprüfter Nachweis vorliegt.

Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. University of Massachusetts Amherst. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

National Center for Health Statistics. (2024, April 16). *Cognitive interviewing*. Centers for Disease Control and Prevention. https://www.cdc.gov/nchs/ccqder/question-evaluation/cognitive-interviewing.html

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. *European Journal of Information Systems, 25*(1), 77–89. https://doi.org/10.1057/ejis.2014.36

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114

---

## Status

- **Erstellt:** Quellen- und Konstruktregister für das Modul, Befragtenfassung (Kern unverändert plus Modul), Itemregister Z01–Z06, Codebuch-Ergänzung, Auswertungsskript, Maßnahmenlogik, Pretestplan, Manifest.
- **Geprüft:** Nur formal und technisch. Kern zeichengleich und unverändert (Exitstatus 0). Modulskript mit synthetischen Testfällen (Exitstatus 0 bzw. 2 wie erwartet). Selbstprüfung, kein unabhängiges Gutachten.
- **Berechnet:** Nichts über Beschäftigte. NICHT_BERECHNET.
- **Fehlt:** STARA-Volltext (R1), Erhebungsrahmen (R2, R3), fachliche Zweitdurchsicht, Pretest des Moduls, Onlineformular und Oberflächenabgleich (Freigabestatus OFFEN), reale Daten.
- Das Modul ist **kein** STARA-Instrument und **nicht** validiert. Der Kern GARI-DE-0.1 bleibt ein nicht psychometrisch validierter Entwurf mit offener POWERPILOT-Grenze.
