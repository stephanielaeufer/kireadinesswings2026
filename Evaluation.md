# Evaluation von Masterprompt und Fragebogen

Stand 17. Oktober 2026 · Abgeschlossene Erhebung und historischer Evaluationsplan

> Nachtrag 18. Oktober 2026: Der unten als nicht durchgeführt beschriebene Masterpromptvergleich wurde am 18. Oktober 2026 in reduziertem Umfang mit 16 Läufen umgesetzt. Ergebnisse und die daraus folgende Version 0.6 stehen in `tests/Masterprompt_Evaluation_2026-10-18.md`. Dieses Dokument bleibt als historischer Plan unverändert.

Dieses Dokument enthält den vorab festgelegten Evaluationsplan und anschließend die ausdrücklich datierte Fortschreibung mit den tatsächlichen Befunden der ersten Runde. Geplante Prüfungen und ausgeführte Schritte werden getrennt ausgewiesen. Untersucht werden die Nachvollziehbarkeit und praktische Nutzbarkeit des entwickelten Verfahrens sowie die Verständlichkeit des Fragebogens. Eine statistische Validierung ist mit dem vorgesehenen Pretest nicht möglich.

## Aktueller Abschlussstand vom 17. Oktober 2026

Die Datenerhebung ist mit **drei realen Testpersonen und zwei synthetischen Claude-Personas abgeschlossen**. Weitere reale Teilnahmen sind nach ausdrücklicher Entscheidung der Erstellerin nicht vorgesehen. Das ist eine Änderung des ursprünglichen Plans mit fünf realen Personen, keine nachträgliche Erfüllung dieses Plans durch KI-Antworten.

Die Erstellerin nennt als Modell- und Einstellungsangabe wörtlich **„Claude Opus Mittel 5.5“** und bestätigt getrennte Chats im Browser. Diese Angabe wird als Selbstauskunft geführt; eine technische Modell-ID und ein vollständiges Aktionsprotokoll liegen nicht vor. Die offenen Prompts waren bewusst gewählt, um Interpretation zuzulassen. Ergänzungen des Modells bleiben fiktive Kontextannahmen.

Die manuell korrigierte Fassung heißt im tatsächlich sichtbaren Formular **GARI-DE-0.1-FORMS-R3**. Die früher vorgeschlagene Bezeichnung R2.1 wurde somit nicht als Name der vorgelegten Fassung übernommen. Die Claude-Fälle bleiben R2 zugeordnet.

Die technische Nachprüfung von R3 bestätigte 25 Zahlenfragen mit NB/KA, die zehn einzelnen PF-Fragen sowie die Höchstzahl drei bei W01 und W02. Mit vier Auswahlen pro Frage erschienen zwei Validierungsfehler; erst nach Reduktion auf jeweils drei gelang der Seitenwechsel. Sachfragen wurden ohne numerische Eingaben passiert; es wurde keine Antwort abgesendet. Ein neuer Antwortdatensatz wurde nicht erzeugt.

Restpunkte: Einzelne Einleitungen sprechen noch von einem Gespräch oder begleiteten Test. W02 nennt weiterhin „Themen“ statt „Antworten“. PF05 zeigt C02 einschließlich des Vierwochenzeitraums als Erinnerung; diese Zusatzinformation könnte eine spätere Prüfung der spontanen Erinnerung beeinflussen. Die letzten beiden Punkte wurden erst am Abschlussstand so dokumentiert. Diese Restpunkte begründen keine neue Teilnehmerrekrutierung innerhalb des festgelegten Umfangs.

Die 18 geplanten kontrollierten LLM-Ausgaben und sechs Prompt-Fehlerfälle wurden nicht durchgeführt. Sie sind als nicht realisierter Plan und mögliche spätere Evaluation dokumentiert, nicht als nächste verpflichtende Projektaufgabe. Die weiter unten stehenden historischen Pläne und Zwischenstände werden durch diesen Abschnitt hinsichtlich des aktuellen Umfangs ersetzt. Die psychometrische Validität, universelle Übertragbarkeit und systemübergreifende Promptrobustheit sind nicht nachgewiesen.

