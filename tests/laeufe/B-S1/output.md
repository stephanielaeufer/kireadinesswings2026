# Fragebogen zur Readiness für generative KI bei Mitarbeitenden

Szenario S1 · Fiktiver Dienstleistungsbetrieb mit 40 Beschäftigten · Betriebsart ANWENDEN · Stand 18. Oktober 2026

Kontext: fiktive Verfahrensdemonstration laut Briefing. Es gibt keine realen Daten. Es liegen keine Befragungsdaten vor. Dieses Dokument enthält deshalb keine Ergebnisse, keine Kennwerte und keine Maßnahmenentscheidungen. Es enthält das Instrument und die Regeln, nach denen später ausgewertet wird.

## Überblick

Geliefert werden folgende Teile:

1. **Fragebogen** in der Erhebungsfassung für das Onlineformular. Fester Kern GARI-DE-0.1 (34 Items) unverändert, danach ein getrennt gekennzeichnetes Kontextmodul S1 (5 Items).
2. **Quellenzuordnung** je Item und je Quelle, mit Quellengrenzen.
3. **Codebuch** für Kern und Kontextmodul, mit Datenformat und Fehlwertregeln.
4. **Auswertungsplan** vom Datenexport bis zum Bericht.
5. **Plan zur Ableitung von Maßnahmen** mit Zuordnungstabelle und Vorlage je Empfehlung.
6. **Offene Rückfragen** und Entscheidungen, die vor dem Feldstart nötig sind.

### Leitentscheidungen

- **Der Kern bleibt unverändert.** Definition, Itemwortlaut, Antwortformate, Reihenfolge, Zeitbezüge und Kerninstruktionen werden aus der Itembank GARI-DE-0.1 übernommen. Die Itembank erlaubt nur Kontaktangaben und einen organisatorischen Erhebungshinweis außerhalb des Fragebogens. Die pretestbezogene Einleitung wird laut `frozen_text_note` durch eine gesondert dokumentierte Erhebungseinleitung ersetzt.
- **Kontextfragen kommen ans Ende.** Sie stehen nach W03 und vor dem Schlusstext. So verändern sie weder Reihenfolge noch Kontext der Kernitems. Sie bekommen eigene IDs (X01–X05) und eine eigene Version (KM-S1-0.1).
- **Kontextdaten werden getrennt gespeichert.** Die Rechenroutine für GARI-DE-0.1 stoppt bei unbekannten IDs. Deshalb gehen Kernantworten und Kontextantworten in zwei Dateien, verbunden über denselben zufälligen Antwortcode.
- **Betriebliche Voraussetzungen werden gesondert erfasst.** Das Briefing verlangt das ausdrücklich. Dafür gibt es zusätzlich einen kurzen Betriebsbogen (B01–B07), den die Geschäftsführung oder eine benannte Stelle ausfüllt. Er ist nicht Teil der Mitarbeitendenbefragung.
- **Keine Readiness-Klasse.** Es gibt keinen Gesamtscore, keine Umrechnung auf 100, keine Gewichtung und keine Einstufung in „bereit“ oder „nicht bereit“. Das folgt dem Codebuch.
- **Selbstbericht bleibt Selbstbericht.** Alle Fähigkeitsitems messen Selbsteinschätzungen. Sie sind keine Leistungstests und keine Grundlage für Aussagen über einzelne Beschäftigte.

### Warum diese Kontextfragen

| ID | Inhalt | Zweck aus dem Briefing | Warum nicht schon im Kern abgedeckt |
|---|---|---|---|
| X01 | Tätigkeitsbereich | Briefing nennt drei Bereiche: Verwaltung, Kundenkontakt, Operative Tätigkeit | C01 fragt nach Büro- gegenüber anderer Arbeit, nicht nach dem Bereich |
| X02 | Zugang zu einem Computerarbeitsplatz | Das freigegebene Chat-Werkzeug ist für Büroarbeitsplätze vorgesehen | C04 fragt nach Zugang zu GenAI, nicht nach dem technischen Arbeitsplatz |
| X03 | Kenntnis und Nutzung des freigegebenen Chat-Werkzeugs | Ein freigegebenes Werkzeug existiert; bisherige Nutzung ist unbekannt | C02 und C04 nennen kein konkretes Werkzeug |
| X04 | Ansprechperson bei Fragen | Betriebliche Voraussetzungen, Unterstützung | C05 fragt nach Regeln, nicht nach Unterstützung |
| X05 | Bevorzugte Lernform | Hinweise auf Weiterbildungsbedarf in umsetzbare Formate übersetzen | W01 fragt nach Themen, nicht nach Formaten |

Bewusst nicht ergänzt: Alter, Geschlecht, Betriebszugehörigkeit, Führungsfunktion. Bei 40 Beschäftigten erhöhen solche Merkmale das Risiko, Personen zu erkennen. Für den Zweck des Briefings werden sie nicht gebraucht. Ebenfalls nicht ergänzt: Vertrauen in GenAI. Die bereitgestellte Vertrauensstudie (Do Khac et al., 2025) betrifft Entscheidungstragende, nicht die gesamte Belegschaft.

---

## 1 Fragebogen (Erhebungsfassung Onlineformular)

Erhebungsfassung: **GARI-DE-0.1 (Kern, unverändert) + Kontextmodul KM-S1-0.1 + Erhebungseinleitung S1-Online-0.1**

### Startseite (Erhebungseinleitung, ersetzt die Pretest-Einleitung)

Die folgenden Absätze ersetzen nur die organisatorischen Pretest-Absätze (Gespräch, Testkürzel, begleiteter Test). Titel und Definition sind unverändert übernommen. Angaben in eckigen Klammern trägt der Betrieb vor dem Versand ein.

**Fragebogen zum Umgang mit generativer KI**

Dieser Fragebogen erfasst Ihre Erfahrungen, Einschätzungen und Weiterbildungswünsche zu generativer KI bei der Arbeit. Es geht nicht um die Bewertung Ihrer Arbeitsleistung. Die Ergebnisse helfen, passende Unterstützung und Weiterbildung zu planen. Geschätzte Dauer: 10 bis 15 Minuten für den Hauptteil und etwa 2 Minuten für fünf Zusatzfragen am Ende. Die Dauer ist noch nicht gemessen.

Generative KI erzeugt oder bearbeitet auf Eingaben hin Inhalte, zum Beispiel Texte, Bilder, Audio, Videos oder Programmcode. Gemeint sind sowohl eigenständige Anwendungen als auch entsprechende Funktionen in anderen Programmen.

Die Teilnahme ist freiwillig. Sie können einzelne Fragen auslassen oder den Fragebogen jederzeit beenden. Es gibt keine richtigen oder falschen Antworten. Bitte tragen Sie keine Namen, Personalnummern oder vertraulichen Informationen ein.

