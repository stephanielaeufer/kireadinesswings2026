# Projektgrundlage zur Readiness für generative KI

Stand 17. Oktober 2026

> Nachtrag 18. Oktober 2026: Dieses Dokument beschreibt den Planungsstand vor der Evaluation des Masterprompts. Den aktuellen Stand enthalten `PROJEKTKONTEXT.md`, `CHANGELOG.md` und `tests/Masterprompt_Evaluation_2026-10-18.md`. Die Gliederung der Hausarbeit folgt inzwischen den sechs Punkten des Study Guides.

Entwickelt wird ein unternehmensübergreifend wiederverwendbares Verfahren, das den Status quo bei Mitarbeitenden sichtbar macht und Hinweise auf Weiterbildungsbedarf ableitet. Das DSR-Artefakt besteht aus theoriegestützten Leitlinien, umgesetzt in einem Masterprompt mit definierten Ein- und Ausgaben. Fragebogen und Ergebnisbericht sind Anwendungen dieses Artefakts.

## Thema und Forschungsfrage

**Vorschlag für die Themeneintragung**

Entwicklung und formative Evaluation eines theoriegestützten Masterprompts zur Erfassung der Readiness für generative KI und des Weiterbildungsbedarfs von Mitarbeitenden

**Forschungsfrage**

Wie lässt sich ein theoriegestützter Masterprompt gestalten und formativ evaluieren, der unternehmensübergreifend standardisierte Fragebögen zur Readiness für generative KI erstellt und aus erhobenen Antworten nachvollziehbare Hinweise auf Weiterbildungsbedarf ableitet?

Drei Teilfragen konkretisieren die Untersuchung: Welche Konstrukte und Messinstrumente eignen sich für diesen Zweck? Welche Promptregeln sichern Quellenbezug, Standardisierung und eine nachvollziehbare Auswertung? Welche Probleme zeigen sich in dokumentierten Testfällen und einem webbasierten Pretest mit schriftlicher Nachbefragung, und welche Verbesserungen folgen daraus?

Die Formulierung verspricht eine Entwicklung und formative Prüfung. Eine statistische Validierung oder nachgewiesene universelle Einsetzbarkeit wird damit nicht behauptet.

## Festgelegter Umfang

| Aspekt | Festlegung |
|---|---|
| Technologie | Generative KI, beispielsweise zur Erzeugung und Bearbeitung von Text, Bild, Audio, Video oder Code |
| Zielgruppe | Mitarbeitende aus allen Tätigkeitsbereichen eines Unternehmens, einschließlich Personen ohne bisherige KI-Nutzung |
| Zweck | Status quo, subjektiv eingeschätzte Fähigkeiten und Bereitschaft, Lernwünsche sowie betriebliche Voraussetzungen beschreiben |
| Sprache | Deutsch als Ausgangsversion; andere Sprachen erfordern eine dokumentierte Übersetzungs- und Prüfphase |
| Empirie | Abgeschlossen mit drei realen Testpersonen und zwei getrennten synthetischen Claude-Fällen; keine weitere reale Teilnahme vorgesehen |
| Prozess | Briefing, Quellenprüfung, Fragebogen, Codebuch, Pretest, Auswertung und Maßnahmenbericht |
| Systeme | Freie Wahl; NotebookLM optional; zusätzliche Agenten nur bei begründetem praktischem Nutzen |
| Abgabe | 1. November 2026 |
| Themeneintragung | Spätestens 18. Oktober 2026 |
| Umfang | Zehn inhaltstragende Seiten von Einleitung bis Fazit einschließlich erklärender Tabellen und Abbildungen |
| Zitation | APA; APA 7 als Arbeitsstandard, soweit keine abweichende modulbezogene Vorgabe vorliegt |
| Bereitstellung | GitHub mit README, versioniertem Prompt, Quellenzuordnung und Evaluationsnachweisen |

## Aktueller Abschlussstand vom 17. Oktober 2026

Die Datenerhebung ist mit **drei realen Testpersonen und zwei synthetischen Claude-Personas abgeschlossen**. Weitere reale Teilnahmen sind nach ausdrücklicher Entscheidung der Erstellerin nicht vorgesehen. Das ist eine Änderung des ursprünglichen Plans mit fünf realen Personen, keine nachträgliche Erfüllung dieses Plans durch KI-Antworten.

Die Erstellerin nennt als Modell- und Einstellungsangabe wörtlich **„Claude Opus Mittel 5.5“** und bestätigt getrennte Chats im Browser. Diese Angabe wird als Selbstauskunft geführt; eine technische Modell-ID und ein vollständiges Aktionsprotokoll liegen nicht vor. Die offenen Prompts waren bewusst gewählt, um Interpretation zuzulassen. Ergänzungen des Modells bleiben fiktive Kontextannahmen.

