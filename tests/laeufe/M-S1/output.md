# GARI-DE-0.1 angewendet auf Szenario S1 (fiktive Demonstration)

**Betriebsart:** ANWENDEN (ausdrücklich angegeben)
**Kontextart:** FIKTIVE_DEMONSTRATION. Das Unternehmen ist erfunden. Es gibt keine realen Daten.
**Promptversion:** Masterprompt 0.5 vom 17. Oktober 2026
**Fragebogenversion (Kern):** GARI-DE-0.1 (Itembank vom 29. September 2026)
**Codebuch:** GARI-DE-0.1, Projektpaket 0.2, Stand 29. September 2026, redaktionell fortgeschrieben am 17. Oktober 2026
**Erhebungsfassung (Umsetzungskennung, neu):** `GARI-DE-0.1/S1-DEMO-ONLINE-E1`
**Datum der Bearbeitung:** 18. Oktober 2026
**System und Modell:** Claude (Anthropic), Modellangabe laut Systemumgebung „Opus 5.5“ (`claude-opus-5-5`). Temperatur, Seed und weitere Parameter: NICHT_VERFUEGBAR. Gleiche Prompts garantieren keine identischen Ausgaben.
**Datenart:** keine Antwortdaten (`antwortdaten_vorhanden: false`)
**Berechnungsstatus:** NICHT_BERECHNET

---

## 1 Kurzbeschreibung, Kontext und Annahmen

### 1.1 Ziel

Aus der geprüften Kernbank GARI-DE-0.1 entsteht eine unternehmensbezogene Befragungsfassung für einen fiktiven Dienstleistungsbetrieb. Der Kern bleibt unverändert. Angepasst wird nur der organisatorische Rahmen außerhalb des Fragebogens (Einleitung, Abschluss, Kontaktangaben). Dazu kommen Codebuch, Umsetzungsvorgaben für das Onlineformular, ein Begleitmanifest, ein Prüfbericht und die vorbereitete Logik für Maßnahmen.

### 1.2 Briefing-Abgleich (Angaben unverändert übernommen)

| Prüfpunkt | Angabe im Briefing | Bewertung für ANWENDEN |
|---|---|---|
| Zweck | Status quo beschreiben; Hinweise auf Weiterbildungsbedarf ableiten; betriebliche Voraussetzungen gesondert erfassen | Deckt sich mit dem Zweck des Kerns (C-, W-Items für Voraussetzungen; U/K/L/G/A/I für Profil) |
| Zielpopulation | Mitarbeitende aller Tätigkeitsbereiche einschließlich Personen ohne bisherige GenAI-Nutzung | Passt: alle Fragen werden allen gezeigt, NB ist auswählbar, Nichtnutzung erzeugt keinen Fähigkeitswert 0 |
| Betriebsgröße | 40 Beschäftigte | Relevant für Gruppenberichte und Datenschutz (siehe 3.4 und Rückfrage 3) |
| Tätigkeitsbereiche | Verwaltung, Kundenkontakt, Operative Tätigkeit | Der Kern erfasst Tätigkeit nur über C01 (Büro/Bildschirm, andere Arbeit, gemischt). Die drei Bereiche des Briefings werden **nicht** als neues Item ergänzt (siehe 4.3, Punkt P5) |
| Sprache | Deutsch | Passt |
| Technologiebezug | Generative KI | Passt; Definition bleibt unverändert |
| Zugang | Heterogene Erfahrung; ein freigegebenes Chat-Werkzeug für Büroarbeitsplätze | Wird **nicht** in Items oder Einleitung genannt, damit C04/C05 nicht vorweggenommen werden (siehe 4.3, Punkt P6) |
| Bisherige Nutzung | Unbekannt, mit dem Fragebogen zu erheben | C02, C03 erheben dies |
| Zugelassene Anwendungen | Nur „ein freigegebenes Chat-Werkzeug für Büroarbeitsplätze“; Details unbekannt | Bleibt unbekannt |
| Aufgabenbezug | Nicht näher angegeben | Bleibt unbekannt; C06, W02 (TASK_FIT) und W03 erheben ihn |
| Betrachtungszeitraum | Nicht angegeben | Im Kern festgelegt: C02 vergangene vier Wochen; A/I kommende drei Monate |
| Gewünschte Ausgabe | ANWENDEN | Befragungsfassung mit unverändertem Kern |
| Erhebungsweg | Onlineformular, Zugang über Link, freiwillig | Plattform nicht benannt; Anonymität damit nicht gesichert (siehe 3.4) |
| Art der Daten | Keine Antwortdaten | Keine Auswertung möglich; nur Vorbereitung |
| Kernbank-/Codebuchversion | GARI-DE-0.1 / GARI-DE-0.1 | Passt zur bereitgestellten Bank und zum Codebuch |

### 1.3 Getroffene Annahmen (eigene Entscheidungen, gekennzeichnet)

- A1: Die Onlinefassung ist eine **Erhebungsfassung** im Sinn von `frozen_text_note`. Die Pretest-Einleitung (Hinweis auf das anschließende Gespräch, Testkürzel, begleiteter Test) passt nicht zu einer freiwilligen Onlinebefragung und wird ersetzt. Das ist durch `context_changes_allowed` gedeckt („Kontaktangaben und organisatorischer Erhebungshinweis außerhalb des Fragebogens“). Die Definition generativer KI und alle Kerninstruktionen bleiben wörtlich.
- A2: Die Fragebogenversion der Daten bleibt `GARI-DE-0.1`, solange der Abgleich (Abschnitt 4) keine Kernabweichung zeigt. Die Umsetzung erhält zusätzlich die eigene Kennung `GARI-DE-0.1/S1-DEMO-ONLINE-E1`. Zeigt der Abgleich eine Kernabweichung, gilt diese Kennung nicht mehr als GARI-DE-0.1 und die Daten dürfen nicht unter GARI-DE-0.1 gerechnet werden.
- A3: Weil es sich um eine Demonstration handelt, werden keine Unternehmensmerkmale ergänzt. Platzhalter in eckigen Klammern (`[VOR VERSAND ERGÄNZEN: …]`) markieren Angaben, die für einen echten Einsatz fehlen.
- A4: Die Rückfragen in Abschnitt 8 konnten nicht gestellt werden. Alles, was ohne Antwort möglich ist, ist erledigt. Wo eine Antwort den nächsten Schritt ändert, ist eine vorläufige Lösung beschrieben und als offen markiert.

### 1.4 Stand des Projekts, der bei jeder Anwendung mitzuteilen ist

- Die Quelle POWERPILOT_2025 (A01–A04, I01–I03) ist anhand der bereitgestellten Itemsammlung (Datensatz_v1.docx) geprüft. Der direkte Vergleich mit dem OSF-Online-Anhang (https://doi.org/10.17605/OSF.IO/GEBK9) ist **offen**; der Anhang war am 29. September 2026 und beim erneuten Abruf am 17. Oktober 2026 nicht zugänglich (Quellen_APA.md).
- Es gibt **keine** vollständige Primärquellenprüfung aller Items durch diese Sitzung und **keine** psychometrische Validierung der Kombination. Die fünf Teilbereichswerte sind vorläufige deskriptive Projektwerte.
- Formativer Pretest laut Masterprompt: drei reale Pretestfälle der Fassung R1, zwei synthetische Claude-Personas der Fassung R2 (SYNTHETIC_DEMO, Herkunft LLM_PERSONA), letzte Formularfassung R3. Der Abschluss der Erhebung ist **keine** allgemeine Freigabe oder Validierung. Die Dokumente zu Pretest und R3 (`pretest/Abschluss_Evaluation_R3.md`, `pretest/GoogleForms_Runde2_Anleitung.md`) lagen dieser Sitzung **nicht** vor; ihr Inhalt wurde daher nicht übernommen und nicht geprüft.
- Die Bearbeitungszeit von 10–15 Minuten ist eine Schätzung, nicht gemessen.

---

## 2 Quellen- und Konstruktregister mit Evidenzgrenzen

### 2.1 Zugriffsgrenze dieser Sitzung

In dieser Sitzung lagen nur vier Dateien vor: `briefing.json`, `instrument/Itembank_GARI_DE_0.1.json`, `instrument/Codebuch.md`, `Quellen_APA.md`. **Keine Originalquelle (PDF, Fragebogen, Artikel) wurde in dieser Sitzung eingesehen.** Alle Angaben zum Prüfstand der Quellen stammen aus der Projektdokumentation (Quellen_APA.md, `source_register` der Bank) und werden als dokumentierter Projektstand wiedergegeben, nicht als eigene Prüfung.

### 2.2 Quellenregister

| Quellen-ID | Nachweis (APA) | Dokumentierter Prüfstand laut Projekt | Zugänglichkeit laut Projekt | Fundstelle | Zielgruppe / Sprache | Konstrukt / Instrument | Grenzen |
|---|---|---|---|---|---|---|---|
| MAILS_DE_2023 | Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014 | Publizierter Autoren-Volltext und deutscher Originalfragebogen geprüft (3 Seiten, 34 Items, Auswertungszuordnung) | Vollständig | Deutsche Fragebogen-PDF, Items 1–6, 7–12, 26–28 (S. 1–2); Zuordnung und Mittelwertregel S. 3 | 300 deutschsprachige Erwachsene; Deutsch | KI-Kompetenz (Anwendung, Verständnis), Lern-Selbstwirksamkeit; MAILS | Evidenz betrifft allgemeine KI und Selbstberichte; Übertragung auf GenAI im Arbeitskontext ist Anpassung; deutsche und englische Fassung unterscheiden sich in der Reihenfolge der Lernitems (Register folgt deutscher PDF); Rechte für öffentliche veränderte Itemtexte ungeklärt |
| MAILS_SHORT_2024 | Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), Article e39686. https://doi.org/10.1016/j.heliyon.2024.e39686 | Volltext eingesehen, v. a. Abschnitte 2.1 und 3.4 | Vollständig | Abschnitte 2.1, 3.4 | laut Projekt nicht näher dokumentiert | Weitere Validitätsevidenz; Zehn-Item-Kurzfassung | Kurzfassung enthält KI-Entwicklung und wird **nicht** eingesetzt; Kurzfassung benötigt laut Artikel weitere Validierung |
| POWERPILOT_2025 | Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114 | Paper und bereitgestellte Itemsammlung (Datensatz_v1.docx, Questionnaire 2 / PowerPilot) | Paper vollständig; Itemwortlaut nur über bereitgestellte Itemsammlung; OSF-Anhang nicht zugänglich | Datensatz_v1.docx, 1 – Intention to use, Items 1–3; 2 – Attitude, Items 1–4 | laut Titel Deutschland; Kontext Energie-Monitoring-App | Einstellung, Nutzungsabsicht (RAA-Bezug) | Direkter Wortlautvergleich mit OSF-Anhang offen; Kontextwechsel von Energieanwendung zu GenAI im Beruf ist inhaltliche Anpassung; Nutzungsbedingungen der Originalitems vor Veröffentlichung prüfen |
| AJZEN_TPB | Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. University of Massachusetts Amherst. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf | Siebenseitiges Originaldokument eingesehen | Vollständig | ohne Seitenangabe im Projekt | Methodenanleitung | Verhaltensdefinition über Ziel, Handlung, Kontext, Zeit | Begründet die Zeit- und Kontextspezifikation von A/I; liefert keine Items für GenAI |
| PEFFERS_2007 | Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302 | Abschnitte zu den sechs Aktivitäten, Demonstration, Evaluation, Kommunikation im Volltext | Vollständig (ohne Detailprüfung aller Fallstudien) | Abschnitte zu den Aktivitäten | Methodenliteratur | DSR-Prozess | Entwicklungsmethode, kein Messinstrument |
| VENABLE_2016 | Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. *European Journal of Information Systems, 25*(1), 77–89. https://doi.org/10.1057/ejis.2014.36 | Verlagsvolltext | Vollständig | nicht spezifiziert | Methodenliteratur | Evaluationsstrategie | Testumfang ist eigene Entscheidung |
| BOATENG_2018 | Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149 | Volltext | Vollständig | nicht spezifiziert | Methodenliteratur | Skalenentwicklung | Kleine Pretests ersetzen keine Validierungsstudie |