Das Formular fragt nicht nach Ihrem Namen. Ergebnisse werden nur zusammengefasst berichtet. Gruppen mit weniger als [Mindestgröße, siehe Rückfrage R1] Antworten werden nicht getrennt ausgewiesen. Bei einem kleinen Betrieb kann eine vollständige Anonymität trotzdem nicht garantiert werden. Auswertung durch: [Stelle]. Zugriff auf Einzelantworten haben nur: [Personen oder Stelle]. Löschung der Einzelantworten: [Datum]. Fragen zur Befragung: [Kontaktperson, E-Mail].

Befragungszeitraum: [Startdatum] bis [Enddatum].

**Bitte beachten:** Kein Feld ist ein Pflichtfeld. Ein leer gelassenes Feld zählt als „keine Angabe“.

### Hinweise zur Umsetzung im Onlineformular

- Seitenaufbau: Startseite, dann je ein Formularabschnitt pro Teil 1 bis 6, dann Schlussseite. Der Hinweis „Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.“ steht am Ende von Teil 3 und passt zu diesem Seitenwechsel.
- Einzelwahlfragen als Optionsfelder. „Keine Angabe“ als eigene Option, kein Pflichtfeld.
- 0–10-Items und 1–7-Items als Optionsfeld-Raster oder einzelne Optionsfragen mit den Optionen 0 bis 10 (bzw. 1 bis 7), „NB“ und „KA“. Keine Schieberegler, weil diese einen Startwert vorgeben und „NB“ nicht abbilden. Nur Endanker beschriften, keine Zwischenanker.
- W01 und W02 als Kästchenfragen mit der Regel „höchstens 3“, X05 mit „höchstens 2“. Die exklusiven Optionen lassen sich in üblichen Formularwerkzeugen technisch nicht erzwingen. Der Hinweistext bleibt deshalb stehen, und Verstöße werden bei der Datenaufbereitung nach Codebuch behandelt. Die Höchstzahl-Regel vor dem Start mit einem Testdurchlauf prüfen, auch über einen Seitenwechsel hinweg. Im Projekt wurde bei einem bereitgestellten Formular eine Fehlfunktion beim Seitenwechsel festgestellt.
- Keine Sprungregeln. Alle Personen sehen alle Fragen.
- Keine Erfassung von E-Mail-Adresse, Anmeldenamen oder IP-Adresse aktivieren. Keine Pflichtanmeldung.
- Die Kerninstruktion „Kreisen Sie pro Aussage eine Zahl ein“ stammt aus der Papierfassung. Sie wird hier unverändert übernommen, weil Kerninstruktionen nicht ohne neue Version geändert werden dürfen. Siehe Rückfrage R4.

### Kern GARI-DE-0.1 (unverändert)

Die folgenden Teile 1 bis 5 entsprechen wortgleich dem festgehaltenen Fragebogentext der Itembank GARI-DE-0.1, einschließlich aller Instruktionen.

#### Teil 1: Ihre Tätigkeit und bisherige Nutzung

Bitte wählen Sie pro Frage genau eine Antwort.

**C01**  Wie sieht Ihre hauptsächliche Tätigkeit aus?

□ Überwiegend Büro- oder Bildschirmarbeit  
□ Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst  
□ Etwa gleich große Anteile beider Bereiche  
□ Keine Angabe

**C02**  An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt?

□ An keinem Tag  
□ An 1 bis 3 Tagen  
□ An 4 bis 9 Tagen  
□ An 10 bis 15 Tagen  
□ An 16 oder mehr Tagen  
□ Kann ich nicht einschätzen  
□ Keine Angabe

**C03**  Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt?

□ Ja  
□ Nein  
□ Ich bin mir nicht sicher  
□ Keine Angabe

**C04**  Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen?

□ Ja  
□ Nein  
□ Ich weiß es nicht  
□ Keine Angabe

**C05**  Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit?

□ Ja  
□ Teilweise  
□ Nein  
□ Ich weiß nicht, ob es solche Regeln gibt  
□ Keine Angabe

**C06**  Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre?

□ Ja  
□ Nein  
□ Kann ich noch nicht beurteilen  
□ Keine Angabe

#### Teil 2: Anwendung und Verständnis

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

#### Teil 3: Lernen und Prüfen

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

#### Teil 4: Einstellung und geplante Nutzung

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

#### Teil 5: Weiterbildung und Unterstützung

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

### Kontextmodul KM-S1-0.1 (neu, betriebsspezifisch)

#### Teil 6: Ihr Arbeitsumfeld

Zum Schluss folgen fünf Fragen zu Ihrem Arbeitsumfeld. Sie helfen, Unterstützung passend zu planen.

**X01**  In welchem Bereich arbeiten Sie überwiegend?

□ Verwaltung  
□ Kundenkontakt  
□ Operative Tätigkeit  
□ In mehreren Bereichen etwa gleich viel  
□ Keine Angabe

**X02**  Haben Sie bei Ihrer Arbeit regelmäßig Zugang zu einem Computerarbeitsplatz?

□ Ja, ich habe einen eigenen oder fest zugeteilten Computerarbeitsplatz  
□ Ja, ich nutze einen gemeinsam genutzten Computerarbeitsplatz  
□ Nein  
□ Keine Angabe

**X03**  Im Betrieb ist für Büroarbeitsplätze ein Chat-Werkzeug mit generativer KI freigegeben. Welche Aussage trifft auf Sie zu?

□ Ich nutze dieses Werkzeug bereits für meine Arbeit  
□ Ich kenne es, nutze es aber nicht  
□ Ich wusste nicht, dass es ein solches Werkzeug gibt  
□ Ich bin mir nicht sicher, welches Werkzeug gemeint ist  
□ Keine Angabe

**X04**  Wissen Sie, an wen Sie sich im Betrieb mit Fragen zu generativer KI wenden können?

□ Ja  
□ Nein  
□ Ich bin mir nicht sicher  
□ Keine Angabe

**X05**  Wie würden Sie am liebsten zu generativer KI lernen? Bitte höchstens zwei Antworten auswählen.

□ Kurze Schulung in der Gruppe  
□ Begleitetes Üben an eigenen Arbeitsaufgaben  
□ Kurze schriftliche Anleitung oder Video zum Selbstlernen  
□ Austausch mit Kolleginnen und Kollegen, die das Werkzeug schon nutzen  
□ Derzeit kein Lernbedarf  
□ Keine Angabe

„Derzeit kein Lernbedarf“ und „Keine Angabe“ bitte nur allein auswählen.

### Schlussseite (ersetzt den pretestbezogenen Schlusstext)

Vielen Dank für Ihre Teilnahme. Ihre Antworten sind gespeichert. Bei Fragen zur Befragung wenden Sie sich an [Kontaktperson].

