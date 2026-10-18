# GARI-DE-0.1 im fiktiven Produktionsbetrieb: Befragungsfassung, Register, Codebuch und Prüfbericht

**Betriebsart: ANWENDEN** (ausdrücklich angegeben)
**Kontext: FIKTIVE DEMONSTRATION.** Das Unternehmen ist erfunden. Es gibt keine realen Daten. Alle Angaben in eckigen Klammern sind offene Platzhalter. Ich habe sie bewusst nicht mit erfundenen Unternehmensmerkmalen gefüllt.

## 0 Kopfangaben

| Angabe | Eintrag |
|---|---|
| Datum | 18. Oktober 2026 |
| System / Modell | Claude (Anthropic); angezeigte Modellbezeichnung „Opus 5.5“ (Kennung claude-opus-5-5) |
| Weitere Systemparameter (Temperatur, Kontextlänge usw.) | NICHT_VERFUEGBAR |
| Promptversion | Masterprompt 0.5 vom 17. Oktober 2026 |
| Referenzbank | `instrument/Itembank_GARI_DE_0.1.json`, Version GARI-DE-0.1, Stand 29. September 2026, 34 Item-IDs (SHA-256-Präfix der bereitgestellten Datei: 12582782e64397d3) |
| Codebuch | `instrument/Codebuch.md`, GARI-DE-0.1, Projektpaket 0.2, Stand 29. September 2026, redaktionell fortgeschrieben 17. Oktober 2026 (SHA-256-Präfix: 65c5bd31bcd93303) |
| Quellenstand | `Quellen_APA.md`, Stand 17. Oktober 2026 |
| Briefing | `briefing.json`, Version 0.1, Szenario S2 |
| Fragebogenversion (Kern) | GARI-DE-0.1, unverändert |
| Umsetzungskennung der Onlinefassung | noch nicht vergeben; Vorschlag `GARI-DE-0.1/ONLINE-S2-E1` (siehe 4.5) |
| Datenart | Keine Antwortdaten vorhanden. Künftig: SYNTHETIC_DEMO für jede Erprobung dieses fiktiven Falls; SURVEY nur bei einem realen Einsatz |
| Berechnungsstatus | NICHT_BERECHNET (keine Daten; Auswertungsskript nicht beigefügt) |

Gleiche Prompts garantieren keine identischen LLM-Ausgaben. Dieses Dokument ist eine Ausgabe eines einzelnen Laufs.

---

## 1 Kurzbeschreibung, Annahmen und Rückfragen

### 1.1 Ziel, Zielgruppe, Kontext

Ein fiktiver Produktionsbetrieb mit 400 Beschäftigten will den Status quo zu generativer KI beschreiben, Hinweise auf Weiterbildungsbedarf ableiten und betriebliche Voraussetzungen gesondert erfassen. Befragt werden Mitarbeitende aller Tätigkeitsbereiche: Schichtarbeit in der Produktion, Logistik, Verwaltung und Führung. Personen ohne bisherige Nutzung sind ausdrücklich eingeschlossen. Nicht alle haben einen eigenen PC oder freigegebene KI-Werkzeuge. Die Befragung läuft als freiwilliges Onlineformular über einen Link, teilweise über ein Tablet im Pausenraum.

### 1.2 Prüfung der Eingangsangaben

| Angabe | Stand laut Briefing | Behandlung |
|---|---|---|
| Zweck | Status quo, Weiterbildungshinweise, betriebliche Voraussetzungen | unverändert übernommen |
| Zielpopulation | alle Mitarbeitenden, auch Nichtnutzende | unverändert übernommen; GARI-DE-0.1 zeigt allen alle Fragen |
| Tätigkeitsbereiche | Schichtarbeit Produktion, Logistik, Verwaltung, Führung | Kern-Item C01 bildet diese vier Bereiche nicht ab (nur Büro / andere Arbeit / gemischt). Siehe Rückfrage R2 |
| Sprache | Deutsch | Kern ist deutschsprachig |
| Bezug | generative KI | Kerndefinition F3 unverändert |
| Bisherige Nutzung | unbekannt, wird erhoben | C02, C03 |
| Zugelassene Anwendungen | nicht angegeben | UNBEKANNT; nicht ergänzt |
| Betriebliche Regeln | nicht angegeben | UNBEKANNT; C05 erfasst nur die Kenntnis aus Sicht der Befragten |
| Zugang | nicht alle haben PC oder freigegebene Werkzeuge | als Kontext übernommen; C04 und W02 = ACCESS erfassen das |
| Betrachtungszeitraum | nicht angegeben | Kern legt fest: vergangene vier Wochen (C02), nächste drei Monate (A, I); unverändert |
| Erhebungszeitraum | nicht angegeben | Platzhalter [ERHEBUNGSZEITRAUM] |
| Gewünschte Ausgabe | nicht ausdrücklich angegeben | Annahme: Ergebnisumfang laut Masterprompt für ANWENDEN |
| Art der Daten | keine Antwortdaten | keine Auswertung möglich; Auswertungsregeln vorbereitet |
| Erhebungsweg | Onlineformular, Link, freiwillig, teils Tablet im Pausenraum | Plattform unbekannt; Vorgaben plattformneutral formuliert |
| Mindestgruppengröße für Berichte | nicht angegeben | Platzhalter [MINDESTGRUPPE]; siehe R1 |
| Kontaktstelle | nicht angegeben | Platzhalter [KONTAKTSTELLE] |

### 1.3 Getroffene Annahmen

- A-1: Die Betriebsart ANWENDEN ist ausdrücklich gesetzt. Itembank und Codebuch liegen vor. Ich erstelle deshalb eine unternehmensbezogene Befragungsfassung mit unverändertem Kern und keinen Entwicklungsentwurf.
- A-2: Das Briefing ist eine fiktive Demonstration. Der Fragebogen wird nicht an reale Personen verteilt. Alle betriebsspezifischen Zusagen bleiben Platzhalter.
- A-3: Die Onlineplattform ist unbekannt. Ich setze keine bestimmte Plattform voraus. Plattformspezifische Prüfpunkte sind als zu prüfende Fragen formuliert, nicht als Tatsachen.
- A-4: Der Rahmentext der Word-Fassung ist auf einen begleiteten Pretest zugeschnitten (Testkürzel, anschließendes Gespräch, „den Test beenden“). Die Bank erlaubt laut `frozen_text_note`, diese organisatorische Pretest-Einleitung für eine spätere Vollbefragung als gesondert dokumentierte Erhebungsfassung zu ersetzen. Das tue ich in Abschnitt 3.3, mit Einzelnachweis. Definition, Items, Skalen, Reihenfolge, Zeitbezüge und alle Kerninstruktionen bleiben wörtlich.
- A-5: Die in der Kerninstruktion stehende Formulierung „Kreisen Sie pro Aussage eine Zahl ein“ stammt aus der Papierfassung. Ich übernehme sie trotzdem unverändert, weil Instruktionen zum Kern gehören. Die Folge steht als offenes Problem P-03 im Prüfbericht.
- A-6: Projektdateien, die der Masterprompt nennt, die aber in dieser Sitzung nicht beigefügt sind, habe ich nicht verwendet: `auswertung/score.py`, `tests/test_scoring.py`, `pretest/GoogleForms_Runde2_Anleitung.md`, `pretest/Abschluss_Evaluation_R3.md`, der Word-Fragebogen und die Beispieldateien. Ich greife nicht still auf ältere Fassungen oder Erinnerungen an diese Dateien zurück. Siehe P-09.

### 1.4 Rückfragen (gebündelt, höchstens drei)

Die folgenden Punkte ändern den nächsten Schritt wesentlich. Alles andere ist bereits erstellt. Bis zur Antwort gelten die genannten Voreinstellungen.

**R1 Plattform, Anonymität und Berichtsebene.** Welche Formularplattform wird verwendet, wer hat Zugriff auf die Rohdaten, werden Anmeldung, E-Mail-Adresse, IP-Adresse oder Gerätekennung erfasst, und ab welcher Mindestzahl an Antworten darf eine Gruppe berichtet werden?
*Voreinstellung bis zur Antwort:* Kein Anonymitätsversprechen im Einleitungstext (Platzhalter [ANONYMITAETSSATZ] bleibt leer). Berichte nur für den Gesamtbetrieb und für die drei C01-Kategorien, jeweils nur ab [MINDESTGRUPPE] Antworten. Freigabestatus OFFEN.

**R2 Gruppenauswertung nach den vier Tätigkeitsbereichen.** Soll nach Schichtarbeit Produktion, Logistik, Verwaltung und Führung getrennt berichtet werden? Der Kern kann das nicht. Dafür wäre ein Zusatzmodul außerhalb des Kerns nötig (Entwurf in 3.4), mit eigenem Risiko der Wiedererkennbarkeit, vor allem bei Führungskräften.
*Voreinstellung bis zur Antwort:* Zusatzmodul wird **nicht** eingesetzt. Gruppen nur über C01.

**R3 Organisatorischer Rahmen der Teilnahme.** Erhebungszeitraum, Kontaktstelle, darf die Teilnahme in der Arbeitszeit erfolgen, und wie wird der Link verteilt (zum Beispiel Aushang mit QR-Code, E-Mail, Tablet)? Gibt es bereits betriebliche Regeln oder freigegebene Werkzeuge, auf die nach der Befragung verwiesen werden soll?
*Voreinstellung bis zur Antwort:* Platzhalter [ERHEBUNGSZEITRAUM], [KONTAKTSTELLE]. Keine Aussage zu Arbeitszeit. Kein Verweis auf Regeln oder Werkzeuge im Fragebogen. Der Kern bleibt davon ohnehin unberührt.

---

## 2 Quellen- und Konstruktregister mit Evidenzgrenzen

### 2.1 Quellenregister

Wichtig: Ich habe in dieser Sitzung keine Originalquelle selbst eingesehen. Der Prüfstand in der Spalte „Dokumentierter Prüfstand“ ist aus `Quellen_APA.md` und dem `source_register` der Itembank übernommen. Er ist eine Projektangabe, keine erneute Prüfung durch mich.

