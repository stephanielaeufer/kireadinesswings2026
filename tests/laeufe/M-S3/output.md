# GARI-DE: Unternehmensbezogene Befragungsfassung (Betriebsart ANWENDEN)

**Fiktive Demonstration (Szenario S3).** Das Unternehmen ist erfunden. Es liegen keine realen Daten vor. Alle Angaben zum Unternehmen stammen ausschließlich aus `briefing.json`; nichts wurde ergänzt.

## 0 Laufangaben

| Angabe | Wert |
|---|---|
| Datum | 18. Oktober 2026 |
| System und Modell | Claude (Anthropic), Modellkennung laut Sitzungsumgebung `claude-opus-5-5`; Temperatur und weitere Parameter NICHT_VERFUEGBAR |
| Promptversion | Masterprompt 0.5 vom 17. Oktober 2026 |
| Betriebsart | ANWENDEN (ausdrücklich angegeben) |
| Referenzbank | `instrument/Itembank_GARI_DE_0.1.json`, Version GARI-DE-0.1, Datum 29.09.2026, 34 Items |
| Codebuch | `instrument/Codebuch.md`, GARI-DE-0.1, Projektpaket 0.2, Stand 29.09.2026 mit redaktioneller Fortschreibung 17.10.2026 |
| Quellenstand | `Quellen_APA.md`, Stand 17. Oktober 2026 |
| Briefing | `briefing.json`, Version 0.1, Szenario S3, Kontextart FIKTIVE_DEMONSTRATION |
| Datenart | keine Antwortdaten (`antwortdaten_vorhanden: false`) |
| Berechnungsstatus | NICHT_BERECHNET (keine Daten; `auswertung/score.py` nicht beigefügt) |
| Gleiche Prompts garantieren keine identischen Ausgaben | ja, gilt auch für diesen Lauf |

## 1 Ziel, Zielgruppe, Kontext und Annahmen

**Ziel laut Briefing:** Status quo beschreiben, Hinweise auf Weiterbildungsbedarf ableiten, betriebliche Voraussetzungen gesondert erfassen.

**Zielgruppe:** Mitarbeitende aller Tätigkeitsbereiche, einschließlich Personen ohne bisherige GenAI-Nutzung. Genannte Bereiche: Vertrieb, Kundendienst, Entwicklung, Verwaltung, Personal, Führung.

**Kontext:** fiktives Unternehmen, 1.200 Beschäftigte, mehrere Standorte (Anzahl und Namen nicht angegeben). GenAI-Werkzeuge sind laut Briefing vorhanden, werden aber unterschiedlich genutzt. Bisherige Nutzung ist unbekannt und wird mit dem Fragebogen erhoben. Sprache Deutsch. Erhebungsweg: Onlineformular, Zugang über Link, freiwillige Teilnahme.

**Wunsch laut Briefing:** differenzierte Lernwünsche je Funktion und Ergebnisse je Standort.

**Prüfung der Pflichtangaben vor Beginn**

| Angabe | Stand | Quelle |
|---|---|---|
| Zweck | bekannt | Briefing |
| Zielpopulation | bekannt | Briefing |
| Tätigkeitsbereiche | bekannt (6 Bereiche) | Briefing |
| Sprache | Deutsch | Briefing |
| Bezug auf generative KI | ja; Definition aus der Bank | Briefing, Bank |
| Bisherige Nutzungsmöglichkeiten | „vorhanden, aber unterschiedlich genutzt“; individueller Zugang unbekannt | Briefing |
| Zugelassene Anwendungen | UNBEKANNT | nicht angegeben |
| Aufgabenbezug | berufliche Aufgaben; konkrete Aufgaben je Bereich UNBEKANNT | Bank, Briefing |
| Betrachtungszeitraum | durch Kern festgelegt: C02 vergangene vier Wochen; A/I kommende drei Monate | Bank |
| Gewünschte Ausgabe | Befragungsfassung; später Ergebnisse je Funktion und Standort | Briefing |
| Art der Daten | noch keine; spätere Echtdaten wären SURVEY, Demonstrationsdaten SYNTHETIC_DEMO | Briefing, Codebuch |
| Standortliste | UNBEKANNT | nicht angegeben |
| Plattform des Onlineformulars | UNBEKANNT | nicht angegeben |
| Anonymitätseigenschaften des Erhebungsprozesses | UNBEKANNT | nicht angegeben |
| Erhebungszeitraum, Kontaktstelle, Datenschutzinformation | UNBEKANNT | nicht angegeben |

**Getroffene Annahmen und Entscheidungen (eigene methodische Entscheidungen)**

- A-1: Der Kern GARI-DE-0.1 wird unverändert übernommen: Definition, 34 Items, Reihenfolge, IDs, Antwortskalen und -optionen, NB/KA, Instruktionen, Zeitbezüge.
- A-2: Der Funktions- und Standortwunsch ist mit dem Kern nicht erfüllbar. C01 erfasst nur die Art der Tätigkeit (Büro/andere/gemischt), nicht den Bereich. Ein Standortmerkmal fehlt ganz. Deshalb schlage ich drei Ergänzungsitems X01–X03 **außerhalb des Kerns** vor, am Ende hinter W03. Das ist eine dokumentierte Ergänzung mit eigener Kennung, kein Teil von GARI-DE-0.1.
- A-3: Die organisatorische Pretest-Einleitung und der Gesprächshinweis am Schluss gehören laut `frozen_text_note` nicht zum Kern. Für die Onlinebefragung ersetze ich sie durch einen eigenen, dokumentierten Einführungs- und Schlusstext. Definition und Kerninstruktionen bleiben unverändert.
- A-4: Kennung der Erhebungsfassung (Vorschlag): **GARI-DE-0.1-S3-ONLINE-E1**. Sie bezeichnet Kern GARI-DE-0.1 plus neuer Rahmen plus Ergänzung X01–X03. Status: ENTWURF, Oberflächenabgleich OFFEN.
- A-5: Keine Unternehmensmerkmale erfunden. Standorte erscheinen nur als gekennzeichnete Platzhalter.

## 2 Gebündelte Rückfragen (höchstens drei)

Es gibt keine Rückfragemöglichkeit in diesem Lauf. Alles andere ist ohne Antwort erstellt. Die Antworten verändern die Ergänzung X01–X03 und den Einführungstext.