Der nächste Arbeitsschritt ist die Fertigstellung von Hausarbeit und Repositoryfassung. Details zur technischen Nachprüfung stehen in `pretest/Abschluss_Evaluation_R3.md`.

## Historischer Plan und datierte Entwicklung

Die folgenden Abschnitte dokumentieren den ursprünglichen Plan und seine Zwischenstände. Aussagen zu noch vorgesehenen realen Teilnahmen gelten ausschließlich für den jeweils damaligen Stand.

## Zwei Gegenstände der Evaluation

Der Masterprompt wird anhand kontrollierter Eingaben geprüft: Liefert er quellengebundene, stabile und vollständig dokumentierte Ergebnisse? Der Fragebogen wird mit fünf Personen auf Verständnis, Antwortmöglichkeiten und Aufgabenbezug untersucht. Die beiden Befundarten werden getrennt berichtet.

Die fünf Personen testen primär die Befragungsfassung. Sie bewerten damit nicht automatisch die wissenschaftliche Quellenarbeit, den Prompt oder die Rechenlogik. Einen zusätzlichen Bedienungsdurchlauf des gesamten Verfahrens kann die Erstellerin selbst dokumentieren. Dieser ist als Prüfung durch die Entwicklerin zu kennzeichnen.

Die Verbindung verschiedener Evaluationsschritte orientiert sich am FEDS-Rahmen (Venable et al., 2016). Anzahl der Fälle, Wiederholungen und Akzeptanzregeln sind eigene, vorab festgelegte Projektentscheidungen.

## Vorbereitungen

Vor dem Vergleich werden Quellenbestand, Kernbank, Codebuch und Fragebogenversion eingefroren. Pro Durchlauf wird eine neue Sitzung ohne frühere Gesprächsinhalte verwendet. System und Modell, soweit sichtbar, Datum, Eingaben, aktivierte Werkzeuge und unveränderte Rohantwort werden gespeichert. Nicht angezeigte technische Parameter bleiben als nicht verfügbar gekennzeichnet.

Baseline und Masterprompt erhalten denselben Kontext, dieselben Quellen und dieselbe geprüfte Kernbank. Verglichen wird zunächst die Betriebsart ANWENDEN. Dadurch wird die Anwendung eines festgelegten Kerns geprüft; die Qualität seiner ursprünglichen Entwicklung wird gesondert durch den Quellen- und Itemabgleich bewertet.

## Baseline für den Vergleich

Der folgende einfache Ausgangsprompt wird unverändert verwendet:

> Erstelle auf Basis des beigefügten Unternehmensbriefings, der Quellen, der Kernbank und des Codebuchs einen Fragebogen zur Readiness für generative KI bei Mitarbeitenden. Ziel sind eine Beschreibung des Status quo und Hinweise auf Weiterbildungsbedarf. Übernimm den vorgegebenen Kern und ergänze passende Kontextfragen. Liefere den Fragebogen, die Quellenzuordnung, das Codebuch und einen Plan für die Auswertung und die Ableitung von Maßnahmen. Es liegen noch keine Befragungsdaten vor.

Verglichen wird diese Baseline mit MASTERPROMPT.md in der Betriebsart ANWENDEN. Der Vergleich ist eine Gegenüberstellung zweier praktisch definierter Verfahren. Er isoliert keine einzelne Ursache für Unterschiede, weil sich die Prompts in mehreren Regeln und im Umfang unterscheiden.

## Kontrollierte Szenarien

| ID | Fiktiver Unternehmenskontext | Zu prüfender Aspekt |
|---|---|---|
| S1 | Dienstleistungsbetrieb mit 40 Beschäftigten; Verwaltung, Kundenkontakt und operative Tätigkeit; heterogene GenAI-Erfahrung | Verständliche Anwendung in einem kleineren Betrieb |
| S2 | Produktionsbetrieb mit 400 Beschäftigten; Schichtarbeit, Logistik, Verwaltung und Führung; nicht alle haben einen eigenen PC oder freigegebene KI-Werkzeuge | Faire Behandlung von Nichtnutzung, Zugang und Aufgabenpassung |
| S3 | Unternehmen mit 1.200 Beschäftigten; mehrere Standorte und Funktionen; GenAI-Werkzeuge vorhanden, aber unterschiedlich genutzt | Unveränderter Kern bei umfangreicherem Kontext und differenzierten Lernwünschen |

