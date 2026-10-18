# Fragebogen zur Readiness für generative KI bei Mitarbeitenden

Erhebungspaket für das Szenario S3 · Kern GARI-DE-0.1 mit Kontextmodul S3-K-0.1 · Stand 18. Oktober 2026

Fiktives Unternehmen mit 1.200 Beschäftigten an mehreren Standorten. Verfahrensdemonstration. Es liegen keine Befragungsdaten vor. Alle Aussagen unten sind deshalb Plan, Regel oder Vorlage. Kein Ergebnis, keine Zahl zu Beschäftigten und keine Maßnahme ist aus Daten abgeleitet.

## Inhalt

1. Kurzüberblick und Grundentscheidungen
2. Offene Rückfragen und getroffene Arbeitsannahmen
3. Fragebogen (Erhebungsfassung für das Onlineformular)
4. Gesonderte Erfassung der betrieblichen Voraussetzungen
5. Quellenzuordnung
6. Codebuch
7. Auswertungsplan
8. Plan für die Ableitung von Maßnahmen
9. Grenzen
10. Prüfliste vor dem Start

---

## 1. Kurzüberblick und Grundentscheidungen

**Zweck laut Briefing.** Status quo beschreiben. Hinweise auf Weiterbildungsbedarf ableiten. Betriebliche Voraussetzungen gesondert erfassen. Lernwünsche je Funktion sichtbar machen. Ergebnisse je Standort.

**Was der Fragebogen leistet.** Er beschreibt Selbsteinschätzungen, Nutzungshäufigkeit, Zugang, Regelkenntnis, Einstellung, Nutzungsabsicht, Lernwünsche und Hindernisse. Er misst keine tatsächliche Kompetenz. Er liefert keinen Gesamtscore, keine Reifegradstufe und keine Einteilung in „bereit“ oder „nicht bereit“. Er dient nicht zur Bewertung einzelner Personen.

**Grundentscheidungen.**

| Nr. | Entscheidung | Begründung |
|---|---|---|
| E1 | Der Kern GARI-DE-0.1 (34 Items C01–W03) wird unverändert übernommen: Definition, Wortlaut, Antwortformate, Reihenfolge, Zeitbezüge und Kerninstruktionen. | Vorgabe der Itembank (`context_changes_allowed`) und des Codebuchs. Jede Änderung würde eine neue Fragebogenversion erzeugen und die Vergleichbarkeit verändern. |
| E2 | Nur die organisatorische Pretest-Rahmung (Untertitel, Einleitung, Testkürzel, Schlusssatz zum Gespräch) wird durch eine Erhebungsrahmung ersetzt. Das ist als gesonderte Erhebungsfassung dokumentiert. | Die Itembank erlaubt das ausdrücklich (`frozen_text_note`). Der Hinweis auf ein begleitendes Gespräch passt nicht zu einer freiwilligen Onlinebefragung. |
| E3 | Die Kontextfragen stehen als eigenes Modul S3-K-0.1 **nach** dem Kern (Z01–Z04). | So bleibt die geprüfte Reihenfolge und Startsituation des Kerns erhalten. Die Kontextfragen sind neu und ungeprüft. Sie werden getrennt kodiert und gespeichert. |
| E4 | Keine Sprungregeln. Alle Fragen werden allen Personen gezeigt. Keine Pflichtfelder. | Codebuch: filterlose Fassung. Freiwillige Teilnahme. Personen ohne bisherige Nutzung gehören ausdrücklich zur Zielgruppe. |
| E5 | Betriebliche Voraussetzungen werden zusätzlich bei Fachstellen erhoben, nicht nur bei Mitarbeitenden (Abschnitt 4). | Briefing: „gesondert erfassen“. C04 und C05 zeigen Wahrnehmung. Ob Zugang und Regeln tatsächlich existieren, ist eine Organisationsfrage. |
| E6 | Standort- und Funktionsauswertungen nur oberhalb einer Mindestgruppengröße. | Schutz der Teilnehmenden. Das Codebuch verlangt, zulässige Gruppenberichte gesondert festzulegen. |
| E7 | Keine weiteren demografischen Merkmale (Alter, Geschlecht, Betriebszugehörigkeit). | Für den Zweck nicht nötig. Jedes weitere Merkmal erhöht das Risiko der Wiedererkennbarkeit in kleinen Gruppen. |

---

## 2. Offene Rückfragen und getroffene Arbeitsannahmen

Eine Rückfrage war in diesem Lauf nicht möglich. Die folgenden Punkte bitte vor dem Start klären. Bis dahin gilt jeweils die genannte Arbeitsannahme.

| Nr. | Rückfrage | Arbeitsannahme in diesem Paket |
|---|---|---|
| R1 | Wie heißen die Standorte und wie viele Beschäftigte arbeiten jeweils dort? | Z03 enthält eine vom Unternehmen zu befüllende Liste mit Codes S01, S02 und so weiter je tatsächlichem Standort. Ohne Kopfzahlen je Standort kann keine Teilnahmequote je Standort berechnet werden. |
| R2 | Ist „Führung“ ein eigener Tätigkeitsbereich oder eine Rolle innerhalb der Bereiche? | Führung wird als Rolle erfasst (Z02), nicht als Bereich in Z01. Eine Vertriebsleitung bleibt so im Vertrieb sichtbar und zugleich in der Gruppe mit Führungsverantwortung. Für Berichte heißt „Führung“ dann: Z02 = YES. |
| R3 | Was bedeutet „Entwicklung“ im Unternehmen (Produkt-, Software-, Organisationsentwicklung)? | Der Begriff aus dem Briefing wird ohne Zusatz verwendet. Bei Unklarheit im Pretest des Moduls nachschärfen. |
| R4 | Welche Mindestgruppengröße für Berichte ist mit Datenschutz und Arbeitnehmervertretung vereinbart? | Vorschlag: mindestens 10 gültige Antworten je berichteter Gruppe. Das ist eine eigene Planungsannahme, keine aus den Quellen belegte Regel. |
| R5 | Welche Plattform wird für das Onlineformular verwendet? Speichert sie IP-Adressen, Zeitstempel oder Anmeldedaten? | Plattform offen. Annahme: Zugang über einen allgemeinen Link ohne Anmeldung, ohne personenbezogene Einladungslinks, IP-Speicherung deaktiviert. |
| R6 | Welche GenAI-Werkzeuge sind aktuell wo freigegeben, und gibt es schriftliche Regeln? | Wird über die Organisationserfassung in Abschnitt 4 geklärt, nicht vorausgesetzt. |
| R7 | Darf die papierbezogene Kerninstruktion „Kreisen Sie … ein“ für das Onlineformular sprachlich angepasst werden? | Nein, sie bleibt wörtlich. Eine Anpassung wäre eine Änderung der Instruktion und erfordert laut Codebuch eine neue Version. Siehe Abschnitt 3.1. |
| R8 | Feldzeit, Erinnerungen, Absender der Einladung, Empfänger der Berichte? | Vorschlag: drei Wochen Feldzeit, zwei Erinnerungen an alle, Einladung über einen allgemeinen Kanal, Berichte nur aggregiert an Projektverantwortliche, Geschäftsführung und Arbeitnehmervertretung. |
| R9 | Haben alle Beschäftigten, auch ohne Bildschirmarbeitsplatz, Zugang zum Link während der Arbeitszeit? | Annahme: ja, etwa über Tablet, Terminal oder Mobilgerät. Sonst entsteht eine systematische Lücke bei C01 = OTHER_WORK. |

---

## 3. Fragebogen (Erhebungsfassung für das Onlineformular)

### 3.1 Hinweise zur technischen Umsetzung