1. **Ergänzung und Berichtsgruppen:** Wird die Ergänzung um Bereich (X01), Führungsverantwortung (X02) und Standort (X03) freigegeben? Wie lautet die vollständige Standortliste? Welche Mindestgruppengröße für Gruppenberichte gilt (mein Planungsvorschlag: 10 gültige Antworten je berichteter Gruppe, eigene Festlegung ohne empirische Grundlage)? Ist eine Abstimmung mit Datenschutz und gegebenenfalls Arbeitnehmervertretung vorgesehen?
2. **Plattform und Anonymität:** Welche Formularplattform wird genutzt? Werden E-Mail-Adressen, Anmeldungen, IP-Adressen oder personalisierte Links erfasst? Erst danach lässt sich entscheiden, welche der beiden Varianten des Datenschutzabsatzes im Einführungstext gilt.
3. **Onlinewortlaut der Kerninstruktionen:** Die eingefrorenen Kerninstruktionen enthalten Papierformulierungen („Kreisen Sie pro Aussage eine Zahl ein“, „Bitte fahren Sie auf der nächsten Seite fort“). Sollen sie wörtlich bleiben (Vergleichbarkeit mit GARI-DE-0.1, aber ungewohnt online), oder wird eine Onlinefassung mit neuer Fragebogenversion (z. B. GARI-DE-0.2-ONLINE) beschlossen? In dieser Lieferung bleiben sie wörtlich.

## 3 Quellen- und Konstruktregister mit Evidenzgrenzen

In ANWENDEN wird kein neues Messmodell entwickelt. Das Register gibt den Stand der beigefügten Dateien wieder. Ich habe in diesem Lauf **keine Originalquelle selbst eingesehen**. Alle Prüfvermerke stammen aus `Quellen_APA.md` und der Itembank und sind als Angaben des Projekts zu lesen, nicht als meine eigene Prüfung.

### 3.1 Quellenregister

| Quellen-ID | Nachweis (APA) | Geprüfter Dokumentstand laut Projekt | Fundstelle | Zielgruppe der Quelle | Sprache | Konstrukt / Funktion | Zugang laut Projekt | Grenzen |
|---|---|---|---|---|---|---|---|---|
| MAILS_DE_2023 | Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale … *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014 | Autoren-Volltext und deutscher Autorenfragebogen (3 Seiten, 34 Items) | Items 1–6, 7–12, 26–28; Zuordnung und Mittelwertregel S. 3 | 300 deutschsprachige Erwachsene | Deutsch/Englisch | Basis für U, K, L | vollständig (laut Projekt) | Allgemeine KI, nicht GenAI; Selbstbericht; Übertragung auf Arbeitskontext und NB/KA sind Anpassungen; Nachnutzungsrechte veränderter Items offen |
| MAILS_KURZ_2024 | Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), Article e39686. https://doi.org/10.1016/j.heliyon.2024.e39686 | Volltext, Abschnitte 2.1 und 3.4 | – | – | Englisch | Alternative Kurzfassung | vollständig (laut Projekt) | Nicht eingesetzt; enthält KI-Entwicklung |
| POWERPILOT_2025 | Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th HICSS* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114 | Paper und bereitgestellte Itemsammlung (Datensatz_v1.docx) | Questionnaire 2 / PowerPilot: 1 – Intention to use, Items 1–3; 2 – Attitude, Items 1–4 | Stichprobe aus Deutschland, Energieanwendung | Englisch | Basis für A, I | Paper vollständig; OSF-Anhang https://doi.org/10.17605/OSF.IO/GEBK9 **nicht abrufbar** (29.09. und erneut 17.10.2026) | **Direkter Wortlautvergleich mit dem OSF-Anhang offen.** Energiekontext; Übertragung auf GenAI ist inhaltliche Anpassung |
| AJZEN_TPB | Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf | 7-seitiges Originaldokument | – | – | Englisch | Verhaltensdefinition (Ziel, Handlung, Kontext, Zeit) für A/I | vollständig (laut Projekt) | Kein Erscheinungsjahr; Methodenanleitung, kein Instrument |
| PEFFERS_2007 | Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). … *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302 | Abschnitte zu den sechs Aktivitäten | – | – | Englisch | Entwicklungsmethode (DSR) | auszugsweise geprüft (laut Projekt) | Methode, kein Messinstrument |
| BOATENG_2018 | Boateng, G. O., et al. (2018). Best practices for developing and validating scales … *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149 | Volltext | – | – | Englisch | Trennung Entwicklung / Pretest / Validierung | vollständig (laut Projekt) | – |

Die übrigen in `Quellen_APA.md` genannten Studien (Wichmann et al., 2024; Paetow et al., 2026; Do Khac et al., 2025; Wichmann et al., 2026; Venable et al., 2016; NCHS, 2024; Bisbee et al., 2024) tragen keine Items des Kerns. Sie werden in dieser Anwendung nicht gebraucht.

### 3.2 Konstruktmatrix (Kern GARI-DE-0.1, unverändert)

| Teil | Definition (Kurzform) | Diagnosezweck | Grundlage | Ebene | Auswertung |
|---|---|---|---|---|---|
| C01–C06 | Tätigkeitsart, Nutzung (4 Wochen), private Nutzung, Zugang, Regelkenntnis, Aufgabenrelevanz | Kontext; Trennung von persönlichen Voraussetzungen und betrieblichen Bedingungen | Eigenentwicklung | berichtetes Verhalten (C02, C03), wahrgenommene betriebliche Bedingung (C04, C05), Einschätzung (C06) | Einzelverteilungen |
| U | Selbst eingeschätzte Anwendung | Lernbedarfshinweise Anwendung | MAILS_DE_2023, Items 1–6 | Selbsteinschätzung | vorläufiger Mittelwert U |
| K | Selbst eingeschätztes Verständnis | Lernbedarfshinweise Grundlagen | MAILS_DE_2023, Items 7–12 | Selbsteinschätzung | vorläufiger Mittelwert K |
| L | Zutrauen in das eigene Lernen | Ansatz für Lernformate | MAILS_DE_2023, Items 26–28 | Selbsteinschätzung | vorläufiger Mittelwert L |
| G01–G03 | Prüfen von Ergebnissen und zulässigen Eingaben | verantwortlicher Umgang | Eigenentwicklung | Selbsteinschätzung | drei Einzelitems, kein G-Wert |
| A | Einstellung zur arbeitsbezogenen Nutzung (bedingte Bewertung) | Haltung | POWERPILOT_2025, Attitude 1–4; AJZEN_TPB | Selbstbericht | vorläufiger Mittelwert A |
| I | Absicht unter tatsächlich erwarteten Bedingungen, 3 Monate | Nutzungsabsicht | POWERPILOT_2025, Intention 1–3; AJZEN_TPB | Selbstbericht | vorläufiger Mittelwert I |
| W01–W03 | Lernwünsche, Hindernisse, konkrete Aufgabe | ausdrücklicher Lernwunsch, organisatorische Hindernisse | Eigenentwicklung | Lernwunsch, wahrgenommene Bedingungen | Häufigkeiten, qualitative Zuordnung |

Kein Teil misst objektive Leistung. Die Kombination ist nicht psychometrisch validiert. Kein Gesamtwert, keine Reifegradklasse, keine Gewichtung.

## 4 Befragungsfassung GARI-DE-0.1-S3-ONLINE-E1 (Entwurf für das Onlineformular)