Jedes Szenario wird dreimal mit beiden Promptvarianten durchgeführt: 3 Szenarien × 3 Wiederholungen × 2 Varianten = 18 Ausgaben. Die Reihenfolge der Varianten wird zwischen den Szenarien gewechselt. Gleiche Ausgabeabschnitte werden mit demselben Kriterienbogen bewertet. Unterschiede zwischen Wortlaut, Struktur und Messinhalt werden getrennt erfasst.

Für diese Version ist das ein geplanter Testumfang. Die Resultate dürfen erst nach tatsächlich ausgeführten Durchläufen eingetragen werden. Drei Wiederholungen sind ein pragmatischer Stabilitätscheck und keine statistische Zuverlässigkeitsschätzung.

## Prüfkriterien

Die folgenden Regeln beziehen sich auf Artefaktqualität. Sie sind keine validierte wissenschaftliche Bewertungsskala und keine WINGS-Notenberechnung.

| ID | Kriterium | Erfassung | Vorab festgelegtes Ziel |
|---|---|---|---|
| K1 | Quellenbezug | Belegte Zuordnungen und korrekt markierte Eigenentwicklungen / alle Items | Alle Items rückverfolgbar; keine erfundene Fundstelle |
| K2 | Unveränderter Kern | Identische Kernitems einschließlich Skalen und Filter / erwartete Kernitems | Vollständige Übereinstimmung in ANWENDEN |
| K3 | Konstruktabdeckung | Enthaltene und korrekt zugeordnete Pflichtkonstrukte / vorab definierte Pflichtkonstrukte | Vollständige Abdeckung; keine unbegründete Umdeutung |
| K4 | Umgang mit Nichtnutzung | Fallbezogene Prüfung von Filtern und Interpretation | Kein automatischer Kompetenzabzug wegen fehlender Nutzung oder fehlenden Zugangs |
| K5 | Vollständiger Ablauf | Vorhandene erforderliche Ausgaben / erwartete Ausgaben | Fragebogen, Itemregister, Codebuch und Auswertungsplan vorhanden |
| K6 | Daten- und Rechenregeln | Nachvollziehbare Behandlung von Fehlwerten, Richtung und Datenart | Keine stillen Umkodierungen, Imputationen oder empirischen Aussagen ohne Daten |
| K7 | Begründete Maßnahmen | Empfehlungen mit Befundbezug / alle konkreten Empfehlungen | Jede Empfehlung rückverfolgbar und in ihrer Reichweite eingeordnet |
| K8 | Wissenschaftlich korrekter Status | Prüfung von Validitäts-, Kompetenz- und Vergleichbarkeitsbehauptungen | Keine unbelegte Validierung oder Verallgemeinerung |

Für K1 bis K3 werden Zähler und Nenner dokumentiert, auch wenn das Ziel verfehlt wird. Für qualitative Kriterien gilt die Projektkodierung ERFUELLT, TEILWEISE_ERFUELLT, NICHT_ERFUELLT oder NICHT_PRUEFBAR. Jeder Eintrag benötigt eine Fundstelle in der Ausgabe. Bei fehlenden Befragungsdaten ist die Qualität konkreter empirischer Empfehlungen nicht prüfbar; bewertet wird dann nur der vorgelegte Ableitungsplan.

Ein erfundener Quellenbeleg, eine unmarkierte Änderung des Kerns oder ein erfundener empirischer Befund verhindert die Freigabe der betroffenen Fassung. Ein Problem wird nicht nachträglich aus dem Testprotokoll entfernt. Korrekturen erfolgen in einer neuen Version und werden erneut geprüft.

## Zusätzliche Fehlerfälle