- Seitenaufteilung wie unten. Kern auf Seite 2 bis 6, Kontextmodul auf Seite 7.
- Keine Pflichtfelder. Leere Felder werden als KEINE_ANGABE kodiert.
- Einzelwahl (C01–C06, Z01–Z03): Optionsfelder, genau eine Auswahl technisch möglich.
- Skalen 0–10 und 1–7: je Item eine Einzelwahl mit den Zahlen plus „NB“ und „KA“ in genau dieser Reihenfolge. Keine Zwischenanker ergänzen. Keine vorausgewählten Werte. Keine Schieberegler, weil diese einen Startwert nahelegen.
- W01 und W02: Kästchen mit technischer Begrenzung auf höchstens drei Antworten. Z04: höchstens zwei. Die Begrenzung vor dem Start mit Testeinträgen prüfen, auch beim Wechsel zwischen Seiten. In der Projektprüfung trat bei einer Formularumsetzung eine Fehlfunktion beim Seitenwechsel auf (Quellen_APA.md, Abschnitt zur Forms-Umsetzung). Exklusive Optionen (NONE, UNKNOWN, KA) lassen sich in vielen Werkzeugen nicht technisch erzwingen. Widersprüche werden dann nach Codebuch behandelt (Abschnitt 6.4).
- Die Kerninstruktion „Kreisen Sie pro Aussage eine Zahl ein“ bleibt wörtlich, weil sie zum eingefrorenen Kern gehört. Online ist „einkreisen“ als „auswählen“ zu verstehen. Ob das stört, gehört in den kurzen Funktionstest vor dem Start (Abschnitt 10). Wird der Satz geändert, ist das eine neue Version, die getrennt ausgewertet wird.
- Antwortnummer statt Testkürzel: Die Plattform vergibt je abgeschicktem Formular eine zufällige, nicht sprechende Antwortnummer. Keine Namen, keine Personalnummern, keine E-Mail-Adressen.

### 3.2 Seite 1 · Einleitung (Erhebungsrahmung, ersetzt die Pretest-Rahmung)

**Fragebogen zum Umgang mit generativer KI**

Erhebungsfassung · Kern GARI-DE-0.1 mit Kontextmodul S3-K-0.1 · [Feldzeit eintragen]

Dieser Fragebogen erfasst Ihre Erfahrungen, Einschätzungen und Weiterbildungswünsche zu generativer KI bei der Arbeit. Die Ergebnisse helfen bei der Planung passender Weiterbildung und Unterstützung. Es geht nicht um die Bewertung Ihrer Arbeitsleistung. Geschätzte Dauer: etwa 15 Minuten.

Generative KI erzeugt oder bearbeitet auf Eingaben hin Inhalte, zum Beispiel Texte, Bilder, Audio, Videos oder Programmcode. Gemeint sind sowohl eigenständige Anwendungen als auch entsprechende Funktionen in anderen Programmen.

Die Teilnahme ist freiwillig. Sie können einzelne Fragen auslassen oder jederzeit abbrechen. Es gibt keine richtigen oder falschen Antworten. Auch wenn Sie generative KI noch nie genutzt haben, ist Ihre Teilnahme wichtig. Bitte tragen Sie keine Namen, Personalnummern oder vertraulichen Informationen ein.

Wir fragen nicht nach Ihrem Namen. Ergebnisse werden nur zusammengefasst berichtet, und nur für Gruppen mit mindestens [Mindestgruppengröße laut R4] Antworten. Kleinere Gruppen werden zusammengelegt oder nicht ausgewiesen. Rückfragen zur Befragung: [Kontaktstelle eintragen]. Informationen zum Datenschutz: [Link eintragen].

Hinweis zur Dauer: Für den Kern sind 10 bis 15 Minuten geschätzt, noch nicht gemessen. Das Kontextmodul verlängert die Bearbeitung leicht. Der Wert in der Einleitung ist nach dem Funktionstest zu bestätigen.

### 3.3 Seite 2 bis 6 · Kern GARI-DE-0.1 (wörtlich aus der Itembank)

Die Einträge „☐ Keine Angabe“ bei C01–C06 und die Optionen „NB“ und „KA“ sind Teil des Kerns. Die Seitenumbrüche folgen den Abschnittsüberschriften der Befragungsfassung.


#### Seite 2 · Ihre Tätigkeit und bisherige Nutzung

> Bitte wählen Sie pro Frage genau eine Antwort.

**C01**  Wie sieht Ihre hauptsächliche Tätigkeit aus?

- ☐ Überwiegend Büro- oder Bildschirmarbeit
- ☐ Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst
- ☐ Etwa gleich große Anteile beider Bereiche
- ☐ Keine Angabe

**C02**  An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt?

- ☐ An keinem Tag
- ☐ An 1 bis 3 Tagen
- ☐ An 4 bis 9 Tagen
- ☐ An 10 bis 15 Tagen
- ☐ An 16 oder mehr Tagen
- ☐ Kann ich nicht einschätzen
- ☐ Keine Angabe

**C03**  Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt?

- ☐ Ja
- ☐ Nein
- ☐ Ich bin mir nicht sicher
- ☐ Keine Angabe

**C04**  Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen?

- ☐ Ja
- ☐ Nein
- ☐ Ich weiß es nicht
- ☐ Keine Angabe

**C05**  Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit?

- ☐ Ja
- ☐ Teilweise
- ☐ Nein
- ☐ Ich weiß nicht, ob es solche Regeln gibt
- ☐ Keine Angabe

**C06**  Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre?

- ☐ Ja
- ☐ Nein
- ☐ Kann ich noch nicht beurteilen
- ☐ Keine Angabe


#### Seite 3 · Anwendung und Verständnis

> Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

> 0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

> NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**U01**  Ich kann eine generative KI bedienen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**U02**  Ich kann mir berufliche Aufgaben durch generative KI erleichtern.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**U03**  Ich kann generative KI gezielt für meine Arbeitsziele einsetzen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**U04**  Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**U05**  Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**U06**  Ich kann generativer KI verständlich mitteilen, was ich brauche.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**K01**  Ich kenne die zentralen Konzepte generativer KI.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**K02**  Ich kann erklären, was generative KI bedeutet.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**K03**  Ich kann Chancen und Grenzen generativer KI einschätzen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**K04**  Ich kann Vor- und Nachteile generativer KI beurteilen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**K05**  Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**K06**  Ich kann mir künftige Anwendungen generativer KI vorstellen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`


#### Seite 4 · Lernen und Prüfen

> Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

> 0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

> NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**L01**  Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**L02**  Ich kann mich über Neuerungen bei generativer KI informieren.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**L03**  Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**G01**  Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**G02**  Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

**G03**  Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA`

> Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.


#### Seite 5 · Einstellung und geplante Nutzung

> Wie sehr stimmen Sie den folgenden Aussagen zu? Gemeint ist die Nutzung für Ihre beruflichen Aufgaben in den kommenden drei Monaten. „Freigegeben“ bedeutet, dass Ihr Unternehmen die betreffende Nutzung erlaubt.

> 1 = stimme überhaupt nicht zu   ·   7 = stimme vollständig zu

> NB = nicht beurteilbar   ·   KA = keine Angabe. Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein.

**A01**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft.

`1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA`

**A02**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend.

`1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA`

**A03**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig.

`1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA`

**A04**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm.

`1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA`

> Für die folgenden drei Aussagen: Denken Sie an die Bedingungen, die Sie in den nächsten drei Monaten tatsächlich erwarten. Setzen Sie keinen gesicherten Zugang voraus, wenn dieser unklar ist. Fehlender Zugang bedeutet jedoch nicht automatisch, dass Sie nicht antworten können.

**I01**  Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

`1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA`

**I02**  Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

`1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA`

**I03**  Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen.

`1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA`


#### Seite 6 · Weiterbildung und Unterstützung

> Bei W01 und W02 sind jeweils höchstens drei Antworten möglich. „Kein Weiterbildungswunsch“, „derzeit nichts“, „kann ich noch nicht einschätzen“ und „keine Angabe“ dürfen innerhalb einer Frage nur allein gewählt werden.

**W01**  Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen.

- ☐ Grundlagen generativer KI

- ☐ Passende Einsatzmöglichkeiten für meine Aufgaben