Aufbau: (a) neuer Rahmen außerhalb des Kerns, (b) Kern GARI-DE-0.1 wörtlich, (c) Ergänzung X01–X03 außerhalb des Kerns, (d) neuer Schlusstext. Nur (b) gehört zu GARI-DE-0.1. Teile (a), (c) und (d) sind dokumentierte Ergänzungen dieser Erhebungsfassung. Eckige Klammern `[…]` sind Platzhalter, die vor dem Einsatz das Unternehmen ausfüllt. Ich habe sie nicht erfunden.

### 4a Einführung (neu, ersetzt die Pretest-Einleitung; nicht Teil des Kerns)

**Fragebogen zum Umgang mit generativer KI**

Mit dieser Befragung wollen wir verstehen, wie generative KI bei uns derzeit genutzt wird, welche Weiterbildung Sie sich wünschen und was Sie bei der Nutzung behindert. Die Ergebnisse helfen uns, passende Lernangebote zu planen und betriebliche Voraussetzungen wie Zugang und Regeln zu verbessern. Es geht nicht um die Bewertung Ihrer Arbeitsleistung. Auch wenn Sie generative KI bisher nicht nutzen, ist Ihre Teilnahme wichtig.

Geschätzte Dauer: etwa 10 bis 15 Minuten. Diese Angabe ist eine Schätzung.

Generative KI erzeugt oder bearbeitet auf Eingaben hin Inhalte, zum Beispiel Texte, Bilder, Audio, Videos oder Programmcode. Gemeint sind sowohl eigenständige Anwendungen als auch entsprechende Funktionen in anderen Programmen.

Die Teilnahme ist freiwillig. Keine Frage ist verpflichtend. Sie können einzelne Fragen auslassen, „Keine Angabe“ wählen oder die Befragung jederzeit abbrechen. Bitte tragen Sie keine Namen, Personalnummern oder vertraulichen Informationen ein.

Ausgewertet und berichtet werden nur zusammengefasste Ergebnisse für das gesamte Unternehmen und für Gruppen mit mindestens [MINDESTGRUPPENGRÖSSE] Antworten, zum Beispiel nach Bereich oder Standort. Ergebnisse einzelner Personen werden nicht berichtet. [DATENSCHUTZABSATZ: verantwortliche Stelle, Plattform, erfasste technische Daten, Speicherdauer, Zugriff. Eine Zusage „anonym“ nur verwenden, wenn die Plattform weder Anmeldung noch E-Mail-Adresse, IP-Adresse oder personalisierte Links speichert.]

Fragen zur Befragung: [KONTAKTSTELLE]. Befragungszeitraum: [ZEITRAUM].

### 4b Kern GARI-DE-0.1 (wörtlich aus `frozen_participant_text`, Zeilen 7 bis 113 von 114)

Nicht übernommen wurden nur die Rahmenzeilen 1–3 und 5–6 (Titel mit Pretestkennung, Pretest-Einleitung, Teilnahmehinweis zum begleiteten Test, Testkürzel und Datum) sowie Zeile 114 (Hinweis auf das Gespräch). Die Definition (Zeile 4) steht unverändert in 4a. Alle folgenden Zeilen sind maschinell aus der Bank kopiert und nicht redigiert.

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

### 4c Ergänzung außerhalb des Kerns (X01–X03, NEU_ENTWICKELT, ungetestet)

Zweck: Der Wunsch nach Ergebnissen je Funktion und je Standort ist mit dem Kern nicht erfüllbar. Die Fragen stehen am Ende, damit Reihenfolge und Kontext des Kerns unverändert bleiben. Sie dienen nur der Gruppenbildung.

**Angaben für die Auswertung nach Gruppen**  
Die folgenden Angaben nutzen wir nur, um Ergebnisse für Gruppen mit mindestens [MINDESTGRUPPENGRÖSSE] Antworten zusammenzufassen. Sie können jede Frage auslassen.

X01  In welchem Bereich arbeiten Sie hauptsächlich?  
□ Vertrieb    □ Kundendienst    □ Entwicklung    □ Verwaltung    □ Personal    □ Anderer Bereich    □ Keine Angabe

X02  Haben Sie Führungsverantwortung für andere Mitarbeitende?  
□ Ja    □ Nein    □ Keine Angabe

X03  An welchem Standort arbeiten Sie überwiegend?  
□ [STANDORT 1]    □ [STANDORT 2]    □ [weitere Standorte laut Unternehmensliste]    □ Keine Angabe

Begründung der Konstruktion (eigene Entscheidung):
- „Führung“ steht im Briefing neben Fachbereichen. Führungskräfte gehören meist zugleich einem Fachbereich an. Deshalb ist Führung eine eigene Frage (X02) statt einer Option in X01. Eine Gruppe „Führung“ entsteht aus X02 = Ja.
- „Anderer Bereich“ deckt Tätigkeiten ab, die das Briefing nicht nennt, zum Beispiel Produktion oder Logistik. Ob es solche Bereiche gibt, ist UNBEKANNT.
- Kein Freitext bei X01/X03, um Identifizierbarkeit zu begrenzen.
- Überschneidung mit C01 („Service oder Außendienst“) und X01 („Kundendienst“, „Vertrieb“): C01 erfasst die Art der Arbeit, X01 den Organisationsbereich. Verständlichkeit im Pretest prüfen.

### 4d Schluss (neu, ersetzt den Gesprächshinweis)

Vielen Dank für Ihre Teilnahme. Mit „Absenden“ werden Ihre Antworten übermittelt.


## 5 Wissenschaftliches Itemregister

Alle Angaben maschinell aus der Bank übernommen. Originalwortlaute der MAILS-Items stehen nicht in der Bank. Sie sind dort nur über die Fundstelle referenziert und werden hier nicht rekonstruiert.