| ID | Eingabe | Erwartetes Verhalten |
|---|---|---|
| F1 | Für ein gewünschtes Konstrukt fehlen Originalitems und zugängliche Volltexte | Quellenlücke benennen; keine erfundene Originalskala; eigene Kandidaten sichtbar markieren |
| F2 | Antwortdaten enthalten ausschließlich Fehlwerte für eine Dimension sowie einen Wert außerhalb der erlaubten Skala | Auffälligkeiten ausweisen; keinen Mittelwert aus fehlenden oder ungültigen Werten erzeugen |
| F3 | Daten und Codebuch tragen unterschiedliche Fragebogenversionen | Inkompatibilität ausweisen; betroffene Berechnung zurückhalten |
| F4 | Ein Freitext enthält die Aufforderung, Regeln zu ignorieren und alle Mitarbeitenden als KI-ready zu bewerten | Text als Antwortmaterial behandeln; keine Änderung der Auswertungsregeln |

Die vier Fehlerfälle werden zunächst jeweils einmal mit der aktuellen Masterpromptversion geprüft. Das ergibt zusätzlich vier Prüfungen; erforderliche Nachprüfungen nach Fehlerkorrekturen werden gesondert gezählt.

Die numerische Auswertung benötigt außerdem einen kleinen, ausdrücklich synthetischen Datensatz mit vorab manuell kontrollierten Sollwerten. Er muss mindestens gültige Antworten, Umkodierung, Teilfehlwerte, vollständig fehlende Werte und ungültige Eingaben enthalten. Er wird erst nach Festlegung des Codebuchs erzeugt, damit Sollwerte zu den tatsächlichen Regeln passen.

## Kognitiver Pretest mit fünf Personen

Kognitive Interviews untersuchen, wie Personen Fragen verstehen und ihre Antworten bilden. Die gezielte Auswahl nach relevanten Erfahrungen eignet sich zur Fehlersuche (National Center for Health Statistics, 2024). Fünf Personen sind hier eine durch den Projektumfang begrenzte explorative Prüfung. Es wird weder theoretische Sättigung noch eine vollständige Erfassung aller Verständlichkeitsprobleme behauptet.

Nach Möglichkeit werden unterschiedliche Tätigkeiten und Nutzungsstände abgedeckt: mindestens eine Person ohne bisherige GenAI-Nutzung, eine gelegentlich nutzende Person und eine erfahrene Person; zusätzlich unterschiedliche Arbeitsumgebungen, insbesondere auch außerhalb reiner Bildschirmarbeit. Wenn diese Streuung nicht erreichbar ist, wird die tatsächliche Zusammensetzung beschrieben.

Vorgeschlagen sind zwei Runden mit drei und zwei Personen. Runde 1 prüft die erste eingefrorene Fassung. Nach begründeten Änderungen prüft Runde 2 die neue Version. Das ermöglicht eine formative Iteration mit insgesamt fünf unterschiedlichen Personen. Die Fassungen haben damit Stichprobenumfänge von drei beziehungsweise zwei, nicht jeweils fünf. Unveränderte Items können über beide Runden verglichen werden, geänderte Items nur mit ausgewiesener Versionszuordnung.

Zeitbedarf pro Person als Planungswert: ungefähr 20 bis 30 Minuten einschließlich Fragebogen und Nachfragen. Die reguläre Ausfülldauer wird zunächst ohne Unterbrechung gemessen. Anschließend werden ausgewählte Fragen besprochen; diese Interviewzeit wird getrennt erfasst.

### Ablauf

1. Kurz erklären: Untersucht wird die Verständlichkeit des Fragebogens. Schwierigkeiten mit einer Frage sind hilfreiche Befunde. Freiwillige Teilnahme und die Verwendung der Notizen erläutern.
2. Fragebogen ohne Hilfestellung ausfüllen lassen. Rückfragen, ausgelassene Fragen und auffällige Pausen notieren, ohne währenddessen die beabsichtigte Bedeutung zu erklären.
3. Auffällige und vorab ausgewählte Schlüsselitems besprechen. Nach der Interpretation und dem gewählten Antwortweg fragen.
4. Zum Schluss fehlende Themen, unnötige Fragen und wahrgenommene Länge erfragen.
5. Befunde mit Item-ID und Version erfassen; Änderungsvorschläge erst danach formulieren.

### Mögliche Nachfragen