- ☐ Klare Eingaben formulieren und Ergebnisse verbessern

- ☐ Antworten und Quellen überprüfen

- ☐ Betriebliche Regeln und zulässige Dateneingaben

- ☐ Bei neuen Entwicklungen auf dem Laufenden bleiben

- ☐ Anderes Thema

- ☐ Derzeit kein Weiterbildungswunsch

- ☐ Ich kann meinen Bedarf noch nicht einschätzen

- ☐ Keine Angabe

**W02**  Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen.

- ☐ Kein Zugang zu einem freigegebenen Werkzeug

- ☐ Unklare betriebliche Regeln

- ☐ Zu wenig Zeit zum Ausprobieren oder Lernen

- ☐ Mir fehlt Wissen über die Nutzung

- ☐ Ich erkenne keinen passenden Einsatz für meine Aufgaben

- ☐ Unsicherheit über die Verlässlichkeit der Ergebnisse

- ☐ Etwas anderes

- ☐ Derzeit nichts

- ☐ Kann ich noch nicht einschätzen

- ☐ Keine Angabe

**W03**  Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen.

- ☐ Keine Angabe

Freitextfeld (mehrzeilig)


### 3.4 Seite 7 · Kontextmodul S3-K-0.1 (neu, ungeprüft)

> Zum Schluss noch einige Angaben zu Ihrem Arbeitsbereich. Sie dienen nur dazu, Ergebnisse für größere Gruppen zusammenzufassen. Sie können jede Frage auslassen.

**Z01**  In welchem Bereich arbeiten Sie hauptsächlich?

- ☐ Vertrieb
- ☐ Kundendienst
- ☐ Entwicklung
- ☐ Verwaltung
- ☐ Personal
- ☐ Anderer Bereich
- ☐ Keine Angabe

**Z02**  Haben Sie Führungsverantwortung für andere Beschäftigte?

- ☐ Ja
- ☐ Nein
- ☐ Keine Angabe

**Z03**  An welchem Standort arbeiten Sie überwiegend?

- ☐ [Standort 1 laut Unternehmensliste]
- ☐ [Standort 2 laut Unternehmensliste]
- ☐ [je ein weiteres Feld für jeden weiteren tatsächlichen Standort]
- ☐ An mehreren Standorten etwa gleich viel
- ☐ Keine Angabe

**Z04**  In welcher Form würden Sie am liebsten zu generativer KI lernen? Bitte höchstens zwei Antworten auswählen.

- ☐ Kurze Lerneinheiten zum Selbstlernen am Bildschirm
- ☐ Live-Schulung online
- ☐ Schulung vor Ort
- ☐ Begleitung bei eigenen Arbeitsaufgaben
- ☐ Austausch mit Kolleginnen und Kollegen
- ☐ Keine Präferenz
- ☐ Keine Angabe

> „Keine Präferenz“ und „Keine Angabe“ bitte nur allein wählen.

### 3.5 Seite 8 · Abschluss (Erhebungsrahmung)

Vielen Dank für Ihre Teilnahme. Ihre Antworten sind gespeichert. Die zusammengefassten Ergebnisse werden voraussichtlich bis [Datum] über [Kanal] vorgestellt.

### 3.6 Begründung der Kontextfragen

| ID | Zweck | Warum so |
|---|---|---|
| Z01 | Lernwünsche (W01), Hindernisse (W02), Aufgabenpassung (C06) und Nutzung (C02) je Funktion beschreiben. | Bereiche aus dem Briefing. „Anderer Bereich“ verhindert erzwungene Fehlzuordnung. Führung bewusst nicht hier (R2). |
| Z02 | Führungskräfte als eigene Gruppe sichtbar machen. | Führungsrolle quer zu den Bereichen. Führungskräfte prägen Lernzeit und Regeln für ihr Team. Do Khac et al. (2025) zeigen, dass Entscheidungstragende eine eigene Perspektive auf GenAI haben. Ihre Items werden nicht übernommen. |
| Z03 | Ergebnisse je Standort, besonders Zugang (C04) und Regelkenntnis (C05). | Briefing-Wunsch. Unterschiede zwischen Standorten können organisatorisch bedingt sein, etwa durch unterschiedliche Einführung von Werkzeugen. |
| Z04 | Format der Maßnahmen planen. | Ohne diese Angabe lässt sich nur das Thema, nicht die Form der Weiterbildung ableiten. Die Frage ist bewusst kurz und auf zwei Antworten begrenzt. |

C01 (Art der Tätigkeit) aus dem Kern bleibt zusätzlich bestehen. C01 und Z01 erfassen Verschiedenes: Arbeitsform und Funktionsbereich.

---

## 4. Gesonderte Erfassung der betrieblichen Voraussetzungen

Diese Erfassung füllen IT, Personalentwicklung, Datenschutz oder Informationssicherheit aus, nicht die Mitarbeitenden. Stichtag: Beginn der Feldzeit. Sie beschreibt, was organisatorisch tatsächlich vorhanden ist. So lassen sich Wahrnehmung (C04, C05, W02) und Ausgangslage getrennt lesen. Die Angaben fließen nicht in Personenwerte ein.

| Nr. | Frage an die Organisation | Erfassung | Bezug im Mitarbeitendenfragebogen |
|---|---|---|---|
| O1 | Welche GenAI-Werkzeuge oder -Funktionen sind für die berufliche Nutzung freigegeben? | Liste je Werkzeug | C04, I01–I03, W02 = ACCESS |
| O2 | Für welche Standorte und Funktionsbereiche gilt die Freigabe? | Matrix Standort × Bereich: ja, teilweise, nein | C04 je Z03 und Z01 |
| O3 | Gibt es schriftliche Regeln zum Einsatz generativer KI? Seit wann? Wo sind sie veröffentlicht? | Ja oder nein, Datum, Ablageort | C05, W02 = RULES |
| O4 | Regeln die Vorgaben, welche Daten eingegeben werden dürfen? | Ja oder nein, Kurzbeschreibung | G03, W01 = DATA_RULES |
| O5 | Gibt es eine benannte Ansprechstelle für Fragen? | Ja oder nein, Stelle | C05 = EXISTENCE_UNKNOWN |
| O6 | Welche Weiterbildungsangebote zu generativer KI gibt es bereits? | Liste mit Thema, Format, Zielgruppe | W01, Z04 |
| O7 | Gibt es eine Regelung für Lernzeit während der Arbeitszeit? | Ja oder nein, Umfang | W02 = TIME |
| O8 | Welche Einführungen von Werkzeugen sind in den nächsten drei Monaten geplant? | Liste mit Standort und Zeitpunkt | I01–I03, Prüfflag C04 = NO bei I ≥ 6 |

Begründung: Wichmann et al. (2026) ordnen Arbeitsergebnisse in ein sozio-technisches Gefüge aus technischen und sozialen Arbeitsbedingungen ein. Daraus folgt hier nur die Planungsentscheidung, Bedingungen getrennt von Selbsteinschätzungen zu erfassen. Die Studie liefert keine Items für diesen Fragebogen.

---

## 5. Quellenzuordnung

### 5.1 Quellen je Item

Status laut Itembank: ADAPTIERT bedeutet Anpassung eines Originalitems. NEU_ENTWICKELT bedeutet Eigenentwicklung ohne Originalitem. Kein Item ist im Projekt empirisch geprüft. Keine Teilskala ist psychometrisch validiert.