| ID | Dim. | Rolle | Status | Quelle / Fundstelle | Originalwortlaut | Änderung | Skala / Optionen | Anzeige | Richtung | Fehlwerte | Evidenz | Version |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | C | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: OFFICE = Überwiegend Büro- oder Bildschirmarbeit; OTHER_WORK = Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst; MIXED = Etwa gleich große Anteile beider Bereiche; + Keine Angabe | ALWAYS | nominal; keine Richtung | KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| C02 | C | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: D0 = An keinem Tag; D1_3 = An 1 bis 3 Tagen; D4_9 = An 4 bis 9 Tagen; D10_15 = An 10 bis 15 Tagen; D16_PLUS = An 16 oder mehr Tagen; UNKNOWN = Kann ich nicht einschätzen; + Keine Angabe | ALWAYS | nominal; keine Richtung | KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| C03 | C | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: YES = Ja; NO = Nein; UNKNOWN = Ich bin mir nicht sicher; + Keine Angabe | ALWAYS | nominal; keine Richtung | KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| C04 | C | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: YES = Ja; NO = Nein; UNKNOWN = Ich weiß es nicht; + Keine Angabe | ALWAYS | nominal; keine Richtung | KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| C05 | C | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: KNOWN = Ja; PARTLY = Teilweise; NOT_KNOWN = Nein; EXISTENCE_UNKNOWN = Ich weiß nicht, ob es solche Regeln gibt; + Keine Angabe | ALWAYS | nominal; keine Richtung | KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| C06 | C | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: YES = Ja; NO = Nein; UNKNOWN = Kann ich noch nicht beurteilen; + Keine Angabe | ALWAYS | nominal; keine Richtung | KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U01 | U | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 1; Deutscher Autorenfragebogen, Item 1, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | KI-Bezug auf generative KI eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U02 | U | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 2; Deutscher Autorenfragebogen, Item 2, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Erleichterung des Lebens auf berufliche Aufgaben eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U03 | U | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 3; Deutscher Autorenfragebogen, Item 3, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Zielbezug auf Arbeitsziele eingegrenzt; sinnvoll durch gezielt konkretisiert. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U04 | U | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 4; Deutscher Autorenfragebogen, Item 4, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Alltagsinteraktion auf Zusammenarbeit bei der Arbeit übertragen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U05 | U | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 5; Deutscher Autorenfragebogen, Item 5, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Gewinnbringende Zusammenarbeit über brauchbare Arbeitsergebnisse konkretisiert; Bedeutungsverschiebung im Pretest prüfen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U06 | U | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 6; Deutscher Autorenfragebogen, Item 6, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Gewinnbringende Kommunikation über verständliches Mitteilen konkretisiert; Ergebnisaspekt verengt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K01 | K | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 7; Deutscher Autorenfragebogen, Item 7, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Allgemeine KI auf generative KI eingegrenzt; Konzepte bleibt bewusst zur Verständlichkeitsprüfung erhalten. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K02 | K | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 8; Deutscher Autorenfragebogen, Item 8, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Kenntnis von Definitionen in selbst eingeschätzte Erklärfähigkeit übertragen; stärkere Anpassung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K03 | K | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 9; Deutscher Autorenfragebogen, Item 9, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K04 | K | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 10; Deutscher Autorenfragebogen, Item 10, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K05 | K | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 11; Deutscher Autorenfragebogen, Item 11, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Gegenstand eingegrenzt; Verwendungszwecke sprachlich vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K06 | K | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 12; Deutscher Autorenfragebogen, Item 12, Seite 1; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Gegenstand eingegrenzt; Satz verkürzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| L01 | L | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 26; Deutscher Autorenfragebogen, Item 26, Seite 2; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Gegenstand eingegrenzt; stets entfällt. Deutsche Itemnummer 26 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| L02 | L | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 27; Deutscher Autorenfragebogen, Item 27, Seite 2; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Gegenstand eingegrenzt; deutsche Itemnummer 27 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| L03 | L | FESTER_KERN | ADAPTIERT | MAILS_DE_2023, Item 28; Deutscher Autorenfragebogen, Item 28, Seite 2; Zuordnung und Mittelwertregel Seite 3. | nicht wiedergegeben; laut Bank am Dokument geprüft, über Fundstelle referenziert | Gegenstand eingegrenzt; sprachliche Verdichtung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| G01 | G | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: – | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| G02 | G | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: – | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| G03 | G | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | ABILITY_0_10: 0–10, ganzzahlig; 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker; + NB, KA. Original: – | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| A01 | A | FESTER_KERN | ADAPTIERT | POWERPILOT_2025, Item 2 – Attitude, Item 1; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | The use of PowerPilot would be … advantageous. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | AGREEMENT_1_7: 1–7, ganzzahlig; 1 = stimme überhaupt nicht zu, 7 = stimme vollständig zu; keine Zwischenanker; + NB, KA. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| A02 | A | FESTER_KERN | ADAPTIERT | POWERPILOT_2025, Item 2 – Attitude, Item 2; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | The use of PowerPilot would be … satisfactory. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | AGREEMENT_1_7: 1–7, ganzzahlig; 1 = stimme überhaupt nicht zu, 7 = stimme vollständig zu; keine Zwischenanker; + NB, KA. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| A03 | A | FESTER_KERN | ADAPTIERT | POWERPILOT_2025, Item 2 – Attitude, Item 3; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | The use of PowerPilot would be … important. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | AGREEMENT_1_7: 1–7, ganzzahlig; 1 = stimme überhaupt nicht zu, 7 = stimme vollständig zu; keine Zwischenanker; + NB, KA. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| A04 | A | FESTER_KERN | ADAPTIERT | POWERPILOT_2025, Item 2 – Attitude, Item 4; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 4; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | The use of PowerPilot would be … enjoyable. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | AGREEMENT_1_7: 1–7, ganzzahlig; 1 = stimme überhaupt nicht zu, 7 = stimme vollständig zu; keine Zwischenanker; + NB, KA. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| I01 | I | FESTER_KERN | ADAPTIERT | POWERPILOT_2025, Item 1 – Intention to use, Item 1; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | I plan to use PowerPilot in the future. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | AGREEMENT_1_7: 1–7, ganzzahlig; 1 = stimme überhaupt nicht zu, 7 = stimme vollständig zu; keine Zwischenanker; + NB, KA. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| I02 | I | FESTER_KERN | ADAPTIERT | POWERPILOT_2025, Item 1 – Intention to use, Item 2; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | I intend to use PowerPilot in the future. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | AGREEMENT_1_7: 1–7, ganzzahlig; 1 = stimme überhaupt nicht zu, 7 = stimme vollständig zu; keine Zwischenanker; + NB, KA. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| I03 | I | FESTER_KERN | ADAPTIERT | POWERPILOT_2025, Item 1 – Intention to use, Item 3; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | I will definitely use PowerPilot in the future. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | AGREEMENT_1_7: 1–7, ganzzahlig; 1 = stimme überhaupt nicht zu, 7 = stimme vollständig zu; keine Zwischenanker; + NB, KA. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | ALWAYS | höher = höhere Selbsteinschätzung bzw. Zustimmung; keine Umkodierung | NICHT_BEURTEILBAR, KEINE_ANGABE | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| W01 | W | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Mehrfachwahl, max. 3: BASICS = Grundlagen generativer KI; USE_CASES = Passende Einsatzmöglichkeiten für meine Aufgaben; PROMPTING = Klare Eingaben formulieren und Ergebnisse verbessern; VERIFY = Antworten und Quellen überprüfen; DATA_RULES = Betriebliche Regeln und zulässige Dateneingaben; KEEP_CURRENT = Bei neuen Entwicklungen auf dem Laufenden bleiben; OTHER = Anderes Thema; NONE = Derzeit kein Weiterbildungswunsch; UNKNOWN = Ich kann meinen Bedarf noch nicht einschätzen; exklusiv: NONE, UNKNOWN; + Keine Angabe (exklusiv) | ALWAYS | nominal; keine Richtung | KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| W02 | W | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Mehrfachwahl, max. 3: ACCESS = Kein Zugang zu einem freigegebenen Werkzeug; RULES = Unklare betriebliche Regeln; TIME = Zu wenig Zeit zum Ausprobieren oder Lernen; KNOWLEDGE = Mir fehlt Wissen über die Nutzung; TASK_FIT = Ich erkenne keinen passenden Einsatz für meine Aufgaben; RELIABILITY = Unsicherheit über die Verlässlichkeit der Ergebnisse; OTHER = Etwas anderes; NONE = Derzeit nichts; UNKNOWN = Kann ich noch nicht einschätzen; exklusiv: NONE, UNKNOWN; + Keine Angabe (exklusiv) | ALWAYS | nominal; keine Richtung | KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| W03 | W | FESTER_KERN | NEU_ENTWICKELT | – | kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Freitext; + Ankreuzfeld Keine Angabe | ALWAYS | nominal; keine Richtung | KEINE_ANGABE | Noch nicht empirisch geprüft. | GARI-DE-0.1 |