Die manuell korrigierte Fassung heißt im tatsächlich sichtbaren Formular **GARI-DE-0.1-FORMS-R3**. Die früher vorgeschlagene Bezeichnung R2.1 wurde somit nicht als Name der vorgelegten Fassung übernommen. Die Claude-Fälle bleiben R2 zugeordnet.

Die technische Nachprüfung von R3 bestätigte 25 Zahlenfragen mit NB/KA, die zehn einzelnen PF-Fragen sowie die Höchstzahl drei bei W01 und W02. Mit vier Auswahlen pro Frage erschienen zwei Validierungsfehler; erst nach Reduktion auf jeweils drei gelang der Seitenwechsel. Sachfragen wurden ohne numerische Eingaben passiert; es wurde keine Antwort abgesendet. Ein neuer Antwortdatensatz wurde nicht erzeugt.

Restpunkte: Einzelne Einleitungen sprechen noch von einem Gespräch oder begleiteten Test. W02 nennt weiterhin „Themen“ statt „Antworten“. PF05 zeigt C02 einschließlich des Vierwochenzeitraums als Erinnerung; diese Zusatzinformation könnte eine spätere Prüfung der spontanen Erinnerung beeinflussen. Die letzten beiden Punkte wurden erst am Abschlussstand so dokumentiert. Diese Restpunkte begründen keine neue Teilnehmerrekrutierung innerhalb des festgelegten Umfangs.

Die 18 geplanten kontrollierten LLM-Ausgaben und sechs Prompt-Fehlerfälle wurden nicht durchgeführt. Sie sind als nicht realisierter Plan und mögliche spätere Evaluation dokumentiert, nicht als nächste verpflichtende Projektaufgabe. Die weiter unten stehenden historischen Pläne und Zwischenstände werden durch diesen Abschnitt hinsichtlich des aktuellen Umfangs ersetzt. Die psychometrische Validität, universelle Übertragbarkeit und systemübergreifende Promptrobustheit sind nicht nachgewiesen.

Der nächste Arbeitsschritt ist die Fertigstellung von Hausarbeit und Repositoryfassung. Details zur technischen Nachprüfung stehen in `pretest/Abschluss_Evaluation_R3.md`.


## Befund aus den neuen Anhängen

Der Evaluationsbogen ist als Bewertungsbogen für eine kreative Präsentation im Praxismodul überschrieben und enthält Hinweise auf eine Disputation. Nach der aktuellen Mitteilung ist in diesem Semester keine Verteidigung vorgesehen. Übernommen werden die inhaltlichen Qualitätskriterien: nachvollziehbare Struktur, begründete Problemstellung, passende wissenschaftliche Literatur, sachlogische Operationalisierung, praktische Lösungsqualität, Evaluation und reflektierte Grenzen.

Die Punktwerte werden nicht eigenständig in eine neue Hausarbeitsgewichtung umgerechnet. Zusätzlich sind die im Bereich Lösungsfindung genannten Teilpunktzahlen nicht konsistent mit dem ausgewiesenen Dimensionsmaximum. Für unsere Planung ist deshalb die qualitative Beschreibung maßgeblich, nicht eine selbst konstruierte Gesamtnote.

Die Word-Datei enthält bereits eine andere Hausarbeit und ist kein eigenständiger Leitfaden für alle WINGS-Formalregeln. Ausgelesen wurden Arial 11 pt, 1,5-facher Zeilenabstand und für die normalen Hochformatabschnitte A4 mit 4 cm linkem, 2,5 cm rechtem sowie je 2 cm oberem und unterem Rand. Die Datei enthält außerdem abweichende Abschnitte und Formatierungen. Für die spätere Hausarbeit werden geeignete Formatvorlagen übernommen und Titelblatt, Verzeichnisse und Metadaten auf dieses Modul angepasst. Die Angaben der Vorarbeit werden dabei nicht ungeprüft weiterverwendet.

## Messmodell als begründeter Arbeitsentwurf

Readiness bezeichnet hier die individuell wahrgenommene Fähigkeit und Bereitschaft, generative KI im Arbeitskontext sachgerecht und verantwortungsvoll einzusetzen. Nutzungsverhalten, persönliche Voraussetzungen und wahrgenommene betriebliche Bedingungen werden getrennt beschrieben. Selbstauskünfte ergeben keinen objektiven Kompetenznachweis.

Der Reasoned Action Approach dient als Erklärungsrahmen für Bereitschaft und Kontextbedingungen. MAILS liefert eine ergänzende Grundlage für Kompetenzfacetten und Selbstwirksamkeit. Ajzens Anleitung betont die genaue Festlegung des interessierenden Verhaltens und seines Kontextes; MAILS bietet modular untersuchte Selbstberichtskonstrukte. Eine Übertragung auf generative KI wird als Anpassung dokumentiert (Ajzen, o. J.; Carolus et al., 2023).