| ID | Teilbereich | Status | Quelle | Fundstelle | Anpassung laut Itembank | Wortlautabgleich und Grenze |
|---|---|---|---|---|---|---|
| C01 | Kontext Kern | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| C02 | Kontext Kern | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| C03 | Kontext Kern | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| C04 | Kontext Kern | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| C05 | Kontext Kern | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| C06 | Kontext Kern | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| U01 | Anwendung | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 1, Seite 1; Zuordnung und Mittelwertregel Seite 3. | KI-Bezug auf generative KI eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| U02 | Anwendung | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 2, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Erleichterung des Lebens auf berufliche Aufgaben eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| U03 | Anwendung | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 3, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Zielbezug auf Arbeitsziele eingegrenzt; sinnvoll durch gezielt konkretisiert. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| U04 | Anwendung | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 4, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Alltagsinteraktion auf Zusammenarbeit bei der Arbeit übertragen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| U05 | Anwendung | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 5, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gewinnbringende Zusammenarbeit über brauchbare Arbeitsergebnisse konkretisiert; Bedeutungsverschiebung im Pretest prüfen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| U06 | Anwendung | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 6, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gewinnbringende Kommunikation über verständliches Mitteilen konkretisiert; Ergebnisaspekt verengt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| K01 | Verständnis | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 7, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Allgemeine KI auf generative KI eingegrenzt; Konzepte bleibt bewusst zur Verständlichkeitsprüfung erhalten. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| K02 | Verständnis | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 8, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Kenntnis von Definitionen in selbst eingeschätzte Erklärfähigkeit übertragen; stärkere Anpassung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| K03 | Verständnis | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 9, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| K04 | Verständnis | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 10, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| K05 | Verständnis | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 11, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Verwendungszwecke sprachlich vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| K06 | Verständnis | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 12, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz verkürzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| L01 | Lernen | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 26, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; stets entfällt. Deutsche Itemnummer 26 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| L02 | Lernen | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 27, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; deutsche Itemnummer 27 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| L03 | Lernen | ADAPTIERT | Carolus et al. (2023), deutscher MAILS-Autorenfragebogen | Deutscher Autorenfragebogen, Item 28, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; sprachliche Verdichtung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | Originalwortlaut an der deutschen PDF geprüft. Evidenz: allgemeine KI, Selbstbericht, 300 Erwachsene. Rechte für veränderte Fassung offen. |
| G01 | Prüfen | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| G02 | Prüfen | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| G03 | Prüfen | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| A01 | Einstellung | ADAPTIERT | Wichmann et al. (2025), bereitgestellte Itemsammlung Questionnaire 2 / PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Original: „The use of PowerPilot would be … advantageous.“. Abgleich mit bereitgestellter Itemsammlung; OSF-Anhang GEBK9 nicht abrufbar, Gleichheit offen. |
| A02 | Einstellung | ADAPTIERT | Wichmann et al. (2025), bereitgestellte Itemsammlung Questionnaire 2 / PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Original: „The use of PowerPilot would be … satisfactory.“. Abgleich mit bereitgestellter Itemsammlung; OSF-Anhang GEBK9 nicht abrufbar, Gleichheit offen. |
| A03 | Einstellung | ADAPTIERT | Wichmann et al. (2025), bereitgestellte Itemsammlung Questionnaire 2 / PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Original: „The use of PowerPilot would be … important.“. Abgleich mit bereitgestellter Itemsammlung; OSF-Anhang GEBK9 nicht abrufbar, Gleichheit offen. |
| A04 | Einstellung | ADAPTIERT | Wichmann et al. (2025), bereitgestellte Itemsammlung Questionnaire 2 / PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 4; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | Original: „The use of PowerPilot would be … enjoyable.“. Abgleich mit bereitgestellter Itemsammlung; OSF-Anhang GEBK9 nicht abrufbar, Gleichheit offen. |
| I01 | Nutzungsabsicht | ADAPTIERT | Wichmann et al. (2025), bereitgestellte Itemsammlung Questionnaire 2 / PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Original: „I plan to use PowerPilot in the future.“. Abgleich mit bereitgestellter Itemsammlung; OSF-Anhang GEBK9 nicht abrufbar, Gleichheit offen. |
| I02 | Nutzungsabsicht | ADAPTIERT | Wichmann et al. (2025), bereitgestellte Itemsammlung Questionnaire 2 / PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Original: „I intend to use PowerPilot in the future.“. Abgleich mit bereitgestellter Itemsammlung; OSF-Anhang GEBK9 nicht abrufbar, Gleichheit offen. |
| I03 | Nutzungsabsicht | ADAPTIERT | Wichmann et al. (2025), bereitgestellte Itemsammlung Questionnaire 2 / PowerPilot | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | Original: „I will definitely use PowerPilot in the future.“. Abgleich mit bereitgestellter Itemsammlung; OSF-Anhang GEBK9 nicht abrufbar, Gleichheit offen. |
| W01 | Weiterbildung | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| W02 | Weiterbildung | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |
| W03 | Weiterbildung | NEU_ENTWICKELT | Eigenentwicklung, kein Originalitem | – | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Kein Abgleich möglich. Noch nicht empirisch geprüft. |

Kontextmodul S3-K-0.1:

| ID | Status | Quelle | Anmerkung |
|---|---|---|---|
| Z01 | NEU_ENTWICKELT | Eigenentwicklung auf Basis der Tätigkeitsbereiche im Briefing | Kein Originalitem. Nicht getestet. |
| Z02 | NEU_ENTWICKELT | Eigenentwicklung auf Basis des Briefings (Bereich „Führung“) | Kein Originalitem. Nicht getestet. |
| Z03 | NEU_ENTWICKELT | Eigenentwicklung auf Basis des Briefing-Wunsches „Ergebnisse je Standort“ | Kein Originalitem. Nicht getestet. Antwortliste vom Unternehmen. |
| Z04 | NEU_ENTWICKELT | Eigenentwicklung für die Maßnahmenplanung | Kein Originalitem. Nicht getestet. |

### 5.2 Rolle der übrigen Quellen

| Quelle | Verwendung in diesem Paket | Grenze |
|---|---|---|
| Ajzen (o. J.), Constructing a TPB questionnaire | Verhalten über Ziel, Handlung, Kontext und Zeit definiert: „freigegebene generative KI“, „berufliche Aufgaben“, „nächste drei Monate“ in A01–A04 und I01–I03. | Kein Erscheinungsjahr in der Fassung. Keine vollständige TPB-Erhebung; subjektive Norm und wahrgenommene Verhaltenskontrolle sind nicht als Skalen enthalten. |
| Carolus et al. (2023), MAILS | Grundlage für U01–U06, K01–K06, L01–L03 und die Antwortanker 0–10. Motivation der Teilbereichsmittelwerte. | Evidenz betrifft allgemeine KI, Selbstberichte, 300 deutschsprachige Erwachsene. Übertragung auf generative KI am Arbeitsplatz ungeprüft. Nachnutzungsrechte der veränderten Fassung offen. |
| Koch et al. (2024), MAILS-Kurzfassung | Geprüft und bewusst nicht eingesetzt. | Kurzfassung enthält KI-Entwicklung und passt nur teilweise zum Zweck. Weitere Validierung gefordert. |
| Wichmann et al. (2025), PowerPilot | Grundlage für A01–A04 und I01–I03 sowie das siebenstufige Zustimmungsformat. | Energie-App-Kontext. Wortlautvergleich mit OSF-Anhang offen. |
| Paetow et al. (2026), Task-technology fit | Gedanklicher Hintergrund für die Aufgabenpassung in C06 und W02 = TASK_FIT. | Keine Items übernommen. Übertragbarkeit auf generative KI nicht geprüft. |
| Do Khac et al. (2025), Vertrauen bei Entscheidungstragenden | Begründung, Führung als eigene Gruppe (Z02) sichtbar zu machen. | Zielgruppe Entscheidungstragende, nicht die gesamte Belegschaft. Keine Items übernommen. Bibliografische Ausgabedaten vor Abgabe aktualisieren. |
| Wichmann et al. (2026), sozio-technische Bedingungen | Begründung der getrennten Organisationserfassung (Abschnitt 4). | Kontext virtuelle Meetings. Keine Items übernommen. |
| Wichmann et al. (2024), KI-Akzeptanz Gesundheit | Nicht verwendet. | Gesundheitsbezogene Konstrukte werden nicht übernommen. |
| Boateng et al. (2018) | Trennung von Itementwicklung, Pretest und weiterführender Prüfung der Messqualität. Grundlage für die optionale Prüfung in Abschnitt 7.6. | Der kleine Pretest des Kerns ersetzt keine Validierung. |
| National Center for Health Statistics (2024), Cognitive interviewing | Methodische Orientierung für den Kurztest des Kontextmoduls (Abschnitt 10). | Begründet keine bestimmte Mindestzahl an Testpersonen. |
| Peffers et al. (2007); Venable et al. (2016) | Einordnung dieses Laufs als Demonstration im DSR-Prozess. | Keine Aussage über die Messqualität des Fragebogens. |
| Bisbee et al. (2024) | Begründung, warum keine synthetischen Antworten als Ersatz für Befragungsdaten dienen. | Untersucht politische Befragungen und frühere Modelle. |
| Google (o. D.), Regeln für Formulare | Technische Begrenzung der Kästchenfragen, falls diese Plattform gewählt wird. | Plattform noch offen (R5). |