### Betriebsbogen zu den betrieblichen Voraussetzungen (gesondert, nicht Teil der Mitarbeitendenbefragung)

Ausfüllen durch Geschäftsführung oder benannte Stelle, einmal vor Feldstart. Zweck: Antworten der Beschäftigten (zum Beispiel C04, C05, X03, X04) mit dem tatsächlichen Stand vergleichen. Ohne diesen Abgleich lässt sich nicht unterscheiden, ob eine Antwort „Ich weiß nicht, ob es Regeln gibt“ auf fehlende Regeln oder auf fehlende Information zurückgeht.

| ID | Frage | Antwortformat |
|---|---|---|
| B01 | Welches GenAI-Werkzeug ist für die Arbeit freigegeben? Seit wann? | Freitext: Name, Datum |
| B02 | Für welche Arbeitsplätze oder Bereiche gilt die Freigabe? | Verwaltung / Kundenkontakt / Operative Tätigkeit / nur Büroarbeitsplätze / alle; Anmerkung |
| B03 | Wie viele Beschäftigte haben technisch Zugang (Konto oder Arbeitsplatz)? | Zahl; „unbekannt“ |
| B04 | Gibt es schriftliche Regeln zur Nutzung (zum Beispiel zulässige Daten, Prüfpflichten)? | ja, schriftlich / mündlich vereinbart / in Arbeit / nein |
| B05 | Wie wurden die Regeln bekannt gemacht und wo sind sie zu finden? | Freitext |
| B06 | Gibt es eine benannte Ansprechperson oder Stelle für Fragen? | ja (Funktion nennen) / nein |
| B07 | Welche Lernzeit und welches Budget stehen für Weiterbildung zu GenAI in den nächsten sechs Monaten zur Verfügung? | Stunden je Person; Betrag; „noch offen“ |

Der Betriebsbogen ist eine Sachstandserfassung. Er wird nicht gescort und nicht mit den Personenwerten verrechnet.

---

## 2 Quellenzuordnung

### 2.1 Quellen und ihre Rolle

| Quellen-ID | Quelle (APA) | Rolle in diesem Fragebogen | Grenze |
|---|---|---|---|
| MAILS_DE_2023 | Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014 ; deutscher Autorenfragebogen, Items 1–6, 7–12, 26–28, Auswertungszuordnung S. 3 | Vorlage für U01–U06, K01–K06, L01–L03 und für die Mittelwertregel je Teilbereich | Evidenz gilt für allgemeine KI, Selbstbericht, 300 deutschsprachige Erwachsene. Die Anpassung auf generative KI und Arbeit ist nicht validiert. Rechte für öffentliche veränderte Itemtexte noch zu klären. |
| (ergänzend) | Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), Article e39686. https://doi.org/10.1016/j.heliyon.2024.e39686 | Einordnung der Validitätsevidenz | Kurzfassung enthält KI-Entwicklung, passt nur teilweise, wird nicht eingesetzt |
| POWERPILOT_2025 | Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114 | Vorlage für A01–A04 (Einstellung) und I01–I03 (Nutzungsabsicht), siebenstufiges Zustimmungsformat | Wortlaut aus bereitgestellter Itemsammlung; OSF-Anhang nicht abrufbar, direkter Wortlautvergleich offen. Energiekontext auf GenAI übertragen, nicht validiert. |
| Ajzen (o. J.) | Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. University of Massachusetts Amherst. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf | Begründung der Verhaltensdefinition nach Ziel, Handlung, Kontext und Zeit in A und I: freigegebene GenAI, berufliche Aufgaben, nächste drei Monate | Methodische Anleitung, keine Itemvorlage |
| Boateng et al. (2018) | Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149 | Begründung, warum Kontextitems vor dem Einsatz getestet werden und warum keine Messqualität behauptet wird | Kein Ersatz für eine Validierungsstudie |
| NCHS (2024) | National Center for Health Statistics. (2024, April 16). *Cognitive interviewing*. Centers for Disease Control and Prevention. https://www.cdc.gov/nchs/ccqder/question-evaluation/cognitive-interviewing.html | Methode für den Kurztest der neuen Kontextitems | Keine Regel für eine ausreichende Fallzahl |
| Paetow et al. (2026) | Paetow, T., Wichmann, J., & Leyer, M. (2026). Task-technology fit in virtual reality. In *Proceedings of the 59th HICSS* (pp. 319–328). https://hdl.handle.net/10125/111430 | Theoretischer Hintergrund für die Unterscheidung von Aufgabenpassung (C06, W02 = TASK_FIT) und Kompetenz | Keine Itemübernahme; Übertragbarkeit auf GenAI nicht geprüft |
| Do Khac et al. (2025) | Do Khac, L. T., Leyer, M., Wichmann, J., & Richter, A. (2025). Divisional perspectives on trust in generative AI. *Enterprise Information Systems*. Advance online publication. https://doi.org/10.1080/17517575.2025.2481557 | Begründung, warum kein Vertrauensmodul ergänzt wird | Zielgruppe Entscheidungstragende, nicht die Belegschaft |
| Eigenentwicklung | Projektinterne Entwicklung GARI-DE-0.1 bzw. KM-S1-0.1 | C01–C06, G01–G03, W01–W03, X01–X05, B01–B07 | Keine Originalitems, noch nicht empirisch geprüft |

Nicht verwendet: Wichmann, Gesk & Leyer (2024, Gesundheitskontext) und Wichmann, Gesk & Leyer (2026, virtuelle Meetings). Ihre Konstrukte passen nicht direkt zum Zweck. Peffers et al. (2007), Venable et al. (2016) und Bisbee et al. (2024) betreffen Entwicklungsmethode und Evaluation, nicht den Fragebogeninhalt.

### 2.2 Zuordnung je Item: fester Kern

Angaben aus der Itembank GARI-DE-0.1. Die Spalte „Fundstelle“ verweist bei adaptierten Items auf den Originalwortlaut. Der MAILS-Originalwortlaut wird hier nicht abgedruckt, weil die Itembank ihn nur über die Fundstelle referenziert.