| Quellen-ID | Nachweis | Dokumentierter Prüfstand | Zugang laut Projekt | Zielgruppe / Sprache | Konstrukt / Funktion | Grenzen |
|---|---|---|---|---|---|---|
| MAILS_DE_2023 | Carolus et al. (2023); deutscher Autorenfragebogen MAILS | Artikel-Volltext und deutscher Originalfragebogen geprüft; Items 1–6, 7–12, 26–28; Zuordnung und Mittelwertregel S. 3 | vollständig (laut Projekt) | 300 deutschsprachige Erwachsene; Deutsch | Anwendung (U), Verständnis (K), Lernen (L) | Evidenz betrifft allgemeine KI und Selbstberichte. Übertragung auf generative KI und Arbeitskontext ist eine Anpassung. Fehlwertoptionen ergänzt. Nutzungsrechte für veränderte Items vor öffentlicher Veröffentlichung klären |
| MAILS_2024 | Koch et al. (2024) | Volltext eingesehen, Abschnitte 2.1 und 3.4 | vollständig (laut Projekt) | Deutsch/Englisch | Kurzfassung als Alternative geprüft | Kurzfassung nicht eingesetzt (enthält KI-Entwicklung). Fordert selbst weitere Validierung |
| POWERPILOT_2025 | Wichmann et al. (2025), HICSS-58, S. 961–970; bereitgestellte Itemsammlung Questionnaire 2 / PowerPilot | Paper und bereitgestellte Itemsammlung (Datensatz_v1.docx) geprüft | auszugsweise: OSF-Anhang GEBK9 am 29.09.2026 und beim erneuten Abruf nicht zugänglich | Deutschland; englischer Itemwortlaut in der Sammlung | Einstellung (A), Nutzungsabsicht (I), RAA-Anschluss | **Direkter Wortlautvergleich mit dem OSF-Anhang offen.** Energieanwendung statt GenAI; Kontext, Zeitraum und Gegenstand angepasst |
| AJZEN_TPB | Ajzen (o. J.), Constructing a TPB questionnaire | Siebenseitiges Originaldokument eingesehen | vollständig (laut Projekt) | – | Verhaltensdefinition über Ziel, Handlung, Kontext, Zeit | Begründet die Konstruktion von A und I, ist kein Messinstrument |
| PEFFERS_2007 | Peffers et al. (2007) | Abschnitte zu den sechs Aktivitäten im Volltext geprüft | vollständig für diese Abschnitte | – | Entwicklungsmethode (DSR) | Methode, kein Messmodell |
| FEDS_2016 | Venable et al. (2016) | Verlagsvolltext | vollständig (laut Projekt) | – | Evaluationsrahmen | Testumfang ist eigene Entscheidung |
| BOATENG_2018 | Boateng et al. (2018) | Volltext | vollständig (laut Projekt) | – | Trennung Itementwicklung, Pretest, Validierung | belegt keine Validität dieser Kombination |
| NCHS_2024 | National Center for Health Statistics (2024) | Methodenseite gelesen | vollständig (laut Projekt) | – | Kognitive Interviews | begründet keinen Mindestumfang von fünf Personen |
| BISBEE_2024 | Bisbee et al. (2024) | Verlags-PDF, Abstract und Schlussdiskussion | auszugsweise | politische Befragungen | Grenzen von LLM-Personas | keine Validierung dieses Fragebogens |
| WICHMANN_2024, PAETOW_2026, DOKHAC_2025, WICHMANN_2026 | siehe Literaturverzeichnis | bereitgestellt als Paper Fragebogen 1, 3, 4, 5 | laut Projekt bereitgestellt | Gesundheit, VR, Entscheidungstragende, virtuelle Meetings | Hintergrund zu Akzeptanz, Aufgabenpassung, Vertrauen, Arbeitsbedingungen | **Keine Items im Kern.** Bewusst nicht als eigene Module aufgenommen |

### 2.2 Konstruktmatrix (Kern GARI-DE-0.1, unverändert übernommen)

| Bereich | Definition im Projekt | Diagnosezweck | Grundlage | Instrument / Herkunft | Überschneidung | Platz | Ebene |
|---|---|---|---|---|---|---|---|
| C | Tätigkeit, berufliche und private Nutzung, Zugang, Regelkenntnis, Aufgabenrelevanz | Einordnen, Voraussetzungen erkennen | eigene Projektentscheidung | 6 NEU_ENTWICKELTE Einzelitems | C04 mit W02 = ACCESS; C05 mit W02 = RULES; C06 mit W02 = TASK_FIT | Seite 2 | betriebliche Bedingungen und Verhalten |
| U | Selbst eingeschätzte Anwendung | möglicher Lernbedarf | MAILS (Anwendung) | 6 ADAPTIERTE MAILS-Items | mit I (Absicht) und C02 (Nutzung) inhaltlich verwandt, aber Selbsteinschätzung statt Verhalten | Seite 3 | persönlich, Selbsteinschätzung |
| K | Selbst eingeschätztes Verständnis | möglicher Lernbedarf | MAILS (Wissen/Verstehen) | 6 ADAPTIERTE MAILS-Items | K03/K04 mit G01 | Seite 3 | persönlich, Selbsteinschätzung |
| L | Zutrauen in das eigene Lernen | Ansatzpunkt für Lernangebote | MAILS (Items 26–28) | 3 ADAPTIERTE Items | mit W01 = KEEP_CURRENT | Seite 4 | persönlich, Selbsteinschätzung |
| G | Prüfen von Ergebnissen, Quellen, zulässigen Eingaben | verantwortlicher Umgang | eigene Begründung | 3 NEU_ENTWICKELTE Einzelitems, **kein Mittelwert** | G03 mit C05 und W01 = DATA_RULES | Seite 4 | persönlich, Selbsteinschätzung |
| A | Einstellung zur arbeitsbezogenen Nutzung freigegebener GenAI | Haltung, bedingte Bewertung | RAA (Ajzen) | 4 ADAPTIERTE PowerPilot-Items | nicht mit Absicht gleichsetzen | Seite 5 | persönlich, Einstellung |
| I | Absicht unter tatsächlich erwarteten Bedingungen, nächste drei Monate | geplante Nutzung | RAA (Ajzen) | 3 ADAPTIERTE PowerPilot-Items | hängt von C04 ab; C04 = NO bei I ≥ 6 nur Prüfhinweis | Seite 5 | persönlich, berichtete Absicht |
| W | Lernwünsche, Hindernisse, Freitext | Lernwunsch und Organisationsbedarf trennen | eigene Begründung | 3 NEU_ENTWICKELTE Items | W02 ergänzt C04/C05/C06 | Seite 6 | Lernwunsch und wahrgenommene Bedingungen |

Nicht im Kern und nicht ergänzt: Vertrauen, Aufgaben-Technologie-Passung als Skala, soziale Arbeitsbedingungen, objektive Leistung. Grund laut Projekt: keine geprüfte Übertragbarkeit der Items auf GenAI bei allen Beschäftigten. In ANWENDEN darf ich den Kern ohnehin nicht erweitern.

**Keine der fünf Teilbereichszusammenfassungen (U, K, L, A, I) ist als GenAI-Skala validiert.** Die Kombination ist nicht psychometrisch geprüft. Die vollständige Primärquellenprüfung aller Items ist nicht belegt: Bei POWERPILOT_2025 fehlt der Abgleich mit dem OSF-Anhang. Diese Grenze gilt auch für diesen Einsatz.

---

## 3 Befragungsfassung für den fiktiven Produktionsbetrieb

### 3.1 Hinweise zur Fassung

- Kern: GARI-DE-0.1, alle 34 Item-IDs, Wortlaute, Reihenfolge, Antwortoptionen, Fehlwertoptionen, Instruktionen und die Definition **unverändert** aus `frozen_participant_text` übernommen.
- Organisatorischer Rahmen (Seite 1 und Abschlussseite): ersetzt als gesondert dokumentierte Erhebungsfassung. Jede Ersetzung ist mit `[E…]` markiert und in 3.3 begründet. Die Markierungen sind Begleitdokumentation und erscheinen nicht im Formular.
- Seitenumbrüche folgen den Abschnitten der Word-Fassung. Der Kernhinweis „Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.“ steht dadurch tatsächlich vor einem Seitenwechsel.
- Keine Frage ist Pflicht. Es gibt keine Sprungregeln. Alle Personen sehen alle Fragen.
- „( )“ steht für eine auswählbare Einzelwahloption, „- [ ]“ für ein Kästchen bei Mehrfachwahl.
- Für die Demonstration wird kein Name und keine Personalnummer erhoben.

### 3.2 Text für Befragte

#### Seite 1 von 7: Einleitung

**Fragebogen zum Umgang mit generativer KI**  `[Kern-Rahmentext F0, unverändert]`

Onlinebefragung · GARI-DE-0.1 · Umsetzungskennung [UMSETZUNG_ID] · [ERHEBUNGSZEITRAUM]  `[E1, ersetzt F1]`

Dieser Fragebogen erfasst Ihre Erfahrungen, Einschätzungen und Weiterbildungswünsche zu generativer KI bei der Arbeit. Es geht dabei nicht um die Bewertung Ihrer Arbeitsleistung. Geschätzte Dauer für den Fragebogen: 10 bis 15 Minuten.  `[E2, ersetzt F2: Satz zum Pretestgespräch entfernt, übrige Sätze wörtlich]`

Die Ergebnisse werden nur zusammengefasst ausgewertet, für den gesamten Betrieb und für Gruppen mit mindestens [MINDESTGRUPPE] Antworten. Einzelne ausgefüllte Fragebögen werden nicht an Vorgesetzte weitergegeben. Die Ergebnisse dienen der Planung von Weiterbildung und von betrieblichen Voraussetzungen, zum Beispiel Zugang und Regeln.  `[E3, neu; nur einsetzen, wenn der Betrieb diese Zusagen verbindlich festgelegt hat]`

Generative KI erzeugt oder bearbeitet auf Eingaben hin Inhalte, zum Beispiel Texte, Bilder, Audio, Videos oder Programmcode. Gemeint sind sowohl eigenständige Anwendungen als auch entsprechende Funktionen in anderen Programmen.  `[F3, Kern-Definition, unverändert]`

Die Teilnahme ist freiwillig. Sie können einzelne Fragen auslassen oder die Befragung jederzeit beenden. Bitte tragen Sie keine Namen, Personalnummern oder vertraulichen Informationen ein. Im Fragebogen werden weder Name noch Personalnummer abgefragt. [ANONYMITAETSSATZ: nur nach geprüfter Formulareinstellung einsetzen, siehe Abschnitt 4.4]  `[E4, ersetzt F4]`

Wenn Sie ein gemeinsam genutztes Tablet verwenden: Bitte schließen Sie die Seite nach dem Absenden oder Abbrechen. [SATZ_ZU_NICHT_ABGESENDETEN_ANTWORTEN: nur nach Plattformprüfung einsetzen]  `[E5, neu, Kontext Tablet im Pausenraum]`

Fragen zur Befragung: [KONTAKTSTELLE]  `[E6, neu, erlaubte Kontaktangabe]`

*F5 „Testkürzel / Datum“ entfällt in der Onlinefassung. Eine zufällige technische Antwort-ID wird vom System vergeben und nicht abgefragt.*

#### Seite 2 von 7

**Ihre Tätigkeit und bisherige Nutzung**

Bitte wählen Sie pro Frage genau eine Antwort.

**C01**  Wie sieht Ihre hauptsächliche Tätigkeit aus?

Antwortoptionen (Einzelwahl): ( ) Überwiegend Büro- oder Bildschirmarbeit | ( ) Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst | ( ) Etwa gleich große Anteile beider Bereiche | ( ) Keine Angabe

**C02**  An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt?

Antwortoptionen (Einzelwahl): ( ) An keinem Tag | ( ) An 1 bis 3 Tagen | ( ) An 4 bis 9 Tagen | ( ) An 10 bis 15 Tagen | ( ) An 16 oder mehr Tagen | ( ) Kann ich nicht einschätzen | ( ) Keine Angabe

**C03**  Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt?

Antwortoptionen (Einzelwahl): ( ) Ja | ( ) Nein | ( ) Ich bin mir nicht sicher | ( ) Keine Angabe

**C04**  Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen?

Antwortoptionen (Einzelwahl): ( ) Ja | ( ) Nein | ( ) Ich weiß es nicht | ( ) Keine Angabe

**C05**  Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit?

Antwortoptionen (Einzelwahl): ( ) Ja | ( ) Teilweise | ( ) Nein | ( ) Ich weiß nicht, ob es solche Regeln gibt | ( ) Keine Angabe

**C06**  Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre?

Antwortoptionen (Einzelwahl): ( ) Ja | ( ) Nein | ( ) Kann ich noch nicht beurteilen | ( ) Keine Angabe

#### Seite 3 von 7