---

## 6. Codebuch

### 6.1 Geltung

Für den Kern gilt das Codebuch GARI-DE-0.1 unverändert. Die folgenden Tabellen geben es für dieses Paket vollständig wieder und ergänzen das Kontextmodul. Die Itembank `Itembank_GARI_DE_0.1.json` bleibt die maschinenlesbare Referenz.

### 6.2 Kernitems GARI-DE-0.1

Skala ABILITY_0_10: 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Skala AGREEMENT_1_7: 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker. Höhere Zahl bedeutet jeweils höhere Selbsteinschätzung oder Zustimmung. Keine umgepolten Items. Keine Sprungregeln.

| ID | Kurzinhalt | Typ | Gültige Werte (Code = Antworttext) | Zulässige Fehlwerte | Zusammenfassung |
|---|---|---|---|---|---|
| C01 | Wie sieht Ihre hauptsächliche Tätigkeit aus? | Einzelwahl | OFFICE = Überwiegend Büro- oder Bildschirmarbeit; OTHER_WORK = Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst; MIXED = Etwa gleich große Anteile beider Bereiche | KEINE_ANGABE | Einzelverteilung |
| C02 | An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt? | Einzelwahl | D0 = An keinem Tag; D1_3 = An 1 bis 3 Tagen; D4_9 = An 4 bis 9 Tagen; D10_15 = An 10 bis 15 Tagen; D16_PLUS = An 16 oder mehr Tagen; UNKNOWN = Kann ich nicht einschätzen | KEINE_ANGABE | Einzelverteilung |
| C03 | Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt? | Einzelwahl | YES = Ja; NO = Nein; UNKNOWN = Ich bin mir nicht sicher | KEINE_ANGABE | Einzelverteilung |
| C04 | Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen? | Einzelwahl | YES = Ja; NO = Nein; UNKNOWN = Ich weiß es nicht | KEINE_ANGABE | Einzelverteilung |
| C05 | Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit? | Einzelwahl | KNOWN = Ja; PARTLY = Teilweise; NOT_KNOWN = Nein; EXISTENCE_UNKNOWN = Ich weiß nicht, ob es solche Regeln gibt | KEINE_ANGABE | Einzelverteilung |
| C06 | Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre? | Einzelwahl | YES = Ja; NO = Nein; UNKNOWN = Kann ich noch nicht beurteilen | KEINE_ANGABE | Einzelverteilung |
| U01 | Ich kann eine generative KI bedienen. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von U (6 Items, nur vollständig) |
| U02 | Ich kann mir berufliche Aufgaben durch generative KI erleichtern. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von U (6 Items, nur vollständig) |
| U03 | Ich kann generative KI gezielt für meine Arbeitsziele einsetzen. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von U (6 Items, nur vollständig) |
| U04 | Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von U (6 Items, nur vollständig) |
| U05 | Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von U (6 Items, nur vollständig) |
| U06 | Ich kann generativer KI verständlich mitteilen, was ich brauche. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von U (6 Items, nur vollständig) |
| K01 | Ich kenne die zentralen Konzepte generativer KI. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von K (6 Items, nur vollständig) |
| K02 | Ich kann erklären, was generative KI bedeutet. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von K (6 Items, nur vollständig) |
| K03 | Ich kann Chancen und Grenzen generativer KI einschätzen. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von K (6 Items, nur vollständig) |
| K04 | Ich kann Vor- und Nachteile generativer KI beurteilen. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von K (6 Items, nur vollständig) |
| K05 | Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von K (6 Items, nur vollständig) |
| K06 | Ich kann mir künftige Anwendungen generativer KI vorstellen. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von K (6 Items, nur vollständig) |
| L01 | Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von L (3 Items, nur vollständig) |
| L02 | Ich kann mich über Neuerungen bei generativer KI informieren. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von L (3 Items, nur vollständig) |
| L03 | Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von L (3 Items, nur vollständig) |
| G01 | Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Einzelitem, kein G-Mittelwert |
| G02 | Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Einzelitem, kein G-Mittelwert |
| G03 | Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf. | Ganzzahl | ganze Zahlen 0–10 | NICHT_BEURTEILBAR, KEINE_ANGABE | Einzelitem, kein G-Mittelwert |
| A01 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft. | Ganzzahl | ganze Zahlen 1–7 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von A (4 Items, nur vollständig) |
| A02 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend. | Ganzzahl | ganze Zahlen 1–7 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von A (4 Items, nur vollständig) |
| A03 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig. | Ganzzahl | ganze Zahlen 1–7 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von A (4 Items, nur vollständig) |
| A04 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm. | Ganzzahl | ganze Zahlen 1–7 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von A (4 Items, nur vollständig) |
| I01 | Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | Ganzzahl | ganze Zahlen 1–7 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von I (3 Items, nur vollständig) |
| I02 | Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | Ganzzahl | ganze Zahlen 1–7 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von I (3 Items, nur vollständig) |
| I03 | Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen. | Ganzzahl | ganze Zahlen 1–7 | NICHT_BEURTEILBAR, KEINE_ANGABE | Teil von I (3 Items, nur vollständig) |
| W01 | Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen. | Mehrfachwahl, max. 3; exklusiv: NONE, UNKNOWN | BASICS = Grundlagen generativer KI; USE_CASES = Passende Einsatzmöglichkeiten für meine Aufgaben; PROMPTING = Klare Eingaben formulieren und Ergebnisse verbessern; VERIFY = Antworten und Quellen überprüfen; DATA_RULES = Betriebliche Regeln und zulässige Dateneingaben; KEEP_CURRENT = Bei neuen Entwicklungen auf dem Laufenden bleiben; OTHER = Anderes Thema; NONE = Derzeit kein Weiterbildungswunsch; UNKNOWN = Ich kann meinen Bedarf noch nicht einschätzen | KEINE_ANGABE | Häufigkeit je Option |
| W02 | Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen. | Mehrfachwahl, max. 3; exklusiv: NONE, UNKNOWN | ACCESS = Kein Zugang zu einem freigegebenen Werkzeug; RULES = Unklare betriebliche Regeln; TIME = Zu wenig Zeit zum Ausprobieren oder Lernen; KNOWLEDGE = Mir fehlt Wissen über die Nutzung; TASK_FIT = Ich erkenne keinen passenden Einsatz für meine Aufgaben; RELIABILITY = Unsicherheit über die Verlässlichkeit der Ergebnisse; OTHER = Etwas anderes; NONE = Derzeit nichts; UNKNOWN = Kann ich noch nicht einschätzen | KEINE_ANGABE | Häufigkeit je Option |
| W03 | Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen. | Text | Freitext (UTF-8) | KEINE_ANGABE | Qualitative Themenzuordnung |

### 6.3 Kontextmodul S3-K-0.1

