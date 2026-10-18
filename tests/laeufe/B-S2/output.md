# Fragebogen zur GenAI-Readiness von Mitarbeitenden: Erhebungspaket für Szenario S2

Fiktiver Produktionsbetrieb mit 400 Beschäftigten · Kern GARI-DE-0.1 · Kontextmodul KX-S2-0.1 · Stand 18. Oktober 2026

**Wichtig vorab:** Es liegen keine Befragungsdaten vor. Dieses Dokument enthält deshalb keine Ergebnisse, keine Kennwerte und keine Maßnahmenentscheidungen. Es enthält das Instrument, die Quellenzuordnung, das Codebuch und den Plan, wie aus künftigen Daten Hinweise auf Weiterbildungsbedarf und organisatorische Voraussetzungen werden. Das Unternehmen ist fiktiv (Verfahrensdemonstration laut Briefing).

## Inhalt

1. Kurzüberblick und Designentscheidungen
2. Fragebogen (Erhebungsfassung S2)
3. Quellenzuordnung
4. Codebuch
5. Gesonderte Erfassung betrieblicher Voraussetzungen
6. Auswertungsplan
7. Plan zur Ableitung von Maßnahmen
8. Ablauf, Grenzen und offene Rückfragen

---

## 1. Kurzüberblick und Designentscheidungen

| Punkt | Entscheidung | Begründung |
|---|---|---|
| Kern | Alle 34 Items C01–W03 der geprüften Kernbank GARI-DE-0.1 werden unverändert übernommen: Wortlaut, Antwortformat, Reihenfolge, Definition, Instruktionen, Zeitbezüge. | Die Itembank erlaubt nur Kontaktangaben und organisatorische Hinweise außerhalb des Fragebogens. Laut Codebuch braucht jede andere Änderung eine neue Fragebogenversion. |
| Rahmentexte | Die Pretest-Einleitung (Gespräch, Testkürzel, begleiteter Test) und der Pretest-Schlusssatz werden durch eine dokumentierte Erhebungsfassung ersetzt. Definition und Kerninstruktionen bleiben wörtlich. | `frozen_text_note` der Itembank erlaubt das nur als gesondert dokumentierte Erhebungsfassung. |
| Kontextfragen | Fünf neue Kontextfragen X01–X05 als eigener Teil 6 **nach** W03. | Der Kern bleibt in Inhalt und Reihenfolge unberührt. Die Fragen decken ab, was der Kern für S2 nicht erfasst: Tätigkeitsbereich laut Briefing, Geräteausstattung, Teilnahmeweg (Tablet), passende Lernform und Lernzeit bei Schichtarbeit. |
| Datentrennung | Kerndaten (34 IDs) und Kontextdaten (X01–X05) werden in zwei getrennten JSON-Dateien geführt, verbunden über eine systemvergebene Antwortkennung. | Die Rechenroutine für GARI-DE-0.1 stoppt bei unbekannten IDs. Sie bleibt dadurch unverändert nutzbar. |
| Betriebliche Voraussetzungen | Werden **nicht** bei Beschäftigten abgefragt, sondern über eine eigene Betriebs-Checkliste (B01–B10) bei Geschäftsführung, IT, Personal und Datenschutz. | Briefing: „Betriebliche Voraussetzungen gesondert erfassen“. Ob es freigegebene Werkzeuge oder Regeln gibt, ist ein Sachverhalt. Beschäftigte können dazu nur ihre Wahrnehmung angeben (C04, C05). |
| Keine Sprungregeln | Alle Fragen für alle Personen, auch ohne bisherige Nutzung. | Codebuch und Zielgruppe laut Briefing. Nichtnutzung erzeugt keinen Fehlwert und keinen Nullwert. |
| Keine Reifegradklassen | Kein Gesamtscore, keine Gewichtung, keine Einteilung in „bereit“ oder „nicht bereit“, keine Bewertung einzelner Personen. | Codebuch, Rechenregeln. |
| Datensparsamkeit | Kein Alter, Geschlecht, Name, keine Personalnummer, keine Schicht- oder Teamkennung. | Freiwillige, anonym angelegte Onlinebefragung. Kleine Gruppen wären sonst schnell identifizierbar. |

Versionsbezeichnung der Erhebung: **GARI-DE-0.1 (Kern) + Erhebungsfassung S2-E1 (Rahmentexte) + KX-S2-0.1 (Kontextmodul)**. In den Kerndaten bleibt `questionnaire_version` = `GARI-DE-0.1`, weil der Kern unverändert ist. Ob die Anfügung des Kontextmoduls für die Hausarbeit als neue Gesamtversion gilt, ist als Rückfrage offen (Abschnitt 8).

---

## 2. Fragebogen (Erhebungsfassung S2)

Hinweise für die Umsetzung im Onlineformular stehen in Kästen mit „Umsetzung“. Sie sind **nicht** Teil des Teilnehmendentexts. Platzhalter in eckigen Klammern füllt der Betrieb vor Feldstart aus. Alles andere ist Teilnehmendentext.

### Startseite

**Fragebogen zum Umgang mit generativer KI**

Erhebungsfassung S2-E1 · Fragen GARI-DE-0.1 und KX-S2-0.1 · [Feldzeitraum]

Dieser Fragebogen erfasst Ihre Erfahrungen, Einschätzungen und Weiterbildungswünsche zu generativer KI bei der Arbeit. Die Ergebnisse helfen dem Betrieb, passende Weiterbildungen und Rahmenbedingungen zu planen. Es geht nicht um die Bewertung Ihrer Arbeitsleistung. Ihre Antworten sind auch dann wichtig, wenn Sie generative KI noch nie genutzt haben. Geschätzte Dauer: etwa 15 Minuten.

Generative KI erzeugt oder bearbeitet auf Eingaben hin Inhalte, zum Beispiel Texte, Bilder, Audio, Videos oder Programmcode. Gemeint sind sowohl eigenständige Anwendungen als auch entsprechende Funktionen in anderen Programmen.

Die Teilnahme ist freiwillig. Sie können einzelne Fragen auslassen oder den Fragebogen jederzeit beenden. Wir fragen nicht nach Namen, Personalnummern oder Anmeldedaten. Ergebnisse werden nur zusammengefasst berichtet, für Gruppen ab [Mindestgruppengröße] Personen. Bitte tragen Sie keine Namen, Personalnummern oder vertraulichen Informationen ein.

Wenn Sie am Tablet im Pausenraum teilnehmen: Tippen Sie am Ende auf „Absenden“. Danach startet der Fragebogen für die nächste Person leer.

Fragen zur Befragung: [Kontaktstelle]. Informationen zum Datenschutz: [Link oder Aushang].

> **Umsetzung Startseite.** Kein Testkürzel- und Datumsfeld für Teilnehmende. Das Formularsystem vergibt je Absendung eine zufällige Antwortkennung und einen Zeitstempel. Keine Anmeldung, keine E-Mail-Erfassung, keine IP-Speicherung, keine Bestätigungs-E-Mail. Die Dauerangabe „etwa 15 Minuten“ ist eine Schätzung (Kern laut Itembank 10–15 Minuten, noch nicht gemessen, plus Kontextmodul) und wird im technischen Vortest gemessen.

### Teile 1 bis 5: Kernfragen GARI-DE-0.1 (unverändert)

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
`[Freitextfeld, mehrzeilig]`

> **Umsetzung Teile 1 bis 5.** Jede Frage ist optional (kein Pflichtfeld), weil Auslassen erlaubt ist. Die Instruktionen bleiben wörtlich, auch „Kreisen Sie … ein“. Im Formular wird jede 0–10-Frage als Einzelwahl mit 13 Optionen umgesetzt (0, 1, …, 10, NB, KA), jede 1–7-Frage als Einzelwahl mit 9 Optionen (1, …, 7, NB, KA). Nur Endanker beschriften, keine Zwischenanker. Seitenumbruch genau an der Stelle „Bitte fahren Sie auf der nächsten Seite fort“. W01 und W02 als Kästchenfragen mit Regel „höchstens 3“. Die Höchstzahl im Formular auf jeder Seite einzeln testen (laut Quellenliste trat bei Google Forms eine Fehlfunktion beim Seitenwechsel auf). Exklusivität von „Derzeit kein Weiterbildungswunsch“, „Derzeit nichts“, „kann ich noch nicht einschätzen“ und „Keine Angabe“ lässt sich in einfachen Formularen meist nicht erzwingen. Sie wird bei der Übertragung geprüft (Codebuch, Abschnitt 4.5).