**Anwendung und Verständnis**

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**U01**  Ich kann eine generative KI bedienen.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**U02**  Ich kann mir berufliche Aufgaben durch generative KI erleichtern.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**U03**  Ich kann generative KI gezielt für meine Arbeitsziele einsetzen.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**U04**  Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**U05**  Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**U06**  Ich kann generativer KI verständlich mitteilen, was ich brauche.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**K01**  Ich kenne die zentralen Konzepte generativer KI.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**K02**  Ich kann erklären, was generative KI bedeutet.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**K03**  Ich kann Chancen und Grenzen generativer KI einschätzen.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**K04**  Ich kann Vor- und Nachteile generativer KI beurteilen.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**K05**  Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**K06**  Ich kann mir künftige Anwendungen generativer KI vorstellen.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

#### Seite 4 von 7

**Lernen und Prüfen**

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**L01**  Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**L02**  Ich kann mich über Neuerungen bei generativer KI informieren.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**L03**  Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**G01**  Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**G02**  Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

**G03**  Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf.

Antwortoptionen (Einzelwahl): ( ) 0 | ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) 8 | ( ) 9 | ( ) 10 | ( ) NB | ( ) KA

Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.

#### Seite 5 von 7

**Einstellung und geplante Nutzung**

Wie sehr stimmen Sie den folgenden Aussagen zu? Gemeint ist die Nutzung für Ihre beruflichen Aufgaben in den kommenden drei Monaten. „Freigegeben“ bedeutet, dass Ihr Unternehmen die betreffende Nutzung erlaubt.

1 = stimme überhaupt nicht zu   ·   7 = stimme vollständig zu

NB = nicht beurteilbar   ·   KA = keine Angabe. Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein.

**A01**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft.

Antwortoptionen (Einzelwahl): ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) NB | ( ) KA

**A02**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend.

Antwortoptionen (Einzelwahl): ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) NB | ( ) KA

**A03**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig.

Antwortoptionen (Einzelwahl): ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) NB | ( ) KA

**A04**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm.

Antwortoptionen (Einzelwahl): ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) NB | ( ) KA

Für die folgenden drei Aussagen: Denken Sie an die Bedingungen, die Sie in den nächsten drei Monaten tatsächlich erwarten. Setzen Sie keinen gesicherten Zugang voraus, wenn dieser unklar ist. Fehlender Zugang bedeutet jedoch nicht automatisch, dass Sie nicht antworten können.

**I01**  Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

Antwortoptionen (Einzelwahl): ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) NB | ( ) KA

**I02**  Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

Antwortoptionen (Einzelwahl): ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) NB | ( ) KA

**I03**  Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen.

Antwortoptionen (Einzelwahl): ( ) 1 | ( ) 2 | ( ) 3 | ( ) 4 | ( ) 5 | ( ) 6 | ( ) 7 | ( ) NB | ( ) KA

#### Seite 6 von 7

**Weiterbildung und Unterstützung**

Bei W01 und W02 sind jeweils höchstens drei Antworten möglich. „Kein Weiterbildungswunsch“, „derzeit nichts“, „kann ich noch nicht einschätzen“ und „keine Angabe“ dürfen innerhalb einer Frage nur allein gewählt werden.

**W01**  Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen.

- [ ] Grundlagen generativer KI
- [ ] Passende Einsatzmöglichkeiten für meine Aufgaben
- [ ] Klare Eingaben formulieren und Ergebnisse verbessern
- [ ] Antworten und Quellen überprüfen
- [ ] Betriebliche Regeln und zulässige Dateneingaben
- [ ] Bei neuen Entwicklungen auf dem Laufenden bleiben
- [ ] Anderes Thema
- [ ] Derzeit kein Weiterbildungswunsch
- [ ] Ich kann meinen Bedarf noch nicht einschätzen
- [ ] Keine Angabe

**W02**  Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen.

- [ ] Kein Zugang zu einem freigegebenen Werkzeug
- [ ] Unklare betriebliche Regeln
- [ ] Zu wenig Zeit zum Ausprobieren oder Lernen
- [ ] Mir fehlt Wissen über die Nutzung
- [ ] Ich erkenne keinen passenden Einsatz für meine Aufgaben
- [ ] Unsicherheit über die Verlässlichkeit der Ergebnisse
- [ ] Etwas anderes
- [ ] Derzeit nichts
- [ ] Kann ich noch nicht einschätzen
- [ ] Keine Angabe

**W03**  Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen.

- [ ] Keine Angabe

Freitextfeld (mehrzeilig, optional)

#### Seite 7 von 7: Abschluss

Vielen Dank für Ihre Teilnahme. Ihre Antworten werden mit „Absenden“ übermittelt.  `[E7, ersetzt F113]`


### 3.3 Kontextänderungen gegenüber der Word-Fassung (vollständige Liste)

| Nr. | Stelle in `frozen_participant_text` | Original | Onlinefassung | Begründung | Folge für Vergleichbarkeit |
|---|---|---|---|---|---|
| E1 | Zeile 1 (Untertitel) | „Fassung für den Verständlichkeitstest · GARI-DE-0.1 · 29. September 2026“ | „Onlinebefragung · GARI-DE-0.1 · Umsetzungskennung [UMSETZUNG_ID] · [ERHEBUNGSZEITRAUM]“ | kein Verständlichkeitstest; Umsetzung muss identifizierbar sein | keine inhaltliche |
| E2 | Zeile 2 | enthält „Im anschließenden Gespräch prüfen wir, ob die Fragen verständlich sind.“ | dieser Satz entfällt; übrige drei Sätze wörtlich | kein Gespräch vorgesehen | gering; Zweckangabe und Dauer unverändert |
| E3 | neu nach Zeile 2 | – | Satz zu Gruppenauswertung, Weitergabe und Verwendungszweck mit [MINDESTGRUPPE] | Masterprompt verlangt Beschreibung der vorgesehenen Ausgaben auf Gruppenebene | Rahmungseffekt nicht geprüft; nur einsetzen, wenn verbindlich zugesagt |
| E4 | Zeile 4 | „… oder den Test beenden. … Beim begleiteten Test kennt die durchführende Person Sie; eine vollständige Anonymität wird deshalb nicht zugesagt.“ | „… oder die Befragung jederzeit beenden. …“; Satz zum begleiteten Test entfällt; neuer Satz: keine Abfrage von Name oder Personalnummer; [ANONYMITAETSSATZ] als Platzhalter | anderes Erhebungssetting; Anonymität nur nach geprüfter Einstellung zusagen | Regel zum Auslassen von Fragen ist identisch („Sie können einzelne Fragen auslassen“) |
| E5 | neu | – | Hinweis für gemeinsam genutztes Tablet | Besonderheit Pausenraum | keine inhaltliche |
| E6 | neu | – | Kontaktstelle | in `context_changes_allowed` ausdrücklich erlaubt | keine |
| – | Zeile 5 | „Testkürzel / Datum“ | entfällt | kein Testkürzel bei Onlinebefragung; Datum entsteht technisch | keine Itemänderung |
| E7 | Zeile 113 | „Vielen Dank. Im Gespräch können Sie jetzt …“ | „Vielen Dank für Ihre Teilnahme. Ihre Antworten werden mit „Absenden“ übermittelt.“ | kein Gespräch | keine inhaltliche; Schlussseite ist organisatorisch, Ersetzung trotzdem als Abweichung geführt |

Nicht geändert, obwohl sachlich zu prüfen: Zeilen 21, 49 („Kreisen Sie pro Aussage eine Zahl ein.“) und 68 („Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein.“). Siehe P-03.

**Hinweis zur Einstufung von E1 bis E7:** `context_changes_allowed` erlaubt wörtlich nur „Kontaktangaben und organisatorischer Erhebungshinweis außerhalb des Fragebogens“. `frozen_text_note` erlaubt zusätzlich, die organisatorische Pretest-Einleitung für eine Vollbefragung als gesondert dokumentierte Erhebungsfassung zu ersetzen. E1 bis E5 und E7 stützen sich auf diese zweite Regel. Sie ist eine Ermessensauslegung. Deshalb bekommt die Onlinefassung eine eigene Umsetzungskennung, und die Freigabe bleibt OFFEN, bis die Projektverantwortliche diese Einstufung bestätigt.

### 3.4 Optionales Zusatzmodul außerhalb des Kerns (nur nach Entscheidung zu R2)

Status: **NICHT EINGESETZT.** Entwurf zur Entscheidung. Nicht Teil von GARI-DE-0.1.

| ID | Text | Optionen | Status | Platz |
|---|---|---|---|---|
| S2-X01 | In welchem Bereich arbeiten Sie hauptsächlich? | ( ) Produktion im Schichtbetrieb ( ) Logistik ( ) Verwaltung ( ) Anderer Bereich ( ) Keine Angabe | NEU_ENTWICKELT, Kontextitem, ungeprüft | eigene Seite **nach** W03, vor dem Abschluss, damit Kernreihenfolge und Kernkontext unverändert bleiben |
| S2-X02 | Haben Sie Führungsverantwortung für andere Beschäftigte? | ( ) Ja ( ) Nein ( ) Keine Angabe | NEU_ENTWICKELT, Kontextitem, ungeprüft | wie oben |

Begründung: Das Briefing nennt vier Bereiche, C01 trennt nur Büro, andere Arbeit und gemischt. Führung liegt quer zu den Bereichen und wird deshalb getrennt gefragt.
Risiken: Kleine Gruppen, besonders Führung in Logistik oder Verwaltung, können Personen wiedererkennbar machen. Berichte dann nur ab [MINDESTGRUPPE] und keine Kreuzung von S2-X01 × S2-X02 × C01. Die Zusatzfragen dürfen nicht im Antwortobjekt der 34 Kern-IDs gespeichert werden, weil die Rechenroutine laut Codebuch bei unbekannten IDs stoppt. Sie gehören in ein getrenntes Feld `context_supplement`.

---

## 4 Umsetzungs- und Erhebungsvorgaben für das Onlineformular

Diese Vorgaben sind ein Vorschlag für die Übertragung. Sie belegen keine erfolgreiche Umsetzung. Ein Erzeugungsprompt oder die Selbstauskunft eines erzeugenden Systems ist kein Nachweis.

### 4.1 Feldtypen und Exportkodierung je Item

Allgemeine Regeln:

- NB und KA müssen **auswählbare Optionen** sein. Ein Hinweistext reicht nicht. Kann ein Skalenfragetyp der Plattform (etwa eine lineare Skala) keine NB/KA-Option aufnehmen, wird eine Einzelwahl mit allen Zahlen plus NB und KA verwendet. Keine Option darf still entfallen.
- Keine numerischen Ersatzcodes für NB oder KA (zum Beispiel 99, -1 oder 0). 0 ist auf der 0–10-Skala eine gültige Fähigkeitseinschätzung.
- Die exportierten Zahlen werden beim Einlesen in Ganzzahlen umgewandelt. Text wie „10“ bleibt im Rohexport erhalten und wird nur über die Zuordnungstabelle übersetzt.
- Einzelwahl: Die Plattform muss genau eine Auswahl erzwingen.