| Bereich | Funktion für die Diagnose | Geplante Grundlage und Grenze |
|---|---|---|
| Bisherige Nutzung | Erfahrung und Nutzungssituationen beschreiben | Eigene Kontextfragen; Häufigkeit ist kein Kompetenzwert |
| Verständnis und Anwendung | Selbst eingeschätzte Kenntnisse und praktische Fähigkeiten erfassen | Passende MAILS-Teilskalen prüfen; keine beliebige Kurzfassung als validiert ausgeben |
| Bewertung und verantwortlicher Umgang | Umgang mit möglichen Fehlern, Grenzen und sensiblen Inhalten erfassen | Kompetenzliteratur und gesondert gekennzeichnete GenAI-Ergänzungen; keine Gleichsetzung mit blindem Vertrauen |
| Selbstwirksamkeit | Zutrauen in Lernen und Bewältigen konkreter Aufgaben erfassen | Überschneidungen zwischen MAILS und wahrgenommener Verhaltenskontrolle prüfen |
| Einstellung und Nutzungsabsicht | Bereitschaft unter einem klar definierten Anwendungskontext beschreiben | Ausgewählte RAA-Konstrukte; keine vollständige Prüfung des RAA-Wirkungsmodells |
| Aufgabenpassung und Rahmenbedingungen | Relevanz, Zugang, Regeln, Zeit und Unterstützung einordnen | Getrenntes Kontextmodul; TTF- und soziotechnische Literatur als ergänzende Begründung |
| Lernwünsche | Gewünschte Themen und konkrete Aufgaben erfassen | Eigene Bedarfsfragen; Wünsche und nachgewiesene Kompetenzlücken unterscheiden |

Die Tabelle beschreibt den Rahmen. In der Fassung GARI-DE-0.1 sind 34 Frage-IDs konkret festgelegt: sechs Kontextfragen, 15 Anpassungen aus den vollständigen MAILS-Teilbereichen Anwendung, Verständnis und Lernen, drei eigene GenAI-Fragen, vier Einstellungs- und drei Absichtsfragen sowie drei Fragen zu Weiterbildung und Hindernissen. Die sieben RAA-bezogenen Items stammen aus der bereitgestellten PowerPilot-Itemsammlung; der direkte Wortlautvergleich mit dem verlinkten Original-Anhang ist noch offen. Für die MAILS-Items wurde der deutsche Autorenfragebogen geprüft.

Problemlösen, globale KI-Ethik, Emotionsregulation und Persuasionskontrolle sind nicht als eigene Skalen enthalten. Fragen zu Ergebnisprüfung und zulässigen Eingaben ersetzen keine vollständige Ethikmessung. Die Fassung misst keine objektive Kompetenz und keine vollständige organisationale Readiness. Begründungen und Änderungen stehen in Itemregister.md; die Auswahl ist kein validiertes neues Messmodell. Die geschätzte Bearbeitungszeit beträgt 10–15 Minuten und wird im Pretest gemessen.

Ein fester Kern erhält stabile IDs, Formulierungen, Antwortskalen und Auswertungsregeln. Betriebsspezifische Einleitungen, Aufgabenbeispiele und Zusatzmodule werden gesondert versioniert. Falls der Kern angepasst werden muss, entsteht eine neue Version; Vergleichbarkeit wird erneut geprüft.

## Vom Befund zur Maßnahme

Jede Empfehlung benötigt eine dokumentierte Verbindung zwischen Antworten, deren Interpretation und einer geeigneten Maßnahme. Die folgenden Beispiele sind eigene Verfahrensregeln, keine validierten Klassifikationsgrenzen.

| Beispielhafter Befund | Vorläufiger Handlungsansatz | Zusätzliche Prüfung |
|---|---|---|
| Unsicherheit bei einer anwendungsbezogenen Fähigkeit und entsprechender Lernwunsch | Passende praktische Lernaufgabe oder Einführung anbieten | Aufgabenbezug und vorhandene Unterstützung |
| Fehlender Zugang zu freigegebenen Werkzeugen | Zugang und Zuständigkeit klären | Keine Kompetenzlücke allein aus Nichtnutzung ableiten |
| Regeln zur Nutzung sind unbekannt | Verständliche Orientierung und Ansprechstelle bereitstellen | Prüfen, ob Regeln bestehen und zugänglich sind |
| Hohe Selbsteinschätzung bei zugleich berichteten Schwierigkeiten mit der Ergebnisprüfung | Vertiefenden Lernbedarf gezielt untersuchen | Selbsteinschätzung nicht als Leistungsnachweis behandeln |
| Keine erkennbare Aufgabenpassung | Geeignete Anwendungsfälle gemeinsam prüfen | Geringe Nutzung kann sachlich angemessen sein |