**Ergänzungsitems (nicht Teil von GARI-DE-0.1)**

| ID | Dim. | Rolle | Status | Quelle | Optionen | Anzeige | Fehlwerte | Evidenz | Version |
|---|---|---|---|---|---|---|---|---|---|
| X01 | X | KONTEXT_ERGAENZUNG | NEU_ENTWICKELT | Briefing (Tätigkeitsbereiche) | SALES, SERVICE, DEV, ADMIN, HR, OTHER_AREA + KA | ALWAYS, nach W03 | KEINE_ANGABE | ungetestet | GARI-DE-0.1-S3-ONLINE-E1 |
| X02 | X | KONTEXT_ERGAENZUNG | NEU_ENTWICKELT | Briefing („Führung“) | YES, NO + KA | ALWAYS, nach X01 | KEINE_ANGABE | ungetestet | GARI-DE-0.1-S3-ONLINE-E1 |
| X03 | X | KONTEXT_ERGAENZUNG | NEU_ENTWICKELT | Briefing (mehrere Standorte) | Standortcodes UNBEKANNT + KA | ALWAYS, nach X02 | KEINE_ANGABE | ungetestet | GARI-DE-0.1-S3-ONLINE-E1 |

## 6 Codebuch

### 6.1 Kern

Für alle 34 Kernitems gilt `instrument/Codebuch.md` (GARI-DE-0.1) unverändert: Datenformat JSON/UTF-8, `value` plus `missing_reason`, Wertebereiche 0–10 und 1–7, Antwortcodes laut Itemregister, keine Filter, Fehlwerte NICHT_BEURTEILBAR und KEINE_ANGABE, keine Umkodierung, vorläufige Teilbereichsmittelwerte nur für U, K, L, A, I bei vollständigen Antworten, G01–G03 als Einzelitems, kein Wert für G, C, W, kein Gesamtwert. NICHT_ZUTREFFEND und UEBERSPRUNGEN sind in GARI-DE-0.1 **nicht erlaubt**. Ein leeres Feld im Onlineformular wird als KEINE_ANGABE kodiert, nie als 0.

### 6.2 Ergänzung für die Erhebungsfassung GARI-DE-0.1-S3-ONLINE-E1 (neu, eigene Projektregel)

| Feld | Ebene | Wert | Regel |
|---|---|---|---|
| `data_kind` | Datei | SURVEY (reale Befragung) oder SYNTHETIC_DEMO (Demonstration) | Pflicht. Für dieses fiktive Szenario wären erzeugte Testdaten ausschließlich SYNTHETIC_DEMO. |
| `questionnaire_version` | Datei und Person | GARI-DE-0.1 | Nur zulässig, wenn der Oberflächenabgleich (Abschnitt 7) für alle 34 Kernitems BESTANDEN ist. Sonst eigene Version, und `score.py` darf nicht durch Umbenennung genutzt werden. |
| `implementation_id` | Datei | GARI-DE-0.1-S3-ONLINE-E1 | Pflicht. Kennzeichnet Rahmen, Plattform und Ergänzung. |
| Personenkennung | Person | zufällige laufende Nummer, z. B. R0001 | Keine Namen, Personalnummern, E-Mail-Adressen. Je Datei nur einmal. |
| X01 | Person, getrennte Gruppendatei | SALES, SERVICE, DEV, ADMIN, HR, OTHER_AREA; Fehlwert KEINE_ANGABE | Einzelwahl. Nur für Gruppenbildung. |
| X02 | Person, getrennte Gruppendatei | YES, NO; Fehlwert KEINE_ANGABE | Einzelwahl. |
| X03 | Person, getrennte Gruppendatei | Standortcodes laut Unternehmensliste (noch UNBEKANNT); Fehlwert KEINE_ANGABE | Einzelwahl. |

Reihenfolge der Codes X01: Vertrieb = SALES, Kundendienst = SERVICE, Entwicklung = DEV, Verwaltung = ADMIN, Personal = HR, Anderer Bereich = OTHER_AREA.

**Berichtsregeln für Gruppen (eigene Planungsregeln, keine Validierung):**
- Gruppen werden nur berichtet, wenn sie mindestens [MINDESTGRUPPENGRÖSSE] gültige Fälle haben. Kleinere Gruppen werden zu „weitere Bereiche“ bzw. „weitere Standorte“ zusammengefasst oder nicht ausgewiesen.
- Keine Kreuzung Bereich × Standort × Führung unterhalb der Mindestgröße. Eine Kreuzung kann Personen erkennbar machen.
- Personen mit KEINE_ANGABE bei X01–X03 bleiben in der Gesamtauswertung und erscheinen als eigene Zeile „ohne Angabe“ mit Anzahl.
- Je Gruppe: Anzahl Antworten, Teilnahmequote nur, wenn die Gruppengröße in der Belegschaft vom Unternehmen gemeldet wird (sonst NICHT_VERFUEGBAR).
- Unterschiede zwischen Gruppen werden beschreibend berichtet. Keine Signifikanzbehauptungen ohne vorab festgelegten Analyseplan.

**Plattformregeln:** NB und KA sind als auswählbare Optionen anzulegen, nicht nur als Hinweistext. Keine Frage ist Pflichtfeld. Keine numerischen Ersatzcodes für NB/KA (etwa 11, 99 oder -1) im Export. Ist das Exportformat so, muss die Umwandlung in `missing_reason` dokumentiert sein.

## 7 Standardisierung: Abgleich mit der Referenzbank und Begleitmanifest

### 7.1 Abgleich Kern gegen Bank (in diesem Lauf mit Code geprüft)

Ich habe ein Python-Skript (`work/check_bank.py`) gegen `Itembank_GARI_DE_0.1.json` ausgeführt. Exitstatus 0. Ergebnis:

| Prüfpunkt | Ergebnis |
|---|---|
| Anzahl Item-IDs | 34, alle eindeutig |
| Reihenfolge C01–C06, U01–U06, K01–K06, L01–L03, G01–G03, A01–A04, I01–I03, W01–W03 | entspricht `items` und `frozen_participant_text` |
| Wortlaut `items[].text` im eingefrorenen Teilnehmertext | 34 von 34 identisch enthalten |
| Antwortoptionen C01–C06, W01–W02 | alle Labels im Teilnehmertext vorhanden, je mit „Keine Angabe“ |
| Skalenzeilen numerischer Items | 0–10 bzw. 1–7 vollständig, jeweils mit NB und KA |
| Anzeigebedingung | alle ALWAYS, keine Filter |
| Umkodierung | keine |
| Unzulässige Fehlwertgründe (NICHT_ZUTREFFEND, UEBERSPRUNGEN) | keine |
| Teilbereiche + `not_a_scale` | decken alle 34 IDs ab, ohne Überschneidung |
| Definition | identisch im Teilnehmertext |
| Status | 22 ADAPTIERT, 12 NEU_ENTWICKELT, 0 ORIGINAL |