#### Teil 6: Angaben zu Arbeitsbereich und Teilnahme

Diese Angaben helfen, Ergebnisse nach Arbeitsbereichen getrennt auszuwerten und Weiterbildungen passend zu planen. Kleine Gruppen werden nicht gesondert ausgewiesen. Die Antworten sind keine Zusage für bestimmte Angebote.

**X01**  In welchem Bereich arbeiten Sie überwiegend? Wenn Sie Personalverantwortung für andere Beschäftigte haben, wählen Sie bitte „Führung“.

□ Produktion (Schichtarbeit)  
□ Logistik  
□ Verwaltung  
□ Führung  
□ Anderer Bereich  
□ Keine Angabe  

**X02**  Welches Gerät können Sie bei der Arbeit für Arbeit am Bildschirm nutzen?

□ Einen eigenen dienstlichen PC, Laptop oder ein eigenes dienstliches Tablet  
□ Nur ein gemeinsam genutztes Gerät, zum Beispiel an der Linie, im Lager oder im Pausenraum  
□ Kein dienstliches Gerät  
□ Keine Angabe  

**X03**  Wie füllen Sie diesen Fragebogen gerade aus?

□ Am Tablet im Pausenraum  
□ An einem dienstlichen PC oder Laptop  
□ An einem privaten Smartphone oder anderen privaten Gerät  
□ Anders  
□ Keine Angabe  

**X04**  Welche Form der Weiterbildung zu generativer KI würde für Sie am besten passen? Bitte höchstens zwei Antworten auswählen.

□ Kurze Einführung vor Ort im Betrieb  
□ Übung in einer kleinen Gruppe mit Beispielen aus meiner Arbeit  
□ Online-Lernangebot, das ich mir selbst einteilen kann  
□ Feste Ansprechperson in meinem Bereich  
□ Kurze schriftliche Anleitung  
□ Kann ich noch nicht einschätzen  
□ Keine Angabe  

**X05**  Wann wäre eine Weiterbildung für Sie am ehesten möglich? Bitte höchstens zwei Antworten auswählen.

□ Während der Arbeitszeit direkt an meinem Arbeitsplatz  
□ Während der Arbeitszeit in einem Schulungsraum  
□ Unmittelbar vor oder nach meiner Schicht beziehungsweise Arbeitszeit  
□ Zu festen Terminen tagsüber  
□ Kann ich noch nicht einschätzen  
□ Keine Angabe  

Bei X04 und X05 dürfen „Kann ich noch nicht einschätzen“ und „Keine Angabe“ nur allein gewählt werden.

### Abschlussseite

Vielen Dank für Ihre Teilnahme. Ihre Antworten sind gespeichert. Die zusammengefassten Ergebnisse werden [Zeitpunkt] über [Weg, zum Beispiel Aushang, Intranet, Teambesprechung] vorgestellt.

Am Tablet: Der Fragebogen startet jetzt für die nächste Person neu.

> **Umsetzung Tablet im Pausenraum.** Formular im Kiosk- oder Gastmodus öffnen. Automatisches Ausfüllen und Verlauf im Browser deaktivieren. Nach dem Absenden automatisch zur leeren Startseite zurück. Bei Inaktivität (zum Beispiel nach einigen Minuten) Eingaben verwerfen und neu starten, damit die nächste Person keine fremden Antworten sieht. Aufstellung so, dass niemand mitlesen kann. Mindestens einen alternativen Weg anbieten (QR-Code und Link für private Geräte, Zugang an dienstlichen PCs), weil der Pausenraum nicht für alle Schichten und Pausenlängen passt. Tablet-Darstellung der 13 Antwortoptionen vorab auf Zeilenumbrüche prüfen: Die Zahlen müssen in einer erkennbaren Reihenfolge von 0 bis 10 stehen, sonst ist das Antwortformat faktisch verändert.

---

## 3. Quellenzuordnung

### 3.1 Grundsätze

- Die Spalten „Status“, „Fundstelle“, „Anpassung“ und „Grenze“ geben die Einträge der Kernbank GARI-DE-0.1 wieder. Sie wurden nicht erweitert.
- Ich habe keine der Originalquellen selbst eingesehen. Die Zuordnung stützt sich auf Itembank und Quellenliste. Originalwortlaute stehen nur dort, wo die Itembank sie enthält (A01–I03). Für die MAILS-Items führt die Itembank den Originalwortlaut nur über die Fundstelle.
- Eigenentwicklungen werden nicht nachträglich mit Literatur „belegt“. Eine Quelle kann ein Item motivieren, ohne dass dadurch ein geprüftes Originalitem vorliegt.
- Die Zahlen der Kernbank gelten für Selbstberichte. Kein Item misst beobachtete Leistung.

### 3.2 Kernitems C01–W03

| ID | Status | Quelle | Fundstelle | Anpassung laut Itembank | Grenze |
|---|---|---|---|---|---|
| C01 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| C02 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| C03 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| C04 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| C05 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| C06 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| U01 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 1, Seite 1; Zuordnung und Mittelwertregel Seite 3. | KI-Bezug auf generative KI eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| U02 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 2, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Erleichterung des Lebens auf berufliche Aufgaben eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| U03 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 3, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Zielbezug auf Arbeitsziele eingegrenzt; sinnvoll durch gezielt konkretisiert. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| U04 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 4, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Alltagsinteraktion auf Zusammenarbeit bei der Arbeit übertragen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| U05 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 5, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gewinnbringende Zusammenarbeit über brauchbare Arbeitsergebnisse konkretisiert; Bedeutungsverschiebung im Pretest prüfen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| U06 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 6, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gewinnbringende Kommunikation über verständliches Mitteilen konkretisiert; Ergebnisaspekt verengt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K01 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 7, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Allgemeine KI auf generative KI eingegrenzt; Konzepte bleibt bewusst zur Verständlichkeitsprüfung erhalten. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K02 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 8, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Kenntnis von Definitionen in selbst eingeschätzte Erklärfähigkeit übertragen; stärkere Anpassung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K03 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 9, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K04 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 10, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K05 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 11, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Verwendungszwecke sprachlich vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K06 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 12, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz verkürzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| L01 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 26, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; stets entfällt. Deutsche Itemnummer 26 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| L02 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 27, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; deutsche Itemnummer 27 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| L03 | ADAPTIERT | Carolus et al. (2023), MAILS, deutscher Autorenfragebogen | Deutscher Autorenfragebogen, Item 28, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; sprachliche Verdichtung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| G01 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| G02 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| G03 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| A01 | ADAPTIERT | Wichmann et al. (2025), Itemsammlung PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Original: „The use of PowerPilot would be … advantageous.“ | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| A02 | ADAPTIERT | Wichmann et al. (2025), Itemsammlung PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Original: „The use of PowerPilot would be … satisfactory.“ | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| A03 | ADAPTIERT | Wichmann et al. (2025), Itemsammlung PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Original: „The use of PowerPilot would be … important.“ | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| A04 | ADAPTIERT | Wichmann et al. (2025), Itemsammlung PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 4; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Original: „The use of PowerPilot would be … enjoyable.“ | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| I01 | ADAPTIERT | Wichmann et al. (2025), Itemsammlung PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Original: „I plan to use PowerPilot in the future.“ | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| I02 | ADAPTIERT | Wichmann et al. (2025), Itemsammlung PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Original: „I intend to use PowerPilot in the future.“ | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| I03 | ADAPTIERT | Wichmann et al. (2025), Itemsammlung PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Original: „I will definitely use PowerPilot in the future.“ | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| W01 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| W02 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |
| W03 | NEU_ENTWICKELT | Eigenentwicklung | keine Originalfundstelle | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Noch nicht empirisch geprüft. |

### 3.3 Inhaltliche Zuordnung der Teilbereiche zu den Quellen