Weitere im Projekt geführte Quellen (Wichmann et al., 2024; Paetow et al., 2026; Do Khac et al., 2025; Wichmann et al., 2026; NCHS, 2024; Bisbee et al., 2024; Google-Hilfe zu Formularregeln) liefern in GARI-DE-0.1 **kein** Item. Sie sind für ANWENDEN nur als Hintergrund relevant. Die Google-Hilfe ist nur dann einschlägig, wenn die Plattform tatsächlich Google Forms ist (unbekannt).

### 2.3 Konstruktmatrix (Kern GARI-DE-0.1, unverändert)

| Teil | Konstrukt (Definition laut Bank/Codebuch) | Diagnosezweck | Theoretische/instrumentelle Grundlage | Art der Aussage | Zusammenfassung | Überschneidung / Abgrenzung |
|---|---|---|---|---|---|---|
| C01–C06 | Tätigkeit, berufliche und private Nutzung, Zugang, Regelkenntnis, Aufgabenpassung | Rahmenbedingungen; trennt Nichtnutzung aus fehlendem Zugang oder fehlender Aufgabenpassung von Kompetenzfragen | Eigenentwicklung (NEU_ENTWICKELT) | Berichtetes Verhalten bzw. wahrgenommene betriebliche Bedingungen | Einzelitems | Wahrgenommene Bedingungen, nicht persönliche Voraussetzung |
| U01–U06 | Selbst eingeschätzte Anwendung | Profil Anwendung | MAILS, deutsche Items 1–6 (ADAPTIERT) | Selbsteinschätzung | Vorläufiger Mittelwert U (vollständige Fälle) | Nahe an G und I; U misst Können, nicht Absicht |
| K01–K06 | Selbst eingeschätztes Verständnis | Profil Verständnis | MAILS, Items 7–12 (ADAPTIERT) | Selbsteinschätzung | Vorläufiger Mittelwert K | K03/K04 berühren Bewertung; K05/K06 berühren Anwendungsideen |
| L01–L03 | Zutrauen in das eigene Lernen | Lernvoraussetzung | MAILS, Items 26–28 (ADAPTIERT) | Selbsteinschätzung (Selbstwirksamkeit) | Vorläufiger Mittelwert L | Abgrenzung zu W01 (Lernwunsch) |
| G01–G03 | Prüfen von Ergebnissen und zulässigen Eingaben | Verantwortlicher Umgang | Eigenentwicklung (NEU_ENTWICKELT) | Selbsteinschätzung | Drei Einzelitems, **kein** G-Mittelwert | G03 berührt C05 (Regelkenntnis) |
| A01–A04 | Einstellung zur arbeitsbezogenen Nutzung freigegebener GenAI in drei Monaten | Bewertung der Nutzung | POWERPILOT_2025, Attitude 1–4 (ADAPTIERT); RAA | Bedingte Bewertung, keine Absicht | Vorläufiger Mittelwert A | Nicht mit I vermischen |
| I01–I03 | Absicht unter tatsächlich erwarteten Bedingungen | Nutzungsabsicht | POWERPILOT_2025, Intention 1–3 (ADAPTIERT); Ajzen (Ziel, Handlung, Kontext, Zeit) | Berichtete Absicht | Vorläufiger Mittelwert I | Hängt von Zugang ab (C04); Prüfhinweis bei C04 = NO und I = 6/7 |
| W01–W03 | Lernwünsche, Hindernisse, gewünschte Aufgabe | Weiterbildungs- und Maßnahmenplanung | Eigenentwicklung | Geäußerter Wunsch, wahrgenommene Hindernisse | Häufigkeiten; qualitative Zuordnung W03 | W02 ACCESS/RULES überschneidet C04/C05 bewusst |

Es gibt keinen Gesamtwert, keine Gewichtung, keine Reifegradklasse und keinen Wert über G, C oder W. Objektive Leistung wird nicht gemessen.

---

## 3 Befragungsfassung, Itemregister und Codebuch

### 3.1 Befragungsfassung `GARI-DE-0.1/S1-DEMO-ONLINE-E1` (für Befragte)

> **DEMONSTRATION.** Diese Fassung gehört zu einem fiktiven Betrieb. Sie ist nicht versandt worden und nicht in einem Formular umgesetzt.

Aufbau: Teil E (Einleitung, ersetzt) · Kern GARI-DE-0.1 (Abschnitte „Ihre Tätigkeit und bisherige Nutzung“ bis W03, wörtlich aus `frozen_participant_text`, Zeilen 6–112) · Teil Z (Abschluss, ersetzt). Ersetzte Teile sind unten markiert; die Gegenüberstellung steht in 4.2.

#### Teil E: Einleitung (organisatorischer Erhebungshinweis, ersetzt)

**Fragebogen zum Umgang mit generativer KI**

Onlinebefragung · Fragebogen GARI-DE-0.1

Dieser Fragebogen erfasst Ihre Erfahrungen, Einschätzungen und Weiterbildungswünsche zu generativer KI bei der Arbeit. Die Antworten werden nur zusammengefasst für den Betrieb oder für größere Gruppen ausgewertet. Sie sollen zeigen, welche Weiterbildung und welche betrieblichen Voraussetzungen sinnvoll sind. Es geht nicht um die Bewertung Ihrer Arbeitsleistung. Geschätzte Dauer: 10 bis 15 Minuten.

Generative KI erzeugt oder bearbeitet auf Eingaben hin Inhalte, zum Beispiel Texte, Bilder, Audio, Videos oder Programmcode. Gemeint sind sowohl eigenständige Anwendungen als auch entsprechende Funktionen in anderen Programmen.

Die Teilnahme ist freiwillig. Sie können einzelne Fragen auslassen oder die Befragung beenden. Bitte tragen Sie keine Namen, Personalnummern oder vertraulichen Informationen ein. Der Fragebogen fragt nicht nach Ihrem Namen. [VOR VERSAND ERGÄNZEN: geprüfte Angabe, ob die Plattform eine Anmeldung, E-Mail-Adresse oder andere technische Daten speichert, und wer Einzelantworten sehen kann. Erst danach entscheiden, ob und wie von Anonymität gesprochen werden darf.]

Bei Fragen zur Befragung: [VOR VERSAND ERGÄNZEN: Ansprechperson und Kontaktweg]

#### Kern GARI-DE-0.1 (unverändert)

Darstellungshinweis: Fettdruck der IDs und die Zeichen □ bzw. die Zahlenzeilen sind Satzmittel dieses Dokuments. In der Onlineumsetzung entstehen daraus Antwortfelder nach 3.4. Wortlaut, IDs und Reihenfolge sind verbindlich.

#### Ihre Tätigkeit und bisherige Nutzung

Bitte wählen Sie pro Frage genau eine Antwort.

**C01**  Wie sieht Ihre hauptsächliche Tätigkeit aus?

□ Überwiegend Büro- oder Bildschirmarbeit    □ Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst    □ Etwa gleich große Anteile beider Bereiche    □ Keine Angabe

**C02**  An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt?

□ An keinem Tag    □ An 1 bis 3 Tagen    □ An 4 bis 9 Tagen    □ An 10 bis 15 Tagen    □ An 16 oder mehr Tagen    □ Kann ich nicht einschätzen    □ Keine Angabe

**C03**  Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt?

□ Ja    □ Nein    □ Ich bin mir nicht sicher    □ Keine Angabe