| ID | Kurzinhalt | Typ | Gültige Werte (Code = Antworttext) | Zulässige Fehlwerte | Verwendung |
|---|---|---|---|---|---|
| Z01 | Hauptsächlicher Bereich | Einzelwahl | SALES = Vertrieb; SERVICE = Kundendienst; DEVELOPMENT = Entwicklung; ADMIN = Verwaltung; HR = Personal; OTHER_AREA = Anderer Bereich | KEINE_ANGABE | Gruppierungsmerkmal |
| Z02 | Führungsverantwortung | Einzelwahl | YES = Ja; NO = Nein | KEINE_ANGABE | Gruppierungsmerkmal |
| Z03 | Standort | Einzelwahl | S01, S02 und folgende = Standorte laut Unternehmensliste (Zuordnungstabelle Code zu Standort wird vor dem Start fixiert); MULTI_SITE = An mehreren Standorten etwa gleich viel | KEINE_ANGABE | Gruppierungsmerkmal |
| Z04 | Bevorzugte Lernform | Mehrfachwahl, max. 2; exklusiv: NO_PREF | SELF_PACED = Kurze Lerneinheiten zum Selbstlernen am Bildschirm; LIVE_ONLINE = Live-Schulung online; ON_SITE = Schulung vor Ort; ON_THE_JOB = Begleitung bei eigenen Arbeitsaufgaben; PEER = Austausch mit Kolleginnen und Kollegen; NO_PREF = Keine Präferenz | KEINE_ANGABE | Häufigkeit je Option |

Z-Items haben keine Option NICHT_BEURTEILBAR. MULTI_SITE und OTHER_AREA werden in Standort- und Bereichsberichten als eigene Gruppe geführt oder, bei zu kleiner Zahl, nicht ausgewiesen.

### 6.4 Fehlwerte und Eingabekontrolle

- Jede Antwort besteht aus `value` und `missing_reason`.
- NB bei numerischen Fragen: `value: null`, `missing_reason: "NICHT_BEURTEILBAR"`.
- KA oder leeres Feld: `value: null`, `missing_reason: "KEINE_ANGABE"`. Motive werden nicht ergänzt.
- Bei C01–C06 sind „Kann ich nicht einschätzen“, „Ich bin mir nicht sicher“, „Ich weiß es nicht“, „Ich weiß nicht, ob es solche Regeln gibt“ und „Kann ich noch nicht beurteilen“ reguläre Kategorien (UNKNOWN, EXISTENCE_UNKNOWN). Sie werden gezählt und ausdrücklich ausgewiesen.
- W01, W02: NONE und UNKNOWN sind reguläre, exklusive Kategorien. KA ist ein Fehlwert. Eine leere Liste ist unzulässig und bedeutet nicht „keine Wünsche“. Z04: NO_PREF ist regulär und exklusiv.
- NICHT_ZUTREFFEND und UEBERSPRUNGEN gibt es in dieser Fassung nicht.
- Mehr als drei Antworten bei W01 oder W02, mehr als zwei bei Z04, oder eine exklusive Option zusammen mit anderen: In einer anonymen Onlinebefragung ist keine Klärung möglich. Das Item wird als KEINE_ANGABE kodiert, der Grund kommt ins Korrekturprotokoll. Nie selbst eine Antwort auswählen.
- Abgebrochene Formulare werden nur so weit übertragen, wie Angaben vorliegen. Die übrigen Items bleiben fehlend. Gültige 0-Antworten bleiben stets erhalten.
- Nichtnutzung in C02 oder C03 setzt keine Fähigkeitswerte auf null und erzeugt keinen Fehlwert.

### 6.5 Eingabeformat und Datenhaltung

- Kerndatei: JSON, UTF-8, `data_kind` = SURVEY, `questionnaire_version` = GARI-DE-0.1 auf Datei- und Personenebene, alle 34 Item-IDs je Person, Antwortnummer statt Testkürzel, jede Antwortnummer nur einmal.
- Kontextdatei: eigene JSON-Datei mit `module_version` = S3-K-0.1, Antwortnummer und Z01–Z04 im selben Schema aus `value` und `missing_reason`.
- Grund für die Trennung: Die Rechenroutine des Kerns ist auf GARI-DE-0.1 festgelegt und stoppt laut Codebuch bei unbekannten IDs. Z-Items in der Kerndatei würden die Prüfung brechen oder eine stille Anpassung erzwingen. Die Verknüpfung erfolgt erst bei der Gruppenauswertung über die Antwortnummer.
- Die Plattform-Rohdaten (mit Zeitstempeln) werden nach der Übertragung gesperrt und nach der festgelegten Frist gelöscht. Personenwerte bleiben in der Arbeitsdatei. Berichte enthalten nur Aggregate.

### 6.6 Rechenregeln

- Teilbereichswerte je Person als arithmetisches Mittel, nur wenn alle Items gültige Zahlen haben: U (U01–U06), K (K01–K06), L (L01–L03), A (A01–A04), I (I01–I03). Ein Fehlwert macht den ganzen Teilbereichswert fehlend. Das ist eine konservative Projektregel, keine MAILS-Vorschrift.
- G01, G02, G03: drei Einzelitems, kein G-Mittelwert.
- C01–C06, Z01–Z03: Einzelverteilungen.
- W01, W02, Z04: Häufigkeit je Option. Nenner = Personen mit gültiger Antwort auf dieses Item. Jede Option höchstens einmal je Person. Summen über 100 % sind möglich. Fehlende Antworten zusätzlich ausweisen.
- Gruppenwerte: Mittelwert der gültigen Personenwerte, immer mit Zahl vollständiger und unvollständiger Fälle. Keine Ersetzung fehlender Werte. Null gültige Fälle ergeben `null`, nicht 0.
- Kein Gesamtscore, keine Umrechnung auf 100, keine Gewichtung, keine Klassifikation. Werte auf 0–10 und 1–7 werden nicht in einer gemeinsamen Rangliste verglichen.
- Prüfhinweis: C04 = NO bei mindestens einer Antwort 6 oder 7 in I01–I03. Nur Hinweis, keine Änderung, keine Kompetenzaussage. Die Person kann künftigen Zugang erwarten.

---

## 7. Auswertungsplan

Der Plan wird vor Beginn der Feldzeit festgehalten. Abweichungen werden im Bericht als solche benannt.

### 7.1 Datenübernahme und Prüfung

1. Export aus der Plattform. Übertragung in Kern- und Kontextdatei nach Abschnitt 6.5.
2. Korrekturprotokoll für jede nicht eindeutige Antwort.
3. Kerndatei mit der projekteigenen Rechenroutine des GARI-Pakets prüfen und auswerten (laut Codebuch `auswertung/score.py`, vorher Tests mit `python -m unittest discover -s tests -v`). Diese Dateien lagen in diesem Lauf nicht vor und wurden nicht ausgeführt. Die Routine stoppt bei unzulässigen Werten, fehlenden oder unbekannten IDs, doppelten Antwortnummern und abweichender Version. Fehler werden an der Quelle behoben, nicht still repariert.
4. Kontextdatei mit denselben Prüfregeln getrennt prüfen.
5. Verknüpfung über die Antwortnummer erst danach.

### 7.2 Teilnahme und Aussagereichweite

- Gesamtzahl abgeschickter Formulare und Anteil an 1.200 Beschäftigten.
- Teilnahme je Standort und je Bereich, nur wenn das Unternehmen Kopfzahlen je Gruppe liefert (R1).
- Abbruchverlauf: Zahl der Formulare mit Angaben je Seite.
- Anteil fehlender Z-Angaben. Wer Z01 oder Z03 offen lässt, fehlt in Gruppenberichten, nicht im Gesamtbericht.
- Teilnahme ist freiwillig. Die Antwortenden sind keine Zufallsstichprobe. Es ist plausibel, dass KI-interessierte Personen häufiger teilnehmen. Ergebnisse beschreiben deshalb die Teilnehmenden, nicht automatisch die Belegschaft. Keine Gewichtung ohne gesonderte, dokumentierte Entscheidung.