| Teilbereich | Quelle | Wofür die Quelle steht | Was sie nicht leistet |
|---|---|---|---|
| U, K, L | Carolus et al. (2023), deutscher Autorenfragebogen MAILS, Items 1–6, 7–12, 26–28; Zuordnung und Mittelwertregel S. 3 | Facetten Anwendung, Verständnis und Lernzutrauen; Antwortformat 0–10 mit zwei Endankern; Mittelwertbildung je Teilbereich | Evidenz betrifft allgemeine KI, 300 deutschsprachige Erwachsene, Selbstberichte. Die Eingrenzung auf generative KI und den Arbeitskontext ist nicht validiert. Fehlwertregel (vollständige Fälle) ist eine Projektregel, keine MAILS-Vorschrift. |
| U, K, L (Einordnung) | Koch et al. (2024), MAILS-Kurzfassung | Kritische Einordnung erweiterter Validitätsevidenz | Kurzfassung wird nicht eingesetzt, weil sie KI-Entwicklung enthält und nur teilweise zum Zweck passt. |
| A, I | Wichmann et al. (2025), HICSS, Itemsammlung PowerPilot (Datensatz_v1.docx) | Siebenstufige Zustimmung; Einstellung und Nutzungsabsicht im Reasoned Action Approach | Wortlautgleichheit mit dem OSF-Originalanhang ungeprüft (nicht abrufbar). Energieanwendungskontext. Übernahme des Formats bringt keine automatische Vergleichbarkeit. |
| A, I (Formulierung) | Ajzen (o. J.), Constructing a TPB questionnaire | Verhalten über Ziel, Handlung, Kontext und Zeit festlegen: hier „freigegebene generative KI“, „berufliche Aufgaben“, „nächste drei Monate“ | Begründet keine bestimmten Einzelitems. |
| C06, W02 = TASK_FIT, X01 | Paetow et al. (2026), Task-Technology-Fit in VR | Hintergrund für die Frage nach Aufgabenpassung | Items nicht übertragen; Übertragbarkeit auf generative KI ungeprüft. |
| C04, X02, X05, Betriebs-Checkliste | Wichmann et al. (2026), sozio-technische Arbeitsbedingungen | Hintergrund: technische und soziale Arbeitsbedingungen gehören zur Einordnung | Keine Items übernommen. |
| G01–G03, Abschnitt 7 (Prüfen) | Do Khac et al. (2025), Vertrauen in generative KI | Hintergrund für Vertrauen und Ergebnisprüfung | Zielgruppe sind Entscheidungstragende, nicht die gesamte Belegschaft. Keine Items übernommen. |
| Gesamtes Instrument | Wichmann et al. (2024), JMIR | Beispiel theoriegestützter Operationalisierung von KI-Akzeptanz | Gesundheitsbezogene Konstrukte nicht übernommen. |
| Entwicklungsvorgehen | Peffers et al. (2007); Venable et al. (2016) | DSR-Aktivitäten; Verbindung kontrollierter Prüfung mit formativer Rückmeldung | Bewertet nicht die Messqualität. |
| Pretest, Messqualität | Boateng et al. (2018); National Center for Health Statistics (2024) | Trennung von Itementwicklung, Pretest und Validierung; kognitives Interview | Kleine Pretests ersetzen keine psychometrische Validierung. |
| Formularumsetzung | Google (o. D.), Regeln für Formulare | Technische Höchstzahl bei Kästchenfragen | Nur relevant, wenn Google Forms genutzt wird. |
| Grenzen synthetischer Tests | Bisbee et al. (2024) | Synthetische Antworten ersetzen keine realen Befragten | Betrifft politische Befragungsdaten und frühere Modelle. |

### 3.4 Kontextmodul X01–X05

| ID | Status | Herkunft | Begründung | Grenze |
|---|---|---|---|---|
| X01 | NEU_ENTWICKELT (KX-S2-0.1) | Briefing S2, Feld `taetigkeitsbereiche` | Gruppenvergleich nach den vier im Briefing genannten Bereichen. C01 beschreibt die Art der Tätigkeit, nicht den Bereich. Beides bleibt getrennt. | Zuordnung von Führungskräften über Personalverantwortung ist eine eigene Festlegung. Kategorien mit dem Betrieb abstimmen. Keine Literaturgrundlage. |
| X02 | NEU_ENTWICKELT (KX-S2-0.1) | Briefing S2, Feld `arbeitszugang_zu_genai` | Trennt Geräteausstattung von freigegebenem KI-Zugang (C04). So lässt sich ein fehlendes Werkzeug von einem fehlenden Gerät unterscheiden. | Selbstauskunft; Abgleich mit Betriebs-Checkliste B01. |
| X03 | NEU_ENTWICKELT (KX-S2-0.1) | Briefing S2, Feld `besonderheit` | Prüft, ob der Teilnahmeweg mit Antwortmustern zusammenhängt (zum Beispiel mehr fehlende Antworten am Tablet). Dient der Datenqualität, nicht der Inhaltsauswertung. | Keine Literaturgrundlage. |
| X04 | NEU_ENTWICKELT (KX-S2-0.1) | Briefing S2, Zweck „Hinweise auf Weiterbildungsbedarf“ | Übersetzt Lernwünsche (W01) in umsetzbare Formate. | Präferenz, kein Lernerfolg. Optionen vor Einsatz mit dem Betrieb abstimmen. |
| X05 | NEU_ENTWICKELT (KX-S2-0.1) | Briefing S2, Schichtarbeit; Codebuch-Befund W02 = TIME | Macht „zu wenig Zeit“ planbar. | Arbeitsrechtliche Fragen (Arbeitszeit, Vergütung) werden damit nicht beantwortet und sind über die Betriebs-Checkliste zu klären. |

Alle fünf Kontextfragen sind ungeprüft. Sie brauchen vor der Haupterhebung mindestens einen kurzen Verständnistest mit Personen aus Produktion und Logistik (Abschnitt 8).

### 3.5 Literatur (APA)

Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. University of Massachusetts Amherst. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf

Bisbee, J., Clinton, J. D., Dorff, C., Kenkel, B., & Larson, J. M. (2024). Synthetic replacements for human survey data? The perils of large language models. *Political Analysis, 32*(4), 401–416. https://doi.org/10.1017/pan.2024.5

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Do Khac, L. T., Leyer, M., Wichmann, J., & Richter, A. (2025). Divisional perspectives on trust in generative AI: An empirical study of senior decision-makers. *Enterprise Information Systems*. Advance online publication. https://doi.org/10.1080/17517575.2025.2481557

Google. (o. D.). *Regeln für Formulare festlegen*. Google Docs-Editoren-Hilfe. Abgerufen am 17. Oktober 2026, von https://support.google.com/docs/answer/3378864?hl=de

Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), Article e39686. https://doi.org/10.1016/j.heliyon.2024.e39686

National Center for Health Statistics. (2024, April 16). *Cognitive interviewing*. Centers for Disease Control and Prevention. https://www.cdc.gov/nchs/ccqder/question-evaluation/cognitive-interviewing.html

Paetow, T., Wichmann, J., & Leyer, M. (2026). Task-technology fit in virtual reality: Explaining behavioral intention to use and perceived performance. In *Proceedings of the 59th Hawaii International Conference on System Sciences* (pp. 319–328). https://hdl.handle.net/10125/111430

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. *European Journal of Information Systems, 25*(1), 77–89. https://doi.org/10.1057/ejis.2014.36

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114

Wichmann, J., Gesk, T. S., & Leyer, M. (2024). Acceptance of AI in health care for short- and long-term treatments: Pilot development study of an integrated theoretical model. *JMIR Formative Research, 8*, e48600. https://doi.org/10.2196/48600

Wichmann, J., Gesk, T. S., & Leyer, M. (2026). The effect of social interaction in virtual meeting settings on work engagement: A socio-technical systems study. *Information Technology and Management, 27*, 173–185. https://doi.org/10.1007/s10799-025-00453-6

Zusätzliche Fundstelle des Instruments: Deutscher MAILS-Autorenfragebogen, https://downloads.hci.informatik.uni-wuerzburg.de/MAILS-questionnaire-german.pdf