| Item | Formularfeld (Typ) | Sichtbare Option → `value` | NB/KA/leer → `missing_reason` |
|---|---|---|---|
| C01 | Einzelwahl, Pflicht: nein | „Überwiegend Büro- oder Bildschirmarbeit“ → `OFFICE`; „Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst“ → `OTHER_WORK`; „Etwa gleich große Anteile beider Bereiche“ → `MIXED` | „Keine Angabe“ oder leer → null/KEINE_ANGABE |
| C02 | Einzelwahl, Pflicht: nein | „An keinem Tag“ → `D0`; „An 1 bis 3 Tagen“ → `D1_3`; „An 4 bis 9 Tagen“ → `D4_9`; „An 10 bis 15 Tagen“ → `D10_15`; „An 16 oder mehr Tagen“ → `D16_PLUS`; „Kann ich nicht einschätzen“ → `UNKNOWN` | „Keine Angabe“ oder leer → null/KEINE_ANGABE |
| C03 | Einzelwahl, Pflicht: nein | „Ja“ → `YES`; „Nein“ → `NO`; „Ich bin mir nicht sicher“ → `UNKNOWN` | „Keine Angabe“ oder leer → null/KEINE_ANGABE |
| C04 | Einzelwahl, Pflicht: nein | „Ja“ → `YES`; „Nein“ → `NO`; „Ich weiß es nicht“ → `UNKNOWN` | „Keine Angabe“ oder leer → null/KEINE_ANGABE |
| C05 | Einzelwahl, Pflicht: nein | „Ja“ → `KNOWN`; „Teilweise“ → `PARTLY`; „Nein“ → `NOT_KNOWN`; „Ich weiß nicht, ob es solche Regeln gibt“ → `EXISTENCE_UNKNOWN` | „Keine Angabe“ oder leer → null/KEINE_ANGABE |
| C06 | Einzelwahl, Pflicht: nein | „Ja“ → `YES`; „Nein“ → `NO`; „Kann ich noch nicht beurteilen“ → `UNKNOWN` | „Keine Angabe“ oder leer → null/KEINE_ANGABE |
| U01 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| U02 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| U03 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| U04 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| U05 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| U06 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| K01 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| K02 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| K03 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| K04 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| K05 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| K06 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| L01 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| L02 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| L03 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| G01 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| G02 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| G03 | Einzelwahl, Pflicht: nein | „0“ … „10“ → Ganzzahl 0…10 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| A01 | Einzelwahl, Pflicht: nein | „1“ … „7“ → Ganzzahl 1…7 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| A02 | Einzelwahl, Pflicht: nein | „1“ … „7“ → Ganzzahl 1…7 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| A03 | Einzelwahl, Pflicht: nein | „1“ … „7“ → Ganzzahl 1…7 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| A04 | Einzelwahl, Pflicht: nein | „1“ … „7“ → Ganzzahl 1…7 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| I01 | Einzelwahl, Pflicht: nein | „1“ … „7“ → Ganzzahl 1…7 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| I02 | Einzelwahl, Pflicht: nein | „1“ … „7“ → Ganzzahl 1…7 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| I03 | Einzelwahl, Pflicht: nein | „1“ … „7“ → Ganzzahl 1…7 (Datentyp integer, nicht Text) | „NB“ → null/NICHT_BEURTEILBAR; „KA“ oder leer → null/KEINE_ANGABE |
| W01 | Kästchen, höchstens 3, Pflicht: nein | „Grundlagen generativer KI“ → `BASICS`; „Passende Einsatzmöglichkeiten für meine Aufgaben“ → `USE_CASES`; „Klare Eingaben formulieren und Ergebnisse verbessern“ → `PROMPTING`; „Antworten und Quellen überprüfen“ → `VERIFY`; „Betriebliche Regeln und zulässige Dateneingaben“ → `DATA_RULES`; „Bei neuen Entwicklungen auf dem Laufenden bleiben“ → `KEEP_CURRENT`; „Anderes Thema“ → `OTHER`; „Derzeit kein Weiterbildungswunsch“ → `NONE`; „Ich kann meinen Bedarf noch nicht einschätzen“ → `UNKNOWN`; Liste der Codes | „Keine Angabe“ allein oder leer → null/KEINE_ANGABE; Kombination mit exklusiver Option oder KA → siehe Regel X3 |
| W02 | Kästchen, höchstens 3, Pflicht: nein | „Kein Zugang zu einem freigegebenen Werkzeug“ → `ACCESS`; „Unklare betriebliche Regeln“ → `RULES`; „Zu wenig Zeit zum Ausprobieren oder Lernen“ → `TIME`; „Mir fehlt Wissen über die Nutzung“ → `KNOWLEDGE`; „Ich erkenne keinen passenden Einsatz für meine Aufgaben“ → `TASK_FIT`; „Unsicherheit über die Verlässlichkeit der Ergebnisse“ → `RELIABILITY`; „Etwas anderes“ → `OTHER`; „Derzeit nichts“ → `NONE`; „Kann ich noch nicht einschätzen“ → `UNKNOWN`; Liste der Codes | „Keine Angabe“ allein oder leer → null/KEINE_ANGABE; Kombination mit exklusiver Option oder KA → siehe Regel X3 |
| W03 | Absatztext plus Kästchen „Keine Angabe“, Pflicht: nein | Text wörtlich, unbearbeitet | KA angekreuzt und kein Text, oder leer → null/KEINE_ANGABE; Text und KA zugleich → Regel X4 |


Regel X3 (W01/W02, unklare Mehrfachwahl): Laut Codebuch werden Mehrfachmarkierungen, mehr als drei Antworten oder widersprüchliche exklusive Antworten vor der Eingabe geklärt. Bei einer freiwilligen Onlinebefragung ohne Rückkontakt ist keine Klärung möglich. Dann: `value: null`, `missing_reason: "KEINE_ANGABE"`, Eintrag im Korrekturprotokoll mit Antwort-ID, Item und Rohauswahl. Nie selbst eine Antwort auswählen. „Widersprüchlich“ ist: NONE, UNKNOWN oder Keine Angabe zusammen mit einer anderen Option, oder mehr als drei Optionen.

Regel X4 (W03, Text und „Keine Angabe“ zugleich): Das Codebuch regelt diesen Fall nicht. **Codebuchlücke.** Ich lege hier keine Regel stillschweigend fest. Vorschlag zur Festlegung vor der Erhebung: Rohtext unverändert speichern, Fall im Korrekturprotokoll führen, bei der qualitativen Zuordnung als „unklar“ kennzeichnen. Die Entscheidung muss vor Erhebungsbeginn dokumentiert werden (siehe P-06).

### 4.2 Pflichtfelder und Regeln

| Element | Sollzustand | Zu prüfen |
|---|---|---|
| Pflichtfelder | keine | jede der 34 Fragen und S2-X-Fragen einzeln: nicht verpflichtend |
| Sprungregeln | keine | Seitennavigation führt immer zur nächsten Seite |
| W01, W02 Höchstzahl | höchstens 3 | Wird eine Auswahl von 4 beim **vorgesehenen Fortsetzen** tatsächlich blockiert? Ein sichtbarer Hinweis allein reicht nicht |
| W01, W02 Exklusivität | NONE, UNKNOWN, Keine Angabe nur allein | Viele Plattformen können das nicht erzwingen. Dann gilt Regel X3 bei der Datenübertragung. Hinweis F85 bleibt sichtbar |
| Kerninstruktionen | wörtlich | Zeilen 7, 21–23, 49–51, 64, 66–68, 77, 85 einzeln vergleichen |
| Endanker | 0 / 10 bzw. 1 / 7 wörtlich, keine Zwischenanker | keine automatisch ergänzten Beschriftungen an 1–9 bzw. 2–6 |
| Reihenfolge | C01–C06, U01–U06, K01–K06, L01–L03, G01–G03, A01–A04, I01–I03, W01–W03 | keine Zufallsreihenfolge von Fragen oder Optionen |
| Datenerfassung | keine Namen, keine Personalnummern | E-Mail-Erfassung, Anmeldepflicht, Antwortbestätigung per E-Mail: aus, solange R1 nicht anders entschieden ist |

### 4.3 Besonderheit Tablet im Pausenraum

- Gemeinsames Gerät: Prüfen, ob nach dem Absenden eine neue, leere Sitzung beginnt und ob nicht abgesendete Eingaben einer Person für die nächste Person sichtbar bleiben (Zwischenspeicher, automatisches Speichern, Browser-Autovervollständigung). Ergebnis protokollieren. Bis dahin bleibt [SATZ_ZU_NICHT_ABGESENDETEN_ANTWORTEN] leer.
- Mehrfachteilnahme: Bei einem gemeinsamen Gerät ist eine Begrenzung „eine Antwort pro Gerät“ ungeeignet, weil sie andere ausschließt. Ohne Anmeldung ist Mehrfachteilnahme nicht technisch ausschließbar. Das ist eine Grenze des Verfahrens, keine Fehlerquelle, die man später rechnerisch bereinigen könnte.
- Beobachtbarkeit: In einem Pausenraum können andere den Bildschirm sehen. Das kann Antworten beeinflussen, besonders bei C04, C05 und G03. Vorschlag: Aufstellort mit Sichtschutz. Wirkung ist nicht prüfbar und bleibt eine Grenze.
- Darstellung: 13 Optionen pro 0–10-Item (0 bis 10, NB, KA) auf Tabletbreite prüfen. Werden die Optionen untereinander dargestellt, muss die Reihenfolge 0 … 10, NB, KA erhalten bleiben. Dass Hoch- und Querformat gleichwertig sind, ist nicht geprüft.
- Bearbeitungsdauer: Ein Absendezeitstempel ergibt keine Bearbeitungsdauer. Die Angabe „10 bis 15 Minuten“ ist geschätzt und nicht gemessen. In Pausen kann die Zeit knapp sein. Abbrüche sind möglich und werden wie fehlende Angaben geführt, soweit überhaupt etwas übermittelt wurde.
- Zugang für Schichtbeschäftigte ohne eigenen PC: Ob die Teilnahme in der Arbeitszeit möglich ist, ist offen (R3). Die Teilnahmeverteilung nach C01 ist im Bericht immer auszuweisen, weil der Zugangsweg selbst die Stichprobe verzerren kann.

### 4.4 Information zu Anonymität und Datenschutz

- Kein Anonymitätsversprechen, solange nicht geprüft ist: Anmeldung, E-Mail-Erfassung, IP- oder Gerätedaten, Zugriff auf Rohdaten, Freitexte mit identifizierenden Angaben, Gruppengrößen. Bis dahin enthält die Einleitung nur Aussagen, die der Fragebogen selbst sicherstellt (keine Abfrage von Name oder Personalnummer).
- Freitexte (W03) können trotz Hinweis identifizierende Details enthalten. Sie werden vor jeder Weitergabe bereinigt und nie wörtlich an Vorgesetzte gegeben.
- Personenwerte bleiben in der Arbeitsdatei. Berichte nur aggregiert, je Gruppe nur ab [MINDESTGRUPPE] Antworten.
- Rechtliche Anforderungen (zum Beispiel Information nach Datenschutzrecht, Beteiligung einer Arbeitnehmervertretung) habe ich nicht geprüft. Für einen realen Einsatz ist das vor Erhebungsbeginn zu klären. Für die fiktive Demonstration entfällt es.

### 4.5 Begleitmanifest (Vorlage, Stand dieser Sitzung)