**C04**  Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen?

□ Ja    □ Nein    □ Ich weiß es nicht    □ Keine Angabe

**C05**  Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit?

□ Ja    □ Teilweise    □ Nein    □ Ich weiß nicht, ob es solche Regeln gibt    □ Keine Angabe

**C06**  Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre?

□ Ja    □ Nein    □ Kann ich noch nicht beurteilen    □ Keine Angabe

#### Anwendung und Verständnis

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**U01**  Ich kann eine generative KI bedienen.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**U02**  Ich kann mir berufliche Aufgaben durch generative KI erleichtern.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**U03**  Ich kann generative KI gezielt für meine Arbeitsziele einsetzen.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**U04**  Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**U05**  Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**U06**  Ich kann generativer KI verständlich mitteilen, was ich brauche.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**K01**  Ich kenne die zentralen Konzepte generativer KI.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**K02**  Ich kann erklären, was generative KI bedeutet.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**K03**  Ich kann Chancen und Grenzen generativer KI einschätzen.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**K04**  Ich kann Vor- und Nachteile generativer KI beurteilen.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**K05**  Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**K06**  Ich kann mir künftige Anwendungen generativer KI vorstellen.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

#### Lernen und Prüfen

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**L01**  Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**L02**  Ich kann mich über Neuerungen bei generativer KI informieren.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**L03**  Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**G01**  Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**G02**  Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

**G03**  Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf.

`0    1    2    3    4    5    6    7    8    9    10       NB       KA`

Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.

#### Einstellung und geplante Nutzung

Wie sehr stimmen Sie den folgenden Aussagen zu? Gemeint ist die Nutzung für Ihre beruflichen Aufgaben in den kommenden drei Monaten. „Freigegeben“ bedeutet, dass Ihr Unternehmen die betreffende Nutzung erlaubt.

1 = stimme überhaupt nicht zu   ·   7 = stimme vollständig zu

NB = nicht beurteilbar   ·   KA = keine Angabe. Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein.

**A01**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft.

`1    2    3    4    5    6    7       NB       KA`

**A02**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend.

`1    2    3    4    5    6    7       NB       KA`

**A03**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig.

`1    2    3    4    5    6    7       NB       KA`

**A04**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm.

`1    2    3    4    5    6    7       NB       KA`

Für die folgenden drei Aussagen: Denken Sie an die Bedingungen, die Sie in den nächsten drei Monaten tatsächlich erwarten. Setzen Sie keinen gesicherten Zugang voraus, wenn dieser unklar ist. Fehlender Zugang bedeutet jedoch nicht automatisch, dass Sie nicht antworten können.

**I01**  Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

`1    2    3    4    5    6    7       NB       KA`

**I02**  Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

`1    2    3    4    5    6    7       NB       KA`

**I03**  Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen.

`1    2    3    4    5    6    7       NB       KA`

#### Weiterbildung und Unterstützung

Bei W01 und W02 sind jeweils höchstens drei Antworten möglich. „Kein Weiterbildungswunsch“, „derzeit nichts“, „kann ich noch nicht einschätzen“ und „keine Angabe“ dürfen innerhalb einer Frage nur allein gewählt werden.

**W01**  Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen.

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

**W02**  Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen.

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

**W03**  Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen.

□ Keine Angabe

`________________________________________________________________________`

`________________________________________________________________________`

`________________________________________________________________________`

#### Teil Z: Abschluss (ersetzt)

Vielen Dank für Ihre Teilnahme. Mit „Absenden“ übermitteln Sie Ihre Antworten.

### 3.2 Einführungstext für die Einladung (Begleittext, nicht Teil des Fragebogens)

> **DEMONSTRATION.** Platzhalter vor echtem Einsatz füllen.

Betreff: Kurze Befragung zu generativer KI bei der Arbeit

Wir möchten wissen, wie Sie generative KI bei der Arbeit erleben: ob Sie sie nutzen, ob Sie Zugang haben, was Sie sich zutrauen und welche Weiterbildung Sie sich wünschen. Das gilt auch, wenn Sie generative KI bisher nicht nutzen. Ihre Antworten helfen uns, Weiterbildung und betriebliche Voraussetzungen wie Zugang und Regeln sinnvoll zu planen.

Die Teilnahme ist freiwillig und dauert etwa 10 bis 15 Minuten. Sie können einzelne Fragen auslassen oder die Befragung beenden. Es geht nicht um die Bewertung Ihrer Arbeitsleistung. Ausgewertet wird nur zusammengefasst für den ganzen Betrieb oder für Gruppen mit mindestens [VOR VERSAND ERGÄNZEN: Mindestgröße, siehe 3.4.6] Antworten.

[VOR VERSAND ERGÄNZEN: geprüfte Angabe zur Datenspeicherung und zum Zugriff auf Einzelantworten]

Link: [VOR VERSAND ERGÄNZEN] · Teilnahme bis: [VOR VERSAND ERGÄNZEN] · Fragen an: [VOR VERSAND ERGÄNZEN]

Vorgesehene Ausgaben: ein Bericht auf Betriebsebene mit Antwortverteilungen je Frage, Fehlwerten nach Grund, den fünf vorläufigen Teilbereichswerten U, K, L, A, I (nur für vollständige Antworten), Häufigkeiten der Weiterbildungswünsche und Hindernisse sowie einer Themenübersicht aus den Freitexten ohne identifizierende Details. Es gibt keine Einstufung einzelner Personen und keinen Gesamtwert.

Die Einladung nennt bewusst kein konkretes Werkzeug und keine Regeln, damit die Fragen C04 und C05 nicht vorweggenommen werden.

### 3.3 Wissenschaftliches Itemregister GARI-DE-0.1 (alle 34 Items)

Quelle: `instrument/Itembank_GARI_DE_0.1.json`, maschinell übernommen. Die Spalte „Originalwortlaut“ gibt nur wieder, was die Bank selbst enthält. Bei MAILS-Items enthält die Bank keinen Originalwortlaut, sondern nur die Fundstelle; dieser Wortlaut wurde in dieser Sitzung nicht eingesehen. Die Konstruktdefinitionen je Teilbereich stehen in 2.3.