**Rechtehinweis aus Itembank und Quellenliste.** Für die adaptierten MAILS- und PowerPilot-Items sind die Nutzungsrechte für eine öffentliche Weitergabe veränderter Itemtexte nicht geklärt. Die Autorenseite erlaubt die direkte Übernahme der Original-MAILS-Items für wissenschaftliche Untersuchungen. Das ist keine pauschale Erlaubnis für veränderte Fassungen. Eine betriebsinterne Erhebung ist davon getrennt zu prüfen. Vor jeder Veröffentlichung (zum Beispiel Anhang, Repository) klären.

---

## 4. Codebuch

### 4.1 Geltung

Für den Kern gilt das Codebuch GARI-DE-0.1 unverändert. Dieser Abschnitt gibt es vollständig für die Anwendung wieder und ergänzt Regeln für das Kontextmodul KX-S2-0.1 und die Onlineerhebung. Wo beide sich zu widersprechen scheinen, gilt das Codebuch GARI-DE-0.1.

Skalen: 0–10 mit 0 = gar nicht oder kaum ausgeprägt, 10 = sehr gut oder (nahezu) perfekt ausgeprägt. 1–7 mit 1 = stimme überhaupt nicht zu, 7 = stimme vollständig zu. Keine Zwischenanker. Höhere Werte bedeuten höhere Selbsteinschätzung oder Zustimmung. Keine umgepolten Items. Keine Sprungregeln, alle Fragen an alle.

### 4.2 Kernvariablen

| ID | Wortlaut (unverändert) | Typ und Werte | Zulässige Fehlwerte | Zusammenfassung |
|---|---|---|---|---|
| C01 | Wie sieht Ihre hauptsächliche Tätigkeit aus? | Einzelwahl: `OFFICE` = Überwiegend Büro- oder Bildschirmarbeit; `OTHER_WORK` = Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst; `MIXED` = Etwa gleich große Anteile beider Bereiche | `KEINE_ANGABE` | Einzelverteilung |
| C02 | An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt? | Einzelwahl: `D0` = An keinem Tag; `D1_3` = An 1 bis 3 Tagen; `D4_9` = An 4 bis 9 Tagen; `D10_15` = An 10 bis 15 Tagen; `D16_PLUS` = An 16 oder mehr Tagen; `UNKNOWN` = Kann ich nicht einschätzen | `KEINE_ANGABE` | Einzelverteilung |
| C03 | Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt? | Einzelwahl: `YES` = Ja; `NO` = Nein; `UNKNOWN` = Ich bin mir nicht sicher | `KEINE_ANGABE` | Einzelverteilung |
| C04 | Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen? | Einzelwahl: `YES` = Ja; `NO` = Nein; `UNKNOWN` = Ich weiß es nicht | `KEINE_ANGABE` | Einzelverteilung |
| C05 | Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit? | Einzelwahl: `KNOWN` = Ja; `PARTLY` = Teilweise; `NOT_KNOWN` = Nein; `EXISTENCE_UNKNOWN` = Ich weiß nicht, ob es solche Regeln gibt | `KEINE_ANGABE` | Einzelverteilung |
| C06 | Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre? | Einzelwahl: `YES` = Ja; `NO` = Nein; `UNKNOWN` = Kann ich noch nicht beurteilen | `KEINE_ANGABE` | Einzelverteilung |
| U01 | Ich kann eine generative KI bedienen. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von U (6/6 nötig) |
| U02 | Ich kann mir berufliche Aufgaben durch generative KI erleichtern. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von U (6/6 nötig) |
| U03 | Ich kann generative KI gezielt für meine Arbeitsziele einsetzen. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von U (6/6 nötig) |
| U04 | Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von U (6/6 nötig) |
| U05 | Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von U (6/6 nötig) |
| U06 | Ich kann generativer KI verständlich mitteilen, was ich brauche. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von U (6/6 nötig) |
| K01 | Ich kenne die zentralen Konzepte generativer KI. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von K (6/6 nötig) |
| K02 | Ich kann erklären, was generative KI bedeutet. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von K (6/6 nötig) |
| K03 | Ich kann Chancen und Grenzen generativer KI einschätzen. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von K (6/6 nötig) |
| K04 | Ich kann Vor- und Nachteile generativer KI beurteilen. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von K (6/6 nötig) |
| K05 | Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von K (6/6 nötig) |
| K06 | Ich kann mir künftige Anwendungen generativer KI vorstellen. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von K (6/6 nötig) |
| L01 | Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von L (3/3 nötig) |
| L02 | Ich kann mich über Neuerungen bei generativer KI informieren. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von L (3/3 nötig) |
| L03 | Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von L (3/3 nötig) |
| G01 | Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Einzelitem, kein Mittelwert |
| G02 | Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Einzelitem, kein Mittelwert |
| G03 | Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf. | Ganzzahl 0–10 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Einzelitem, kein Mittelwert |
| A01 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft. | Ganzzahl 1–7 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von A (4/4 nötig) |
| A02 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend. | Ganzzahl 1–7 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von A (4/4 nötig) |
| A03 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig. | Ganzzahl 1–7 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von A (4/4 nötig) |
| A04 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm. | Ganzzahl 1–7 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von A (4/4 nötig) |
| I01 | Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | Ganzzahl 1–7 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von I (3/3 nötig) |
| I02 | Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | Ganzzahl 1–7 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von I (3/3 nötig) |
| I03 | Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen. | Ganzzahl 1–7 | `NICHT_BEURTEILBAR`, `KEINE_ANGABE` | Teil von I (3/3 nötig) |
| W01 | Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen. | Liste, max. 3: `BASICS` = Grundlagen generativer KI; `USE_CASES` = Passende Einsatzmöglichkeiten für meine Aufgaben; `PROMPTING` = Klare Eingaben formulieren und Ergebnisse verbessern; `VERIFY` = Antworten und Quellen überprüfen; `DATA_RULES` = Betriebliche Regeln und zulässige Dateneingaben; `KEEP_CURRENT` = Bei neuen Entwicklungen auf dem Laufenden bleiben; `OTHER` = Anderes Thema; `NONE` = Derzeit kein Weiterbildungswunsch; `UNKNOWN` = Ich kann meinen Bedarf noch nicht einschätzen. Exklusiv: `NONE`, `UNKNOWN` | `KEINE_ANGABE` | Häufigkeit je Option |
| W02 | Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen. | Liste, max. 3: `ACCESS` = Kein Zugang zu einem freigegebenen Werkzeug; `RULES` = Unklare betriebliche Regeln; `TIME` = Zu wenig Zeit zum Ausprobieren oder Lernen; `KNOWLEDGE` = Mir fehlt Wissen über die Nutzung; `TASK_FIT` = Ich erkenne keinen passenden Einsatz für meine Aufgaben; `RELIABILITY` = Unsicherheit über die Verlässlichkeit der Ergebnisse; `OTHER` = Etwas anderes; `NONE` = Derzeit nichts; `UNKNOWN` = Kann ich noch nicht einschätzen. Exklusiv: `NONE`, `UNKNOWN` | `KEINE_ANGABE` | Häufigkeit je Option |
| W03 | Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen. | Freitext (String) | `KEINE_ANGABE` | Thematische Zuordnung |

### 4.3 Kontextvariablen (KX-S2-0.1)