### 7.3 Status quo (Gesamtebene)

| Auswertung | Items | Darstellung |
|---|---|---|
| Art der Tätigkeit | C01 | Verteilung mit allen Kategorien und KA |
| Berufliche Nutzung letzte vier Wochen | C02 | Verteilung, UNKNOWN und KA getrennt |
| Private Nutzung | C03 | Verteilung |
| Wahrgenommener Zugang | C04 | Verteilung, neben O1 und O2 aus Abschnitt 4 |
| Regelkenntnis | C05 | Verteilung, neben O3 bis O5 |
| Aufgabenpassung | C06 | Verteilung |
| Anwendung, Verständnis, Lernen | U01–U06, K01–K06, L01–L03 | Primär Einzelverteilungen je Item mit NB- und KA-Zahl. Ergänzend vorläufige Mittelwerte U, K, L mit Zahl vollständiger und unvollständiger Fälle |
| Prüfen und zulässige Eingaben | G01, G02, G03 | Drei getrennte Verteilungen |
| Einstellung und Absicht | A01–A04, I01–I03 | Einzelverteilungen, ergänzend vorläufige Mittelwerte A und I |
| Lernwünsche, Hindernisse | W01, W02 | Häufigkeit je Option, Nenner ausgewiesen |
| Lernform | Z04 | Häufigkeit je Option |
| Freitext | W03 | Themenliste nach 7.5 |
| Prüfhinweis | C04 und I01–I03 | Zahl der Hinweise, ohne Personenbezug |

Wichtige Lesehilfen für den Bericht:

- Hohe NB-Anteile bei einem Fähigkeitsitem zuerst als Frage der Einschätzbarkeit lesen, nicht als geringe Kompetenz.
- Selbsteinschätzungen sind keine Leistungsmessung.
- A beschreibt eine bedingte Bewertung, I eine Absicht unter erwarteten Bedingungen. Beides ist keine tatsächliche Nutzung.

### 7.4 Ergebnisse je Funktion, Führung und Standort

- Gruppen: Z01 (Bereiche), Z02 (Führung ja oder nein), Z03 (Standorte). C01 als zusätzliche Gliederung nach Arbeitsform.
- Pro Gruppe dieselben Darstellungen wie in 7.3, mit Gruppengröße.
- Schwerpunkt für die Funktion: W01, W02, C06, C02, Z04. Das ergibt die gewünschten Lernwunschprofile je Funktion.
- Schwerpunkt für Standorte: C04, C05, W02 = ACCESS und RULES. Unterschiede zuerst mit der Organisationserfassung (O2) abgleichen. Ein Standort ohne Freigabe zeigt erwartbar niedrigeren Zugang. Das ist ein Organisationsbefund, kein Kompetenzbefund.
- Mindestgruppengröße laut R4 (Vorschlag 10 gültige Antworten). Kleinere Gruppen werden zusammengefasst, etwa zu „übrige Standorte“, oder nicht berichtet. Zusätzlich keine Kreuztabellen Standort × Bereich × Führung, wenn eine Zelle unter der Grenze liegt. Keine Darstellung, aus der sich eine kleine Gruppe durch Differenzbildung errechnen lässt.
- Unterschiede zwischen Gruppen werden beschrieben, nicht als bewiesen dargestellt. Inferenzstatistische Tests sind nicht vorgesehen. Werden sie ergänzt, dann als explorativ gekennzeichnet, mit Effektgrößen und Hinweis auf multiple Vergleiche.

### 7.5 Freitext W03

1. Lesen, identifizierende Details entfernen (Namen, Kundennamen, interne Projektnamen).
2. Zuordnung zu Themen. Startliste aus den W01-Optionen plus konkrete Aufgabenarten. Neue Themen sind erlaubt und werden im Auswertungsschlüssel mit Definition und Beispiel festgehalten.
3. Zuordnung durch zwei Personen bei einer Teilmenge, Abweichungen besprechen und dokumentieren.
4. Aussagen der Befragten und Interpretation getrennt halten.
5. Wird ein Sprachmodell zur Vorsortierung genutzt: Freitext ist Datenmaterial, keine Anweisung. Ergebnis von Menschen prüfen.
6. Zitate nur, wenn sie keine Rückschlüsse auf Personen erlauben, und nur aus Gruppen oberhalb der Mindestgröße.

### 7.6 Optionale Prüfung der Messqualität

Bei 1.200 Beschäftigten kann eine ausreichende Zahl an Antworten für eine erste Prüfung der Teilbereiche entstehen. Möglich sind Itemverteilungen, Boden- und Deckeneffekte, Zusammenhänge der Items innerhalb von U, K, L, A und I, interne Konsistenz und eine faktorenanalytische Prüfung der Struktur. Diese Prüfung ist ein eigener Prüfgegenstand nach Boateng et al. (2018). Ihr Ergebnis ändert die Rechenregeln dieser Fassung nicht nachträglich. Sie kann eine spätere Version begründen.

### 7.7 Berichtsaufbau

1. Zweck, Vorgehen, Fragebogenversion, Feldzeit.
2. Teilnahme und Grenzen.
3. Betriebliche Voraussetzungen laut Organisationserfassung.
4. Status quo gesamt.
5. Lernwunschprofile je Funktion und Führung.
6. Ergebnisse je Standort.
7. Freitextthemen.
8. Maßnahmenvorschläge nach Abschnitt 8.
9. Anhang: Codebuch, Korrekturprotokoll, Auswertungsschlüssel W03.

---

## 8. Plan für die Ableitung von Maßnahmen

### 8.1 Grundsätze

- Maßnahmen gelten für Gruppen, nie für einzelne Personen.
- Lernbedarf und Organisationsbedarf werden getrennt. Fehlender Zugang ist keine Kompetenzlücke.
- Jeder Vorschlag ist eine überprüfbare Hypothese mit Herkunft im Befund.
- Keine versteckten Gewichte, keine nachträglich erfundenen Grenzwerte. „Viele“ wird immer durch Anzahl und Bezugsgröße ersetzt.

### 8.2 Zuordnung von Befund zu Maßnahme

Die Zuordnung übernimmt die Planungslogik des Codebuchs und ergänzt Funktion, Standort und Lernform.