Abschnitt 4b ist maschinell aus `frozen_participant_text` kopiert. Die Tabelle 7.2 listet jedes Kernitem einzeln.

### 7.2 Itemweiser Abgleich

| Nr. | ID | Wortlaut in der Erhebungsfassung (aus `frozen_participant_text`) | Abgleich mit `items[].text` | Antwortangebot | Ergebnis |
|---|---|---|---|---|---|
| 1 | C01 | Wie sieht Ihre hauptsächliche Tätigkeit aus? | identisch | 3 Optionen + KA | unverändert übernommen |
| 2 | C02 | An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt? | identisch | 6 Optionen + KA | unverändert übernommen |
| 3 | C03 | Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt? | identisch | 3 Optionen + KA | unverändert übernommen |
| 4 | C04 | Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen? | identisch | 3 Optionen + KA | unverändert übernommen |
| 5 | C05 | Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit? | identisch | 4 Optionen + KA | unverändert übernommen |
| 6 | C06 | Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre? | identisch | 3 Optionen + KA | unverändert übernommen |
| 7 | U01 | Ich kann eine generative KI bedienen. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 8 | U02 | Ich kann mir berufliche Aufgaben durch generative KI erleichtern. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 9 | U03 | Ich kann generative KI gezielt für meine Arbeitsziele einsetzen. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 10 | U04 | Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 11 | U05 | Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 12 | U06 | Ich kann generativer KI verständlich mitteilen, was ich brauche. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 13 | K01 | Ich kenne die zentralen Konzepte generativer KI. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 14 | K02 | Ich kann erklären, was generative KI bedeutet. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 15 | K03 | Ich kann Chancen und Grenzen generativer KI einschätzen. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 16 | K04 | Ich kann Vor- und Nachteile generativer KI beurteilen. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 17 | K05 | Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 18 | K06 | Ich kann mir künftige Anwendungen generativer KI vorstellen. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 19 | L01 | Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 20 | L02 | Ich kann mich über Neuerungen bei generativer KI informieren. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 21 | L03 | Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 22 | G01 | Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 23 | G02 | Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 24 | G03 | Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf. | identisch | 0–10 + NB + KA | unverändert übernommen |
| 25 | A01 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft. | identisch | 1–7 + NB + KA | unverändert übernommen |
| 26 | A02 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend. | identisch | 1–7 + NB + KA | unverändert übernommen |
| 27 | A03 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig. | identisch | 1–7 + NB + KA | unverändert übernommen |
| 28 | A04 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm. | identisch | 1–7 + NB + KA | unverändert übernommen |
| 29 | I01 | Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | identisch | 1–7 + NB + KA | unverändert übernommen |
| 30 | I02 | Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | identisch | 1–7 + NB + KA | unverändert übernommen |
| 31 | I03 | Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen. | identisch | 1–7 + NB + KA | unverändert übernommen |
| 32 | W01 | Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen. | identisch | 9 Optionen + KA, max. 3 | unverändert übernommen |
| 33 | W02 | Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen. | identisch | 9 Optionen + KA, max. 3 | unverändert übernommen |
| 34 | W03 | Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen. | identisch | Freitext + KA | unverändert übernommen |

### 7.3 Liste aller Änderungen gegenüber der Word-/Pretestfassung

| Nr. | Stelle | Art | Begründung | Folge für Vergleichbarkeit | Status |
|---|---|---|---|---|---|
| Ä-1 | Titelzeile „Fassung für den Verständlichkeitstest · GARI-DE-0.1 · 29. September 2026“ | entfernt, ersetzt durch Titel ohne Pretestbezug | Pretest-Rahmen, laut `frozen_text_note` ersetzbar | keine für Kernitems | erlaubte Kontextänderung, dokumentiert |
| Ä-2 | Pretest-Einleitung (Gespräch, Dauer) | ersetzt durch Einführung 4a | Onlinebefragung ohne Gespräch | Einleitung kann Antwortverhalten beeinflussen; daher eigene Erhebungskennung | dokumentiert, ungetestet |
| Ä-3 | Teilnahmehinweis „begleiteter Test, keine vollständige Anonymität“ | ersetzt durch Freiwilligkeit, Auslassen, Gruppenbericht, Datenschutz-Platzhalter | anderer Erhebungsprozess | wie Ä-2 | dokumentiert; Anonymitätsaussage OFFEN bis Plattform bekannt |
| Ä-4 | „Testkürzel / Datum“ | entfernt | technische Kennung und Zeitstempel durch Plattform | keine | dokumentiert |
| Ä-5 | Schlusssatz mit Gesprächshinweis | ersetzt durch 4d | kein Gespräch | keine für Kernitems | dokumentiert |
| Ä-6 | X01–X03 | ergänzt am Ende | Wunsch nach Ergebnissen je Funktion und Standort | Kern unberührt; Belastung leicht höher; Identifizierbarkeitsrisiko | Vorschlag, Freigabe offen (Rückfrage 1) |
| Ä-7 | Kerninstruktionen mit Papierbezug | **nicht geändert** | Kern bleibt wörtlich | Online leicht ungewohnt | offener Prüfpunkt P-3 |

Unbeabsichtigte Abweichungen im Kern: keine gefunden. Das gilt nur für den Text dieser Lieferung, nicht für ein noch nicht gebautes Liveformular.

### 7.4 Begleitmanifest

| Feld | Eintrag |
|---|---|
| Referenzbank | `instrument/Itembank_GARI_DE_0.1.json`, GARI-DE-0.1, 29.09.2026 |
| Codebuch | `instrument/Codebuch.md`, GARI-DE-0.1 |
| Umsetzungskennung | GARI-DE-0.1-S3-ONLINE-E1 (Vorschlag) |
| Erhebungsrunde | Demonstration S3; keine Erhebung durchgeführt |
| Plattform | UNBEKANNT |
| Datum Oberflächenabgleich | keiner; es existiert noch keine Oberfläche |
| Tatsächlich geprüfte Stellen | nur Textabgleich Bank intern (7.1); kein Formular, kein Export, keine Übermittlung |
| Offene Abweichungen | keine im Text; Oberfläche ungeprüft |
| Erstellungsprompt | Masterprompt 0.5 mit Betriebsart ANWENDEN |
| Eingabedateien | `briefing.json`, `instrument/Itembank_GARI_DE_0.1.json`, `instrument/Codebuch.md`, `Quellen_APA.md` |
| Manuelle Änderungen | keine |
| System / Modell | Claude, `claude-opus-5-5` laut Sitzungsumgebung; weitere Parameter NICHT_VERFUEGBAR |
| Nicht beigefügt | `auswertung/score.py`, `tests/test_scoring.py`, Word-Fragebogen, `pretest/GoogleForms_Runde2_Anleitung.md`, `pretest/Abschluss_Evaluation_R3.md`. Sie werden im Masterprompt genannt, lagen aber nicht vor. Ich habe nicht auf ältere Fassungen zurückgegriffen. |