| ID | Wortlaut | Typ und Werte | Zulässige Fehlwerte | Zusammenfassung |
|---|---|---|---|---|
| X01 | In welchem Bereich arbeiten Sie überwiegend? Wenn Sie Personalverantwortung für andere Beschäftigte haben, wählen Sie bitte „Führung“. | Einzelwahl: `PRODUCTION_SHIFT` = Produktion (Schichtarbeit); `LOGISTICS` = Logistik; `ADMIN` = Verwaltung; `LEADERSHIP` = Führung; `OTHER_AREA` = Anderer Bereich | `KEINE_ANGABE` | Einzelverteilung; Gruppierungsvariable |
| X02 | Welches Gerät können Sie bei der Arbeit für Arbeit am Bildschirm nutzen? | Einzelwahl: `OWN_DEVICE` = Eigenes dienstliches Gerät; `SHARED_DEVICE` = Nur gemeinsam genutztes Gerät; `NO_DEVICE` = Kein dienstliches Gerät | `KEINE_ANGABE` | Einzelverteilung; Gruppierungsvariable |
| X03 | Wie füllen Sie diesen Fragebogen gerade aus? | Einzelwahl: `TABLET_BREAKROOM` = Tablet im Pausenraum; `WORK_PC` = Dienstlicher PC oder Laptop; `PRIVATE_DEVICE` = Privates Gerät; `OTHER_MODE` = Anders | `KEINE_ANGABE` | Nur Datenqualität |
| X04 | Welche Form der Weiterbildung zu generativer KI würde für Sie am besten passen? Bitte höchstens zwei Antworten auswählen. | Liste, max. 2: `ONSITE_INTRO` = Kurze Einführung vor Ort; `SMALL_GROUP` = Übung in kleiner Gruppe mit Arbeitsbeispielen; `SELF_PACED` = Online-Lernangebot selbst eingeteilt; `CONTACT_PERSON` = Feste Ansprechperson im Bereich; `WRITTEN_GUIDE` = Kurze schriftliche Anleitung; `UNKNOWN` = Kann ich noch nicht einschätzen. Exklusiv: `UNKNOWN` | `KEINE_ANGABE` | Häufigkeit je Option |
| X05 | Wann wäre eine Weiterbildung für Sie am ehesten möglich? Bitte höchstens zwei Antworten auswählen. | Liste, max. 2: `AT_WORKPLACE` = Arbeitszeit am Arbeitsplatz; `TRAINING_ROOM` = Arbeitszeit im Schulungsraum; `BEFORE_AFTER_SHIFT` = Vor oder nach Schicht beziehungsweise Arbeitszeit; `FIXED_DAYTIME` = Feste Termine tagsüber; `UNKNOWN` = Kann ich noch nicht einschätzen. Exklusiv: `UNKNOWN` | `KEINE_ANGABE` | Häufigkeit je Option |

### 4.4 Eingabeformat

**Kerndatei** (unverändert nach Codebuch GARI-DE-0.1): JSON, UTF-8. `data_kind` = `SURVEY` für die echte Erhebung, `SYNTHETIC_DEMO` für Probedaten, `PRETEST` für den Pretest. `questionnaire_version` = `GARI-DE-0.1` auf Datei- und Personenebene. Je Person alle 34 IDs, auch bei fehlender Antwort. Jede Antwort hat `value` und `missing_reason`. Personenkennung ist die systemvergebene zufällige Antwortkennung, die je Datei nur einmal vorkommen darf.

**Kontextdatei** (neu): gleiche Struktur, `questionnaire_version` = `KX-S2-0.1`, je Person alle fünf IDs X01–X05 mit `value` und `missing_reason`, dieselbe Antwortkennung. Personen ohne Eintrag in einer der beiden Dateien werden im Übertragungsprotokoll ausgewiesen, nicht ergänzt.

Beispielausschnitt Kontextdatei (künstlich, keine Daten):

```json
{
  "X01": {"value": "LOGISTICS", "missing_reason": null},
  "X02": {"value": null, "missing_reason": "KEINE_ANGABE"},
  "X04": {"value": ["SMALL_GROUP", "CONTACT_PERSON"], "missing_reason": null}
}
```

### 4.5 Übertragung aus dem Onlineformular und Fehlwerte

| Formularzustand | Kodierung |
|---|---|
| Zahl 0–10 bzw. 1–7 gewählt | `value` = Ganzzahl, `missing_reason` = null. Eine gewählte 0 bleibt immer 0. |
| NB gewählt | `value` = null, `missing_reason` = `NICHT_BEURTEILBAR` |
| KA gewählt oder Feld leer | `value` = null, `missing_reason` = `KEINE_ANGABE`. Kein Motiv ergänzen. |
| Unsicherheitsoption bei C01–C06 (zum Beispiel `UNKNOWN`, `EXISTENCE_UNKNOWN`) | Reguläre Kategorie, kein Fehlwert. Wird mitgezählt und ausgewiesen. |
| W01, W02: nur `NONE` oder nur `UNKNOWN` | Reguläre Kategorie als Liste mit einem Eintrag |
| W01, W02, X04, X05: „Keine Angabe“ allein oder nichts angekreuzt | `value` = null, `missing_reason` = `KEINE_ANGABE`. Eine leere Liste ist unzulässig. |
| W01, W02: mehr als drei Optionen; X04, X05: mehr als zwei | Keine Auswahl treffen. Item = `KEINE_ANGABE`, Grund im Korrekturprotokoll. |
| Exklusive Option zusammen mit anderen Optionen (auch „Keine Angabe“ plus Thema) | Item = `KEINE_ANGABE`, Grund im Korrekturprotokoll. Nie selbst eine Antwort wählen. |
| W03 leer oder „Keine Angabe“ angekreuzt | `KEINE_ANGABE` |
| W03 Text und zusätzlich „Keine Angabe“ angekreuzt | Widerspruch: `KEINE_ANGABE`, Grund im Korrekturprotokoll. Text nicht verwenden. |
| Abbruch (Formular nicht abgesendet) | Wird nicht gespeichert und nicht übertragen. Teilnahme wird nicht gezählt. |
| Mehrfaches Absenden derselben Person | Nicht erkennbar und nicht prüfbar, weil keine Kennung erhoben wird. Als Grenze berichten. Offensichtliche Doppel (identische Antworten im Abstand von Sekunden) nur im Protokoll vermerken, nicht löschen, außer nach dokumentierter Regel vor Datenansicht. |

`NICHT_ZUTREFFEND` und `UEBERSPRUNGEN` werden nicht verwendet. Die Rechenroutine stoppt bei unzulässigen Werten, fehlenden oder unbekannten IDs, doppelten Kennungen und abweichenden Versionen. Nichts wird still repariert.

### 4.6 Rechenregeln

- **Teilbereichsmittel U, K, L, A, I** je Person nur, wenn alle Items gültige Zahlen haben (U 6, K 6, L 3, A 4, I 3). Sonst bleibt der Personenwert fehlend. Konservative Projektregel, keine MAILS-Vorschrift.
- **G01, G02, G03** bleiben Einzelitems. Kein G-Mittelwert.
- **Gruppenwerte**: Mittelwert der gültigen Personenwerte, immer mit Zahl vollständiger und unvollständiger Fälle. Null gültige Fälle ergibt `null`, nicht 0. Keine Ersetzung fehlender Werte.
- **Primäre Darstellung** sind Einzelverteilungen. Die numerische Behandlung der Antwortzahlen für Mittelwerte ist eine offen ausgewiesene Annahme.
- **Kein** Gesamtscore, keine Umrechnung auf 100, keine Gewichtung, keine Klassen „bereit“ oder „nicht bereit“. 0–10- und 1–7-Werte nicht in einer gemeinsamen Rangliste vergleichen.
- **Mehrfachantworten**: Nenner = Personen mit gültiger Antwort auf dieses Item. Jede Option höchstens einmal je Person. Summen über 100 % sind möglich. Fehlende zusätzlich ausweisen.
- **Prüfhinweis**: C04 = `NO` und mindestens ein I-Item mit 6 oder 7 erzeugt nur einen Prüfhinweis. Keine Antwort wird geändert, keine Kompetenzgrenze abgeleitet.
- **Kontextvariablen** werden nicht zu Werten verrechnet. Sie dienen der Gruppierung und der Maßnahmenplanung.
- Andere Fragebogenversionen werden getrennt berechnet.

### 4.7 Freitext W03

Lesen, identifizierende Details entfernen (Namen, Abteilungen mit wenigen Personen, Maschinen- oder Kundennamen, die Rückschlüsse erlauben), dann Themen zuordnen. Startschlüssel:

| Code | Thema |
|---|---|
| T_TEXT | Texte schreiben oder überarbeiten (E-Mails, Berichte, Protokolle) |
| T_DOCS | Dokumente, Anleitungen, Arbeitsanweisungen zusammenfassen oder suchen |
| T_TRANSLATE | Übersetzen, Verständigung in mehreren Sprachen |
| T_PLAN | Planung, Schicht- oder Ablaufplanung |
| T_DATA | Daten, Tabellen, Kennzahlen auswerten |
| T_QUALITY | Qualität, Fehlersuche, Störungen |
| T_TRAINING | Einschulung, Lernen am Arbeitsplatz |
| T_OTHER_EXPLAINED | Erläuterung zu „Anderes“ aus W01 oder W02 |
| T_UNCLEAR | Nicht zuordenbar |