```yaml
manifest_version: "0.1"
referenzbank: "instrument/Itembank_GARI_DE_0.1.json"
referenzbank_version: "GARI-DE-0.1"
referenzbank_sha256_praefix: "12582782e64397d3"
codebuch: "instrument/Codebuch.md (GARI-DE-0.1, Stand 2026-09-29, fortgeschrieben 2026-10-17)"
codebuch_sha256_praefix: "65c5bd31bcd93303"
questionnaire_version: "GARI-DE-0.1"          # Kern
umsetzungskennung: "GARI-DE-0.1/ONLINE-S2-E1"  # Vorschlag, noch nicht vergeben
kontextaenderungen: ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "F5 entfällt"]
zusatzmodul: "keines (S2-X01/S2-X02 nicht eingesetzt)"
erhebungsrunde: "Demonstration S2, keine Erhebung"
kontextart: "FIKTIVE_DEMONSTRATION"
data_kind_vorgesehen: "SYNTHETIC_DEMO"        # SURVEY nur bei realem Einsatz
plattform: "NICHT_DOKUMENTIERT"
datum_oberflaechenabgleich: null              # noch kein Formular vorhanden
tatsaechlich_gepruefte_stellen: "nur Textfassung gegen Bank (siehe Prüfbericht 7.1); keine Oberfläche"
offene_abweichungen: ["P-01", "P-02", "P-03", "P-04", "P-05", "P-06", "P-07", "P-08", "P-09"]
freigabestatus: "OFFEN"
erstellung:
  verwendeter_prompt: "Masterprompt 0.5 (2026-10-17), Betriebsart ANWENDEN"
  eingabedateien: ["briefing.json", "instrument/Itembank_GARI_DE_0.1.json", "instrument/Codebuch.md", "Quellen_APA.md"]
  system_modell: "Claude (Anthropic), angezeigt: Opus 5.5 (claude-opus-5-5)"
  systemparameter: "NICHT_VERFUEGBAR"
  manuelle_aenderungen: "keine (noch nicht übertragen)"
formularerzeugung:
  erzeugungsprompt: "NICHT_DOKUMENTIERT"
  erzeugendes_system: "NICHT_DOKUMENTIERT"
  manuelle_aenderungen_im_formular: "NICHT_DOKUMENTIERT"
```

---

## 5 Wissenschaftliches Itemregister GARI-DE-0.1 (Anwendung S2)

Alle Felder sind aus der Itembank übernommen. Ergänzt habe ich nur die Konstruktbeschreibung (aus Codebuch und Bank zusammengefasst), die Zeile „Prüfstatus Anwendung“ und den Hinweis zu nicht zulässigen Fehlwertgründen. Bei den MAILS-Items ist der Originalwortlaut laut Bank geprüft, aber nur über die Fundstelle referenziert und nicht abgedruckt. Ich gebe ihn deshalb nicht wieder. Bei A und I ist der englische Wortlaut aus der bereitgestellten Itemsammlung angegeben. Der Abgleich mit dem OSF-Anhang fehlt.

Kontrollierte Platzhalter im Kern: keine. Alle Items haben die Rolle FESTER_KERN.

##### C01

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | C01 / C |
| Konstrukt / Zweck | Kontext: Tätigkeit, berufliche und private Nutzung, Zugang, Regelkenntnis, wahrgenommene Aufgabenrelevanz. Zweck: Einordnung und organisatorische Voraussetzungen; kein Readiness-Wert. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Wie sieht Ihre hauptsächliche Tätigkeit aus? |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | Einzelwahl: OFFICE = Überwiegend Büro- oder Bildschirmarbeit; OTHER_WORK = Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst; MIXED = Etwa gleich große Anteile beider Bereiche; zusätzlich Keine Angabe |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | kategorial, keine Richtung |
| Fehlwerte zulässig | KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### C02

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | C02 / C |
| Konstrukt / Zweck | Kontext: Tätigkeit, berufliche und private Nutzung, Zugang, Regelkenntnis, wahrgenommene Aufgabenrelevanz. Zweck: Einordnung und organisatorische Voraussetzungen; kein Readiness-Wert. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt? |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | Einzelwahl: D0 = An keinem Tag; D1_3 = An 1 bis 3 Tagen; D4_9 = An 4 bis 9 Tagen; D10_15 = An 10 bis 15 Tagen; D16_PLUS = An 16 oder mehr Tagen; UNKNOWN = Kann ich nicht einschätzen; zusätzlich Keine Angabe |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | kategorial, keine Richtung |
| Fehlwerte zulässig | KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### C03

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | C03 / C |
| Konstrukt / Zweck | Kontext: Tätigkeit, berufliche und private Nutzung, Zugang, Regelkenntnis, wahrgenommene Aufgabenrelevanz. Zweck: Einordnung und organisatorische Voraussetzungen; kein Readiness-Wert. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt? |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | Einzelwahl: YES = Ja; NO = Nein; UNKNOWN = Ich bin mir nicht sicher; zusätzlich Keine Angabe |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | kategorial, keine Richtung |
| Fehlwerte zulässig | KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### C04

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | C04 / C |
| Konstrukt / Zweck | Kontext: Tätigkeit, berufliche und private Nutzung, Zugang, Regelkenntnis, wahrgenommene Aufgabenrelevanz. Zweck: Einordnung und organisatorische Voraussetzungen; kein Readiness-Wert. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen? |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | Einzelwahl: YES = Ja; NO = Nein; UNKNOWN = Ich weiß es nicht; zusätzlich Keine Angabe |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | kategorial, keine Richtung |
| Fehlwerte zulässig | KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### C05

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | C05 / C |
| Konstrukt / Zweck | Kontext: Tätigkeit, berufliche und private Nutzung, Zugang, Regelkenntnis, wahrgenommene Aufgabenrelevanz. Zweck: Einordnung und organisatorische Voraussetzungen; kein Readiness-Wert. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit? |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | Einzelwahl: KNOWN = Ja; PARTLY = Teilweise; NOT_KNOWN = Nein; EXISTENCE_UNKNOWN = Ich weiß nicht, ob es solche Regeln gibt; zusätzlich Keine Angabe |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | kategorial, keine Richtung |
| Fehlwerte zulässig | KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### C06

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | C06 / C |
| Konstrukt / Zweck | Kontext: Tätigkeit, berufliche und private Nutzung, Zugang, Regelkenntnis, wahrgenommene Aufgabenrelevanz. Zweck: Einordnung und organisatorische Voraussetzungen; kein Readiness-Wert. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre? |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | Einzelwahl: YES = Ja; NO = Nein; UNKNOWN = Kann ich noch nicht beurteilen; zusätzlich Keine Angabe |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | kategorial, keine Richtung |
| Fehlwerte zulässig | KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### U01

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | U01 / U |
| Konstrukt / Zweck | Selbst eingeschätzte Anwendung generativer KI bei der Arbeit (MAILS-Facette Anwendung, adaptiert). Zweck: Selbsteinschätzung, kein Leistungstest. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 1, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann eine generative KI bedienen. |
| Änderung und Begründung | KI-Bezug auf generative KI eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### U02

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | U02 / U |
| Konstrukt / Zweck | Selbst eingeschätzte Anwendung generativer KI bei der Arbeit (MAILS-Facette Anwendung, adaptiert). Zweck: Selbsteinschätzung, kein Leistungstest. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 2, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann mir berufliche Aufgaben durch generative KI erleichtern. |
| Änderung und Begründung | Erleichterung des Lebens auf berufliche Aufgaben eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### U03

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | U03 / U |
| Konstrukt / Zweck | Selbst eingeschätzte Anwendung generativer KI bei der Arbeit (MAILS-Facette Anwendung, adaptiert). Zweck: Selbsteinschätzung, kein Leistungstest. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 3, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann generative KI gezielt für meine Arbeitsziele einsetzen. |
| Änderung und Begründung | Zielbezug auf Arbeitsziele eingegrenzt; sinnvoll durch gezielt konkretisiert. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### U04

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | U04 / U |
| Konstrukt / Zweck | Selbst eingeschätzte Anwendung generativer KI bei der Arbeit (MAILS-Facette Anwendung, adaptiert). Zweck: Selbsteinschätzung, kein Leistungstest. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 4, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht. |
| Änderung und Begründung | Alltagsinteraktion auf Zusammenarbeit bei der Arbeit übertragen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### U05

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | U05 / U |
| Konstrukt / Zweck | Selbst eingeschätzte Anwendung generativer KI bei der Arbeit (MAILS-Facette Anwendung, adaptiert). Zweck: Selbsteinschätzung, kein Leistungstest. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 5, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen. |
| Änderung und Begründung | Gewinnbringende Zusammenarbeit über brauchbare Arbeitsergebnisse konkretisiert; Bedeutungsverschiebung im Pretest prüfen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### U06

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | U06 / U |
| Konstrukt / Zweck | Selbst eingeschätzte Anwendung generativer KI bei der Arbeit (MAILS-Facette Anwendung, adaptiert). Zweck: Selbsteinschätzung, kein Leistungstest. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 6, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann generativer KI verständlich mitteilen, was ich brauche. |
| Änderung und Begründung | Gewinnbringende Kommunikation über verständliches Mitteilen konkretisiert; Ergebnisaspekt verengt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### K01

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | K01 / K |
| Konstrukt / Zweck | Selbst eingeschätztes Verständnis generativer KI (MAILS-Facetten Wissen/Verstehen, adaptiert). Zweck: Selbsteinschätzung. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 7, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kenne die zentralen Konzepte generativer KI. |
| Änderung und Begründung | Allgemeine KI auf generative KI eingegrenzt; Konzepte bleibt bewusst zur Verständlichkeitsprüfung erhalten. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### K02

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | K02 / K |
| Konstrukt / Zweck | Selbst eingeschätztes Verständnis generativer KI (MAILS-Facetten Wissen/Verstehen, adaptiert). Zweck: Selbsteinschätzung. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 8, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann erklären, was generative KI bedeutet. |
| Änderung und Begründung | Kenntnis von Definitionen in selbst eingeschätzte Erklärfähigkeit übertragen; stärkere Anpassung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### K03

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | K03 / K |
| Konstrukt / Zweck | Selbst eingeschätztes Verständnis generativer KI (MAILS-Facetten Wissen/Verstehen, adaptiert). Zweck: Selbsteinschätzung. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 9, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann Chancen und Grenzen generativer KI einschätzen. |
| Änderung und Begründung | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### K04

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | K04 / K |
| Konstrukt / Zweck | Selbst eingeschätztes Verständnis generativer KI (MAILS-Facetten Wissen/Verstehen, adaptiert). Zweck: Selbsteinschätzung. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 10, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann Vor- und Nachteile generativer KI beurteilen. |
| Änderung und Begründung | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### K05

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | K05 / K |
| Konstrukt / Zweck | Selbst eingeschätztes Verständnis generativer KI (MAILS-Facetten Wissen/Verstehen, adaptiert). Zweck: Selbsteinschätzung. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 11, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen. |
| Änderung und Begründung | Gegenstand eingegrenzt; Verwendungszwecke sprachlich vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### K06

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | K06 / K |
| Konstrukt / Zweck | Selbst eingeschätztes Verständnis generativer KI (MAILS-Facetten Wissen/Verstehen, adaptiert). Zweck: Selbsteinschätzung. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 12, Seite 1; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann mir künftige Anwendungen generativer KI vorstellen. |
| Änderung und Begründung | Gegenstand eingegrenzt; Satz verkürzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### L01

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | L01 / L |
| Konstrukt / Zweck | Zutrauen in das eigene Lernen bei Veränderungen generativer KI (MAILS-Items 26–28, adaptiert). Zweck: Selbsteinschätzung der Lernfähigkeit. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 26, Seite 2; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben. |
| Änderung und Begründung | Gegenstand eingegrenzt; stets entfällt. Deutsche Itemnummer 26 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### L02

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | L02 / L |
| Konstrukt / Zweck | Zutrauen in das eigene Lernen bei Veränderungen generativer KI (MAILS-Items 26–28, adaptiert). Zweck: Selbsteinschätzung der Lernfähigkeit. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 27, Seite 2; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann mich über Neuerungen bei generativer KI informieren. |
| Änderung und Begründung | Gegenstand eingegrenzt; deutsche Itemnummer 27 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### L03

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | L03 / L |
| Konstrukt / Zweck | Zutrauen in das eigene Lernen bei Veränderungen generativer KI (MAILS-Items 26–28, adaptiert). Zweck: Selbsteinschätzung der Lernfähigkeit. |
| Status | ADAPTIERT |
| Quelle | MAILS_DE_2023 |
| Fundstelle | Deutscher Autorenfragebogen, Item 28, Seite 2; Zuordnung und Mittelwertregel Seite 3. |
| Originalwortlaut | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten. |
| Änderung und Begründung | Gegenstand eingegrenzt; sprachliche Verdichtung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. |
| Ursprüngliche Skala | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### G01

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | G01 / G |
| Konstrukt / Zweck | Selbst eingeschätztes Prüfen von Ergebnissen, Quellen und zulässigen Eingaben. Zweck: Einzelhinweise auf verantwortlichen Umgang; keine Skala. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss. |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### G02

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | G02 / G |
| Konstrukt / Zweck | Selbst eingeschätztes Prüfen von Ergebnissen, Quellen und zulässigen Eingaben. Zweck: Einzelhinweise auf verantwortlichen Umgang; keine Skala. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen. |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### G03

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | G03 / G |
| Konstrukt / Zweck | Selbst eingeschätztes Prüfen von Ergebnissen, Quellen und zulässigen Eingaben. Zweck: Einzelhinweise auf verantwortlichen Umgang; keine Skala. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf. |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### A01

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | A01 / A |
| Konstrukt / Zweck | Einstellung zur arbeitsbezogenen Nutzung freigegebener generativer KI (RAA, Itemvorlage PowerPilot). Zweck: bedingte Bewertung, keine Absicht. |
| Status | ADAPTIERT |
| Quelle | POWERPILOT_2025 |
| Fundstelle | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. |
| Originalwortlaut | The use of PowerPilot would be … advantageous. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft. |
| Änderung und Begründung | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. |
| Ursprüngliche Skala | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. |
| Verwendete Antwortskala | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### A02

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | A02 / A |
| Konstrukt / Zweck | Einstellung zur arbeitsbezogenen Nutzung freigegebener generativer KI (RAA, Itemvorlage PowerPilot). Zweck: bedingte Bewertung, keine Absicht. |
| Status | ADAPTIERT |
| Quelle | POWERPILOT_2025 |
| Fundstelle | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. |
| Originalwortlaut | The use of PowerPilot would be … satisfactory. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend. |
| Änderung und Begründung | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. |
| Ursprüngliche Skala | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. |
| Verwendete Antwortskala | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### A03

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | A03 / A |
| Konstrukt / Zweck | Einstellung zur arbeitsbezogenen Nutzung freigegebener generativer KI (RAA, Itemvorlage PowerPilot). Zweck: bedingte Bewertung, keine Absicht. |
| Status | ADAPTIERT |
| Quelle | POWERPILOT_2025 |
| Fundstelle | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. |
| Originalwortlaut | The use of PowerPilot would be … important. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig. |
| Änderung und Begründung | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. |
| Ursprüngliche Skala | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. |
| Verwendete Antwortskala | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### A04

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | A04 / A |
| Konstrukt / Zweck | Einstellung zur arbeitsbezogenen Nutzung freigegebener generativer KI (RAA, Itemvorlage PowerPilot). Zweck: bedingte Bewertung, keine Absicht. |
| Status | ADAPTIERT |
| Quelle | POWERPILOT_2025 |
| Fundstelle | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 4; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. |
| Originalwortlaut | The use of PowerPilot would be … enjoyable. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm. |
| Änderung und Begründung | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. |
| Ursprüngliche Skala | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. |
| Verwendete Antwortskala | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### I01

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | I01 / I |
| Konstrukt / Zweck | Nutzungsabsicht unter tatsächlich erwarteten Bedingungen in den nächsten drei Monaten (RAA, Itemvorlage PowerPilot). |
| Status | ADAPTIERT |
| Quelle | POWERPILOT_2025 |
| Fundstelle | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. |
| Originalwortlaut | I plan to use PowerPilot in the future. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. |
| Änderung und Begründung | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. |
| Ursprüngliche Skala | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. |
| Verwendete Antwortskala | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### I02

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | I02 / I |
| Konstrukt / Zweck | Nutzungsabsicht unter tatsächlich erwarteten Bedingungen in den nächsten drei Monaten (RAA, Itemvorlage PowerPilot). |
| Status | ADAPTIERT |
| Quelle | POWERPILOT_2025 |
| Fundstelle | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. |
| Originalwortlaut | I intend to use PowerPilot in the future. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. |
| Änderung und Begründung | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. |
| Ursprüngliche Skala | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. |
| Verwendete Antwortskala | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### I03

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | I03 / I |
| Konstrukt / Zweck | Nutzungsabsicht unter tatsächlich erwarteten Bedingungen in den nächsten drei Monaten (RAA, Itemvorlage PowerPilot). |
| Status | ADAPTIERT |
| Quelle | POWERPILOT_2025 |
| Fundstelle | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. |
| Originalwortlaut | I will definitely use PowerPilot in the future. |
| Wortlaut geprüft (laut Bank) | ja |
| Befragungsformulierung | Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen. |
| Änderung und Begründung | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. |
| Ursprüngliche Skala | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. |
| Verwendete Antwortskala | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | höher = höhere Selbsteinschätzung/Zustimmung; keine Umkodierung |
| Fehlwerte zulässig | NICHT_BEURTEILBAR, KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### W01

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | W01 / W |
| Konstrukt / Zweck | Geäußerte Weiterbildungswünsche, wahrgenommene Hindernisse und Freitext. Zweck: Lernwunsch und Organisationsbedarf getrennt erfassen. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen. |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | Mehrfachwahl, höchstens 3: BASICS = Grundlagen generativer KI; USE_CASES = Passende Einsatzmöglichkeiten für meine Aufgaben; PROMPTING = Klare Eingaben formulieren und Ergebnisse verbessern; VERIFY = Antworten und Quellen überprüfen; DATA_RULES = Betriebliche Regeln und zulässige Dateneingaben; KEEP_CURRENT = Bei neuen Entwicklungen auf dem Laufenden bleiben; OTHER = Anderes Thema; NONE = Derzeit kein Weiterbildungswunsch; UNKNOWN = Ich kann meinen Bedarf noch nicht einschätzen; exklusiv: NONE, UNKNOWN; zusätzlich Keine Angabe (exklusiv) |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | kategorial, keine Richtung |
| Fehlwerte zulässig | KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### W02

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | W02 / W |
| Konstrukt / Zweck | Geäußerte Weiterbildungswünsche, wahrgenommene Hindernisse und Freitext. Zweck: Lernwunsch und Organisationsbedarf getrennt erfassen. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen. |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | Mehrfachwahl, höchstens 3: ACCESS = Kein Zugang zu einem freigegebenen Werkzeug; RULES = Unklare betriebliche Regeln; TIME = Zu wenig Zeit zum Ausprobieren oder Lernen; KNOWLEDGE = Mir fehlt Wissen über die Nutzung; TASK_FIT = Ich erkenne keinen passenden Einsatz für meine Aufgaben; RELIABILITY = Unsicherheit über die Verlässlichkeit der Ergebnisse; OTHER = Etwas anderes; NONE = Derzeit nichts; UNKNOWN = Kann ich noch nicht einschätzen; exklusiv: NONE, UNKNOWN; zusätzlich Keine Angabe (exklusiv) |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | kategorial, keine Richtung |
| Fehlwerte zulässig | KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |

##### W03

| Feld | Eintrag |
|---|---|
| item_id / dimension_id | W03 / W |
| Konstrukt / Zweck | Geäußerte Weiterbildungswünsche, wahrgenommene Hindernisse und Freitext. Zweck: Lernwunsch und Organisationsbedarf getrennt erfassen. |
| Status | NEU_ENTWICKELT |
| Quelle | keine (Eigenentwicklung) |
| Fundstelle | entfällt |
| Originalwortlaut | Eigenentwicklung ohne Originalitem. |
| Wortlaut geprüft (laut Bank) | nein |
| Befragungsformulierung | Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen. |
| Änderung und Begründung | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. |
| Ursprüngliche Skala | entfällt (keine Vorlage) |
| Verwendete Antwortskala | Freitext; zusätzlich Keine Angabe |
| Rolle | FESTER_KERN |
| Anzeigebedingung | ALWAYS (alle Personen) |
| Auswertungsrichtung | kategorial, keine Richtung |
| Fehlwerte zulässig | KEINE_ANGABE; NICHT_ZUTREFFEND und UEBERSPRUNGEN nicht zulässig |
| Evidenz | Noch nicht empirisch geprüft. |
| Prüfstatus Anwendung | Wortlaut, Position und Optionen gegen frozen_participant_text abgeglichen: identisch. Onlineoberfläche: OFFEN. |
| Version | GARI-DE-0.1 |


---

## 6 Codebuch: Anwendungsteil für S2

Das Codebuch GARI-DE-0.1 gilt unverändert. Dieser Teil ergänzt nur, was die Onlineumsetzung braucht. Er ändert keine Rechenregel.

### 6.1 Datenformat

- JSON, UTF-8. Pflichtfelder auf Dateiebene: `data_kind` (genau PRETEST, SURVEY oder SYNTHETIC_DEMO), `questionnaire_version` = "GARI-DE-0.1".
- Für diesen fiktiven Fall: `data_kind` = SYNTHETIC_DEMO für jede Probe- oder Demonstrationsdatei. Technische Probeläufe der Oberfläche werden in einer eigenen Datei geführt und nie mit Antworten von Testpersonen vermischt.
- Je Person: technische Antwort-ID statt Testkürzel, jede ID nur einmal je Datei, `questionnaire_version` = "GARI-DE-0.1", alle 34 Item-IDs mit `value` und `missing_reason`.
- Zusätzlich empfohlen, außerhalb des Antwortobjekts: `implementation_id` (Umsetzungskennung), `context_supplement` (nur falls S2-X-Fragen eingesetzt werden), `submitted_at` (nur als Absendezeitpunkt, nie als Dauer).
- Die Umsetzungskennung ersetzt nicht die Fragebogenversion. Daten aus der Word-Fassung (Pretest R1), aus Persona-Läufen (R2) oder aus anderen Formularfassungen (R3) dürfen **nicht** durch Umbenennung ihrer Versionsangabe in diese Datei gelangen.

### 6.2 Wertebereiche und Labels

| IDs | `value` | Labels |
|---|---|---|
| C01 | OFFICE, OTHER_WORK, MIXED | siehe 4.1 |
| C02 | D0, D1_3, D4_9, D10_15, D16_PLUS, UNKNOWN | UNKNOWN ist reguläre Kategorie |
| C03 | YES, NO, UNKNOWN | UNKNOWN ist reguläre Kategorie |
| C04 | YES, NO, UNKNOWN | UNKNOWN ist reguläre Kategorie |
| C05 | KNOWN, PARTLY, NOT_KNOWN, EXISTENCE_UNKNOWN | EXISTENCE_UNKNOWN ist reguläre Kategorie |
| C06 | YES, NO, UNKNOWN | UNKNOWN ist reguläre Kategorie |
| U, K, L, G | Ganzzahl 0–10 | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt |
| A, I | Ganzzahl 1–7 | 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu |
| W01 | Liste aus BASICS, USE_CASES, PROMPTING, VERIFY, DATA_RULES, KEEP_CURRENT, OTHER, NONE, UNKNOWN; 1–3 Einträge; NONE und UNKNOWN nur allein | leere Liste unzulässig |
| W02 | Liste aus ACCESS, RULES, TIME, KNOWLEDGE, TASK_FIT, RELIABILITY, OTHER, NONE, UNKNOWN; 1–3 Einträge; NONE und UNKNOWN nur allein | leere Liste unzulässig |
| W03 | Text | unverändert speichern |