| ID | Wortlaut im Fragebogen | Status | Quelle | Fundstelle | Anpassung laut Itembank | Quellengrenze |
|---|---|---|---|---|---|---|
| C01 | Wie sieht Ihre hauptsächliche Tätigkeit aus? | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| C02 | An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt? | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| C03 | Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt? | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| C04 | Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen? | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| C05 | Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit? | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| C06 | Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre? | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| U01 | Ich kann eine generative KI bedienen. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 1, Seite 1; Zuordnung und Mittelwertregel Seite 3. | KI-Bezug auf generative KI eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| U02 | Ich kann mir berufliche Aufgaben durch generative KI erleichtern. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 2, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Erleichterung des Lebens auf berufliche Aufgaben eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| U03 | Ich kann generative KI gezielt für meine Arbeitsziele einsetzen. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 3, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Zielbezug auf Arbeitsziele eingegrenzt; sinnvoll durch gezielt konkretisiert. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| U04 | Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 4, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Alltagsinteraktion auf Zusammenarbeit bei der Arbeit übertragen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| U05 | Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 5, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gewinnbringende Zusammenarbeit über brauchbare Arbeitsergebnisse konkretisiert; Bedeutungsverschiebung im Pretest prüfen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| U06 | Ich kann generativer KI verständlich mitteilen, was ich brauche. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 6, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gewinnbringende Kommunikation über verständliches Mitteilen konkretisiert; Ergebnisaspekt verengt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| K01 | Ich kenne die zentralen Konzepte generativer KI. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 7, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Allgemeine KI auf generative KI eingegrenzt; Konzepte bleibt bewusst zur Verständlichkeitsprüfung erhalten. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| K02 | Ich kann erklären, was generative KI bedeutet. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 8, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Kenntnis von Definitionen in selbst eingeschätzte Erklärfähigkeit übertragen; stärkere Anpassung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| K03 | Ich kann Chancen und Grenzen generativer KI einschätzen. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 9, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| K04 | Ich kann Vor- und Nachteile generativer KI beurteilen. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 10, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| K05 | Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 11, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Verwendungszwecke sprachlich vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| K06 | Ich kann mir künftige Anwendungen generativer KI vorstellen. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 12, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz verkürzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| L01 | Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 26, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; stets entfällt. Deutsche Itemnummer 26 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| L02 | Ich kann mich über Neuerungen bei generativer KI informieren. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 27, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; deutsche Itemnummer 27 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| L03 | Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten. | ADAPTIERT | MAILS_DE_2023 | Deutscher Autorenfragebogen, Item 28, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; sprachliche Verdichtung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut geprüft (Itembank) |
| G01 | Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss. | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| G02 | Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen. | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| G03 | Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf. | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| A01 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft. | ADAPTIERT | POWERPILOT_2025 | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| A02 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend. | ADAPTIERT | POWERPILOT_2025 | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| A03 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig. | ADAPTIERT | POWERPILOT_2025 | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| A04 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm. | ADAPTIERT | POWERPILOT_2025 | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 4; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| I01 | Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | ADAPTIERT | POWERPILOT_2025 | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| I02 | Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | ADAPTIERT | POWERPILOT_2025 | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| I03 | Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen. | ADAPTIERT | POWERPILOT_2025 | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| W01 | Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen. | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| W02 | Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen. | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |
| W03 | Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen. | NEU_ENTWICKELT | Eigenentwicklung | Kein Originalitem | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Wortlautabgleich möglich, da Eigenentwicklung |

### 2.3 Zuordnung je Item: Kontextmodul und Betriebsbogen

| ID | Status | Quelle | Begründung | Prüfstand |
|---|---|---|---|---|
| X01 | NEU_ENTWICKELT | Eigenentwicklung | Briefing: Tätigkeitsbereiche Verwaltung, Kundenkontakt, Operative Tätigkeit | Nicht getestet |
| X02 | NEU_ENTWICKELT | Eigenentwicklung | Briefing: Werkzeug für Büroarbeitsplätze; trennt technische von erlaubter Zugänglichkeit (C04) | Nicht getestet |
| X03 | NEU_ENTWICKELT | Eigenentwicklung | Briefing: ein freigegebenes Chat-Werkzeug; Nutzung unbekannt | Nicht getestet; Werkzeugname vor Versand einsetzen (R2) |
| X04 | NEU_ENTWICKELT | Eigenentwicklung | Briefing-Zweck: betriebliche Voraussetzungen gesondert erfassen | Nicht getestet |
| X05 | NEU_ENTWICKELT | Eigenentwicklung | Briefing-Zweck: Hinweise auf Weiterbildungsbedarf; Format der Maßnahme | Nicht getestet |
| B01–B07 | NEU_ENTWICKELT | Eigenentwicklung | Briefing-Zweck: betriebliche Voraussetzungen gesondert erfassen | Sachstandsbogen, keine Messung |

---

## 3 Codebuch

Gilt für Kern GARI-DE-0.1 (Regeln unverändert aus Codebuch GARI-DE-0.1) und Kontextmodul KM-S1-0.1 (neue Regeln, im gleichen Stil).

### 3.1 Allgemeine Regeln

- Alle Fragen werden allen Personen gezeigt. Keine Sprungregeln. Nichtnutzung in C02, C03 oder X03 erzeugt keinen Fehlwert und setzt Fähigkeitseinschätzungen nicht auf null.
- Skala 0–10: 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt. Skala 1–7: 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu. Keine Zwischenanker. Höhere Zahl = höhere Selbsteinschätzung bzw. Zustimmung. Keine umgepolten Items.
- Fehlwerte: `NICHT_BEURTEILBAR` (NB) nur bei numerischen Items. `KEINE_ANGABE` (KA) bei ausdrücklicher Wahl oder leerem Feld. Motive für fehlende Antworten werden nicht ergänzt.
- Unsicherheitsoptionen bei Einzelwahl (zum Beispiel `UNKNOWN`, `EXISTENCE_UNKNOWN`) sind reguläre Kategorien, werden mitgezählt und ausgewiesen.
- `NICHT_ZUTREFFEND` und `UEBERSPRUNGEN` gibt es in dieser Fassung nicht.
- Gültige 0-Antworten bleiben immer erhalten.
- Mehr als die erlaubte Zahl an Antworten oder widersprüchliche exklusive Antworten: im Korrekturprotokoll vermerken und als `KEINE_ANGABE` kodieren. Nie selbst eine Antwort auswählen.
- Abgebrochene Formulare: nur vorhandene Angaben übertragen, alle übrigen Items `KEINE_ANGABE`.

### 3.2 Variablen des Kerns