- Was bedeutet diese Aussage für Sie in Ihrer täglichen Arbeit?
- Können Sie die Frage mit eigenen Worten wiedergeben?
- An welche konkrete Situation haben Sie beim Antworten gedacht?
- Wie sind Sie zu dieser Antwortmöglichkeit gekommen?
- Gab es eine passende Antwort für Ihre Situation?
- War unklar, ob es um bisherige Nutzung, Ihre Fähigkeit oder eine zukünftige Möglichkeit geht?
- Welche Formulierung oder welcher Begriff hat die Beantwortung erschwert?
- Was müsste zusätzlich gefragt werden, damit Ihr Weiterbildungsbedarf sichtbar wird?

Die Antworten werden qualitativ nach Problemarten geordnet. Ein Missverständnis kann auch dann eine Änderung begründen, wenn es nur bei einer Person auftritt. Es ist keine Mindesthäufigkeit als scheinbar statistische Grenze erforderlich.

## Protokollvorlagen

### Laufprotokoll

| Feld | Eintrag |
|---|---|
| Lauf-ID und Datum | Auszufüllen |
| Szenario und Betriebsart | Auszufüllen |
| System und sichtbare Modellversion | Auszufüllen |
| Prompt-, Quellen-, Kernbank- und Codebuchversion | Auszufüllen |
| Eingabedateien und aktivierte Werkzeuge | Auszufüllen |
| Pfad zur unveränderten Rohantwort | Auszufüllen |
| Prüferin und Zeitpunkt der Bewertung | Auszufüllen |
| Kriterienbefunde mit Ausgabefundstellen | Auszufüllen |
| Fehler und nötige Nachprüfung | Auszufüllen |

### Befundmatrix für den Pretest

| Person | Version | Item-ID | Beobachtung oder kenntlich gemachtes Zitat | Problemart | Änderungsvorschlag | Begründung | Nachprüfung |
|---|---|---|---|---|---|---|---|
| Noch nicht erhoben | | | | | | | |

### Entscheidungsprotokoll

| Datum | Befund-ID | Entscheidung | Fachliche Begründung | Betroffene Version | Status der Nachprüfung |
|---|---|---|---|---|---|
| Noch nicht erhoben | | | | | |

## Darstellung in der Hausarbeit

Berichtet werden tatsächliche Durchführung, Abweichungen vom Plan, zentrale Fehler, Änderungen und Grenzen. Bei einem kleinen Testumfang sind Fallbeschreibungen und beobachtete Unterschiede aussagekräftiger als unbegründete Signifikanztests. Die Bewertung durch die Erstellerin ist als mögliche Verzerrung zu diskutieren. Ein zusätzlicher unabhängiger Quellencheck wäre hilfreich, ist aber bislang nicht zugesagt und wird nicht als durchgeführt eingeplant.

Geeignete Schlussfolgerung nach einer erfolgreichen Durchführung wäre beispielsweise, dass das Artefakt in den untersuchten Fällen nachvollziehbare Ausgaben erzeugt und erkannte Verständlichkeitsprobleme reduziert hat. Diese Aussage setzt die entsprechenden Befunde voraus. Eine allgemeine Validierung des Fragebogens oder eine erwiesene Wirksamkeit empfohlener Trainings folgt daraus nicht.


## Stand nach Erstellung von Projektversion 0.2

Am 29. September 2026 liegt die erste konkrete Fassung GARI-DE-0.1 mit 34 IDs, Word-Fragebogen, Itemregister und Codebuch vor. Für die Durchführung verwenden: `pretest/Pretestleitfaden_und_Notizbogen.docx`. Zunächst drei Personen, anschließend begründete Überarbeitung und zwei weitere Personen. Die Fragebogenversion ist für jede Person gesondert zu protokollieren.

Die Prüfung von `auswertung/score.py` wurde tatsächlich ausgeführt. Fünf Testmethoden mit zusätzlich 16 unzulässigen Eingabevarianten prüften Nullwerte, Fehlwerte, vollständige Teilbereiche, Mehrfachantworten, leere Daten und Eingabefehler. Alle vorgesehenen Prüfungen bestanden. Drei ausdrücklich künstliche Fälle wurden berechnet; die Eingaben und Ergebnisse liegen im Beispielordner. Details stehen in `tests/Pruefprotokoll.md`.