| item_id | dimension_id | Deutsche Befragungsformulierung | Status | Quelle und Fundstelle | Originalwortlaut | Art und Begründung der Änderung | Ursprüngliche Skala | Verwendete Antwortskala | Rolle | Anzeige | Auswertungsrichtung | Fehlwerte (zulässig) | Evidenzstatus | Prüfstatus Wortlaut | Version |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | C | Wie sieht Ihre hauptsächliche Tätigkeit aus? | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | Einzelwahl: OFFICE = Überwiegend Büro- oder Bildschirmarbeit; OTHER_WORK = Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst; MIXED = Etwa gleich große Anteile beider Bereiche; zusätzlich Keine Angabe | FESTER_KERN | ALWAYS | Nominale Kategorien; keine Rangrichtung, keine Umkodierung | KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| C02 | C | An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt? | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | Einzelwahl: D0 = An keinem Tag; D1_3 = An 1 bis 3 Tagen; D4_9 = An 4 bis 9 Tagen; D10_15 = An 10 bis 15 Tagen; D16_PLUS = An 16 oder mehr Tagen; UNKNOWN = Kann ich nicht einschätzen; zusätzlich Keine Angabe | FESTER_KERN | ALWAYS | Nominale Kategorien; keine Rangrichtung, keine Umkodierung | KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| C03 | C | Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt? | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | Einzelwahl: YES = Ja; NO = Nein; UNKNOWN = Ich bin mir nicht sicher; zusätzlich Keine Angabe | FESTER_KERN | ALWAYS | Nominale Kategorien; keine Rangrichtung, keine Umkodierung | KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| C04 | C | Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen? | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | Einzelwahl: YES = Ja; NO = Nein; UNKNOWN = Ich weiß es nicht; zusätzlich Keine Angabe | FESTER_KERN | ALWAYS | Nominale Kategorien; keine Rangrichtung, keine Umkodierung | KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| C05 | C | Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit? | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | Einzelwahl: KNOWN = Ja; PARTLY = Teilweise; NOT_KNOWN = Nein; EXISTENCE_UNKNOWN = Ich weiß nicht, ob es solche Regeln gibt; zusätzlich Keine Angabe | FESTER_KERN | ALWAYS | Nominale Kategorien; keine Rangrichtung, keine Umkodierung | KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| C06 | C | Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre? | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | Einzelwahl: YES = Ja; NO = Nein; UNKNOWN = Kann ich noch nicht beurteilen; zusätzlich Keine Angabe | FESTER_KERN | ALWAYS | Nominale Kategorien; keine Rangrichtung, keine Umkodierung | KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| U01 | U | Ich kann eine generative KI bedienen. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 1, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | KI-Bezug auf generative KI eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| U02 | U | Ich kann mir berufliche Aufgaben durch generative KI erleichtern. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 2, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Erleichterung des Lebens auf berufliche Aufgaben eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| U03 | U | Ich kann generative KI gezielt für meine Arbeitsziele einsetzen. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 3, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Zielbezug auf Arbeitsziele eingegrenzt; sinnvoll durch gezielt konkretisiert. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| U04 | U | Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 4, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Alltagsinteraktion auf Zusammenarbeit bei der Arbeit übertragen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| U05 | U | Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 5, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Gewinnbringende Zusammenarbeit über brauchbare Arbeitsergebnisse konkretisiert; Bedeutungsverschiebung im Pretest prüfen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| U06 | U | Ich kann generativer KI verständlich mitteilen, was ich brauche. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 6, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Gewinnbringende Kommunikation über verständliches Mitteilen konkretisiert; Ergebnisaspekt verengt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| K01 | K | Ich kenne die zentralen Konzepte generativer KI. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 7, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Allgemeine KI auf generative KI eingegrenzt; Konzepte bleibt bewusst zur Verständlichkeitsprüfung erhalten. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| K02 | K | Ich kann erklären, was generative KI bedeutet. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 8, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Kenntnis von Definitionen in selbst eingeschätzte Erklärfähigkeit übertragen; stärkere Anpassung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| K03 | K | Ich kann Chancen und Grenzen generativer KI einschätzen. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 9, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| K04 | K | Ich kann Vor- und Nachteile generativer KI beurteilen. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 10, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| K05 | K | Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 11, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Gegenstand eingegrenzt; Verwendungszwecke sprachlich vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| K06 | K | Ich kann mir künftige Anwendungen generativer KI vorstellen. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 12, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Gegenstand eingegrenzt; Satz verkürzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| L01 | L | Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 26, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Gegenstand eingegrenzt; stets entfällt. Deutsche Itemnummer 26 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| L02 | L | Ich kann mich über Neuerungen bei generativer KI informieren. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 27, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Gegenstand eingegrenzt; deutsche Itemnummer 27 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| L03 | L | Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten. | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 28, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Laut Bank am Dokument geprüft, in der Bank nicht wiedergegeben; nur über Fundstelle referenziert. In dieser Sitzung nicht eingesehen. | Gegenstand eingegrenzt; sprachliche Verdichtung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| G01 | G | Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss. | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| G02 | G | Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen. | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| G03 | G | Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf. | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| A01 | A | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft. | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | „The use of PowerPilot would be … advantageous.“ (laut bereitgestellter Itemsammlung) | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| A02 | A | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend. | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | „The use of PowerPilot would be … satisfactory.“ (laut bereitgestellter Itemsammlung) | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| A03 | A | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig. | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | „The use of PowerPilot would be … important.“ (laut bereitgestellter Itemsammlung) | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| A04 | A | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm. | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 4; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | „The use of PowerPilot would be … enjoyable.“ (laut bereitgestellter Itemsammlung) | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| I01 | I | Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | „I plan to use PowerPilot in the future.“ (laut bereitgestellter Itemsammlung) | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| I02 | I | Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | „I intend to use PowerPilot in the future.“ (laut bereitgestellter Itemsammlung) | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| I03 | I | Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen. | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | „I will definitely use PowerPilot in the future.“ (laut bereitgestellter Itemsammlung) | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker; zusätzlich NB, KA | FESTER_KERN | ALWAYS | Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | Wortlaut gegen Quelle geprüft (laut Bank) | GARI-DE-0.1 |
| W01 | W | Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen. | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | Mehrfachwahl, höchstens 3: BASICS = Grundlagen generativer KI; USE_CASES = Passende Einsatzmöglichkeiten für meine Aufgaben; PROMPTING = Klare Eingaben formulieren und Ergebnisse verbessern; VERIFY = Antworten und Quellen überprüfen; DATA_RULES = Betriebliche Regeln und zulässige Dateneingaben; KEEP_CURRENT = Bei neuen Entwicklungen auf dem Laufenden bleiben; OTHER = Anderes Thema; NONE = Derzeit kein Weiterbildungswunsch; UNKNOWN = Ich kann meinen Bedarf noch nicht einschätzen; exklusiv: NONE, UNKNOWN; zusätzlich Keine Angabe (exklusiv) | FESTER_KERN | ALWAYS | Nominale Kategorien; keine Rangrichtung, keine Umkodierung | KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| W02 | W | Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen. | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | Mehrfachwahl, höchstens 3: ACCESS = Kein Zugang zu einem freigegebenen Werkzeug; RULES = Unklare betriebliche Regeln; TIME = Zu wenig Zeit zum Ausprobieren oder Lernen; KNOWLEDGE = Mir fehlt Wissen über die Nutzung; TASK_FIT = Ich erkenne keinen passenden Einsatz für meine Aufgaben; RELIABILITY = Unsicherheit über die Verlässlichkeit der Ergebnisse; OTHER = Etwas anderes; NONE = Derzeit nichts; UNKNOWN = Kann ich noch nicht einschätzen; exklusiv: NONE, UNKNOWN; zusätzlich Keine Angabe (exklusiv) | FESTER_KERN | ALWAYS | Nominale Kategorien; keine Rangrichtung, keine Umkodierung | KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |
| W03 | W | Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen. | NEU_ENTWICKELT | keine (Eigenentwicklung) | entfällt (kein Originalitem) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | entfällt | Freitext; zusätzlich Keine Angabe | FESTER_KERN | ALWAYS | Nominale Kategorien; keine Rangrichtung, keine Umkodierung | KEINE_ANGABE | Noch nicht empirisch geprüft. | Kein Quellenwortlaut (Eigenentwicklung); inhaltliche Prüfung offen | GARI-DE-0.1 |

Platzhalter im Kern: **keine**. Die Bank weist keine kontrollierten Platzhalter aus. Deshalb wird weder der Werkzeugname noch ein Unternehmensbeispiel in Items eingesetzt.

### 3.4 Codebuch für die Erhebungsfassung `GARI-DE-0.1/S1-DEMO-ONLINE-E1`

Grundlage ist das Codebuch GARI-DE-0.1. Die folgenden Regeln übernehmen es unverändert. Ergänzt sind nur Vorgaben, die die Onlineumsetzung betreffen (3.4.5) und die Berichtsregeln für diesen Betrieb (3.4.6). Diese Ergänzungen sind eigene Planungsentscheidungen.

#### 3.4.1 Datenformat

- JSON, UTF-8.
- Pflichtfeld `data_kind`: genau `PRETEST`, `SURVEY` oder `SYNTHETIC_DEMO`. Für diesen Demonstrationsfall gibt es keine Daten. Würden technische Probeläufe oder ausgedachte Antworten erzeugt, sind sie `SYNTHETIC_DEMO` und getrennt von jeder echten Erhebung zu speichern. `SURVEY` ist nur für eine echte Befragung eines echten Betriebs zulässig.
- `questionnaire_version` = `GARI-DE-0.1` auf Datei- und Personenebene, nur solange der Oberflächenabgleich (Abschnitt 4) keine Kernabweichung zeigt. Zusätzlich im Manifest: Umsetzungskennung `GARI-DE-0.1/S1-DEMO-ONLINE-E1`.
- Ein Personenkürzel darf je Datei nur einmal vorkommen. Für die Onlinebefragung wird es bei der Übertragung fortlaufend vergeben (zum Beispiel `R001`, `R002`), ohne Bezug zu Namen, E-Mail oder Personalnummer. Doppelte Einsendungen derselben Person sind bei offenem Link technisch nicht sicher erkennbar; dies wird im Bericht als Grenze genannt.
- Alle 34 Item-IDs sind je Person vorhanden, auch bei fehlender Antwort.
- Jede Antwort ist ein Objekt aus `value` und `missing_reason`.
- Die äußere Dateistruktur (Feldnamen für Personenliste und Kürzel) richtet sich nach `beispiele/synthetische_antworten.json` und `auswertung/score.py`. Beide Dateien lagen dieser Sitzung nicht vor. Die Struktur ist deshalb vor der ersten Übertragung dort abzulesen; hier wird keine erfunden.

Leere Vorlage für das Antwortobjekt einer Person (alle 34 IDs, Ausgangswert „keine Angabe“; bei der Übertragung durch die tatsächliche Antwort ersetzen):

```json
{
  "C01": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "C02": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "C03": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "C04": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "C05": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "C06": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "U01": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "U02": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "U03": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "U04": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "U05": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "U06": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "K01": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "K02": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "K03": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "K04": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "K05": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "K06": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "L01": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "L02": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "L03": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "G01": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "G02": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "G03": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "A01": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "A02": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "A03": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "A04": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "I01": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "I02": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "I03": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "W01": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "W02": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  },
  "W03": {
    "value": null,
    "missing_reason": "KEINE_ANGABE"
  }
}
```

#### 3.4.2 Wertebereiche, Antwortlabels und Exportcodes

| Itemgruppe | Typ | Zulässige `value` | Zulässige `missing_reason` |
|---|---|---|---|
| C01–C06 | Einzelwahl | Codes laut Tabelle unten | `KEINE_ANGABE` |
| U01–U06, K01–K06, L01–L03, G01–G03 | Ganzzahl | 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` |
| A01–A04, I01–I03 | Ganzzahl | 1–7 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` |
| W01, W02 | Mehrfachwahl, höchstens 3 | Liste von Codes; `NONE` und `UNKNOWN` nur allein | `KEINE_ANGABE` |
| W03 | Freitext | Zeichenkette | `KEINE_ANGABE` |

Bei einer gültigen Antwort ist `missing_reason` = `null`. Bei einem Fehlwert ist `value` = `null`. 0 ist bei den 0–10-Items ein gültiger Wert und **nie** ein Fehlwertcode.

Zuordnung jeder angezeigten Antwort zum Exportcode:

| item_id | Angezeigte Antwort | Exportcode `value` | `missing_reason` |
|---|---|---|---|
| C01 | Überwiegend Büro- oder Bildschirmarbeit | `"OFFICE"` | `null` |
| C01 | Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst | `"OTHER_WORK"` | `null` |
| C01 | Etwa gleich große Anteile beider Bereiche | `"MIXED"` | `null` |
| C01 | Keine Angabe | `null` | `"KEINE_ANGABE"` |
| C02 | An keinem Tag | `"D0"` | `null` |
| C02 | An 1 bis 3 Tagen | `"D1_3"` | `null` |
| C02 | An 4 bis 9 Tagen | `"D4_9"` | `null` |
| C02 | An 10 bis 15 Tagen | `"D10_15"` | `null` |
| C02 | An 16 oder mehr Tagen | `"D16_PLUS"` | `null` |
| C02 | Kann ich nicht einschätzen | `"UNKNOWN"` | `null` |
| C02 | Keine Angabe | `null` | `"KEINE_ANGABE"` |
| C03 | Ja | `"YES"` | `null` |
| C03 | Nein | `"NO"` | `null` |
| C03 | Ich bin mir nicht sicher | `"UNKNOWN"` | `null` |
| C03 | Keine Angabe | `null` | `"KEINE_ANGABE"` |
| C04 | Ja | `"YES"` | `null` |
| C04 | Nein | `"NO"` | `null` |
| C04 | Ich weiß es nicht | `"UNKNOWN"` | `null` |
| C04 | Keine Angabe | `null` | `"KEINE_ANGABE"` |
| C05 | Ja | `"KNOWN"` | `null` |
| C05 | Teilweise | `"PARTLY"` | `null` |
| C05 | Nein | `"NOT_KNOWN"` | `null` |
| C05 | Ich weiß nicht, ob es solche Regeln gibt | `"EXISTENCE_UNKNOWN"` | `null` |
| C05 | Keine Angabe | `null` | `"KEINE_ANGABE"` |
| C06 | Ja | `"YES"` | `null` |
| C06 | Nein | `"NO"` | `null` |
| C06 | Kann ich noch nicht beurteilen | `"UNKNOWN"` | `null` |
| C06 | Keine Angabe | `null` | `"KEINE_ANGABE"` |
| U01 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| U01 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| U01 | KA | `null` | `"KEINE_ANGABE"` |
| U02 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| U02 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| U02 | KA | `null` | `"KEINE_ANGABE"` |
| U03 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| U03 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| U03 | KA | `null` | `"KEINE_ANGABE"` |
| U04 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| U04 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| U04 | KA | `null` | `"KEINE_ANGABE"` |
| U05 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| U05 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| U05 | KA | `null` | `"KEINE_ANGABE"` |
| U06 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| U06 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| U06 | KA | `null` | `"KEINE_ANGABE"` |
| K01 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| K01 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| K01 | KA | `null` | `"KEINE_ANGABE"` |
| K02 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| K02 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| K02 | KA | `null` | `"KEINE_ANGABE"` |
| K03 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| K03 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| K03 | KA | `null` | `"KEINE_ANGABE"` |
| K04 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| K04 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| K04 | KA | `null` | `"KEINE_ANGABE"` |
| K05 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| K05 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| K05 | KA | `null` | `"KEINE_ANGABE"` |
| K06 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| K06 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| K06 | KA | `null` | `"KEINE_ANGABE"` |
| L01 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| L01 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| L01 | KA | `null` | `"KEINE_ANGABE"` |
| L02 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| L02 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| L02 | KA | `null` | `"KEINE_ANGABE"` |
| L03 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| L03 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| L03 | KA | `null` | `"KEINE_ANGABE"` |
| G01 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| G01 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| G01 | KA | `null` | `"KEINE_ANGABE"` |
| G02 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| G02 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| G02 | KA | `null` | `"KEINE_ANGABE"` |
| G03 | Zahl 0 bis 10 | ganze Zahl 0–10 | `null` |
| G03 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| G03 | KA | `null` | `"KEINE_ANGABE"` |
| A01 | Zahl 1 bis 7 | ganze Zahl 1–7 | `null` |
| A01 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| A01 | KA | `null` | `"KEINE_ANGABE"` |
| A02 | Zahl 1 bis 7 | ganze Zahl 1–7 | `null` |
| A02 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| A02 | KA | `null` | `"KEINE_ANGABE"` |
| A03 | Zahl 1 bis 7 | ganze Zahl 1–7 | `null` |
| A03 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| A03 | KA | `null` | `"KEINE_ANGABE"` |
| A04 | Zahl 1 bis 7 | ganze Zahl 1–7 | `null` |
| A04 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| A04 | KA | `null` | `"KEINE_ANGABE"` |
| I01 | Zahl 1 bis 7 | ganze Zahl 1–7 | `null` |
| I01 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| I01 | KA | `null` | `"KEINE_ANGABE"` |
| I02 | Zahl 1 bis 7 | ganze Zahl 1–7 | `null` |
| I02 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| I02 | KA | `null` | `"KEINE_ANGABE"` |
| I03 | Zahl 1 bis 7 | ganze Zahl 1–7 | `null` |
| I03 | NB | `null` | `"NICHT_BEURTEILBAR"` |
| I03 | KA | `null` | `"KEINE_ANGABE"` |
| W01 | Grundlagen generativer KI | `"BASICS"` (in Liste) | `null` |
| W01 | Passende Einsatzmöglichkeiten für meine Aufgaben | `"USE_CASES"` (in Liste) | `null` |
| W01 | Klare Eingaben formulieren und Ergebnisse verbessern | `"PROMPTING"` (in Liste) | `null` |
| W01 | Antworten und Quellen überprüfen | `"VERIFY"` (in Liste) | `null` |
| W01 | Betriebliche Regeln und zulässige Dateneingaben | `"DATA_RULES"` (in Liste) | `null` |
| W01 | Bei neuen Entwicklungen auf dem Laufenden bleiben | `"KEEP_CURRENT"` (in Liste) | `null` |
| W01 | Anderes Thema | `"OTHER"` (in Liste) | `null` |
| W01 | Derzeit kein Weiterbildungswunsch | `"NONE"` (in Liste) | `null` |
| W01 | Ich kann meinen Bedarf noch nicht einschätzen | `"UNKNOWN"` (in Liste) | `null` |
| W01 | Keine Angabe | `null` | `"KEINE_ANGABE"` |
| W02 | Kein Zugang zu einem freigegebenen Werkzeug | `"ACCESS"` (in Liste) | `null` |
| W02 | Unklare betriebliche Regeln | `"RULES"` (in Liste) | `null` |
| W02 | Zu wenig Zeit zum Ausprobieren oder Lernen | `"TIME"` (in Liste) | `null` |
| W02 | Mir fehlt Wissen über die Nutzung | `"KNOWLEDGE"` (in Liste) | `null` |
| W02 | Ich erkenne keinen passenden Einsatz für meine Aufgaben | `"TASK_FIT"` (in Liste) | `null` |
| W02 | Unsicherheit über die Verlässlichkeit der Ergebnisse | `"RELIABILITY"` (in Liste) | `null` |
| W02 | Etwas anderes | `"OTHER"` (in Liste) | `null` |
| W02 | Derzeit nichts | `"NONE"` (in Liste) | `null` |
| W02 | Kann ich noch nicht einschätzen | `"UNKNOWN"` (in Liste) | `null` |
| W02 | Keine Angabe | `null` | `"KEINE_ANGABE"` |
| W03 | Freitext (nicht leer) | Text als Zeichenkette | `null` |
| W03 | Keine Angabe oder leeres Feld | `null` | `"KEINE_ANGABE"` |

#### 3.4.3 Fehlwerte und Eingabekontrolle

- NB bei numerischen Fragen: `value: null`, `missing_reason: "NICHT_BEURTEILBAR"`.
- KA oder leeres Feld: `value: null`, `missing_reason: "KEINE_ANGABE"`. Nicht erkennbare Motive werden nicht ergänzt.
- Die Unsicherheitsoptionen bei C01–C06 („Kann ich nicht einschätzen“, „Ich bin mir nicht sicher“, „Ich weiß es nicht“, „Ich weiß nicht, ob es solche Regeln gibt“, „Kann ich noch nicht beurteilen“) sind reguläre Kategorien und werden mitgezählt und ausgewiesen.
- W01/W02: `NONE` und `UNKNOWN` sind reguläre, exklusive Kategorien. KA ist Fehlwert. Eine leere Liste ist unzulässig und bedeutet nicht „keine Wünsche“.
- `NICHT_ZUTREFFEND` und `UEBERSPRUNGEN` sind in GARI-DE-0.1 **nicht erlaubt**, weil alle Fragen allen gezeigt werden. Sie bleiben künftigen, entsprechend konstruierten Fassungen vorbehalten.
- Mehrfachmarkierung bei Einzelwahl, mehr als drei Antworten bei W01/W02 oder widersprüchliche exklusive Antworten: vor Eingabe klären. Ist keine eindeutige Zuordnung möglich, das Item als `KEINE_ANGABE` kodieren und den Grund im separaten Korrekturprotokoll vermerken. Nie selbst eine der Antworten auswählen.
- Abgebrochene Formulare werden nur so weit übertragen, wie Angaben vorliegen; der Rest bleibt fehlend. Ob die Plattform abgebrochene, nicht abgesendete Formulare überhaupt speichert, ist unbekannt und im Manifest festzuhalten.
- Die Rechenroutine stoppt bei unzulässigen Werten, unbekannten oder fehlenden IDs, doppelten Personen und abweichenden Versionen. Kein stilles Reparieren.

#### 3.4.4 Filter, Skalenbildung und Rechenregeln

- Filter: keine. Alle 34 Fragen werden allen Personen gezeigt. Keine Sprungregeln. Nichtnutzung in C02 oder C03 erzeugt keinen Fehlwert und setzt keine Fähigkeitseinschätzung auf 0.
- Antwortrichtung: höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung. Keine umgepolten Items, daher keine Umkodierung.
- Erlaubte Zusammenfassungen: genau die fünf vorläufigen Teilbereichswerte.
  - U = (U01 + U02 + U03 + U04 + U05 + U06) / 6, nur wenn alle sechs gültig sind.
  - K = (K01 + K02 + K03 + K04 + K05 + K06) / 6, nur wenn alle sechs gültig sind.
  - L = (L01 + L02 + L03) / 3, nur wenn alle drei gültig sind.
  - A = (A01 + A02 + A03 + A04) / 4, nur wenn alle vier gültig sind.
  - I = (I01 + I02 + I03) / 3, nur wenn alle drei gültig sind.