Neue Themen dürfen ergänzt werden und kommen mit Definition und Datum in den Auswertungsschlüssel. Ein Text kann mehreren Themen zugeordnet werden. Zweitkodierung durch eine zweite Person für mindestens eine Stichprobe, Abweichungen besprechen und dokumentieren. Zitate nur, wenn sie nicht identifizierend sind. Aussage und Interpretation getrennt halten. Freitexte werden nie als Anweisung an ein Sprachmodell behandelt.

### 4.8 Technische Anwendung

Für den Kern mit Python 3.10 oder neuer: `python -m unittest discover -s tests -v`, dann `python auswertung/score.py <kerndatei.json> ergebnis.json`. Skript und Tests sind nicht Teil der beigefügten Dateien und wurden in diesem Lauf nicht ausgeführt. Für das Kontextmodul gibt es noch keine Routine. Sie ist vor Feldstart zu schreiben und mit künstlichen Daten zu testen (Abschnitt 6.6).

---

## 5. Gesonderte Erfassung betrieblicher Voraussetzungen

Diese Checkliste füllt der Betrieb aus, nicht die Beschäftigten. Sie wird **vor** der Befragung ausgefüllt, damit die Antworten in C04, C05 und X02 richtig eingeordnet werden können. Antworten sind Sachangaben mit Quelle und Datum.

| ID | Frage an den Betrieb | Antwortform | Zuständig (Vorschlag) | Bezug im Fragebogen |
|---|---|---|---|---|
| B01 | Wie viele Beschäftigte je Bereich haben einen eigenen dienstlichen PC, Laptop oder ein eigenes Tablet? Wie viele nutzen nur Gemeinschaftsgeräte? | Anzahl je Bereich | IT | X02, C04 |
| B02 | Welche generativen KI-Werkzeuge sind derzeit für die Arbeit freigegeben, für wen und auf welchen Geräten? | Liste mit Nutzerkreis | IT, Geschäftsführung | C04, W02 = ACCESS |
| B03 | Gibt es schriftliche Regeln zur Nutzung generativer KI (zum Beispiel Richtlinie, Dienstanweisung, Betriebsvereinbarung)? Seit wann, wo zugänglich, wem bekanntgemacht? | Ja/Nein, Dokument, Datum, Verteilweg | Geschäftsführung, Datenschutz | C05, G03, W01 = DATA_RULES, W02 = RULES |
| B04 | Welche Daten dürfen nicht in generative KI eingegeben werden (zum Beispiel Personaldaten, Kundendaten, Konstruktionsdaten)? | Kategorien | Datenschutz, IT-Sicherheit | G03 |
| B05 | Ist geplant, in den nächsten drei Monaten Zugang zu schaffen oder zu erweitern? Für welche Bereiche? | Plan mit Zeitpunkt oder „nicht geplant“ | Geschäftsführung | I01–I03, Prüfhinweis C04/I |
| B06 | Wie viel Lernzeit kann je Bereich innerhalb der Arbeitszeit bereitgestellt werden? Gibt es Regeln für Schulungen außerhalb der Schicht? | Stunden, Regelung | Personal, Bereichsleitungen | W02 = TIME, X05 |
| B07 | Welche Schulungsformate und -orte sind verfügbar (Schulungsraum, Lernplattform, interne Ansprechpersonen)? | Liste | Personal | X04 |
| B08 | Ist eine Arbeitnehmervertretung einzubinden, und ist sie über die Befragung informiert? | Ja/Nein, Datum | Geschäftsführung, Personal | Feldstart |
| B09 | Wie viele Beschäftigte gibt es je Bereich aus X01 (Produktion Schicht, Logistik, Verwaltung, Führung, Andere)? | Anzahl | Personal | Rücklaufberechnung, Mindestgruppengröße |
| B10 | Wie werden die Einladung und der Link verteilt (Aushang, QR-Code, E-Mail, Schichtbesprechung), und wann ist das Tablet erreichbar? | Beschreibung | Personal, Bereichsleitungen | X03, Erreichbarkeit aller Schichten |

Die Checkliste wird als eigener Dokumentstand mit Datum abgelegt. Abweichungen zwischen Betriebsangaben und Beschäftigtenwahrnehmung (zum Beispiel B03 „Regeln vorhanden“, aber viele C05 = `EXISTENCE_UNKNOWN`) sind ein Befund über Kommunikation, kein Fehler der Befragten.

---

## 6. Auswertungsplan

Der Plan wird vor Feldstart festgehalten. Abweichungen danach werden als solche gekennzeichnet.

### 6.1 Fragen, die die Auswertung beantwortet

| Nr. | Frage | Items |
|---|---|---|
| F1 | Wie verbreitet ist berufliche und private Nutzung generativer KI derzeit? | C02, C03 |
| F2 | Wie viele haben aus eigener Sicht Zugang, Geräte und kennen Regeln? | C04, C05, X02 |
| F3 | Wo sehen Beschäftigte sinnvolle Einsatzmöglichkeiten? | C06, W03 |
| F4 | Wie schätzen Beschäftigte Anwendung, Verständnis, Lernzutrauen und Prüfen ein? | U, K, L, G01–G03 |
| F5 | Wie bewerten sie eine Nutzung in den nächsten drei Monaten, und was planen sie? | A, I |
| F6 | Welche Weiterbildungsthemen werden gewünscht, welche Hindernisse genannt, welche Formate und Zeiten passen? | W01, W02, W03, X04, X05 |
| F7 | Unterscheiden sich diese Beschreibungen zwischen Bereichen und Geräteausstattung? | alle nach X01, X02 |

Alle Fragen sind beschreibend. Es gibt keine Hypothesentests über Ursachen.

### 6.2 Datenaufbereitung (Reihenfolge)

1. Formularexport sichern (schreibgeschützt). Export mit Datum und Prüfsumme protokollieren.
2. Übertragung in Kern- und Kontextdatei nach Abschnitt 4.5, mit Korrekturprotokoll.
3. Routine für den Kern ausführen. Bei Stopp Ursache klären, nicht umgehen.
4. Kontextdatei mit eigener Prüfroutine prüfen (gültige Codes, Höchstzahl, Exklusivität, alle IDs).
5. Verknüpfung über die Antwortkennung. Nicht verknüpfbare Fälle ausweisen.
6. Rücklauf: abgesendete Fragebögen gesamt und je Bereich (X01) im Verhältnis zur Beschäftigtenzahl aus B09. Keine Angabe in X01 als eigene Zeile.

### 6.3 Darstellung

| Inhalt | Darstellung | Pflichtangaben |
|---|---|---|
| C01–C06, X01–X03 | Häufigkeit und Anteil je Kategorie, Unsicherheitsoptionen als eigene Zeile | n gültig, n `KEINE_ANGABE` |
| U01–U06, K01–K06, L01–L03, G01–G03 | Verteilung 0–10 je Item (Balken), Median und Quartile | n gültig, n `NICHT_BEURTEILBAR`, n `KEINE_ANGABE` |
| A01–A04, I01–I03 | Verteilung 1–7 je Item, Median und Quartile | wie oben |
| Teilbereiche U, K, L, A, I | Mittelwert und Standardabweichung der vollständigen Personenwerte, zusätzlich Median | n vollständig, n unvollständig, Hinweis „vorläufiger deskriptiver Projektwert“ |
| W01, W02, X04, X05 | Anteil je Option an Personen mit gültiger Antwort | Nenner, n fehlend, Hinweis „Summe kann über 100 % liegen“ |
| W03 | Themenhäufigkeit, wenige nicht identifizierende Beispielaussagen | Zahl der Texte, Kodierregeln |
| Prüfhinweis C04/I | Anzahl Fälle | Erläuterung, dass das keine Fehlerkennung ist |