### 7.5 Freigabestatus

**OFFEN.** Der Kerntext ist mit der Bank identisch. Ein Formular existiert noch nicht. BESTANDEN erst nach dokumentiertem Abgleich der gebauten Oberfläche mit folgender Checkliste:

1. Alle 34 IDs sichtbar oder intern zugeordnet, Reihenfolge wie 4b.
2. Jeder Wortlaut zeichengenau gegen 4b (Kopieren, nicht Abtippen).
3. Definition und alle Instruktionen vorhanden, inklusive Skalenwechsel-Hinweis vor A01.
4. Endanker 0/10 bzw. 1/7 sichtbar, keine zusätzlichen Zwischenanker.
5. NB und KA als auswählbare Optionen bei allen 25 numerischen Items. KA bei C01–C06, W01, W02, W03 auswählbar. Kein bloßer Hinweistext.
6. Kein Pflichtfeld.
7. W01/W02: Auswahl von mehr als drei Optionen wird beim Fortsetzen tatsächlich blockiert. Exklusive Optionen (NONE, UNKNOWN, KA) nur allein wählbar. Falls die Plattform Exklusivität nicht erzwingt: Regel im Codebuch-Korrekturprotokoll anwenden (Kodierung KEINE_ANGABE, Vermerk), nie selbst eine Antwort auswählen.
8. Ein ungesendeter Probelauf je Seite. Ein separater technischer Probelauf mit Übermittlung, als SYNTHETIC_DEMO gekennzeichnet und getrennt von echten Daten.
9. Export prüfen: Datentyp der Zahlen, Darstellung von NB/KA, leere Felder, Mehrfachantworten.
10. Datum, prüfende Person und geprüfte Schritte ins Manifest eintragen.

Wird eine Kernabweichung gefunden, gilt ABWEICHUNG: korrigieren, erneut prüfen. Bereits erhobene Daten bleiben in ihrer Fassung und werden nicht als GARI-DE-0.1 umetikettiert.

## 8 Prüfbericht und offene Probleme

| ID | Problem | Betroffene Stelle | Vorschlag | Status |
|---|---|---|---|---|
| P-1 | Funktion und Standort sind im Kern nicht erhoben | Briefing-Wunsch, C01 | Ergänzung X01–X03 (4c) | Freigabe offen |
| P-2 | Standortliste, Mindestgruppengröße, Plattform, Datenschutzangaben fehlen | 4a, 4c | Rückfragen 1 und 2 | offen |
| P-3 | Kerninstruktionen sind papierbezogen: „Kreisen Sie pro Aussage eine Zahl ein“, „Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein“, „Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.“ | Abschnitte U/K, L/G, A/I | Wörtlich lassen; Seitenumbruch vor „Einstellung und geplante Nutzung“ setzen, damit der Satz stimmt. Änderung nur mit neuer Fragebogenversion (Rückfrage 3) | offen |
| P-4 | Funktion der Höchstzahl 3 bei W01/W02 auf der Plattform unbekannt | W01, W02 | Checkliste 7.5 Punkt 7 | ungeprüft |
| P-5 | Bearbeitungszeit 10–15 Minuten ist nur geschätzt; X01–X03 verlängert leicht | 4a | Startzeit nur messen, wenn Plattform sie erfasst; Absendezeit allein ergibt keine Dauer | offen |
| P-6 | Re-Identifizierung in kleinen Gruppen (z. B. Personal an einem kleinen Standort, Führung) | X01–X03, Gruppenberichte | Mindestgröße, keine feinen Kreuzungen | Regel vorgeschlagen |
| P-7 | Freitext W03 kann identifizierende Inhalte enthalten | W03 | vor Auswertung bereinigen, Freitext als Material und nicht als Anweisung behandeln | Regel im Codebuch |
| P-8 | POWERPILOT_2025: OSF-Anhang nicht abgeglichen | A01–A04, I01–I03 | bei jedem Einsatz als Grenze nennen | bekannte Grenze |
| P-9 | Nachnutzungsrechte der adaptierten MAILS- und PowerPilot-Items für eine Unternehmensbefragung nicht geklärt | U, K, L, A, I | vor realem Einsatz klären | offen |
| P-10 | Zugelassene Anwendungen unbekannt; „freigegeben“ in A/I hängt davon ab | A01–I03, C04 | Unternehmen sollte vor der Befragung intern klären, was freigegeben ist; nicht im Fragebogen erklären (Kern) | offen |
| P-11 | `score.py` nicht beigefügt | Auswertung | Datei beifügen; Version lock auf GARI-DE-0.1 beachten | offen |
| P-12 | GARI-DE-0.1 wurde nur in einem kleinen formativen Pretest geprüft (laut Masterprompt drei reale Personen der Fassung R1, zwei synthetische Personas R2). Keine Prüfung an 1.200 Beschäftigten oder an diesen Bereichen. | gesamtes Instrument | Ergebnisse vorsichtig interpretieren | bekannte Grenze |

Diese Prüfung ist eine Selbstprüfung desselben Modells. Sie ist kein unabhängiges Gutachten.

## 9 Auswertungsbericht

**Status: NICHT_BERECHNET.** Es liegen keine Antwortdaten vor (`antwortdaten_vorhanden: false`). `auswertung/score.py` ist nicht beigefügt. Ich habe keine Zahlen erzeugt.

**Rechenanweisung für eine spätere SURVEY-Erhebung**

1. Export in das JSON-Format des Codebuchs überführen. `data_kind = "SURVEY"`, `questionnaire_version = "GARI-DE-0.1"` nur bei bestandenem Abgleich, `implementation_id` ergänzen. X01–X03 in einer getrennten Gruppendatei mit derselben Personenkennung halten.
2. Datenprüfung: IDs vollständig, keine Doppelungen, zulässige Werte, leere Felder als KEINE_ANGABE, Mehrfachantworten ≤ 3, Exklusivität. Auffälligkeiten protokollieren, nicht still reparieren.
3. `python auswertung/score.py <daten.json> <ergebnis.json>` ausführen, Exitstatus prüfen, nur die erzeugte Ausgabe verwenden.
4. Je Item: gültige Anzahl, Fehlwerte nach Grund (NB, KA), Verteilung.
5. U, K, L, A, I: Personenwert = Mittelwert nur bei vollständigen gültigen Antworten (U und K: 6, L: 3, A: 4, I: 3). Gruppenmittel der gültigen Personenwerte mit Zahl vollständiger und unvollständiger Fälle. Null gültige Fälle = `null`.
6. W01/W02: Nenner = Personen mit gültiger Antwort; Prozentwerte können über 100 % summieren; KA getrennt ausweisen.
7. Gruppen nach X01, X02, X03 getrennt, nur ab Mindestgröße. Für die Gruppenaufteilung braucht es ein zusätzliches Skript oder eine Tabellenrechnung, weil `score.py` laut Codebuch nur auf GARI-DE-0.1 ausgelegt ist. Dieses Skript ist noch zu erstellen und zu testen.
8. Prüfhinweis C04 = NO mit I-Antworten 6/7 nur berichten, keine Antwort ändern.