| ID | Typ und Bereich | Codes und Anker | Erlaubte Fehlwerte | Zusammenfassung |
|---|---|---|---|---|
| C01 | Einzelwahl | `OFFICE` = Überwiegend Büro- oder Bildschirmarbeit; `OTHER_WORK` = Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst; `MIXED` = Etwa gleich große Anteile beider Bereiche | `KEINE_ANGABE` | Einzelverteilung |
| C02 | Einzelwahl | `D0` = An keinem Tag; `D1_3` = An 1 bis 3 Tagen; `D4_9` = An 4 bis 9 Tagen; `D10_15` = An 10 bis 15 Tagen; `D16_PLUS` = An 16 oder mehr Tagen; `UNKNOWN` = Kann ich nicht einschätzen | `KEINE_ANGABE` | Einzelverteilung |
| C03 | Einzelwahl | `YES` = Ja; `NO` = Nein; `UNKNOWN` = Ich bin mir nicht sicher | `KEINE_ANGABE` | Einzelverteilung |
| C04 | Einzelwahl | `YES` = Ja; `NO` = Nein; `UNKNOWN` = Ich weiß es nicht | `KEINE_ANGABE` | Einzelverteilung |
| C05 | Einzelwahl | `KNOWN` = Ja; `PARTLY` = Teilweise; `NOT_KNOWN` = Nein; `EXISTENCE_UNKNOWN` = Ich weiß nicht, ob es solche Regeln gibt | `KEINE_ANGABE` | Einzelverteilung |
| C06 | Einzelwahl | `YES` = Ja; `NO` = Nein; `UNKNOWN` = Kann ich noch nicht beurteilen | `KEINE_ANGABE` | Einzelverteilung |
| U01 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich U ein |
| U02 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich U ein |
| U03 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich U ein |
| U04 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich U ein |
| U05 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich U ein |
| U06 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich U ein |
| K01 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich K ein |
| K02 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich K ein |
| K03 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich K ein |
| K04 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich K ein |
| K05 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich K ein |
| K06 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich K ein |
| L01 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich L ein |
| L02 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich L ein |
| L03 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich L ein |
| G01 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Einzelitem, kein Mittelwert |
| G02 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Einzelitem, kein Mittelwert |
| G03 | Ganzzahl 0–10 (ABILITY_0_10) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Einzelitem, kein Mittelwert |
| A01 | Ganzzahl 1–7 (AGREEMENT_1_7) | 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich A ein |
| A02 | Ganzzahl 1–7 (AGREEMENT_1_7) | 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich A ein |
| A03 | Ganzzahl 1–7 (AGREEMENT_1_7) | 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich A ein |
| A04 | Ganzzahl 1–7 (AGREEMENT_1_7) | 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich A ein |
| I01 | Ganzzahl 1–7 (AGREEMENT_1_7) | 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich I ein |
| I02 | Ganzzahl 1–7 (AGREEMENT_1_7) | 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich I ein |
| I03 | Ganzzahl 1–7 (AGREEMENT_1_7) | 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | geht in Teilbereich I ein |
| W01 | Mehrfachwahl, max. 3; exklusiv: NONE, UNKNOWN | `BASICS` = Grundlagen generativer KI; `USE_CASES` = Passende Einsatzmöglichkeiten für meine Aufgaben; `PROMPTING` = Klare Eingaben formulieren und Ergebnisse verbessern; `VERIFY` = Antworten und Quellen überprüfen; `DATA_RULES` = Betriebliche Regeln und zulässige Dateneingaben; `KEEP_CURRENT` = Bei neuen Entwicklungen auf dem Laufenden bleiben; `OTHER` = Anderes Thema; `NONE` = Derzeit kein Weiterbildungswunsch; `UNKNOWN` = Ich kann meinen Bedarf noch nicht einschätzen | `KEINE_ANGABE` | Häufigkeit je Option |
| W02 | Mehrfachwahl, max. 3; exklusiv: NONE, UNKNOWN | `ACCESS` = Kein Zugang zu einem freigegebenen Werkzeug; `RULES` = Unklare betriebliche Regeln; `TIME` = Zu wenig Zeit zum Ausprobieren oder Lernen; `KNOWLEDGE` = Mir fehlt Wissen über die Nutzung; `TASK_FIT` = Ich erkenne keinen passenden Einsatz für meine Aufgaben; `RELIABILITY` = Unsicherheit über die Verlässlichkeit der Ergebnisse; `OTHER` = Etwas anderes; `NONE` = Derzeit nichts; `UNKNOWN` = Kann ich noch nicht einschätzen | `KEINE_ANGABE` | Häufigkeit je Option |
| W03 | Freitext | Text | `KEINE_ANGABE` | qualitative Zuordnung |

### 3.3 Variablen des Kontextmoduls KM-S1-0.1

| ID | Typ | Codes | Erlaubte Fehlwerte | Zusammenfassung |
|---|---|---|---|---|
| X01 | Einzelwahl | `ADMIN` = Verwaltung; `CUSTOMER` = Kundenkontakt; `OPERATIONS` = Operative Tätigkeit; `MULTIPLE` = In mehreren Bereichen etwa gleich viel | `KEINE_ANGABE` | Einzelverteilung; Gruppierungsmerkmal nur ab Mindestgröße |
| X02 | Einzelwahl | `OWN` = eigener oder fest zugeteilter Computerarbeitsplatz; `SHARED` = gemeinsam genutzter Computerarbeitsplatz; `NO` = Nein | `KEINE_ANGABE` | Einzelverteilung |
| X03 | Einzelwahl | `USES` = nutzt das Werkzeug bereits; `KNOWS_NOT_USED` = kennt es, nutzt es nicht; `NOT_AWARE` = wusste nicht, dass es das Werkzeug gibt; `UNSURE_WHICH` = unsicher, welches Werkzeug gemeint ist | `KEINE_ANGABE` | Einzelverteilung; `NOT_AWARE` und `UNSURE_WHICH` sind reguläre Kategorien |
| X04 | Einzelwahl | `YES` = Ja; `NO` = Nein; `UNKNOWN` = Ich bin mir nicht sicher | `KEINE_ANGABE` | Einzelverteilung |
| X05 | Mehrfachwahl, max. 2; exklusiv: NONE | `GROUP` = Kurze Schulung in der Gruppe; `COACHED` = Begleitetes Üben an eigenen Aufgaben; `SELF` = Anleitung oder Video zum Selbstlernen; `PEER` = Austausch mit Kolleginnen und Kollegen; `NONE` = Derzeit kein Lernbedarf | `KEINE_ANGABE` | Häufigkeit je Option; Nenner = Personen mit gültiger Antwort |

Keine Kontextvariable geht in einen Mittelwert ein. Keine Kontextvariable verändert einen Kernwert.

### 3.4 Teilbereiche und Rechenregeln (aus Codebuch GARI-DE-0.1, unverändert)

| Teilbereich | Items | Regel | Bereich |
|---|---|---|---|
| U Selbst eingeschätzte Anwendung | U01–U06 | Mittelwert nur bei sechs gültigen Zahlen | 0–10 |
| K Selbst eingeschätztes Verständnis | K01–K06 | Mittelwert nur bei sechs gültigen Zahlen | 0–10 |
| L Zutrauen in das eigene Lernen | L01–L03 | Mittelwert nur bei drei gültigen Zahlen | 0–10 |
| A Einstellung zur Nutzung | A01–A04 | Vorläufiger Mittelwert nur bei vier gültigen Zahlen | 1–7 |
| I Berichtete Nutzungsabsicht | I01–I03 | Vorläufiger Mittelwert nur bei drei gültigen Zahlen | 1–7 |
| G Prüfen und zulässige Eingaben | G01, G02, G03 | Drei Einzelitems, **kein** G-Mittelwert | 0–10 |