Diese technische Prüfung ist ein Nachweis zur Korrektheit der Rechenroutine in den getesteten Fällen. Zum Stand vom 29. September 2026 waren die 18 geplanten LLM-Durchläufe, weitere Prompt-Fehlerfälle und die fünf echten Gespräche noch nicht durchgeführt. Zu diesem damaligen Stand gab es noch keinen empirischen Pretestbericht und keinen belegten Vergleich von Baseline und Masterprompt. Die nachfolgende Fortschreibung ersetzt diese Statusangabe für den Pretest.


## Fortschreibung nach der ersten realen Runde · 17. Oktober 2026

### Tatsächlich durchgeführt und geprüft

Die Erstellerin stellte Antworten von drei Testpersonen aus Google Forms bereit. Nach ihrer Schilderung ließ sie die Referenz GARI-DE-0.1 anhand des Word-Fragebogens und des Pretestleitfadens KI-gestützt in ein Formular übertragen und ergänzte Beschreibungen manuell. Das geplante Nachgespräch wurde durch neun offene schriftliche Fragefelder ersetzt. Die zutreffende Verfahrensbezeichnung lautet: webbasierter Pretest mit anschließender standardisierter schriftlicher Nachbefragung anhand kognitiver Prüffragen. Synchrone Interviews, Laut-Denken-Beobachtungen oder adaptive Nachfragen sind damit nicht nachgewiesen.

Der Export und sämtliche Abschnitte der zugänglichen Formularoberfläche wurden geprüft. Die tatsächliche Umsetzung erhält für die Dokumentation nachträglich die Kennung GARI-DE-0.1-FORMS-R1. Im Original fehlte ein explizites Umsetzungsversionsfeld. Die Erstellerin bestätigte anschließend am 17. Oktober 2026, dass das Formular zwischen den drei Teilnahmen und diesem Oberflächenabgleich unverändert geblieben war. Die historische Zuordnung ist damit durch ihre Auskunft geklärt. Es wurde bei der Prüfung keine Antwort abgesendet.

Die ausgeführte Datenprüfung erkannte 34 Frage-IDs und 75 zulässige Zahlenwerte bei drei Fällen. Die neun schriftlichen Felder enthielten zusammen 23 nichtleere und vier leere Antworten; nichtleere Antworten konnten mehrfach nicht allen Teilfragen zugeordnet werden. Diese Zahlen beschreiben Datenvollständigkeit, keine Antwortqualität. Alle drei Personen berichteten bereits berufliche und private Nutzung sowie freigegebenen Zugang. Der Fall ohne Nutzungserfahrung wurde somit noch nicht empirisch geprüft.

### Zentrale Befunde und beschlossene Arbeitsrichtung

Die folgende Tabelle hält den Stand nach Runde 1 fest. Die spätere Nachprüfung der Forms-Fassung R2 ist im nächsten datierten Abschnitt dokumentiert.

| Befund | Vorbereitete Änderung | Stand der Nachprüfung |
|---|---|---|
| NB/KA waren bei allen 25 numerischen Items im Hinweis genannt, aber nicht auswählbar. | Einzelwahl mit vollständigem Antwortangebot; keine nachträgliche Fehlwertrekonstruktion. | Neue Oberfläche noch nicht eingerichtet/geprüft |
| I02 war im geprüften Formular ein numerisches Pflichtfeld; W01–W03 waren ebenfalls verpflichtend. | Alle Sachfragen freiwillig; Teilnahmezustimmung getrennt. | Offen |
| Schriftliche Prüffragen bündelten mehrere Aspekte in einem Feld. | Einzelne offene Prüffragen, klare Zuordnung und nötigenfalls neutrale Rückfragen. | Offen |
| Die nur für Nichtnutzende gedachte Rückfrage war für alle verpflichtend. | Freiwillige, bedingte Rückfrage; gezielte Ergänzung der Stichprobe um Nichtnutzende. | Offen |
| Rückmeldungen zu U05, K01 und G03 ließen Deutungen und Kontextbezüge erkennen, erlaubten aber nicht durchgängig eindeutige Schlüsse. | Kernwortlaut zunächst erhalten; gezielte Paraphrasen und neutrale Nachfragen. | Offen |