- Die Vollständigkeitsregel ist eine konservative eigene Projektregel, keine aus MAILS belegte Fehlwertvorschrift. Keine Imputation.
- G01–G03 bleiben Einzelitems. Kein Wert für G, C oder W. Kein Gesamtwert, keine Umrechnung auf 100, keine Gewichtung, keine Klassen „bereit“ / „nicht bereit“. 0–10- und 1–7-Werte werden nicht in einer Rangliste verglichen.
- Gruppenwert: Mittelwert der gültigen Personenwerte, immer mit Anzahl vollständiger und unvollständiger Fälle. Null gültige Fälle ergeben `null`, nicht 0.
- Einzelverteilungen sind die primäre Darstellung. Die numerische Behandlung der gleichabständigen Antwortzahlen für die Mittelwerte ist eine transparent gemachte Annahme.
- Mehrfachantworten: Nenner = Personen mit gültiger Antwort auf das Item; jede Option höchstens einmal je Person; Prozentsummen können über 100 liegen; fehlende Antworten zusätzlich ausweisen.
- Prüfhinweis: C04 = `NO` und eine I-Antwort von 6 oder 7 erzeugt nur einen Hinweis (die Person kann künftigen Zugang erwarten). Keine Antwort wird verändert.
- Unterschiedliche Versionen werden getrennt berechnet.

#### 3.4.5 Vorgaben für die Onlineumsetzung (eigene Planungsvorgaben, noch nicht umgesetzt)

Die Plattform ist im Briefing nicht benannt. Die Vorgaben sind deshalb plattformneutral. Sie sind ein Vorschlag und **kein** geprüftes Liveformular.

| Element | Soll | Begründung |
|---|---|---|
| Reihenfolge | Teil E · C01–C06 · U01–K06 · L01–G03 · Seitenwechsel · A01–I03 · W01–W03 · Teil Z | Reihenfolge der Bank; der Satz „Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.“ muss durch einen tatsächlichen Seitenwechsel wahr bleiben |
| Abschnittsüberschriften und Instruktionen | Wörtlich wie in 3.1, je am Abschnittsanfang | Kerninstruktion |
| IDs | Sichtbar vor jedem Fragetext, wie in der Bank (z. B. „C01  …“) | Zuordnung im Abgleich und Export |
| C01–C06 | Einzelwahl (Optionsfelder), alle Optionen einschließlich „Keine Angabe“ als auswählbare Option | „Keine Angabe“ ist im Kern eine eigene Option |
| U, K, L, G | Je Item eine Einzelwahl mit 13 Optionen in dieser Reihenfolge: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, NB, KA; Endanker sichtbar (0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt); keine Zwischenanker | NB/KA müssen auswählbar sein; ein Schieberegler oder eine reine Zahlenskala ohne NB/KA ist unzulässig |
| A, I | Je Item eine Einzelwahl mit 9 Optionen: 1, 2, 3, 4, 5, 6, 7, NB, KA; Endanker 1 = stimme überhaupt nicht zu, 7 = stimme vollständig zu | wie oben |
| W01, W02 | Kästchen (Mehrfachwahl) mit allen 9 Optionen plus „Keine Angabe“; technische Höchstgrenze 3 | Höchstzahl ist Kernregel |
| Exklusivität NONE, UNKNOWN, KA | Wenn die Plattform sie nicht technisch durchsetzt: sichtbarer Kerninstruktionssatz bleibt; Verstöße werden nach 3.4.3 kodiert und protokolliert | Hinweistext ist keine funktionierende Regel; Grenze dokumentieren |
| W03 | Mehrzeiliges Textfeld plus auswählbare Option „Keine Angabe“ | Kern enthält „□ Keine Angabe“ bei W03 |
| Pflichtfelder | **Keine.** Alle Fragen optional | „Sie können einzelne Fragen auslassen“ steht in der Einleitung; Pflichtfelder wären eine Versionsänderung |
| Keine Zusatzfelder | Keine Namens-, E-Mail-, Abteilungs- oder Altersfelder; E-Mail-Erfassung und Anmeldung ausschalten, soweit die Plattform das erlaubt | Datensparsamkeit; nur benötigte Merkmale |
| Export | Pro Item eine Spalte; Zahlen als Text oder Zahl je Plattform, Abbildung auf `value`/`missing_reason` nach 3.4.2; NB/KA nie als Zahl | Exportdatentyp muss im Abgleich geprüft werden |
| Zeitstempel | Absendezeitpunkt nicht als Bearbeitungsdauer verwenden | Absendezeit ergibt keine Dauer |

Offener Konflikt: Die Kerninstruktionen „Kreisen Sie pro Aussage eine Zahl ein“ (zweimal) und „Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein“ beziehen sich auf Papier. Sie bleiben in dieser Fassung wörtlich, weil Instruktionen zum unveränderten Kern gehören. Eine Anpassung an „wählen Sie aus“ wäre eine Instruktionsänderung und braucht eine neue Fragebogenversion (zum Beispiel GARI-DE-0.2-ONLINE) mit eigenem Codebuch; Daten dieser Version dürften dann nicht unter GARI-DE-0.1 gerechnet werden. Entscheidung offen (Rückfrage 2).

#### 3.4.6 Berichtsregeln für diesen Betrieb (eigene Planungsentscheidungen)

- Bericht nur auf Betriebsebene und für Gruppen nach C01. Die drei Tätigkeitsbereiche des Briefings werden nicht erhoben und daher nicht berichtet.
- Mindestgröße für Gruppenberichte: offen (Rückfrage 3). Vorläufige Planungsregel: Eine Gruppe wird nur berichtet, wenn sie mindestens 5 gültige Antworten hat; sonst wird sie mit der nächsten Ebene zusammengefasst. Die Zahl 5 ist eine Datenschutz-Planungsannahme für einen Betrieb mit 40 Beschäftigten, **keine** methodisch belegte Grenze und keine Aussage über Messqualität.
- W03-Freitexte werden vor jeder Weitergabe von identifizierenden Details bereinigt; berichtet werden Themen mit Anzahl, keine Einzelzitate ohne Prüfung auf Wiedererkennbarkeit.
- Jeder Bericht nennt Teilnahmezahl im Verhältnis zu 40 Beschäftigten (Reichweite), Verteilung über C01, Fehlwerte nach Grund und den Hinweis auf Selbstauskunft.
- Personenwerte bleiben in der Arbeitsdatei und werden nicht weitergegeben.

---

## 4 Prüfbericht einschließlich offener Probleme

Hinweis zur Art der Prüfung: Die folgenden Prüfungen hat dasselbe Modell durchgeführt, das die Fassung erstellt hat. Sie sind eine Verfahrens- und Selbstprüfung, **kein** unabhängiges Gutachten.

### 4.1 Kernabgleich Bank gegen Befragungsfassung (ausgeführt)

Ausgeführt mit Python 3 auf `instrument/Itembank_GARI_DE_0.1.json`. Die Kernzeilen in 3.1 wurden maschinell aus `frozen_participant_text` (Zeilen 6–112) übernommen.

| Prüfung | Ergebnis |
|---|---|
| Anzahl Items in `items` | 34, alle IDs eindeutig |
| Reihenfolge der IDs in `frozen_participant_text` = Reihenfolge in `items` | ja |
| Fragetext je ID in `frozen_participant_text` = `text` in `items` | ja, 34 von 34, keine Abweichung |
| Alle Antwortoptionen (`options`) von C01–C06, W01, W02 im Teilnehmertext vorhanden | ja, keine fehlende Option |
| Definition in Teilnehmertext = `definition` | ja, wörtlich |
| Skalenanker 0–10 und 1–7 in Instruktionen = `scales` | ja |
| NB/KA bei allen 25 numerischen Items im Teilnehmertext | ja (Zeilen „… NB KA“) |
| „Keine Angabe“ bei C01–C06, W01, W02, W03 | ja |
| Wörtliche Übernahme der Zeilen 6–112 in diese Ausgabe | maschinell geprüft nach dem Schreiben, Ergebnis in 4.4 |

### 4.2 Erlaubte Kontextänderungen (vollständige Liste)

| Stelle (Zeile in `frozen_participant_text`) | Pretest-Fassung | Erhebungsfassung E1 | Einordnung |
|---|---|---|---|
| 0 Titel | Fragebogen zum Umgang mit generativer KI | unverändert | keine Änderung |
| 1 Untertitel | Fassung für den Verständlichkeitstest · GARI-DE-0.1 · 29. September 2026 | Onlinebefragung · Fragebogen GARI-DE-0.1 | organisatorisch |
| 2 Zweck | „… Im anschließenden Gespräch prüfen wir, ob die Fragen verständlich sind. …“ | Gesprächshinweis ersetzt durch Zweck und aggregierte Auswertung; Satz zur Arbeitsleistung und Dauer beibehalten | organisatorisch |
| 3 Definition | wörtlich | wörtlich | Kern, unverändert |
| 4 Freiwilligkeit | „… oder den Test beenden. … Beim begleiteten Test kennt die durchführende Person Sie; eine vollständige Anonymität wird deshalb nicht zugesagt.“ | „… oder die Befragung beenden. …“; Satz zum begleiteten Test ersetzt durch Platzhalter für geprüfte Datenschutzangabe; Regel zum Auslassen gleich | organisatorisch; Anonymität bewusst **nicht** zugesagt |
| 5 Testkürzel/Datum | Felder zum Ausfüllen | entfällt; Kürzel wird bei Übertragung vergeben | organisatorisch, Datensparsamkeit |
| neu | – | Kontaktzeile mit Platzhalter | durch `context_changes_allowed` gedeckt |
| 113 Abschluss | Hinweis auf Gespräch | Dank und Absendehinweis | organisatorisch |