### 6.3 Fehlwerte

| Code | Bedeutung | Zulässig bei |
|---|---|---|
| NICHT_BEURTEILBAR | NB gewählt | U, K, L, G, A, I |
| KEINE_ANGABE | KA gewählt, Feld leer gelassen, Abbruch vor diesem Item oder nicht eindeutig zuordenbare Mehrfachwahl (X3) | alle 34 Items |
| NICHT_ZUTREFFEND | – | **nicht zulässig** in GARI-DE-0.1 |
| UEBERSPRUNGEN | – | **nicht zulässig** in GARI-DE-0.1 |

Hinweise:
- In einer Onlineplattform lassen sich „KA gewählt“ und „leer gelassen“ im Export oft unterscheiden. Das Codebuch kodiert beide als KEINE_ANGABE. Ich ändere das nicht. Der Rohexport bleibt erhalten, damit die Ursache nachvollziehbar bleibt.
- Bei Abbruch wird nur übertragen, was tatsächlich übermittelt wurde. Ob die Plattform abgebrochene, nicht abgesendete Antworten überhaupt speichert, ist zu prüfen. Wahrscheinlich gehen sie verloren. Dann existiert für diese Person kein Datensatz.
- Nichtnutzung (C02 = D0, C03 = NO) setzt keine Fähigkeitswerte auf 0 und erzeugt keinen Fehlwert.

### 6.4 Zugelassene Zusammenfassungen und Berichtsregeln

- Teilbereichsmittelwerte nur für U (6 Items), K (6), L (3), A (4), I (3), jeweils nur bei vollständig gültigen Antworten. Projektregel, nicht aus MAILS belegt. Keine Imputation.
- G01, G02, G03 nur als Einzelverteilungen. Kein G-, C- oder W-Wert. Kein Gesamtwert, keine Umrechnung auf 100, keine Gewichtung, keine Klassen wie „bereit / nicht bereit“.
- 0–10- und 1–7-Werte nicht in einer gemeinsamen Rangliste vergleichen.
- Gruppenmittelwerte nur mit Anzahl vollständiger und unvollständiger Fälle. Null gültige Fälle ergeben `null`.
- Mehrfachantworten: Nenner = Personen mit gültiger Antwort auf das Item. Prozentwerte können zusammen über 100 liegen. Fehlende getrennt ausweisen.
- C04 = NO bei I-Antworten 6 oder 7: nur Prüfhinweis, keine Änderung.
- Gruppenberichte (C01, gegebenenfalls S2-X01/S2-X02) nur ab [MINDESTGRUPPE] Antworten.
- Bericht immer mit Teilnahmezahl, Bezug auf 400 Beschäftigte und Teilnahmeverteilung nach C01. Keine Hochrechnung auf Nichtteilnehmende.
- Unterschiede zwischen Paper-Pretest und Onlinefassung werden nicht als Veränderung interpretiert. Die Gleichwertigkeit der Darstellungen ist nicht geprüft.

---

## 7 Prüfbericht

### 7.1 Kernabgleich (in dieser Sitzung mit Python 3 ausgeführt)

Ich habe ein eigenes Prüfskript auf die bereitgestellte Itembank angewendet. Geprüft wurde jedes Item gegen `frozen_participant_text`.

| Prüfung | Ergebnis |
|---|---|
| Anzahl Item-IDs | 34, alle eindeutig |
| Wortlaut Item (Feld `text`) = Zeile im eingefrorenen Text | 34 von 34 identisch |
| Reihenfolge Bank = Reihenfolge eingefrorener Text | identisch |
| Einzelwahloptionen C01–C06 inkl. „Keine Angabe“ | 6 von 6 identisch |
| Mehrfachwahloptionen W01, W02 inkl. „Keine Angabe“ | 2 von 2 identisch |
| Skalenzeilen 0–10 bzw. 1–7 mit NB und KA | 25 von 25 identisch |
| Definition (Feld `definition`) = Zeile 3 des eingefrorenen Texts | identisch |
| Übernahme in 3.2 | maschinell aus `frozen_participant_text` erzeugt; Kernzeilen ohne Textänderung, nur Markdown-Formatierung |
| Codebuch-Codes in der Maßnahmenlogik (BASICS, PROMPTING, VERIFY, DATA_RULES, RELIABILITY, ACCESS, TASK_FIT, TIME, NOT_KNOWN, EXISTENCE_UNKNOWN) | alle in der Bank vorhanden |

Status: ADAPTIERT 22 Items (U, K, L, A, I), NEU_ENTWICKELT 12 Items (C, G, W). Kein Item ist ORIGINAL oder nur UEBERSETZT.

Grenze: Geprüft ist die Textfassung dieses Dokuments gegen die Bank. **Eine Onlineoberfläche existiert noch nicht und ist nicht geprüft.** Der Word-Fragebogen lag nicht vor; ich habe ihn nicht mit der Bank verglichen.

### 7.2 Offene Probleme

| ID | Problem | Stelle | Vorschlag | Folge für Vergleichbarkeit | Nachprüfung |
|---|---|---|---|---|---|
| P-01 | Kein Oberflächenabgleich möglich, weil kein Formular existiert | gesamte Onlinefassung | nach Übertragung Abgleich nach 7.3; erst dann Freigabestatus setzen | – | OFFEN |
| P-02 | Ersetzung des Pretest-Rahmentexts stützt sich auf `frozen_text_note`, nicht auf `context_changes_allowed` | E1–E5, E7 | Projektverantwortliche bestätigt Einstufung als Erhebungsfassung; sonst Rahmentext wörtlich lassen (sachlich falsch: „Gespräch“, „Test“) oder neue Version | Rahmung kann Antworten beeinflussen, nicht geprüft | OFFEN |
| P-03 | Kerninstruktion „Kreisen Sie … ein“ passt nicht zum Onlineformular | Zeilen 21, 49, 68 | für GARI-DE-0.1 unverändert lassen; für eine künftige Version neutrale Formulierung („Wählen Sie …“) mit neuer Versionskennung und Pretest | Änderung wäre Instruktionsänderung, daher neue Version | OFFEN |
| P-04 | C01 deckt die vier Briefing-Bereiche nicht ab | C01 | Entscheidung R2; Zusatzmodul 3.4 nur außerhalb des Kerns | Kern unberührt | OFFEN |
| P-05 | Exklusivität und Höchstzahl bei W01/W02 möglicherweise technisch nicht erzwingbar | W01, W02 | Blockade beim Fortsetzen testen; sonst Regel X3 | mehr KEINE_ANGABE möglich | OFFEN |
| P-06 | Codebuchlücke: W03 mit Text und KA zugleich | W03 | Regel vor Erhebung festlegen (Vorschlag X4) | gering | OFFEN |
| P-07 | Anonymität und Datenzugriff ungeklärt; gemeinsames Tablet | Einleitung, 4.3, 4.4 | R1; Tablettest | Teilnahmebereitschaft und Antwortverhalten können betroffen sein | OFFEN |
| P-08 | Bearbeitungsdauer nur geschätzt (10–15 Min.), in Pausen evtl. knapp | Einleitung | Dauer in einer Probe messen, nicht aus Absendezeit ableiten | Abbrüche | OFFEN |
| P-09 | Referenzdateien nicht beigefügt: `auswertung/score.py`, `tests/test_scoring.py`, `pretest/GoogleForms_Runde2_Anleitung.md`, `pretest/Abschluss_Evaluation_R3.md`, Word-Fragebogen, Beispieldateien | Auswertung, Umsetzung, Pretestbefunde | Dateien bereitstellen; Pretestbefunde R1–R3 sind in diesem Dokument deshalb nicht berücksichtigt | – | OFFEN |
| P-10 | POWERPILOT_2025: Wortlautvergleich mit OSF-Anhang offen | A01–A04, I01–I03 | Grenze im Bericht nennen; Abgleich nachholen, falls zugänglich | – | OFFEN |
| P-11 | Lizenz- und Nutzungsrechte für veränderte MAILS- und PowerPilot-Items vor öffentlicher Veröffentlichung ungeklärt | U, K, L, A, I | vor Veröffentlichung klären; interne wissenschaftliche Nutzung laut Projektquelle gedeckt, Umfang nicht erweitert | – | OFFEN |
| P-12 | Gleichwertigkeit Papier/online sowie Tablet/PC nicht geprüft | ganze Fassung | keine Gleichwertigkeit behaupten; Daten getrennt halten | Vergleiche mit Pretestdaten unzulässig | OFFEN |

### 7.3 Prüfliste für den späteren Oberflächenabgleich

Jeden Punkt einzeln protokollieren: geprüfter Schritt, Datum, Gerät, Ergebnis.

1. Alle 34 IDs sichtbar, in Reihenfolge, Wortlaut zeichengenau gegen 3.2.
2. Definition und alle Kerninstruktionen zeichengenau.
3. Endanker wörtlich, keine Zwischenanker ergänzt.
4. NB und KA bei allen 25 numerischen Items auswählbar.
5. „Keine Angabe“ bei C01–C06, W01, W02, W03 auswählbar.
6. Keine Pflichtfelder.
7. W01/W02: Auswahl von 4 Optionen beim Fortsetzen blockiert? Exklusivität erzwungen? Ergebnis festhalten, nicht annehmen.
8. Seitenwechsel vor A01 vorhanden (Kernhinweis Zeile 64).
9. Exportprobe in eigener SYNTHETIC_DEMO-Testdatei: Datentyp der Zahlen, Darstellung von NB/KA, Mehrfachwahl als Liste, Unterscheidung „leer“ vs. „KA“. Eine nicht getestete Übermittlung bleibt ungeprüft; ein erfolgreicher Seitenwechsel belegt die Speicherung nicht.
10. Tablet: neue Sitzung nach Absenden, keine Reste aus fremden Sitzungen, Darstellung der 13 Optionen.
11. Einstellungen zu E-Mail-Erfassung, Anmeldung, Antwortbestätigung.

Freigabestatus: **OFFEN.** BESTANDEN erst nach dokumentiertem Abgleich. Bei Abweichung: ABWEICHUNG mit konkreter Korrektur und erneuter Prüfung.

### 7.4 Verfahrensprüfung dieser Ausgabe

| Prüfpunkt | Ergebnis |
|---|---|
| Quellenkorrektheit | nur Angaben aus `Quellen_APA.md` und Bank verwendet; keine eigene Einsicht in Originalquellen; keine Seitenzahlen ergänzt |
| Unveränderter Kern | maschinell geprüft, siehe 7.1 |
| Datenbehandlung | keine Daten erzeugt; keine Zahlen berechnet |
| Vollständigkeit | Fragebogen, Register (34 Items), Codebuch-Anwendungsteil, Prüfbericht, Auswertungsplan, Maßnahmenvorlage, Änderungsprotokoll vorhanden |
| Unabhängigkeit | Diese Prüfung ist eine Selbstprüfung desselben Modells. Sie ist kein unabhängiges Gutachten. |