- Ein Fehlwert (NB oder KA) in einem Teilbereich lässt den ganzen Personenwert fehlen. Keine Ersetzung. Das ist eine konservative Projektregel, keine MAILS-Vorschrift.
- Gruppenwert = Mittelwert der gültigen Personenwerte, immer mit Anzahl vollständiger und unvollständiger Fälle. Null gültige Fälle ergeben `null`, nicht 0.
- Einzelverteilungen sind die primäre Darstellung. Mittelwerte sind vorläufige deskriptive Projektwerte, keine validierten Skalen.
- Kein Gesamtscore, keine Umrechnung auf 100, keine Gewichtung, keine Klassifikation in „bereit“ oder „nicht bereit“. 0–10-Werte und 1–7-Werte nicht in einer Rangliste vergleichen.
- Mehrfachwahl: Nenner = Personen mit gültiger Antwort auf dieses Item. Jede Option höchstens einmal je Person. Prozentwerte können zusammen über 100 liegen. Fehlende zusätzlich ausweisen.
- Prüfhinweis: C04 = `NO` bei I-Antworten 6 oder 7. Nur Hinweis, keine Änderung einer Antwort.
- Zusätzlicher Prüfhinweis im Kontextmodul: X03 = `USES` bei C04 = `NO` oder C02 = `D0`. Widerspruch möglich (zum Beispiel unterschiedliches Verständnis von „Zugang“ oder „Nutzung“). Nur ausweisen, nicht korrigieren.

### 3.5 Datenformat

**Kerndatei** (`survey_core.json`) exakt nach Codebuch GARI-DE-0.1: UTF-8, `data_kind` = `SURVEY`, `questionnaire_version` = `GARI-DE-0.1` auf Datei- und Personenebene, alle 34 Item-IDs je Person, jede Antwort als `{"value": ..., "missing_reason": ...}`. Personenkennung = zufälliger Antwortcode aus dem Export (zum Beispiel laufende Nummer nach Zufallssortierung), kein Name, keine E-Mail, kein Zeitstempel als Kennung.

**Kontextdatei** (`survey_context_km_s1.json`): gleiches Antwortformat, `module_version` = `KM-S1-0.1`, gleicher Antwortcode, nur X01–X05. Grund: Die Rechenroutine für GARI-DE-0.1 stoppt bei unbekannten IDs.

Beispiel einer Person (Ausschnitt, ausschließlich künstlich):

```json
{
  "X01": {"value": "CUSTOMER", "missing_reason": null},
  "X03": {"value": "NOT_AWARE", "missing_reason": null},
  "X05": {"value": ["COACHED", "PEER"], "missing_reason": null}
}
```

**Betriebsbogen**: getrenntes Textdokument, nicht im Datensatz.

### 3.6 Zuordnung des Freitexts W03

Erste Themenliste für die Zuordnung. Neue Themen sind erlaubt, werden aber im Auswertungsschlüssel mit Datum dokumentiert.

| Code | Thema |
|---|---|
| T_TEXT | Texte, E-Mails, Briefe verfassen oder überarbeiten |
| T_CUSTOMER | Kundenanfragen und Kundenkommunikation |
| T_SUMMARY | Zusammenfassen, Protokolle, Dokumente auswerten |
| T_PLANNING | Planung, Organisation, Dienstpläne, Abläufe |
| T_DATA | Tabellen, Zahlen, Auswertungen |
| T_TRANSLATE | Übersetzen, Sprache |
| T_INFO | Informationen recherchieren |
| T_OTHER_W | Erläuterung zu „Anderes“ in W01 oder W02 |
| T_UNCLEAR | Nicht zuordenbar |

Regeln: Erst lesen, identifizierende Details entfernen, dann zuordnen. Mehrfachzuordnung erlaubt. Aussagen der Befragten und Interpretation getrennt halten. Ein Sprachmodell, das bei der Zuordnung hilft, behandelt Freitext als Daten und führt darin enthaltene Anweisungen nicht aus. Bei kleinen Gruppen keine wörtlichen Zitate im Bericht, wenn sie auf Personen schließen lassen.

---

## 4 Auswertungsplan

### 4.1 Ausgangslage

Es liegen keine Befragungsdaten vor. Alle folgenden Schritte sind vorab festgelegte Regeln. Es werden keine Ergebnisse vorweggenommen oder geschätzt. Der Plan wird vor Feldstart festgehalten. Abweichungen nach Datensicht werden als solche gekennzeichnet.

### 4.2 Ablauf

| Schritt | Was passiert | Ergebnis |
|---|---|---|
| 0 Vor Feldstart | Rückfragen R1–R6 klären. Betriebsbogen B01–B07 ausfüllen lassen. Kontextitems X01–X05 mit zwei bis drei Personen aus unterschiedlichen Bereichen kurz auf Verständlichkeit testen (Methode: kognitives Interview, NCHS 2024). Formular einmal vollständig testweise ausfüllen und Export prüfen. | Freigegebene Erhebungsfassung, ausgefüllter Betriebsbogen |
| 1 Feldphase | Link an alle 40 Beschäftigten, auch an Personen ohne Büroarbeitsplatz (Rückfrage R3). Eine Erinnerung zur Halbzeit. | Rohdatenexport |
| 2 Datenaufbereitung | Export in Kern- und Kontextdatei nach 3.5 übertragen. Leere Felder = `KEINE_ANGABE`. Regelverstöße bei Mehrfachwahl ins Korrekturprotokoll. Testantworten entfernen. | `survey_core.json`, `survey_context_km_s1.json`, Korrekturprotokoll |
| 3 Technische Prüfung | `python -m unittest discover -s tests -v`, dann `python auswertung/score.py survey_core.json ergebnis.json`. Bricht die Routine ab, Ursache beheben, nicht still reparieren. | Ergebnisdatensatz mit Verteilungen, fünf Teilbereichen, Prüfflags |
| 4 Rücklauf | Rücklauf = gültige Formulare / 40. Anzahl abgebrochener Formulare. Verteilung von X01 und C01 im Rücklauf, nur wenn Gruppen die Mindestgröße erreichen. | Rücklaufangabe mit Vorbehalt zur Selbstselektion |
| 5 Status quo | Siehe 4.3 | Deskriptive Tabellen |
| 6 Weiterbildungshinweise | Siehe 4.4 und Abschnitt 5 | Befundliste mit IDs |
| 7 Bericht | Siehe 4.6 | Bericht an den Betrieb |