| Beobachteter Befund | Einordnung | Mögliche Maßnahme und weiterer Prüfbedarf |
|---|---|---|
| W01 = BASICS | Ausdrücklicher Lernwunsch | Einführung anbieten. Vorkenntnisse und Aufgaben prüfen. Format nach Z04 der betroffenen Gruppe. |
| W01 = USE_CASES | Ausdrücklicher Lernwunsch | Anwendungsfälle je Funktion gemeinsam mit der Gruppe sammeln, W03-Themen nutzen. |
| W01 = PROMPTING | Ausdrücklicher Lernwunsch | Übung zu Eingaben und Überarbeitung. Passendes freigegebenes Werkzeug vorausgesetzt (O1, O2). |
| W01 = VERIFY oder W02 = RELIABILITY | Lernwunsch oder wahrgenommene Unsicherheit | Quellen- und Ergebnisprüfung an Arbeitsbeispielen. G01 und G02 ergänzend beschreiben. |
| W01 = DATA_RULES oder C05 = NOT_KNOWN oder EXISTENCE_UNKNOWN | Orientierung und möglicherweise Organisation | Regeln verständlich bereitstellen. Zuständigkeit und tatsächliches Vorhandensein klären (O3 bis O5). G03 ergänzend beschreiben. |
| W01 = KEEP_CURRENT | Ausdrücklicher Lernwunsch | Regelmäßige kurze Information zu Neuerungen. L01–L03 ergänzend beschreiben. |
| C04 = NO oder W02 = ACCESS | Organisatorisches Hindernis | Freigegebene Zugangsmöglichkeiten klären, Abgleich mit O1 und O2. Keine Kompetenzlücke behaupten. |
| W02 = RULES | Organisatorisches Hindernis | Regeln prüfen, vereinfachen oder bekannter machen (O3). |
| C06 = NO oder W02 = TASK_FIT | Unklare oder fehlende Aufgabenpassung | Bedarf und geeignete Anwendungsfälle prüfen. Nutzung kann sachlich unnötig sein. Keine Schulungspflicht ableiten. |
| W02 = TIME | Rahmenbedingung | Lernzeit und Arbeitsorganisation prüfen (O7). Führungskräfte einbeziehen. |
| W02 = KNOWLEDGE | Wahrgenommene Wissenslücke | Abgleich mit W01 derselben Gruppe. Einstiegsangebot prüfen. |
| W01 = NONE oder W02 = NONE | Derzeit kein Wunsch oder kein Hindernis | Kein Angebot aufdrängen. In Verbindung mit C06 lesen. |
| W01 = UNKNOWN oder W02 = UNKNOWN | Bedarf noch nicht einschätzbar | Niedrigschwellige Orientierung, etwa kurze Vorstellung von Anwendungsfällen. |
| Viele NB-Antworten auf einem Fähigkeitsitem | Unklare Einschätzbarkeit | Erst Frageverständnis und Erfahrungsgrundlage prüfen. Nicht als niedrige Kompetenz zählen. |
| Niedrige Fähigkeitsantworten und passender Lernwunsch in derselben Gruppe | Mehrere zusammenpassende Hinweise | Vertiefenden Lernbedarf als Hypothese formulieren. Praktische Aufgabe zur Abklärung anbieten. |
| Prüfhinweis C04 = NO bei I ≥ 6 gehäuft an einem Standort | Mögliche Erwartung künftigen Zugangs oder unklare Lage | Mit O8 abgleichen. Kommunikation zum geplanten Zugang prüfen. |
| Standortunterschied bei C04 oder C05 | Möglicher Organisationsunterschied | Mit O2 und O3 abgleichen, bevor Weiterbildung geplant wird. |
| W03-Thema häuft sich in einer Funktion | Konkreter Anwendungswunsch | Praxisnahe Übung zu genau dieser Aufgabe prüfen. |

### 8.3 Priorisierung

Transparent nach drei Kriterien, jeweils mit Zahlen im Bericht:

1. Geäußerter Wunsch: Anteil und Anzahl in W01 je Gruppe.
2. Aufgabenrelevanz: Anteil C06 = YES in derselben Gruppe, ergänzt durch W03.
3. Umsetzbarkeit: Freigabe vorhanden (O1, O2), Regeln vorhanden (O3), Lernzeit möglich (O7).

Es gibt keine Rechenformel, die diese Kriterien verrechnet. Die Reihenfolge wird im Gremium begründet festgelegt und protokolliert. Organisationsmaßnahmen mit Wirkung auf mehrere Lernwünsche (etwa fehlender Zugang) können vor Schulungen stehen.

### 8.4 Vorlage für jeden Maßnahmenvorschlag

Jeder Vorschlag im Bericht wird mit diesen Feldern dokumentiert. Die Felder werden erst mit echten Daten befüllt.

| Feld | Inhalt |
|---|---|
| Befund-ID | Laufende Nummer, etwa B01 |
| Item-IDs | Zum Beispiel W01, C06, Z01 |
| Datenart | SURVEY |
| Gruppe | Gesamt, Bereich, Führung oder Standort, nur oberhalb der Mindestgröße |
| Fallzahl | Gültige Antworten der Gruppe und fehlende Antworten auf die Items |
| Befund | Beobachtete Verteilung in Zahlen, ohne Wertung |
| Einordnung | Lernbedarf, Organisationsbedarf, Rahmenbedingung oder unklar |
| Lern- oder Organisationsziel | Was nach der Maßnahme anders sein soll |
| Maßnahme | Thema, Format (Z04), Zielgruppe, Verantwortliche Stelle |
| Unsicherheit | Selbstbericht, Selbstselektion, Gruppengröße, offene Organisationsangaben |
| Erfolgskontrolle | Siehe 8.5 |

### 8.5 Erfolgskontrolle

- Teilnahme an Angeboten und Rückmeldung direkt nach dem Angebot.
- Bei Organisationsmaßnahmen: Nachweis der Umsetzung, etwa veröffentlichte Regeln oder freigegebenes Werkzeug je Standort.
- Wiederholungsbefragung mit derselben Fassung GARI-DE-0.1 und S3-K-0.1 nach einem festgelegten Zeitraum, zum Beispiel sechs Monaten. Vergleich nur auf Gruppenebene. Bei geänderter Fassung getrennte Auswertung, kein direkter Vergleich.
- Veränderungen der Selbsteinschätzung sind kein Kompetenznachweis. Für Lernziele mit hoher Bedeutung, etwa Prüfen von Ergebnissen oder zulässige Eingaben, ergänzend praktische Übungsaufgaben im Rahmen der Weiterbildung, nicht als Personenbewertung.

---

## 9. Grenzen

- Selbstberichte. Keine objektive Kompetenzmessung.
- Kern im Projekt nur in einem kleinen Pretest geprüft (drei reale Personen, zwei synthetische Personas getrennt). Keine psychometrische Validierung. Teilbereichsmittelwerte sind vorläufige, deskriptive Projektwerte.
- MAILS-Evidenz betrifft allgemeine KI. PowerPilot-Items stammen aus einem anderen Anwendungskontext. Der Wortlautvergleich mit dem OSF-Anhang ist offen.
- Kontextmodul S3-K-0.1 ist neu und ungetestet.
- Freiwillige Teilnahme führt zu möglicher Selbstselektion.
- Standort- und Funktionsberichte sind durch die Mindestgruppengröße begrenzt. Kleine Standorte oder Bereiche bleiben eventuell unsichtbar.
- Die Kerninstruktion ist papierbezogen formuliert („Kreisen Sie … ein“). Online bleibt sie wörtlich und wird im Funktionstest beobachtet.
- Nachnutzungsrechte für die veränderten MAILS- und PowerPilot-Items sind vor einer öffentlichen Weitergabe zu klären.
- Datenschutz- und Mitbestimmungsfragen sind vor dem Start durch die zuständigen Stellen zu prüfen. Dieses Paket ersetzt keine rechtliche Prüfung.
- Szenario mit fiktivem Unternehmen. Keine realen Daten, keine Ergebnisse.

---

## 10. Prüfliste vor dem Start

1. Rückfragen R1 bis R9 geklärt und Entscheidungen dokumentiert.
2. Standortliste für Z03 und Code-Zuordnung fixiert.
3. Mindestgruppengröße und Berichtsempfänger mit Datenschutz und Arbeitnehmervertretung abgestimmt.
4. Organisationserfassung O1 bis O8 zum Stichtag ausgefüllt.
5. Onlineformular gebaut. Kerntext wörtlich gegen `frozen_participant_text` der Itembank abgeglichen, Zeichen für Zeichen.
6. Funktionstest mit Testeinträgen: alle Optionen wählbar, keine Vorauswahl, keine Pflichtfelder, Höchstzahlen bei W01, W02 und Z04 auch beim Seitenwechsel wirksam, Export vollständig, Antwortnummer eindeutig, keine IP-Speicherung.
7. Kurzer Verständlichkeitstest des Kontextmoduls und der Onlinedarstellung mit einigen Beschäftigten aus unterschiedlichen Bereichen, darunter Personen ohne Bildschirmarbeitsplatz und ohne GenAI-Nutzung. Orientierung an kognitiven Interviews (National Center for Health Statistics, 2024). Bearbeitungsdauer messen und in der Einleitung anpassen. Testantworten mit `data_kind` = PRETEST getrennt halten.
8. Auswertungsplan (Abschnitt 7) und Maßnahmenlogik (Abschnitt 8) vor Feldbeginn datiert ablegen.
9. Rechenroutine und Tests des GARI-Pakets mit der künstlichen Beispieldatei laufen lassen, bevor echte Daten eingehen.