---

## 8 Auswertung

**Status: NICHT_BERECHNET.** Es liegen keine Antwortdaten vor (`antwortdaten_vorhanden: false`). Das Rechenskript `auswertung/score.py` ist nicht beigefügt. Ich gebe deshalb keine Zahlen aus und verwende kein synthetisches Rechenergebnis.

Rechenanleitung für einen späteren Lauf mit passender Datei:

1. Datei prüfen: `data_kind`, `questionnaire_version` = GARI-DE-0.1 auf Datei- und Personenebene, 34 IDs je Person, keine doppelten Antwort-IDs, nur zulässige Werte und Fehlwertgründe. Bei Fehlern stoppen und Prüfbericht ausgeben, nicht reparieren.
2. Skript ausführen: `python auswertung/score.py <eingabe.json> <ergebnis.json>` (Python 3.10 oder neuer). Exitstatus prüfen. Nur die erzeugte Ausgabe verwenden.
3. Für jedes Item: gültige Anzahl, NB-Anzahl, KA-Anzahl, Verteilung aller Kategorien.
4. U, K, L, A, I: Personenwert = Mittel der Items nur bei vollständigen Antworten; Gruppenwert = Mittel der Personenwerte; jeweils Anzahl vollständiger und unvollständiger Fälle.
5. W01, W02: Häufigkeit je Option, Nenner = gültige Antworten auf das Item.
6. Prüfhinweise: C04 = NO bei I ≥ 6; Anzahl Fälle nach Regel X3.
7. W03: lesen, bereinigen, Themen zuordnen, Schlüssel dokumentieren; Zitat und Interpretation trennen.
8. Bei SYNTHETIC_DEMO jede Tabelle und Abbildung sichtbar als Demonstration kennzeichnen.

Keine Alpha-, Faktoren- oder Signifikanzanalysen ohne gesonderte Begründung und ausreichende Fallzahl.

---

## 9 Maßnahmenmatrix (Planungsvorlage ohne Befunde)

Es gibt keine Befunde. Die Tabelle ist eine **vorab festgelegte Interpretationslogik** für diesen Kontext, abgeleitet aus dem Codebuch. Sie enthält keine Empfehlungen an den Betrieb. Befund-IDs werden erst nach einer Auswertung vergeben. Priorisierung ist später eine begründete Planungsentscheidung, keine validierte Regel. Feste Readiness-Grenzwerte gibt es nicht. Berichtet werden Anzahlen je Antwortkategorie.

| Regel | Befundtyp | Items | Einordnung | Mögliche Maßnahme | Zielgruppe | Unsicherheit | Erfolgskontrolle (Vorschlag) |
|---|---|---|---|---|---|---|---|
| M-01 | C04 = NO oder W02 = ACCESS | C04, W02, C01 | organisatorisch | Zuerst prüfen, ob und wo freigegebene Werkzeuge sinnvoll und erlaubt sind; besonders für Personen ohne eigenen PC. **Kein Schulungsdefizit ableiten.** | nach C01 getrennt beschreiben | C04 = UNKNOWN kann Unwissen über vorhandenen Zugang bedeuten | Zugangsregelung dokumentiert; spätere Wiederholung von C04 |
| M-02 | C05 = NOT_KNOWN / EXISTENCE_UNKNOWN, W02 = RULES, W01 = DATA_RULES | C05, W01, W02, G03 | Orientierung, Zuständigkeit | Klären, ob Regeln existieren; wenn ja, verständlich bereitstellen; Zuständigkeit benennen | alle | Regelkenntnis ist Selbstauskunft | Regeln veröffentlicht; C05 bei Wiederholung |
| M-03 | W01 = BASICS, ggf. mit Fähigkeitsantworten | W01, U, K | Lernwunsch | Einführung anbieten; Vorkenntnisse und Aufgaben vorher klären | Personen mit diesem Wunsch | Wunsch ≠ Bedarf | Teilnahme, Rückmeldung, praktische Aufgabe |
| M-04 | W01 = PROMPTING | W01, U06 | Lernwunsch | Übung zu Eingaben und Überarbeitung; **setzt Zugang voraus** (M-01) | Personen mit Wunsch und Zugang | ohne Werkzeug nicht umsetzbar | praktische Übungsaufgabe |
| M-05 | W01 = VERIFY oder W02 = RELIABILITY | W01, W02, G01, G02 | Lernwunsch oder Unsicherheit | Prüfung von Ergebnissen und Quellen an Arbeitsbeispielen | Interessierte | Unsicherheit kann sachlich berechtigt sein | Übung mit Beispielaufgabe |
| M-06 | C06 = NO oder W02 = TASK_FIT | C06, W02, C01 | Aufgabenpassung unklar | Anwendungsfälle je Bereich prüfen; **Nutzung kann sachlich unnötig sein** | nach C01 | Ablehnung kann begründet sein | dokumentierte Anwendungsfallprüfung |
| M-07 | W02 = TIME | W02 | Rahmenbedingung | Lernzeit und Schichtorganisation prüfen | Schichtbeschäftigte besonders beachten | – | Lernzeitregel |
| M-08 | Anteil NB auf einem Fähigkeitsitem auffällig | U, K, L, G | unklare Einschätzbarkeit | erst Frageverständnis und Erfahrungsgrundlage prüfen; **nicht als niedrige Kompetenz zählen** | – | „auffällig“ wird mit tatsächlicher Anzahl und Bezugsgröße berichtet, nicht über einen Grenzwert | gezielte Nachfrage in späterem Pretest |
| M-09 | Bestimmte Fähigkeitsantworten plus passender Lernwunsch | U/K/L/G mit W01 | mehrere Hinweise | vertiefenden Lernbedarf als Hypothese formulieren, praktische Aufgabe zur Abklärung | – | Selbsteinschätzung ist kein Kompetenznachweis | praktische Aufgabe |
| M-10 | W01 = KEEP_CURRENT, hohe L-Werte | W01, L | Ansatzpunkt | vertiefende Angebote für Interessierte | – | Selbsteinschätzung | Teilnahme, Rückmeldung |
| M-11 | W03-Themen | W03 | Lernwunsch, qualitativ | Themen sammeln, mit W01 abgleichen | – | kurze Antworten nicht ausdeuten | dokumentierter Themenschlüssel |

Wirksamkeit eines Trainings ist nicht belegt. Für jede spätere Empfehlung gilt: Thema, Zielgruppe, Ziel, Maßnahme, Befund-ID, Item-IDs, Datenart, Fallzahl, Unsicherheit, Erfolgskontrolle.

---

## 10 Änderungsprotokoll und nächste Eingaben

### 10.1 Änderungsprotokoll dieser Anwendung

| Nr. | Art | Gegenstand | Version |
|---|---|---|---|
| 1 | keine Änderung | 34 Kernitems, Optionen, Skalen, Definition, Instruktionen, Reihenfolge | GARI-DE-0.1 |
| 2 | Kontextänderung | Rahmentext E1–E7, Wegfall Testkürzel/Datum | Umsetzungskennung (Vorschlag) GARI-DE-0.1/ONLINE-S2-E1 |
| 3 | Vorschlag, nicht eingesetzt | Zusatzmodul S2-X01, S2-X02 | keine |
| 4 | Codebuch-Anwendungsteil | Exportzuordnung, Regel X3 (aus Codebuch abgeleitet), Vorschlag X4 (offen) | keine Änderung der Rechenregeln |

### 10.2 Nächste konkret erforderliche Eingaben

1. Antworten auf R1 bis R3.
2. Bestätigung der Einstufung von E1–E7 als zulässige Erhebungsfassung (P-02).
3. Entscheidung zu Regel X4 (P-06).
4. Das tatsächlich erstellte Onlineformular, sein Erzeugungsprompt und eine Exportprobe aus einer getrennten Testsitzung, für den Oberflächenabgleich nach 7.3.
5. Die fehlenden Projektdateien aus P-09, wenn Auswertung, Umsetzungsanleitung oder Pretestbefunde berücksichtigt werden sollen.
6. Erst bei einem realen Einsatz: echte Unternehmensangaben und Antwortdaten mit `data_kind` = SURVEY.

---

## 11 Status

- **Erstellt:** Befragungsfassung mit unverändertem GARI-DE-0.1-Kern und dokumentiertem Online-Rahmentext; Quellenregister und Konstruktmatrix (aus Projektangaben); Itemregister für 34 Items; Codebuch-Anwendungsteil mit Exportzuordnung; Begleitmanifest-Vorlage; Prüfbericht; Rechenanleitung; Maßnahmen-Planungsvorlage; optionaler Entwurf eines Zusatzmoduls.
- **Geprüft:** Nur die Textübereinstimmung von Wortlaut, Reihenfolge, Optionen, Skalen und Definition mit der Bank, per eigenem Python-Skript. Keine Originalquelle, kein Word-Fragebogen, keine Onlineoberfläche, kein Export, kein Tablet.
- **Berechnet:** nichts. Status NICHT_BERECHNET.
- **Fehlt:** Plattform und Formular, Oberflächenabgleich, Anonymitätsentscheidung, Gruppengröße, Antworten auf R1–R3, `score.py` und Tests, Pretestunterlagen R1–R3, OSF-Abgleich für POWERPILOT_2025, Rechteklärung.
- **Freigabestatus:** OFFEN.
- Die Fassung ist eine Demonstration für einen fiktiven Betrieb. Sie ist nicht psychometrisch validiert, und der Einsatz belegt keine allgemeine Freigabe des Instruments.

---

## Literatur

Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. University of Massachusetts Amherst. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf

Bisbee, J., Clinton, J. D., Dorff, C., Kenkel, B., & Larson, J. M. (2024). Synthetic replacements for human survey data? The perils of large language models. *Political Analysis, 32*(4), 401–416. https://doi.org/10.1017/pan.2024.5

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Do Khac, L. T., Leyer, M., Wichmann, J., & Richter, A. (2025). Divisional perspectives on trust in generative AI: An empirical study of senior decision-makers. *Enterprise Information Systems*. Advance online publication. https://doi.org/10.1080/17517575.2025.2481557

Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), Article e39686. https://doi.org/10.1016/j.heliyon.2024.e39686

National Center for Health Statistics. (2024, April 16). *Cognitive interviewing*. Centers for Disease Control and Prevention. https://www.cdc.gov/nchs/ccqder/question-evaluation/cognitive-interviewing.html

Paetow, T., Wichmann, J., & Leyer, M. (2026). Task-technology fit in virtual reality: Explaining behavioral intention to use and perceived performance. In *Proceedings of the 59th Hawaii International Conference on System Sciences* (pp. 319–328). https://hdl.handle.net/10125/111430

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. *European Journal of Information Systems, 25*(1), 77–89. https://doi.org/10.1057/ejis.2014.36

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114

Wichmann, J., Gesk, T. S., & Leyer, M. (2024). Acceptance of AI in health care for short- and long-term treatments: Pilot development study of an integrated theoretical model. *JMIR Formative Research, 8*, e48600. https://doi.org/10.2196/48600

Wichmann, J., Gesk, T. S., & Leyer, M. (2026). The effect of social interaction in virtual meeting settings on work engagement: A socio-technical systems study. *Information Technology and Management, 27*, 173–185. https://doi.org/10.1007/s10799-025-00453-6

Bibliografische Nachweise wurden aus `Quellen_APA.md` übernommen und nicht erneut gegen die Originale geprüft. Ein DOI ersetzt keine Prüfung des behaupteten Inhalts.