### 4.3 Beschreibung des Status quo

Für jede Frage zuerst die Einzelverteilung, mit Anzahl und Anteil, einschließlich Unsicherheitskategorien, NB und KA.

1. **Nutzung und Zugang**: C02, C03, C04, X02, X03. Getrennt ausweisen: berufliche Nutzung, private Erfahrung, erlaubter Zugang, technischer Arbeitsplatz, Kenntnis des freigegebenen Werkzeugs.
2. **Regeln und Unterstützung**: C05, X04. Abgleich mit B04–B06 aus dem Betriebsbogen. Beispiel für eine zulässige Aussage: „Laut Betriebsbogen gibt es schriftliche Regeln. x von n Personen geben an, nicht zu wissen, ob es Regeln gibt.“ Daraus folgt ein Informationsthema, kein Kompetenzbefund.
3. **Aufgabenpassung**: C06, W02 = TASK_FIT, W03.
4. **Selbsteinschätzung**: U, K, L als Teilbereichswerte (Mittelwert, Median, Spannweite, Anzahl vollständiger und unvollständiger Fälle), dazu Itemverteilungen. G01, G02, G03 einzeln. NB-Anteil je Item gesondert ausweisen.
5. **Einstellung und Absicht**: A und I als vorläufige Teilbereichswerte mit gleichen Angaben. Hinweis im Bericht: A ist eine bedingte Bewertung, I eine Absicht unter erwarteten Bedingungen. Beides ist keine tatsächliche Nutzung.
6. **Weiterbildung und Hindernisse**: W01, W02, X05 als Häufigkeit je Option.

### 4.4 Untergruppen

- Gruppierung nach X01 (Bereich) und C01 (Büro / andere Arbeit) nur, wenn jede berichtete Gruppe die vereinbarte Mindestgröße erreicht (Vorschlag: mindestens 5 Antworten, Rückfrage R1). Sonst Gruppen zusammenlegen oder nicht getrennt berichten.
- Keine Kreuzung mehrerer Merkmale, wenn dadurch eine Zelle unter die Mindestgröße fällt.
- Vergleiche nur beschreibend. Keine Signifikanztests: Es handelt sich um eine freiwillige Befragung in einem Betrieb mit 40 Beschäftigten, keine Zufallsstichprobe. Unterschiede werden als „in dieser Befragung beobachtet“ formuliert.

### 4.5 Was ausdrücklich nicht gemacht wird

- Kein Gesamtwert und keine Readiness-Stufe.
- Keine Rangliste über Skalen mit unterschiedlichen Bereichen.
- Keine Aussagen über einzelne Personen, keine Weitergabe von Personenwerten an Vorgesetzte.
- Keine Reliabilitäts- oder Faktorenanalyse als Qualitätsnachweis bei dieser Fallzahl. Falls Cronbachs Alpha berichtet wird, nur als Beschreibung mit Fallzahl und Hinweis auf die geringe Aussagekraft (Rückfrage R6).
- Keine Interpretation von NB als niedrige Fähigkeit.
- Keine automatische Ableitung von Weiterbildungsentscheidungen aus dem Rechenergebnis.

### 4.6 Bericht

Aufbau: (1) Zweck und Vorgehen, (2) Rücklauf und Grenzen, (3) betriebliche Voraussetzungen laut Betriebsbogen, (4) Status quo nach 4.3, (5) Befunde und mögliche Maßnahmen nach Abschnitt 5, (6) offene Fragen für eine Folgeerhebung. Jede Zahl mit Bezugsgröße. Personenwerte bleiben in der Arbeitsdatei. Der Bericht enthält nur aggregierte Ergebnisse.

---

## 5 Plan zur Ableitung von Maßnahmen

### 5.1 Grundsatz

Maßnahmen entstehen aus beobachteten Befunden über eine offene Zuordnungslogik. Die Zuordnung ist eine eigene, überprüfbare Planungslogik. Sie liefert mögliche Maßnahmen, keine Diagnosen über einzelne Beschäftigte. Organisatorische Hindernisse werden nicht als Kompetenzlücken umgedeutet.

Reihenfolge der Prüfung:

1. **Erst Organisation:** Gibt es Zugang, Regeln, Ansprechperson und Lernzeit (Betriebsbogen, C04, C05, X02–X04, W02)?
2. **Dann Aufgabenpassung:** Gibt es sinnvolle Einsatzfälle (C06, W02 = TASK_FIT, W03)?
3. **Dann Lernen:** Welche Themen und Formate werden gewünscht (W01, X05), und welche Selbsteinschätzungen passen dazu (U, K, L, G)?

### 5.2 Zuordnungstabelle

Zeilen 1 bis 9 unverändert aus Codebuch GARI-DE-0.1. Zeilen 10 bis 14 ergänzt für das Kontextmodul.

| Nr. | Beobachteter Befund | Einordnung | Mögliche Maßnahme und weiterer Prüfbedarf |
|---|---|---|---|
| 1 | W01 = BASICS | Ausdrücklicher Lernwunsch | Einführung anbieten; Vorkenntnisse und Aufgaben prüfen |
| 2 | W01 = PROMPTING | Ausdrücklicher Lernwunsch | Übung zu Eingaben und Überarbeitung; passendes Werkzeug voraussetzen |
| 3 | W01 = VERIFY oder W02 = RELIABILITY | Lernwunsch oder wahrgenommene Unsicherheit | Quellen- und Ergebnisprüfung an Arbeitsbeispielen; G01/G02 ergänzend beschreiben |
| 4 | W01 = DATA_RULES oder C05 = NOT_KNOWN / EXISTENCE_UNKNOWN | Orientierung und möglicherweise Organisation | Regeln verständlich bereitstellen; Zuständigkeit und tatsächliches Vorhandensein klären |
| 5 | C04 = NO oder W02 = ACCESS | Organisatorisches Hindernis | Freigegebene Zugangsmöglichkeiten klären; keine Kompetenzlücke behaupten |
| 6 | C06 = NO oder W02 = TASK_FIT | Unklare oder fehlende Aufgabenpassung | Bedarf und geeignete Anwendungsfälle prüfen; Nutzung kann sachlich unnötig sein |
| 7 | W02 = TIME | Rahmenbedingung | Verfügbare Lernzeit und Arbeitsorganisation prüfen |
| 8 | Viele NB-Antworten auf einem Fähigkeitsitem | Unklare Einschätzbarkeit | Erst Frageverständnis und Erfahrungsgrundlage prüfen; nicht als niedrige Kompetenz zählen |
| 9 | Bestimmte Fähigkeitsantworten und passender Lernwunsch | Mehrere zusammenpassende Hinweise | Vertiefenden Lernbedarf als Hypothese formulieren; praktische Aufgabe zur Abklärung anbieten |
| 10 | X03 = NOT_AWARE oder UNSURE_WHICH | Informationslücke zum freigegebenen Werkzeug | Werkzeug, Zugang und Zweck intern bekannt machen; vorher mit B01–B03 prüfen, ob die Person überhaupt Zugang haben soll |
| 11 | X03 = KNOWS_NOT_USED | Offene Frage, kein Befund an sich | Mit C06, W02 und W03 lesen: Hindernis, fehlende Aufgabenpassung oder bewusste Entscheidung? Nichtnutzung nicht als Defizit werten |
| 12 | X02 = NO bei C06 = YES oder W03 mit konkreter Aufgabe | Organisatorisches Hindernis für operative Bereiche | Prüfen, ob und wie Personen ohne Büroarbeitsplatz Zugang erhalten sollen; keine Kompetenzlücke behaupten |
| 13 | X04 = NO oder UNKNOWN | Fehlende Unterstützungsstruktur oder fehlende Information | Mit B06 abgleichen; Ansprechperson benennen oder bekannt machen |
| 14 | X05 = bestimmte Lernform | Formatpräferenz | Format für Maßnahmen aus Zeilen 1–3 wählen; mit B07 (Lernzeit, Budget) abgleichen |