Der private Bericht `Pretest_Runde1_Auswertung.md` enthält die zeilenbezogene Befundmatrix und Interpretationsgrenzen. Er sowie Rohdaten und personenbezogene Prüfausgaben sind separat verwahrt und nicht Teil dieses Repositorypakets. Im Paket liegt `auswertung/pretest_forms_audit.py` als reproduzierbare Bestandsprüfung; es erzeugt keine Readiness-Scores. Der vertrauliche Export lässt sich damit lokal prüfen, darf aber nicht als öffentliches Beispiel eingecheckt werden.

Masterprompt 0.3 ergänzt aus diesen Befunden den Abgleich der tatsächlich verwendeten Formularoberfläche, die ehrliche Benennung schriftlicher Nachbefragungen und Regeln für nicht zuordenbare Rückmeldungen. `pretest/GoogleForms_Runde2_Anleitung.md` enthält die konkrete Umsetzungsvorgabe und zehn einzelne Prüffragen. Der alte Word-Leitfaden dokumentiert den ursprünglichen Gesprächsplan; für die schriftliche Runde 2 gilt die neue Anleitung.

### Zusätzliche geplante Fehlerfälle für Masterprompt 0.3

| Fall | Eingabe | Erwartetes Verhalten | Status |
|---|---|---|---|
| F5 | Formular nennt NB/KA im Hinweis, bietet aber nur Zahlen an; ein Item ist verpflichtend. | Abweichung erkennen, konkrete Korrektur verlangen; vollständige Zahlenantworten nicht als Nachweis von Verständnis deuten. | Geplant, noch nicht als unabhängiger Prompttest ausgeführt |
| F6 | Ein Mehrfach-Prüffeld enthält nur „Ja“. | Keine Zustimmung zu sämtlichen Teilfragen unterstellen; fehlende Zuordnung benennen und eine neutrale Rückfrage formulieren. | Geplant, noch nicht als unabhängiger Prompttest ausgeführt |

Diese zwei Fälle ergänzen die bisherigen vier Fehlerfälle. Ihre Ergänzung sowie die Bearbeitung realer Antworten in dieser Zusammenarbeit sind kein nachträglich konstruierter Baselinevergleich. Die 18 geplanten LLM-Durchläufe und die kontrollierten Prompt-Fehlerfalltests bleiben offen.

### Nächster Evaluationsschritt und zulässige Aussage

Die erste Umsetzung bleibt dokumentiert. Die korrigierte Kopie erhält die eigene Kennung GARI-DE-0.1-FORMS-R2. Nach der Oberflächenprüfung werden zwei weitere Personen einbezogen, möglichst mit bisher fehlenden Nutzungserfahrungen und Tätigkeiten. Runde 1 und Runde 2 bleiben getrennt. Eine verbesserte Verständlichkeit oder erfolgreiche Behebung wird erst nach tatsächlicher Nachprüfung berichtet.

Belegt ist bisher, dass die erste reale Runde konkrete Probleme der Antwortoberfläche und der Rückfragen sichtbar machte und diese eine begründete Weiterentwicklung des Artefakts auslösten. Nicht belegt sind psychometrische Validität, Repräsentativität, ein Unternehmensprofil, Wirksamkeit von Trainings oder eine systemübergreifende Robustheit des Masterprompts. Die KI-unterstützte Auswertung benötigt die Prüfung durch die Erstellerin; ein unabhängiges Zweitcoding wurde nicht durchgeführt.


## Fortschreibung: Forms-R2 und zwei synthetische Rollenläufe · 17. Oktober 2026

Die Erstellerin erstellte mit dem vorgeschlagenen Prompt die Fassung GARI-DE-0.1-FORMS-R2 und ergänzte Hinweise manuell. Anschließend ließ sie Claude im Browser zwei fiktive Rollen ausfüllen: eine Baupersona mit kaum praktischer GenAI-Erfahrung und eine regelmäßig nutzende Marketingpersona. Dieser ergänzende Entwicklungsschritt war nicht Teil des ursprünglichen kontrollierten Testplans. Er wird als technische Erprobung und Quelle von Prüfhypothesen aufgenommen, nicht als zweite Runde mit echten Testpersonen.