Ergebnis: keine Änderung an Definition, Items, Antwortoptionen, Skalen, Instruktionen, Reihenfolge oder Zeitbezügen. Ob „den Test beenden“ → „die Befragung beenden“ in Zeile 4 bereits Kerninstruktion ist, ist eine Auslegungsfrage. Die Zeile gehört zum Pretest-Rahmen; die Regel zum Auslassen bleibt inhaltlich gleich. Entscheidung als eigene Einordnung gekennzeichnet.

### 4.3 Offene Probleme und Risiken

| Nr. | Problem | Betroffene Stelle | Vorschlag | Folge für Vergleichbarkeit | Status |
|---|---|---|---|---|---|
| P1 | Papierinstruktion „Kreisen Sie … ein“ in Onlineform | Zeilen 21, 49, 68 | Entweder wörtlich lassen (aktuelle Fassung) oder neue Version mit eigenem Codebuch | Neue Version wäre nicht unter GARI-DE-0.1 rechenbar | OFFEN, Rückfrage 2 |
| P2 | Keine Onlineumsetzung vorhanden | gesamte Fassung | Formular nach 3.4.5 bauen, dann Oberflächenabgleich nach 4.5 | – | Freigabestatus OFFEN |
| P3 | Anonymität nicht gesichert | Teil E, Einladung | Plattformeinstellungen prüfen, erst dann Formulierung festlegen | – | OFFEN, Rückfrage 1 |
| P4 | Exklusivität und Höchstzahl bei W01/W02 möglicherweise technisch nicht durchsetzbar | W01, W02 | Technische Regel testen (Fortsetzen mit 4 Auswahlen muss blockiert werden); Exklusivität sonst nach Codebuch kodieren | Bei fehlender Sperre mehr KA-Fälle möglich | OFFEN |
| P5 | Briefing nennt drei Tätigkeitsbereiche; Kern hat nur C01 mit anderer Einteilung | C01 | Kein neues Item im Kern. Falls Gruppenvergleich nach den drei Bereichen nötig ist: eigene Version mit dokumentiertem Zusatzitem außerhalb des Kerns und angepasster Rechenroutine (die aktuelle Routine stoppt bei unbekannten IDs) | Ein Zusatzitem würde das Datenformat ändern | OFFEN, Rückfrage 3 |
| P6 | Werkzeug laut Briefing nur für Büroarbeitsplätze freigegeben | C04, I01–I03, A01–A04 | Nicht in Fragebogen oder Einladung nennen; bei Auswertung C04 nach C01 betrachten. Hohe Anteile C04 = NO bei OTHER_WORK sind ein Zugangsbefund, kein Kompetenzbefund | – | Planungsregel |
| P7 | Doppelte Einsendungen bei offenem Link nicht erkennbar | Datenqualität | Im Bericht als Grenze nennen; keine nachträgliche Entfernung ohne Beleg | – | dokumentiert |
| P8 | `score.py`, Tests, Beispieldaten und Pretestdokumente lagen nicht vor | Rechnen, äußere Dateistruktur | Vor einer echten Auswertung mit diesen Dateien arbeiten | – | OFFEN |
| P9 | MAILS-Originalwortlaut in dieser Sitzung nicht eingesehen | U, K, L | Register übernimmt Projektstand; keine eigene Bestätigung | – | dokumentiert |
| P10 | POWERPILOT_2025: OSF-Anhang nicht verglichen | A, I | Bei Zugang Wortlaut vergleichen | – | OFFEN |
| P11 | Rechte für öffentliche, veränderte Itemtexte ungeklärt | MAILS- und POWERPILOT-Items | Vor Veröffentlichung klären; interne Befragung ist davon getrennt zu beurteilen | – | OFFEN |
| P12 | Bearbeitungszeit nicht gemessen | Teil E | Angabe „geschätzt“ beibehalten; Messung nur mit geeignetem Verfahren | – | OFFEN |

### 4.4 Ergebnis der maschinellen Wortlautprüfung dieser Ausgabe

Ausgeführt mit Python 3 nach dem Zusammensetzen dieser Ausgabe: Der Kernabschnitt in 3.1 wurde nach Entfernen der Satzzeichen für Markdown (Fettdruck der IDs, Überschriftenzeichen, Codeformat der Zahlenzeilen) Zeile für Zeile mit `frozen_participant_text` Zeilen 6–112 verglichen.

- Zeilen in identischer Reihenfolge und identischem Wortlaut: ja (107 Zeilen im Abschnitt, Soll 107; fehlende Zeilen: 0)
- Fragetexte mit ID gefunden: 34 von 34
- Ergebnis: keine Abweichung des Kerntextes

### 4.5 Vorgesehener Oberflächenabgleich (noch nicht durchgeführt)

Nach dem Bau des Formulars, vor dem Versand, in einer **ungesendeten** Sitzung oder einem getrennten technischen Probelauf (`SYNTHETIC_DEMO`), nie mit echten Antworten vermischt:

1. Alle 34 IDs sichtbar und in Bankreihenfolge.
2. Jeder Fragetext zeichengenau gegen `items[].text`.
3. Definition und alle Abschnittsinstruktionen zeichengenau gegen 3.1.
4. Endanker 0–10 und 1–7 korrekt, keine Zwischenanker.
5. Jede Antwortoption einschließlich NB und KA auswählbar, nicht nur als Hinweis.
6. Seitenwechsel vor „Einstellung und geplante Nutzung“.
7. Keine Pflichtfelder.
8. W01/W02: Versuch, mit vier Auswahlen fortzusetzen oder abzusenden; protokollieren, ob blockiert wird. Exklusive Optionen zusammen mit anderen wählen; protokollieren, was passiert.
9. Exportdatei eines Probelaufs: Spalten, Datentypen, Darstellung von NB/KA und Mehrfachantworten. Ein erfolgreicher Seitenwechsel belegt nicht die Speicherung; die Übermittlung gesondert prüfen oder als ungeprüft ausweisen.
10. Abweichungen mit konkreter Korrektur und Nachprüfung im Manifest eintragen.

Freigabestatus erst danach: BESTANDEN, OFFEN oder ABWEICHUNG. Aktueller Status: **OFFEN**.

### 4.6 Begleitmanifest

| Feld | Eintrag |
|---|---|
| Referenzbank | `instrument/Itembank_GARI_DE_0.1.json`, Version GARI-DE-0.1, Datum 2026-09-29 |
| Codebuch | Codebuch GARI-DE-0.1, Projektpaket 0.2, Stand 2026-09-29, fortgeschrieben 2026-10-17 |
| Fragebogenversion (Kern) | GARI-DE-0.1 |
| Umsetzungskennung | GARI-DE-0.1/S1-DEMO-ONLINE-E1 |
| Kontextart | FIKTIVE_DEMONSTRATION |
| Erhebungsrunde | keine (nicht versandt) |
| Plattform | NICHT_DOKUMENTIERT (Briefing: „Onlineformular“) |
| Datum Oberflächenabgleich | nicht durchgeführt |
| Tatsächlich geprüfte Stellen | Bank gegen Teilnehmertext (4.1); Ausgabetext gegen Bank (4.4). Keine Formularoberfläche geprüft |
| Offene Abweichungen | keine Kernabweichung im Text; Probleme P1–P12 offen |
| Erstellungsprompt | Masterprompt 0.5 vom 17. Oktober 2026, Betriebsart ANWENDEN |
| Eingabedateien | briefing.json (Version 0.1, Szenario S1); instrument/Itembank_GARI_DE_0.1.json; instrument/Codebuch.md; Quellen_APA.md (Stand 17. Oktober 2026) |
| Manuelle Änderungen | keine |
| System/Modell | Claude, Modellangabe „Opus 5.5“ (`claude-opus-5-5`); weitere Parameter NICHT_VERFUEGBAR |
| Speicherung abgebrochener Formulare | NICHT_DOKUMENTIERT |
| Freigabestatus | OFFEN |

---

## 5 Auswertungsbericht

Nicht erstellt. Es liegen keine Antwortdaten vor (`antwortdaten_vorhanden: false`). Berechnungsstatus: **NICHT_BERECHNET**. Es werden keine Zahlen zu diesem Betrieb genannt. Ein synthetisches Rechenergebnis aus dem Projekt wird nicht verwendet.

Rechenanweisung für eine spätere Auswertung (im entpackten Projektordner, Python 3.10 oder neuer, ohne Zusatzpakete; laut Codebuch):

```bash
python -m unittest discover -s tests -v
python auswertung/score.py <antwortdatei.json> <ergebnis.json>
```

Schritte:

1. Daten nach 3.4 übertragen; `data_kind` und `questionnaire_version` setzen. Nur wenn der Oberflächenabgleich BESTANDEN ist, darf `GARI-DE-0.1` eingetragen werden.
2. Tests ausführen; sie prüfen nur die Rechenroutine, nicht Verständlichkeit oder Messqualität.
3. `score.py` ausführen und den tatsächlichen Exitstatus prüfen. Bei Abbruch (unzulässige Werte, IDs, Duplikate, Versionen) nichts reparieren, sondern Prüfbericht erstellen.
4. Nur die erzeugte Ausgabe berichten: je Item gültige Anzahl, Fehlwerte nach Grund, Verteilung; U, K, L, A, I nur mit Anzahl vollständiger und unvollständiger Fälle; W01/W02 mit Nenner; Prüfhinweise C04/I.
5. NB-Anteile nur berichten, wenn NB im Formular tatsächlich auswählbar war (Abgleich Schritt 5).
6. Reichweite (Teilnahmen von 40) und Verteilung über C01 nennen. Keine Hochrechnung, keine Signifikanz-, Alpha- oder Faktorenanalysen.

`score.py` lag dieser Sitzung nicht vor und wurde nicht ausgeführt.

---

## 6 Maßnahmenmatrix (vorbereitet, ohne Befunde)