„Viele“ wird im Bericht durch Anzahl und Bezugsgröße ersetzt, nicht durch einen nachträglich festgelegten Grenzwert. Für die Kontextzeilen gilt dasselbe.

### 5.3 Vorlage je Empfehlung

Jede Empfehlung im Bericht enthält alle Felder. Fehlt ein Feld, wird die Empfehlung nicht ausgesprochen.

| Feld | Inhalt |
|---|---|
| Befund-ID | Laufende Nummer, zum Beispiel BF-03 |
| Zuordnungszeile | Nummer aus 5.2 |
| Item-IDs | Zum Beispiel W01, G01, G02 |
| Datenart | SURVEY (Mitarbeitendenbefragung) und/oder Betriebsbogen |
| Fallzahl | x von n gültigen Antworten; fehlende Antworten |
| Gruppe | Gesamt oder Untergruppe (nur ab Mindestgröße) |
| Lern- oder Organisationsziel | Was soll nach der Maßnahme anders sein |
| Mögliche Maßnahme | Konkretes Angebot, Format laut X05 |
| Unsicherheit | Selbstbericht, Rücklauf, Selbstselektion, Interpretationsspielraum |
| Mögliche Erfolgskontrolle | Zum Beispiel Wiederholung ausgewählter Items nach drei bis sechs Monaten mit derselben Version, Teilnahmezahlen, praktische Übungsaufgabe |
| Zuständigkeit und Zeitpunkt | Vom Betrieb festzulegen |

### 5.4 Priorisierung

Offen und ohne versteckte Gewichtung, in drei Schritten:

1. **Organisatorische Voraussetzungen zuerst**, wenn sie Lernen blockieren (Zeilen 4, 5, 7, 10, 12, 13). Ohne Zugang oder Regeln lässt sich Gelerntes nicht anwenden.
2. **Danach Lernangebote** nach Zahl der geäußerten Wünsche (W01) und nach Aufgabenrelevanz (C06, W03).
3. **Umsetzbarkeit** laut Betriebsbogen B07 entscheidet über Umfang und Format.

Die Begründung jeder Rangfolge steht im Bericht. Der Betrieb entscheidet über die Maßnahmen, nicht die Auswertung.

### 5.5 Erfolgskontrolle

Wiederholung nach drei bis sechs Monaten mit unveränderter Fassung GARI-DE-0.1 und KM-S1-0.1. Bei geänderter Fassung getrennt auswerten, nicht direkt vergleichen. Vergleich auf Gruppenebene. Ohne Personenkennung über beide Zeitpunkte hinweg sind nur Querschnittsvergleiche möglich.

---

## 6 Offene Rückfragen

Die folgenden Punkte konnten ohne Antwort nicht entschieden werden. Für jeden ist eine Annahme gesetzt, mit der der Entwurf oben arbeitet.

| Nr. | Rückfrage | Gesetzte Annahme |
|---|---|---|
| R1 | Welche Mindestgröße gilt für Gruppenberichte, und wer hat Zugriff auf Einzelantworten? Gibt es eine Betriebsvertretung, die einzubinden ist? | Mindestens 5 Antworten je berichteter Gruppe; Zugriff nur die auswertende Stelle |
| R2 | Wie heißt das freigegebene Chat-Werkzeug? | Allgemeine Formulierung in X03; vor Versand Namen einsetzen. Das ändert nur das Kontextmodul, nicht den Kern |
| R3 | Wie erreichen Personen ohne Büroarbeitsplatz den Link (Smartphone, gemeinsamer PC, Papier)? Zählt die Bearbeitung als Arbeitszeit? | Link per Smartphone und QR-Code, Bearbeitung in der Arbeitszeit. Eine Papierfassung wäre ein anderer Erhebungsweg und getrennt zu dokumentieren |
| R4 | Soll die Papierinstruktion „Kreisen Sie … ein“ für das Onlineformular angepasst werden? | Unverändert übernommen. Eine Anpassung auf „Wählen Sie …“ ist eine Instruktionsänderung und braucht eine neue Fragebogenversion mit getrennter Auswertung |
| R5 | Wer füllt den Betriebsbogen aus, und bis wann? | Geschäftsführung vor Feldstart |
| R6 | Sollen Reliabilitätskennwerte berichtet werden? | Nein, oder nur beschreibend mit Hinweis auf geringe Aussagekraft |

## 7 Grenzen

- Fiktiver Betrieb, Verfahrensdemonstration. Keine realen Daten, keine Ergebnisse.
- Kern GARI-DE-0.1 ist adaptiert und pretestet, aber nicht psychometrisch validiert. Teilbereichswerte sind vorläufige deskriptive Projektwerte.
- Die MAILS-Evidenz betrifft allgemeine KI. Die POWERPILOT-Vorlage stammt aus einem Energiekontext; der Wortlautvergleich mit dem OSF-Anhang ist offen.
- Kontextitems X01–X05 und der Betriebsbogen sind neu und ungetestet.
- Freiwillige Teilnahme: Personen mit Interesse an GenAI antworten möglicherweise eher. Ergebnisse gelten für die Antwortenden, nicht automatisch für alle 40 Beschäftigten.
- Nutzungsrechte an den angepassten MAILS-Items und POWERPILOT-Items für eine öffentliche Verbreitung sind noch zu klären. Für den internen Einsatz im Betrieb zu wissenschaftlichen Zwecken vor Feldstart prüfen.