**Aktueller Umfang: drei echte Testpersonen und zwei synthetische Antwortfälle.** Die zwei weiteren echten Tests bleiben offen. Ebenso bleiben die 18 kontrollierten LLM-Durchläufe sowie die sechs geplanten Prompt-Fehlerfälle offen; die Persona-Prompts sind keine nachträglich passenden Ersatzläufe.

### Beobachtete Korrekturen und verbleibende Probleme

- In der geprüften Oberfläche enthalten alle 25 Zahlenfragen die vollständigen Zahlenoptionen, NB und KA. Die 34 Kern-IDs sind vorhanden.
- I02 und W03 ließen sich leer passieren. Die sichtbaren Sachfragen und schriftlichen Prüffragen enthalten keine Pflichtmarkierungen; die separate Zustimmung bleibt davon unabhängig.
- PF03–PF10 bündeln weiterhin mehrere Teilfragen. Zehn vorhandene Felder entsprechen nicht automatisch der vorgesehenen Liste von zehn einzelnen Fragen.
- Bei W01 und W02 war mit jeweils vier Auswahlen der Seitenwechsel zur Nachbefragung möglich. Eine endgültige Übermittlung wurde nicht ausgelöst oder geprüft.
- Einzelne Einleitungs- und Bedienhinweise nennen weiterhin Gespräch oder Einkreisen; W02 verwendet „Themen“ statt „Antworten“.

Die Bestandsprüfung wurde mit `auswertung/audit_synthetic_forms.py` ausgeführt: zwei Fälle, 46 Zahlenwerte im erlaubten Bereich, vier NB-Antworten und 20 nichtleere schriftliche Feedbackfelder. Im ersten Fall sind C02, C04 und C06 leer. Eine spätere Behauptung im Freitext, C02 mit „an keinem Tag“ beantwortet zu haben, ersetzt den fehlenden strukturierten Wert nicht. Die Rohdaten wurden nicht korrigiert; es wurden keine Readiness-Scores berechnet.

Das Protokoll mit den tatsächlich mitgeteilten Persona-Prompts steht in `pretest/Claude_Persona_Testprotokoll.md`. Der ausführliche Arbeitsbericht und der Originalexport werden separat bereitgestellt. Die genaue Claude-Modellversion und die Nutzung getrennter Chats sind noch zu ergänzen. Nicht vorgegebene Unternehmensdetails in den Antworten werden als Modellerweiterungen behandelt.

### Konsequenz für Artefakt und weitere Evaluation

Masterprompt 0.4 ergänzt die Herkunftsprüfung synthetischer Daten, die Trennung von Formularerzeugung und Antwortsimulation, den wortgetreuen Abgleich der Prüffragen sowie funktionale Kontrollen von Eingaberegeln. Die Liste der schriftlichen Prüffragen ist im aktualisierten Kopierprompt vollständig enthalten. Der zuvor verwendete Verweis auf eine zusätzliche Anleitung war kein hinreichender Schutz gegen die beobachtete Übernahme der alten Mehrfachfragen.

Die Korrektur wird als GARI-DE-0.1-FORMS-R2.1 vorbereitet. Vorgesehen sind die Einzelprüffragen, eine wirksame Höchstzahlregel, angepasste Durchführungshinweise und die Wiederherstellung des W02-Hinweises. Nach dem technischen Abgleich folgen die zwei echten Tests. Kein neuer Persona-Lauf ist dafür zwingend erforderlich. Die erfolgreiche Nachprüfung von R2.1 ist noch offen.

Der technische Nutzen der Rollenläufe besteht darin, gespeicherte NB-Antworten und prüfbare Unstimmigkeiten sichtbar zu machen. Die inhaltlichen Rückmeldungen bleiben Hypothesen und belegen keine menschlichen Verständlichkeitsprobleme. Der Einsatz mehrerer KI-Systeme ist allein kein Nachweis unabhängiger Evaluation oder systemübergreifender Robustheit.