Getrennte Abbildungen für 0–10- und 1–7-Skalen. Keine gemeinsame Rangliste.

### 6.4 Gruppenvergleiche

- Gruppierung nach X01 (Bereich) und X02 (Gerät). Zusätzlich C01 und C04 als beschreibende Kreuztabellen, zum Beispiel W02 nach C04.
- **Mindestgruppengröße**: Ergebnisse einer Gruppe werden nur berichtet, wenn mindestens [n_min] Personen in der Gruppe eine gültige Angabe haben. Vorschlag: n_min = 10, vor Feldstart mit Betrieb und Datenschutz festzulegen (Rückfrage). Kleinere Gruppen werden zusammengefasst, zum Beispiel „Führung“ mit dem Bereich, oder nicht ausgewiesen. Die Regel gilt auch für jede Kreuztabellenzelle, die Rückschlüsse auf Personen erlaubt.
- Freitexte werden nie nach Gruppe aufgeschlüsselt, wenn die Gruppe unter n_min liegt.
- Unterschiede werden mit Fallzahlen beschrieben. Keine Signifikanztests als Entscheidungsgrundlage: Die Teilnahme ist freiwillig, die Stichprobe ist nicht zufällig, und die Instrumente sind nicht validiert. Wenn Konfidenzintervalle berichtet werden, dann nur als Hinweis auf Unschärfe, nicht als Beleg für die Belegschaft.

### 6.5 Prüfungen zur Datenqualität

| Prüfung | Vorgehen | Konsequenz |
|---|---|---|
| Rücklauf je Bereich | Anteil je X01 an B09 | Geringer Rücklauf in einem Bereich wird als Grenze berichtet. Aussagen für diesen Bereich nur mit Vorbehalt. |
| NB- und KA-Häufung | Anteil je Item, nach X01 und nach C02 = `D0` | Häufung bei Nichtnutzenden ist erwartbar. Nicht als niedrige Kompetenz werten. Frageverständnis prüfen. |
| Teilnahmeweg | Fehlwertanteile und Verteilungen nach X03 | Auffällige Unterschiede (zum Beispiel Tablet) als Hinweis auf Darstellungsprobleme berichten. |
| Gleichförmige Antworten | Anzahl Personen mit identischem Wert in allen 0–10-Items | Nur berichten. Nicht ausschließen, weil gleichförmige Einschätzungen plausibel sein können. |
| Prüfhinweis C04/I | Anzahl | Beschreiben, nichts ändern. |
| Interne Konsistenz | Cronbachs Alpha für U, K, L, A, I nur bei ausreichend vielen vollständigen Fällen, rein beschreibend | Kein Validitätsnachweis. Wird als erste Kennzahl für eine spätere Prüfung festgehalten. |

### 6.6 Vor Feldstart mit künstlichen Daten prüfen

- Künstlichen Datensatz mit `data_kind` = `SYNTHETIC_DEMO` erzeugen, der alle Sonderfälle enthält: lauter 0, lauter NB, gemischt, W01 mit `NONE`, W02 mit vier Kreuzen, Exklusivverstoß, C04 = `NO` mit I = 7, leere Kontextdatei für eine Person.
- Kernroutine und Kontextprüfung ausführen. Erwartete Ergebnisse vorher von Hand festlegen und vergleichen.
- Künstliche Ergebnisse nie in einen Bericht über den Betrieb übernehmen. Synthetische Antworten ersetzen keine realen Befragten (Bisbee et al., 2024).

### 6.7 Berichtsaufbau

1. Zweck, Vorgehen, Feldzeit, Teilnahmewege
2. Rücklauf gesamt und je Bereich, Grenzen
3. Betriebliche Voraussetzungen laut Checkliste B01–B10
4. Nutzung, Zugang, Regeln, Aufgabenpassung (F1–F3)
5. Selbsteinschätzungen (F4) und Einstellung, Absicht (F5)
6. Weiterbildungswünsche, Hindernisse, Formate, Zeiten (F6)
7. Unterschiede nach Bereich und Gerät (F7)
8. Befunde und mögliche Maßnahmen (Abschnitt 7)
9. Grenzen, offene Fragen, nächste Erhebung

Personenwerte bleiben in der Arbeitsdatei. Der Bericht enthält nur aggregierte Werte.

---

## 7. Plan zur Ableitung von Maßnahmen

### 7.1 Grundregeln

- Maßnahmen sind **Vorschläge auf Gruppenebene**. Es gibt keine Entscheidung über einzelne Beschäftigte und keine Einteilung von Personen.
- Organisatorische Hindernisse (Zugang, Gerät, Regeln, Zeit) werden zuerst als Aufgabe des Betriebs behandelt, nicht als Kompetenzlücke der Beschäftigten.
- Fehlende Nutzung ist kein Mangel. Generative KI kann für manche Tätigkeiten sachlich unnötig sein.
- „Viele“ oder „wenige“ wird immer durch die tatsächliche Zahl mit Bezugsgröße ersetzt, zum Beispiel „23 von 61 Personen mit gültiger Antwort in der Logistik“. Es gibt keine nachträglich erfundenen Grenzwerte.
- Selbsteinschätzungen sind keine gemessenen Fähigkeiten. Ein Lernbedarf aus Selbsteinschätzungen ist eine Hypothese, die eine praktische Aufgabe oder ein Gespräch klärt.

### 7.2 Zuordnung Befund zu möglicher Maßnahme

Die Zeilen M01–M09 übernehmen die Planungslogik des Codebuchs GARI-DE-0.1. M10–M13 ergänzen sie für das Kontextmodul und die Betriebs-Checkliste.

| Nr. | Beobachteter Befund | Einordnung | Mögliche Maßnahme | Weiterer Prüfbedarf |
|---|---|---|---|---|
| M01 | W01 = BASICS | Ausdrücklicher Lernwunsch | Einführung in Grundlagen generativer KI, Format nach X04 und Zeitfenster nach X05 | Vorkenntnisse (C02, C03, U, K) und Aufgaben (C06) der Gruppe prüfen |
| M02 | W01 = PROMPTING | Ausdrücklicher Lernwunsch | Übung zu Eingaben und Überarbeitung an Arbeitsbeispielen | Setzt ein freigegebenes Werkzeug voraus (C04, B02). Ohne Zugang erst M05. |
| M03 | W01 = VERIFY oder W02 = RELIABILITY | Lernwunsch oder wahrgenommene Unsicherheit | Quellen- und Ergebnisprüfung an Beispielen aus dem eigenen Bereich | G01 und G02 ergänzend beschreiben |
| M04 | W01 = DATA_RULES oder C05 = NOT_KNOWN / EXISTENCE_UNKNOWN | Orientierung, möglicherweise Organisation | Regeln verständlich bereitstellen (kurz, mit Beispielen, auch ohne PC zugänglich, zum Beispiel Aushang) | Mit B03, B04 klären, ob Regeln existieren und wie sie verteilt wurden. G03 ergänzend beschreiben. |
| M05 | C04 = NO oder W02 = ACCESS | Organisatorisches Hindernis | Freigegebene Zugangsmöglichkeiten klären | Mit B02, B05 abgleichen. Keine Kompetenzlücke behaupten. |
| M06 | C06 = NO oder W02 = TASK_FIT | Unklare oder fehlende Aufgabenpassung | Bedarf und geeignete Anwendungsfälle mit dem Bereich prüfen, W03 auswerten | Nutzung kann sachlich unnötig sein. Kein Schulungsdruck. |
| M07 | W02 = TIME | Rahmenbedingung | Lernzeit und Arbeitsorganisation prüfen, Zeitfenster nach X05 | B06 |
| M08 | Hohe Zahl NB auf einem Fähigkeitsitem (mit Anzahl und Bezugsgröße) | Unklare Einschätzbarkeit | Erst Frageverständnis und Erfahrungsgrundlage prüfen | Nicht als niedrige Kompetenz zählen. Nach C02, C03 aufschlüsseln. |
| M09 | Bestimmte Fähigkeitsantworten und passender Lernwunsch, zum Beispiel niedrige G01/G02 und W01 = VERIFY in derselben Gruppe | Mehrere zusammenpassende Hinweise | Vertiefenden Lernbedarf als Hypothese formulieren, praktische Aufgabe zur Abklärung anbieten | Zusammentreffen auf Gruppenebene beschreiben, keine Personenprofile |
| M10 | X02 = NO_DEVICE oder SHARED_DEVICE in einem Bereich | Organisatorisches Hindernis (Ausstattung) | Lernformate ohne eigenen PC planen (Schulungsraum, Gemeinschaftsgerät mit Zeitfenster, Papier-Kurzanleitung) | Mit B01 abgleichen. Nicht in Kompetenzaussage umdeuten. |
| M11 | X04 zeigt bevorzugte Formate je Bereich | Umsetzungshinweis | Format der Maßnahmen M01–M04 danach wählen | Präferenz ist kein Wirksamkeitsnachweis |
| M12 | W02 = KNOWLEDGE | Wahrgenommene Wissenslücke | Mit W01 abgleichen, welche Themen dahinterstehen. Einstieg nach M01 oder M02. | Selbstauskunft |
| M13 | W01 oder W02 = UNKNOWN bei vielen Personen (mit Zahl) oder W01 = NONE | Noch kein formulierter Bedarf oder kein Wunsch | Unverbindliches Kurzformat zum Kennenlernen anbieten, Ergebnisse von M06 abwarten | Kein Wunsch ist eine legitime Antwort |