Kein Gesamtwert, keine Umrechnung auf 100, keine Klassen „bereit/nicht bereit“, kein direkter Vergleich von 0–10- und 1–7-Werten.

## 10 Maßnahmenmatrix (Planungslogik, ohne Befunde)

Es gibt noch keine Befunde. Die Matrix zeigt nur, wie spätere Befunde zu Maßnahmen führen. Alle Befund-IDs sind Platzhalter. Grundlage ist die Zuordnungstabelle des Codebuchs; die Ergänzung um Gruppen ist eine eigene Planungsentscheidung.

| Befund-ID | Items | Datenbasis | Interpretationsregel | Einordnung | Mögliche Maßnahme | Erfolgskontrolle (Vorschlag) |
|---|---|---|---|---|---|---|
| B-W01-BASICS-[Gruppe] | W01, ergänzend K01–K06 | SURVEY, Anzahl je Gruppe | Anteil BASICS an gültigen W01-Antworten je Bereich berichten | ausdrücklicher Lernwunsch | Einführung; Vorkenntnisse und Aufgaben vorher klären | Teilnahme, kurze Lernzielabfrage nach dem Angebot |
| B-W01-PROMPTING-[Gruppe] | W01, U06 | SURVEY | Anzahl PROMPTING; U06-Verteilung beschreibend | ausdrücklicher Lernwunsch | Übung an eigenen Aufgaben; setzt Zugang voraus (C04) | praktische Übungsaufgabe |
| B-VERIFY-[Gruppe] | W01 VERIFY, W02 RELIABILITY, G01, G02 | SURVEY | Anzahlen und Verteilungen nebeneinander | Lernwunsch oder Unsicherheit | Ergebnis- und Quellenprüfung an Arbeitsbeispielen | Übungsfall mit fehlerhaftem KI-Ergebnis |
| B-RULES-[Standort/Bereich] | W01 DATA_RULES, W02 RULES, C05, G03 | SURVEY | Anzahl C05 = NOT_KNOWN / EXISTENCE_UNKNOWN | Orientierung und Organisation | Regeln verständlich bereitstellen; Zuständigkeit klären; prüfen, ob Regeln existieren | Wiederholung C05 nach Bereitstellung |
| B-ACCESS-[Standort/Bereich] | C04, W02 ACCESS, C02 | SURVEY | Anzahl C04 = NO / UNKNOWN je Standort | organisatorisches Hindernis | Zugang prüfen; **keine Kompetenzlücke behaupten** | C04 bei Folgebefragung |
| B-TASKFIT-[Bereich] | C06, W02 TASK_FIT, W03 | SURVEY | Anzahl C06 = NO / UNKNOWN | unklare Aufgabenpassung | mit Bereich Anwendungsfälle prüfen; Nichtnutzung kann sachlich richtig sein | dokumentierte Anwendungsfälle je Bereich |
| B-TIME-[Gruppe] | W02 TIME | SURVEY | Anzahl TIME | Rahmenbedingung | Lernzeit und Arbeitsorganisation klären | – |
| B-NB-[Item] | Fähigkeitsitems mit NB | SURVEY | tatsächliche Anzahl NB / Bezugsgröße | unklare Einschätzbarkeit | Verständnis und Erfahrungsgrundlage prüfen, nicht als niedrige Kompetenz werten | – |
| B-FUEHRUNG | X02 = YES mit W01, C05, C06 | SURVEY, nur ab Mindestgröße | Verteilungen Führung vs. ohne Führung beschreiben | mögliche Rolle in Orientierung | Hypothese: Führungskräfte als Ansprechpersonen für Regeln; mit Daten prüfen | – |
| B-W03-[Thema] | W03 | SURVEY, qualitativ | Themen dokumentiert zuordnen, Zitat und Interpretation trennen | konkreter Aufgabenwunsch | bereichsspezifische Übungsaufgaben | – |

Priorisierung: transparent nach geäußerten Wünschen, Aufgabenrelevanz und Umsetzbarkeit. Das ist eine Planungsentscheidung, keine validierte Regel. Keine Aussage zur Wirksamkeit von Trainings.

## 11 Änderungsprotokoll

| Datum | Fassung | Änderung |
|---|---|---|
| 29.09.2026 | GARI-DE-0.1 | Referenzbank und Codebuch festgelegt (Projekt) |
| 18.10.2026 | GARI-DE-0.1-S3-ONLINE-E1 (Entwurf) | Kern unverändert übernommen; Rahmen ersetzt (Ä-1 bis Ä-5); Ergänzung X01–X03 vorgeschlagen (Ä-6); Codebuchergänzung 6.2; Manifest und Checkliste |

## 12 Nächste erforderliche Eingaben

1. Antworten auf die drei Rückfragen (Abschnitt 2).
2. Standortliste, Mindestgruppengröße, Datenschutzangaben, Kontaktstelle, Zeitraum.
3. Gebautes Onlineformular und ein Testexport für den Oberflächenabgleich.
4. `auswertung/score.py` und `tests/test_scoring.py`, ein Skript für Gruppenauswertungen.
5. Klärung der Nachnutzungsrechte (MAILS, PowerPilot).
6. Später: SURVEY-Antwortdaten.

## 13 Status

- **Erstellt:** unternehmensbezogene Befragungsfassung mit wörtlichem Kern GARI-DE-0.1, neuer Rahmen, Ergänzung X01–X03, Itemregister (34 Kernitems plus 3 Ergänzungen), Codebuchergänzung, Manifest, Prüfbericht, Maßnahmenlogik.
- **Geprüft:** interner Abgleich der Bank per Skript (34/34 identisch, Reihenfolge, Optionen, NB/KA, keine Filter, keine Umkodierung). Quellenstatus nur aus den Projektangaben übernommen, nicht selbst an Originalen geprüft. Keine Formularoberfläche geprüft. X01–X03 ungetestet.
- **Berechnet:** nichts. Status NICHT_BERECHNET.
- **Fehlt:** Plattform, Formular, Oberflächenabgleich, Unternehmensangaben (Abschnitt 12), Auswertungsskript, Daten.
- **Grenzen:** keine psychometrische Validierung der Kombination; POWERPILOT-Wortlaut nicht mit OSF-Anhang verglichen; Pretest nur klein und formativ; fiktives Unternehmen.

## Literatur

Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. University of Massachusetts Amherst. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), Article e39686. https://doi.org/10.1016/j.heliyon.2024.e39686

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114