Es gibt noch keine Befunde. Die Matrix legt **vor** der Erhebung fest, wie aus Befunden Maßnahmen werden. Sie übernimmt die Planungslogik des Codebuchs und ergänzt die Anwendung auf diesen Betrieb. Sie trifft keine diagnostischen Entscheidungen über einzelne Beschäftigte. Befund-IDs werden erst nach der Auswertung vergeben (Schema `B-S1-01`, `B-S1-02` …). Priorisierung ist eine begründete Planungsentscheidung nach geäußerten Wünschen, Aufgabenrelevanz und Umsetzbarkeit, ohne versteckte Gewichtung.

| Regel-ID | Auslösender Befund (Items) | Art | Interpretationsregel | Mögliche Maßnahme / Ziel | Zielgruppe | Unsicherheit | Erfolgskontrolle (Vorschlag) |
|---|---|---|---|---|---|---|---|
| R1 | W01 = BASICS | Geäußerter Lernwunsch | Anzahl und Anteil an gültigen W01-Antworten berichten | Einführung in generative KI; Ziel: Grundbegriffe und sichere erste Nutzung des freigegebenen Werkzeugs | Personen mit diesem Wunsch, getrennt nach C04 | Selbstauskunft; Vorkenntnisse unbekannt | Teilnahme; kurze praktische Aufgabe nach der Einführung |
| R2 | W01 = PROMPTING | Geäußerter Lernwunsch | wie R1 | Übung zu Eingaben und Überarbeitung an eigenen Aufgaben | nur sinnvoll mit Zugang (C04 = YES) | Zugang Voraussetzung | Vorher-nachher-Aufgabe mit Arbeitsbeispiel |
| R3 | W01 = VERIFY oder W02 = RELIABILITY; ergänzend Verteilungen G01, G02 | Lernwunsch bzw. wahrgenommene Unsicherheit | G01/G02 nur beschreibend, keine Grenzwerte | Ergebnis- und Quellenprüfung an Arbeitsbeispielen | Personen mit Wunsch oder Hindernis | Selbsteinschätzung ist kein Leistungsnachweis | Übung mit fehlerhaften KI-Antworten |
| R4 | W01 = DATA_RULES, W02 = RULES, C05 = NOT_KNOWN oder EXISTENCE_UNKNOWN; ergänzend G03 | Orientierung, organisatorisch | Erst klären, ob Regeln existieren | Regeln verständlich bereitstellen, Zuständigkeit benennen | ganzer Betrieb | Unklar, ob Regeln fehlen oder unbekannt sind | Folgebefragung C05; Nachfragen bei Zuständigen |
| R5 | C04 = NO oder UNKNOWN; W02 = ACCESS | Organisatorisches Hindernis | Keine Kompetenzlücke ableiten; nach C01 aufschlüsseln (Werkzeug laut Briefing nur Büroarbeitsplätze) | Freigegebene Zugangsmöglichkeiten prüfen, auch für OTHER_WORK, wenn Aufgaben passen | v. a. C01 = OTHER_WORK, MIXED | Zugang kann auch sachlich nicht nötig sein (mit C06 lesen) | Entscheidung dokumentiert; spätere C04-Verteilung |
| R6 | C06 = NO oder W02 = TASK_FIT | Fehlende oder unklare Aufgabenpassung | Nicht als Ablehnung oder Defizit werten | Anwendungsfälle gemeinsam prüfen; Nutzung kann unnötig sein | betroffene Gruppen | Grund unbekannt | Liste geprüfter Anwendungsfälle |
| R7 | W02 = TIME | Rahmenbedingung | Anzahl berichten | Lernzeit und Arbeitsorganisation prüfen | betroffene Gruppen | – | Vereinbarte Lernzeit vorhanden |
| R8 | NB-Antworten auf einem Fähigkeitsitem (tatsächliche Anzahl und Nenner) | Unklare Einschätzbarkeit | Nicht als niedrige Kompetenz zählen; nur wenn NB auswählbar war | Frageverständnis und Erfahrungsgrundlage prüfen | – | Ursache offen | gezielte neutrale Nachfrage |
| R9 | Niedrige Selbsteinschätzungen in U/K/L/G **und** passender Lernwunsch W01 **und** C06 = YES | Mehrere zusammenpassende Hinweise | Nur als Hypothese; Antwortkategorien und Anzahlen nennen, keine Schwelle | Vertiefendes Angebot plus praktische Aufgabe zur Abklärung | nur aggregiert | Selbstbericht; keine validierte Grenze | Praktische Aufgabe |
| R10 | W01 = NONE bei niedriger Nutzung | Kein geäußerter Wunsch | Kritisch begründete Zurückhaltung ist kein Schulungsdefizit; mit W02, C06 lesen | Kein Pflichtangebot; offenes Informationsangebot | – | Motiv unbekannt | – |
| R11 | Hohe Selbsteinschätzungen und häufige Nutzung (C02) | Mögliche Stärke | Kein objektiver Kompetenznachweis | Vertiefende Angebote; ggf. interner Austausch | – | Selbstbericht | – |
| R12 | W03-Themen | Qualitative Hinweise | Aussagen der Befragten getrennt von Interpretation; neue Themen im Auswertungsschlüssel dokumentieren | Anwendungsbeispiele für Schulungen | – | Kleine Zahlen, selektive Antworten | – |

Keine Wirksamkeit eines Trainings wird behauptet.

---

## 7 Änderungsprotokoll

| Nr. | Datum | Änderung | Art | Version |
|---|---|---|---|---|
| 1 | 2026-10-18 | Erhebungsfassung `GARI-DE-0.1/S1-DEMO-ONLINE-E1` aus GARI-DE-0.1 abgeleitet | neue Umsetzungskennung | Kern GARI-DE-0.1 |
| 2 | 2026-10-18 | Pretest-Einleitung (Zeilen 1, 2, 4, 5) und Abschluss (Zeile 113) durch Online-Erhebungshinweise ersetzt; Kontaktzeile ergänzt | organisatorisch, `context_changes_allowed` | Kern unverändert |
| 3 | 2026-10-18 | Codebuch-Ergänzungen 3.4.5 (Onlineumsetzung) und 3.4.6 (Berichtsregeln) | eigene Planungsentscheidungen | Rechenregeln unverändert |
| 4 | 2026-10-18 | Maßnahmenregeln R1–R12 für den Betrieb konkretisiert | Planung | – |

Keine Änderung an Items, Skalen, Optionen, Instruktionen, Reihenfolge, Filtern oder Rechenregeln.

---

## 8 Rückfragen (gebündelt, höchstens drei)

Diese Fragen ändern den nächsten Schritt. Alles andere ist bereits vorbereitet.

1. **Plattform und Datenschutz:** Welche Plattform wird verwendet, wird eine Anmeldung oder E-Mail-Adresse erfasst, werden abgebrochene Formulare gespeichert, und wer sieht Einzelantworten? Davon hängen der Datenschutzsatz in Teil E und der Oberflächenabgleich ab.
2. **Papierinstruktion „Kreisen Sie … ein“:** Soll die Onlinefassung den Kernwortlaut beibehalten (dann bleibt GARI-DE-0.1 und die Rechenroutine nutzbar) oder soll eine neue Version mit Onlineformulierung entstehen (dann neues Codebuch, angepasste Routine, keine Rechnung unter GARI-DE-0.1)?
3. **Gruppenberichte:** Reicht die Aufschlüsselung nach C01 oder wird ein Vergleich nach Verwaltung, Kundenkontakt und Operativer Tätigkeit gebraucht (dann neue Version mit dokumentiertem Zusatzitem)? Und welche Mindestgruppengröße gilt für Berichte (vorläufig 5 als Planungsannahme)?

---

## 9 Nächste konkret erforderliche Eingaben

- Antworten auf die drei Rückfragen.
- Für einen echten Einsatz: reales Briefing statt Demonstration, Kontaktperson, Zeitraum, Link.
- Gebautes Formular und Exportprobe für den Oberflächenabgleich (4.5).
- `auswertung/score.py`, `tests/`, `beispiele/synthetische_antworten.json` für Dateistruktur und Rechnung.
- Antwortdaten einer tatsächlich durchgeführten Erhebung mit passender Version.

---

## 10 Status

| Bereich | Stand |
|---|---|
| Erstellt | Befragungsfassung E1 (Kern wörtlich, Rahmen ersetzt), Einladungstext, Quellen- und Konstruktregister, Itemregister für 34 Items, Codebuch mit Exportzuordnung und leerer Vorlage, Umsetzungsvorgaben, Manifest, Maßnahmenregeln |
| Geprüft | Maschineller Abgleich Bank gegen Teilnehmertext und Ausgabetext gegen Bank (Selbstprüfung desselben Modells). Keine Originalquelle in dieser Sitzung eingesehen. Kein Formular geprüft. |
| Berechnet | Nichts. NICHT_BERECHNET, da keine Daten vorliegen |
| Freigabe | OFFEN |
| Evidenzgrenzen | Keine psychometrische Validierung der Kombination; vorläufige deskriptive Teilbereichswerte; POWERPILOT_2025 nur gegen bereitgestellte Itemsammlung geprüft, OSF-Vergleich offen; MAILS-Evidenz betrifft allgemeine KI; formativer Pretest (3 reale R1, 2 synthetische R2) ist keine Validierung |
| Fehlt | Plattformentscheidung, Oberflächenabgleich, reale Daten, Rechenroutine in der Sitzung |

---

## Literatur

Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. University of Massachusetts Amherst. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), Article e39686. https://doi.org/10.1016/j.heliyon.2024.e39686

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. *European Journal of Information Systems, 25*(1), 77–89. https://doi.org/10.1057/ejis.2014.36

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114

Alle Nachweise und Prüfvermerke sind aus `Quellen_APA.md` (Stand 17. Oktober 2026) übernommen. Ein DOI ersetzt keine Inhaltsprüfung.