### 7.3 Priorisierung

Transparent nach drei Kriterien, ohne versteckte Gewichtung. Jedes Kriterium wird für jede Maßnahme getrennt als Text mit Zahlen festgehalten.

1. **Geäußerte Wünsche**: Zahl und Anteil der Personen mit passendem W01- oder W02-Eintrag, je Bereich.
2. **Aufgabenrelevanz**: C06 = YES und W03-Themen im Bereich.
3. **Umsetzbarkeit**: Zugang, Regeln, Lernzeit, Format laut B01–B07. Maßnahmen, die ein nicht vorhandenes Werkzeug brauchen, folgen auf die organisatorische Klärung.

Daraus folgt eine sinnvolle Reihenfolge: zuerst organisatorische Voraussetzungen klären (M04, M05, M07, M10), dann Grundlagen und Regeln für alle, die das wünschen (M01, M04), dann Anwendung und Prüfen für Gruppen mit Zugang und Aufgabenpassung (M02, M03, M09). Die tatsächliche Reihenfolge wird erst mit Daten festgelegt.

### 7.4 Vorlage für jede Empfehlung

| Feld | Inhalt |
|---|---|
| Befund-ID | zum Beispiel M03-LOG |
| Item-IDs | zum Beispiel W01, W02, G01, G02 |
| Datenart | `SURVEY` (nie `SYNTHETIC_DEMO` oder `PRETEST`) |
| Fallzahl | gültige Antworten / Personen in der Gruppe / Beschäftigte laut B09 |
| Beobachtung | wörtlich die Zahlen |
| Lern- oder Organisationsziel | zum Beispiel „Beschäftigte der Logistik kennen die geltenden Eingaberegeln“ |
| Mögliche Maßnahme | Format, Zeitfenster, Zuständigkeit |
| Unsicherheit | Rücklauf, Selbstbericht, Fehlwerte, Kleinheit der Gruppe |
| Erfolgskontrolle | siehe 7.5 |

### 7.5 Erfolgskontrolle

- Wiederholung derselben Items nach der Maßnahme mit **unveränderter** Version, damit Werte vergleichbar bleiben. Veränderungen nur auf Gruppenebene beschreiben. Eine Änderung kann auch andere Ursachen haben, zum Beispiel neuen Zugang.
- Organisatorische Kennzahlen aus der Checkliste: Zugang geschaffen (B02), Regeln verteilt (B03), Lernzeit bereitgestellt (B06).
- Kurze praktische Aufgabe am Ende einer Schulung, zum Beispiel eine KI-Antwort mit Quellenangabe prüfen. Ergebnis nur anonym und aggregiert.
- Teilnahme und Rückmeldung zu Maßnahmen getrennt von der Readiness-Befragung erfassen.

---

## 8. Ablauf, Grenzen und offene Rückfragen

### 8.1 Ablauf bis zum Bericht

| Schritt | Inhalt |
|---|---|
| 1 | Rückfragen 8.3 klären, Platzhalter füllen, Betriebs-Checkliste B01–B10 ausfüllen |
| 2 | Formular bauen, Darstellung auf Tablet, Smartphone und PC prüfen (13-stufige Skala, Seitenumbruch, Höchstzahlen) |
| 3 | Verständnistest der Rahmentexte und X01–X05 mit wenigen Personen aus Produktion und Logistik, auch ohne KI-Erfahrung. Kernitems nur auf technische Darstellung prüfen, Wortlaut bleibt. |
| 4 | Künstliche Daten und Routinen testen (6.6) |
| 5 | Feldphase lang genug, dass alle Schichten erreicht werden. Einladung über mehrere Wege (B10). |
| 6 | Export, Übertragung, Auswertung nach Abschnitt 6 |
| 7 | Bericht, Rückmeldung an Beschäftigte, Maßnahmenplanung nach Abschnitt 7 |

### 8.2 Grenzen

- Selbstberichte. Keine beobachtete Kompetenz.
- Die adaptierten Items sind nicht für generative KI im Arbeitskontext validiert. Die Teilbereichsmittel sind vorläufige deskriptive Projektwerte.
- Für A und I ist der Wortlaut nicht mit dem OSF-Originalanhang abgeglichen.
- Kontextfragen X01–X05 und die Rahmentexte sind neu und ungeprüft.
- Freiwillige Teilnahme. Wer mit KI wenig anfangen kann oder wenig Zeit hat, nimmt eventuell seltener teil. Der Rücklauf je Bereich zeigt das nur zum Teil.
- Ohne Kennung sind Mehrfachteilnahmen nicht ausschließbar.
- Die Kernversion GARI-DE-0.1 wurde für den Verständlichkeitstest festgehalten. Die geschätzte Dauer ist nicht gemessen.
- Das Unternehmen ist fiktiv. Alles hier ist ein Verfahrensplan, kein Befund.

### 8.3 Offene Rückfragen

Diese Punkte kann ich ohne Antwort nicht entscheiden. Bis zur Klärung gelten die markierten Vorschläge.

1. **Version**: Gilt die Anfügung von Teil 6 und die ersetzte Einleitung als neue Gesamtversion (zum Beispiel GARI-DE-0.1-S2), oder reicht die getrennte Dokumentation als Erhebungsfassung S2-E1 plus KX-S2-0.1? Vorschlag: getrennte Dokumentation wie hier, Kern bleibt GARI-DE-0.1.
2. **Mindestgruppengröße**: Welche Zahl gilt? Vorschlag: 10.
3. **Bereiche**: Passen die vier Bereiche und „Anderer Bereich“ zur tatsächlichen Organisation? Gehören Instandhaltung oder Qualität zur Produktion?
4. **Führung**: Soll Führung als eigener Bereich gelten (wie im Briefing) oder als Zusatzfrage zum Bereich? Vorschlag: eigener Bereich, ggf. mit anderem Bereich zusammenfassen, wenn unter n_min.
5. **Formularwerkzeug**: Welches System, und erfüllt es die Anforderungen an Speicherort, Datenschutz und Kioskbetrieb am Tablet?
6. **Arbeitszeit**: Gilt die Teilnahme als Arbeitszeit, auch in der Pause am Tablet?
7. **Arbeitnehmervertretung und Datenschutz**: Wer gibt die Befragung frei, und welcher Datenschutzhinweis wird verlinkt?
8. **Mehrsprachigkeit**: Laut Briefing ist die Sprache Deutsch. Gibt es Beschäftigte, die eine einfachere oder übersetzte Fassung brauchen? Eine Übersetzung wäre eine neue Version.
9. **Rechte**: Ist die Verwendung der adaptierten MAILS- und PowerPilot-Items im Betrieb und in einer möglichen Veröffentlichung geklärt?
10. **Wiederholung**: Ist eine zweite Erhebung nach den Maßnahmen geplant? Davon hängt die Erfolgskontrolle in 7.5 ab.