Ohne empirisch begründete Schwellen entstehen keine Reifegradklassen, Gesamtnoten oder gewichteten 0-bis-100-Werte. Erste Auswertungen zeigen Antwortverteilungen und, soweit methodisch begründet, getrennte Skalenwerte. Der Bericht benennt Datenbasis, Unsicherheit und Grenzen jeder Empfehlung.

## Umsetzung der sechs DSR-Aktivitäten

| Aktivität nach Peffers et al. | Umsetzung im Projekt | Nachweis |
|---|---|---|
| Problem und Motivation | Unterschiedliche Fragen, unklare Konstrukte und schwer prüfbare KI-Ausgaben als praktisches Problem präzisieren | Einleitung und Anforderungen |
| Ziele der Lösung | Wissenschaftliche Fundierung, stabile Kernfragen, vollständiger Ablauf und prüfbare Empfehlungen festlegen | Anforderungs- und Kriterienmatrix |
| Entwicklung | Quellen prüfen, Konstrukte auswählen, Itemregister und Masterprompt entwickeln | Versionierte Dateien und Entscheidungsprotokoll |
| Demonstration | Formularumsetzung und technische Rechenbeispiele demonstrieren | Dokumentierte Formularfassungen und künstliche Rechenbeispiele |
| Evaluation | Drei reale Fälle, zwei synthetische Personas und technische Prüfungen getrennt berichten | Bewertete Ergebnisse und dokumentierte Änderungen |
| Kommunikation | Vorgehen, Befunde und Grenzen in Hausarbeit und GitHub darstellen | Zehn Seiten und referenzierbare Projektversion |

Die Evaluationslogik verbindet kontrollierte Verfahrensprüfungen mit Nutzerfeedback. Die Zuordnung orientiert sich am FEDS-Rahmen; Zahl und Zuschnitt der Testfälle sind eigene, dem Umfang angepasste Planungsentscheidungen (Venable et al., 2016).

## Seitenbudget für die Hausarbeit

| Kapitel | Inhalt | Seiten |
|---|---|---:|
| 1 Einleitung | Problem, Ziel, Forschungsfrage und Abgrenzung | 1,0 |
| 2 Theoretische Grundlage | Readiness, begründete Modellauswahl und Operationalisierung | 2,0 |
| 3 Methodisches Vorgehen | DSR und vorab festgelegtes Evaluationsdesign | 1,0 |
| 4 Entwicklung des Artefakts | Anforderungen, Promptarchitektur und zentrale Entscheidungen | 2,0 |
| 5 Demonstration und Evaluation | Testfälle, Pretestbefunde und tatsächlich durchgeführte Iterationen | 2,5 |
| 6 Diskussion und Fazit | Antwort auf Forschungsfrage, Grenzen und Weiterentwicklung | 1,5 |
| Gesamt | Tabellen und Abbildungen innerhalb dieser Budgets | 10,0 |

GitHub trägt die vollständigen Materialien. Die Hausarbeit muss dennoch ohne Öffnen des Repositorys verständlich bleiben und die entscheidenden Befunde selbst enthalten. Ein Anhang ersetzt keine wesentliche Argumentation im Haupttext.

## Ursprünglicher Zeitplan als historische Planung

| Zeitraum | Arbeitsergebnis |
|---|---|
| 18. bis 25. September | Thema, Konstruktdefinitionen, Quellenprüfung und erste Itemauswahl |
| 26. September bis 2. Oktober | Fragebogenkern und Codebuch erstellt am 29. September; erste praktische Promptdurchläufe vorbereiten |
| 3. bis 9. Oktober | Baselinevergleich, Überarbeitung und möglichst bereits Themeneintragung |
| 10. bis 16. Oktober | Pretest mit fünf Personen, dokumentierte Anpassungen und Nachprüfung |
| Spätestens 18. Oktober | Verbindliche Frist zur Themeneintragung |
| 19. bis 25. Oktober | Hausarbeit mit tatsächlichen Ergebnissen und vollständiger Projektstruktur |
| 26. bis 31. Oktober | Quellen-, Format- und Funktionsprüfung; Abgabeversion festhalten |
| 1. November | Abgabe |

Der Plan ist eine Arbeitsplanung und keine Terminbuchung. Fachliche Entscheidungen und Testprotokolle werden laufend festgehalten, damit die spätere Prozessdarstellung auf tatsächlich ausgeführter Arbeit beruht.
