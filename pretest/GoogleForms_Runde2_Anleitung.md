# Google Forms: korrigierte Umsetzung für Runde 2

**Historische Umsetzungsanleitung. Aktueller Stand vom 17. Oktober 2026:** Die Erstellerin hat eine Fassung mit sichtbarer Kennung GARI-DE-0.1-FORMS-R3 erstellt. Die Erhebung ist mit drei realen Personen und zwei synthetischen Fällen abgeschlossen; die unten geplanten weiteren echten Teilnahmen werden nicht mehr durchgeführt. Für Befunde und Restpunkte gilt `Abschluss_Evaluation_R3.md`. Der vorgeschlagene Name R2.1 war ein Planungsname. Er wird nicht rückwirkend als Name von R3 verwendet.


Stand: 17. Oktober 2026 · Nachprüfung von R2 abgeschlossen; Korrekturvorschlag R2.1 für die zwei noch geplanten echten Tests

Referenz: GARI-DE-0.1. Vorgesehene Kennzeichnung der neuen Onlinefassung: **GARI-DE-0.1-FORMS-R2.1**. Die Kernitemtexte, Zahlenbereiche und IDs bleiben im Vorschlag erhalten. Geändert werden Darstellung, verfügbare Antwortoptionen gegenüber Runde 1, Pflichtfeldeinstellungen und die gesonderte Pretest-Nachbefragung. Daher ist dies eine eigene Fassung; sie wird nicht stillschweigend mit Runde 1 zusammengeführt.


## Aktueller Befund und konkrete Nacharbeit

Die geprüfte Fassung **GARI-DE-0.1-FORMS-R2** enthält NB/KA in allen Zahlenfragen und keine verpflichtenden Sachfragen mehr. Die zehn schriftlichen Felder entsprechen allerdings nicht der unten festgelegten Liste: Acht Felder enthalten weiterhin mehrere Teilfragen. Bei W01 und W02 war der Seitenwechsel mit jeweils vier Auswahlen möglich. Einzelne Texte sprechen noch von Gespräch und Einkreisen.

Für die Kopie R2.1 sind daher vier gezielte Korrekturen vorgesehen:

1. Den Abschnitt mit den schriftlichen Rückfragen durch PF01–PF10 aus Abschnitt 3 ersetzen. Die IDs sind versionsgebunden: PF04 bedeutet in R2 etwas anderes als PF04 in der hier vorgesehenen Fassung. Alte Antworten nicht unter neue Fragetexte umetikettieren.
2. Bei W01 und W02 über Dreipunkt-Menü → Antwortenvalidierung eine Höchstzahl von drei Auswahlen festlegen. In einer Prüfsitzung vier auswählen und kontrollieren, dass das Weitergehen blockiert wird. Die endgültige Übermittlung wurde bisher nicht getestet.
3. Auf der ersten Seite „Beim Gespräch weiß ich, wer Sie sind …“ durch „Die durchführende Person kann Ihre Teilnahme kennen; die Darstellung in der Hausarbeit erfolgt ohne Namen.“ ersetzen. Auf der folgenden Einführungsseite „Im anschließenden Gespräch …“ durch die Ankündigung schriftlicher Rückfragen ersetzen. In „Lernen und Prüfen“ „Kreisen Sie … ein“ durch „Wählen Sie pro Aussage eine Antwort.“ ersetzen.
4. In W02 wieder „Bitte höchstens drei Antworten auswählen.“ verwenden. Den zusätzlichen Satz „Innerhalb einer Frage darf nur eine exklusive Antwort allein gewählt werden.“ aus beiden W-Titeln entfernen; den konkreten Abschnittshinweis zu den allein zu wählenden Antwortkategorien beibehalten.

Für diese Nacharbeit ist keine erneute Erzeugung des gesamten Sachfragebogens erforderlich. Die korrigierte Oberfläche anschließend prüfen und dann mit zwei echten Personen erproben. Die vorhandenen Claude-Antworten bleiben als SYNTHETIC_DEMO in der bisherigen R2-Fassung dokumentiert.

## 1. Formular für Runde 2 vorbereiten

Eine Kopie der bereits mit zwei synthetischen Fällen erprobten R2-Umsetzung erstellen. Den bisherigen Export und die erste Fassung aufbewahren. In Titel oder Beschreibung die Fassung und ein Datum nennen; im Durchführungsprotokoll die verwendete Fassung jedem Testkürzel zuordnen. Eigene technischen Probeläufe getrennt von den zwei echten Pretests halten.

Google dokumentiert numerische Endpunkte für die lineare Skala sowie frei vorgebbare Optionen für Einzelwahlfragen. Daher ist **Multiple Choice mit genau einer auswählbaren Antwort je Item** die vorgeschlagene Umsetzung für die Zahlenfragen (Google, o. D.-a). Keine Checkboxen für diese Items verwenden. Ein Raster wäre möglich, sollte aber wegen der vielen Spalten erst nach einer Darstellungskontrolle auf kleinen Bildschirmen verwendet werden; die Einzelwahl pro Frage ist hier der Arbeitsvorschlag.

| Fragen | Fragetyp | Antwortangebot | Pflichtfeld |
|---|---|---|---|
| C01–C06 | Multiple Choice/Einzelwahl | Sämtliche Kategorien aus der Referenzbank einschließlich Unsicherheitsoptionen und Keine Angabe | Nein |
| U01–U06, K01–K06, L01–L03, G01–G03 | Multiple Choice/Einzelwahl | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Nicht beurteilbar (NB), Keine Angabe (KA) | Nein |
| A01–A04, I01–I03 | Multiple Choice/Einzelwahl | 1, 2, 3, 4, 5, 6, 7, Nicht beurteilbar (NB), Keine Angabe (KA) | Nein |
| W01, W02 | Kästchen/Mehrfachwahl | Vollständiges jeweiliges Angebot aus der Bank einschließlich Keine Angabe | Nein |
| W03 | Absatz/Freitext | Freiwilliger Text; Hinweis, dass leer gelassen oder „Keine Angabe“ eingetragen werden kann | Nein |
| Schriftliche Nachbefragung | Je Prüffrage ein Absatzfeld | Freitext; eine klar umrissene Frage pro Feld | Nein |

Eine gesonderte Zustimmung zur Teilnahme darf weiterhin Voraussetzung des Beginns sein. Wer nicht teilnehmen möchte, kann den Vorgang verlassen; keine Umfrageantwort wird verlangt. Die Sachfragen dürfen trotzdem ausgelassen werden, wie in der Einleitung angekündigt. Insbesondere I02 und W03 nicht als Pflichtfragen übernehmen.

Zahlenoptionen aufsteigend anordnen, anschließend NB und KA. Keine Zufallsreihenfolge, Sterne, zusätzlichen Zwischenanker oder Vorauswahl. Die beiden Endanker des jeweiligen Abschnitts unverändert anzeigen:

- 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt.
- 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu.

NB bedeutet: Es fehlt eine Grundlage für die Einschätzung. 0 ist eine tatsächliche Fähigkeitseinschätzung. KA bedeutet, dass keine Angabe gemacht werden soll. NB oder KA niemals als 0, 11, 12 oder mittleren Skalenwert kodieren. Ein leer gelassenes Feld verrät den Grund nicht. Das vorhandene Codebuch behandelt es als KEINE_ANGABE; im Rohdatenprotokoll bleiben eine explizite KA-Auswahl und ein leeres Feld unterscheidbar.

W01 und W02: höchstens drei Auswahlen über Antwortenvalidierung einstellen. Google beschreibt dafür eine Höchstzahlregel (Google, o. D.-b). Der Hinweis zu exklusiven Optionen bleibt zusätzlich stehen. Eine Höchstzahl von drei verhindert nicht jede unzulässige Mischung, etwa „kein Wunsch“ plus ein Thema. Solche Kombinationen weiterhin prüfen und nach Codebuch behandeln; keine unbelegte automatische Exklusivitätsprüfung behaupten. Freitexte nicht durch künstliche Mindestzeichenlängen verlängern lassen.

## 2. Bedien- und Pretesthinweise anpassen

Die Definition von generativer KI sowie die inhaltlichen Instruktionen zu Fähigkeit, Zustimmung und erwarteten Einsatzbedingungen werden aus der Bank übernommen. Folgende Anpassungen gehören ausdrücklich in das Änderungsprotokoll der Onlinefassung:

| Stelle | Onlinefassung |
|---|---|
| Papierbedienung „Kreisen Sie … ein“ | „Wählen Sie pro Aussage eine Antwort.“ |
| Ankündigung eines anschließenden Gesprächs | „Nach dem Fragebogen folgen kurze schriftliche Rückfragen dazu, wie Sie die Fragen verstanden haben. Es geht um die Verbesserung des Fragebogens, nicht um die Bewertung Ihrer Arbeitsleistung.“ |
| Ankündigung am Ende | „Bitte beantworten Sie nun die schriftlichen Rückfragen. Wenn eine Frage unklar ist, ist auch dieser Hinweis hilfreich.“ |
| Übergang zu A/I | „Ab hier wechselt die Skala: 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu.“ |

Der Kern enthält keine Schulung und keine Erklärung vermeintlich richtiger Antworten. Keine Beispiele einfügen, die „zentrale Konzepte“ oder „brauchbare Ergebnisse“ schon vor der Prüfung verbindlich ausdeuten. Die Wirkung einer solchen Erklärung wäre eine zusätzliche Veränderung des Instruments.

Die ursprüngliche Zeitangabe bleibt eine Schätzung, bis die tatsächliche Dauer erfasst wurde. Für Runde 2 nach Möglichkeit Beginn und Ende des Fragebogens sowie der Nachbefragung separat protokollieren. Werden die Zeiten nur von der Person geschätzt, als Schätzung kennzeichnen. Der Google-Forms-Absendezeitstempel allein reicht nicht.

## 3. Schriftliche Prüffragen zum direkten Übernehmen

Diese Fragen bilden einen **separaten Evaluationsabschnitt**, keine zusätzlichen Readiness-Items und keinen Score. Je Nummer genau ein eigenes Absatzfeld. Kurze Erläuterungen sind ausreichend; die Felder bleiben freiwillig.

| ID | Wortlaut | Zweck |
|---|---|---|
| PF01 | Was verstehen Sie in diesem Fragebogen unter „generativer KI“? | Begriffsverständnis ohne zusätzliche Vorgabe prüfen |
| PF02 | Was bedeutet für Sie die Antwort 0 bei den Fragen zu Ihren Fähigkeiten? | Bedeutung des gültigen Nullwerts |
| PF03 | In welcher Situation würden Sie bei diesen Fragen „Nicht beurteilbar (NB)“ auswählen? | NB von einer niedrigen Fähigkeitseinschätzung unterscheiden |
| PF04 | In welcher Situation würden Sie „Keine Angabe (KA)“ auswählen? | KA gegenüber NB prüfen |
| PF05 | Auf welchen Zeitraum haben Sie sich bei C02 bezogen? | Erinnerungsbezug prüfen |
| PF06 | Was bedeutet die Aussage U05 für Sie in eigenen Worten? | Arbeitsunterstützung bzw. vollständige Delegation explorieren |
| PF07 | Was verstehen Sie in K01 unter „zentralen Konzepten“? | Unklaren Begriff prüfen |
| PF08 | Woran haben Sie beim Beantworten von G03 gedacht? | Regelbezug neutral untersuchen |
| PF09 | Welche Bedingungen haben Sie bei Ihrer Antwort auf I03 zugrunde gelegt? | Erwarteten Arbeitskontext prüfen |
| PF10 | Welche Stelle im Fragebogen hat Ihnen Schwierigkeiten bereitet? Bitte beschreiben Sie die Stelle möglichst mit der Frage-ID. | Offene Fehlersuche |

Bei PF06–PF09 den jeweiligen Originalitemtext aus der Bank als Beschreibung ergänzen, ohne eine Interpretation vorzugeben. Die Reihenfolge von Fragebogen und Prüffragen beibehalten: erst die vollständige Sachbefragung, dann die Nachbefragung.

Ergänzende, bedingte Rückfragen nur bei Bedarf und jeweils einzeln stellen:

- An eine Person ohne bisherige berufliche **und** private Nutzung: „Bei welcher Fähigkeitsfrage konnten Sie keine Einschätzung abgeben?“ Als freiwillige Frage mit dem Zusatz „Falls Sie generative KI noch nie selbst genutzt haben …“ anzeigen oder gezielt nachträglich stellen. Kein Pflichtfeld für alle.
- Bei einem Hinweis auf W01/W02: „Welche konkrete Antwortmöglichkeit hat Ihnen bei [Item-ID] gefehlt?“ Eine mögliche Schwierigkeit mit der Auswahlgrenze gesondert klären.
- Bei unklarem Skalenwechsel: „Was bedeutet die Antwort 1 im Abschnitt Einstellung und geplante Nutzung?“ Keine bloße Ja/Nein-Frage zum Bemerken des Wechsels.
- Bei weiter offenem Prüfbedarf: jeweils einzeln nach dem Unterschied G01/G02, K03/K04 oder nach „zufriedenstellend“ in A02 fragen.

Werden Rückfragen außerhalb des Formulars gestellt, Antwort, Datum, Kürzel, Item-ID und Kommunikationsform dokumentieren. Keine Interpretation in die ursprüngliche Antwort eintragen. Eine Antwort „Ja“ auf eine offene Paraphrasierungsfrage wird als nicht ausreichend erklärt markiert und gegebenenfalls nachgefragt.

## 4. Kopierprompt für die KI-gestützte Forms-Übertragung

Zusammen mit `Fragebogen_GARI_DE_0.1.docx` und möglichst `Itembank_GARI_DE_0.1.json` verwenden. Der Pretestleitfaden dient als Hintergrund; die Nachfragen werden nach Abschnitt 3 dieser Anleitung einzeln umgesetzt.

```text
Erstelle eine neue Google-Forms-Fassung für die zweite Pretestrunde.
Referenz: GARI-DE-0.1. Neue Umsetzungskennung: GARI-DE-0.1-FORMS-R2.1.

1. Übernimm alle 34 Frage-IDs, ihre Kernitemtexte, Reihenfolge, vollständigen
   Antwortkategorien und die inhaltlichen Instruktionen aus der beigefügten
   Referenz. Erfinde keine neuen Sachfragen, Skalen oder Antwortanker.
2. U01–U06, K01–K06, L01–L03 und G01–G03 werden JEWEILS eine
   Multiple-Choice-Einzelwahlfrage mit 13 Optionen: 0 bis 10,
   Nicht beurteilbar (NB), Keine Angabe (KA).
3. A01–A04 und I01–I03 werden JEWEILS eine Multiple-Choice-Einzelwahlfrage
   mit 9 Optionen: 1 bis 7, Nicht beurteilbar (NB), Keine Angabe (KA).
   Verwende für diese 25 Fragen nicht den Fragetyp Lineare Skala.
4. Zeige die unveränderten Endanker. Erhalte die Erklärung zu NB gegenüber 0
   und die Instruktion zu den tatsächlich erwarteten Bedingungen bei I01–I03.
5. Alle 34 Sachfragen sind freiwillig; kein Pflichtfeld. Eine gesonderte
   Zustimmung zum Beginn ist davon unabhängig. Keine Zufallsreihenfolge.
6. W01 und W02 bleiben Mehrfachwahlfragen mit höchstens drei Auswahlen,
   den vollständigen Optionen und dem Hinweis auf exklusive Antworten.
   W03 bleibt freiwilliger Freitext. Füge keine Mindesttextlänge ein.
7. Ersetze papierbezogene Bedienhinweise durch passende Auswahlhinweise.
   Beschreibe die Nachbefragung als schriftliche Rückfragen, nicht als ein
   geführtes Gespräch. Dokumentiere diese Änderungen separat.
8. Verwende für die schriftliche Nachbefragung ausschließlich die zehn unten
   vollständig aufgeführten Prüffragen, wortgleich und je ein freiwilliges
   Absatzfeld. Übernimm hierfür keine frühere gebündelte Nachfrageliste.
   Die bloße Zahl von zehn Feldern belegt keine Übereinstimmung.
   Die zusätzliche Rückfrage für Nichtnutzende darf kein Pflichtfeld für alle sein.
9. Falls eine Funktion nicht umsetzbar ist, benenne die genaue offene Stelle.
   Lasse keine Antwortoption stillschweigend weg. Behaupte keinen erfolgreichen
   Abgleich, solange er nicht tatsächlich durchgeführt wurde.
10. Gib zuletzt eine Prüfliste aus: 34 IDs, 25 vollständige Zahlenfragen mit
    NB/KA, keine verpflichtenden Sachfragen, korrekte W01/W02-Angebote,
    freiwilliges W03 und den wortgetreuen Abgleich jeder Prüffrage.

Verbindliche schriftliche Prüffragen:
PF01 Was verstehen Sie in diesem Fragebogen unter „generativer KI“?
PF02 Was bedeutet für Sie die Antwort 0 bei den Fragen zu Ihren Fähigkeiten?
PF03 In welcher Situation würden Sie bei diesen Fragen „Nicht beurteilbar (NB)“ auswählen?
PF04 In welcher Situation würden Sie „Keine Angabe (KA)“ auswählen?
PF05 Auf welchen Zeitraum haben Sie sich bei C02 bezogen?
PF06 Was bedeutet die Aussage U05 für Sie in eigenen Worten?
PF07 Was verstehen Sie in K01 unter „zentralen Konzepten“?
PF08 Woran haben Sie beim Beantworten von G03 gedacht?
PF09 Welche Bedingungen haben Sie bei Ihrer Antwort auf I03 zugrunde gelegt?
PF10 Welche Stelle im Fragebogen hat Ihnen Schwierigkeiten bereitet? Bitte beschreiben Sie die Stelle möglichst mit der Frage-ID.

Fehlt die angehängte Referenzbank oder der vollständige Fragebogen, melde
die fehlende Grundlage. Rekonstruiere keine Sachfragen aus Erinnerung.
```

Ein Erzeugungsprompt garantiert keine korrekte Umsetzung. Die folgenden Kontrollen müssen am tatsächlich erzeugten Formular erfolgen; der KI-Selbstbericht reicht dafür nicht.

## 5. Kurze Abnahme vor den zwei Tests

Die folgende Liste gilt für die noch zu erstellende Korrekturfassung R2.1. Der oben dokumentierte R2-Abgleich ersetzt nicht die Kontrolle dieser geänderten Kopie.

| Kontrolle | Erwartetes Ergebnis für R2.1 | Nachprüfung R2.1 |
|---|---|---|
| Alle 34 IDs und Kernwortlaute abgleichen | Keine fehlende, doppelte oder unbemerkte geänderte Frage | Offen |
| Alle 25 numerischen Fragen prüfen | Je 13 bzw. 9 Optionen, korrekte Endanker, NB und KA auswählbar | Offen |
| Je einen Pfad mit 0, NB und KA ansehen | Drei unterschiedliche Antwortmöglichkeiten, keine Umkodierung in Zahlenersatzwerte | Offen |
| I02 und W03 leer lassen | Weitergehen möglich | Offen |
| W01/W02 mit vier Themen in einer Testkopie prüfen | Höchstzahlregel verhindert vier Auswahlen | Offen |
| Exklusive Mehrfachoptionen kontrollieren | Hinweis sichtbar; verbleibende technische Grenze dokumentiert und Datenprüfung vorgesehen | Offen |
| Angaben ohne bisherige Nutzung durchgehen | Alle Sachfragen weiterhin erreichbar; NB möglich; keine fremde Pflicht-Rückfrage | Offen |
| Nachbefragung prüfen | Ein eigener Antwortplatz pro Prüffrage | Offen |
| Smartphoneansicht prüfen | Optionen und Anker vollständig les- und bedienbar | Offen |
| Probeexport aus separater Testkopie prüfen | Zahlen, NB, KA und leere Felder bleiben unterscheidbar; Testdaten nicht unter echten Antworten | Offen |

Dann zwei weitere Personen testen. Nach Möglichkeit eine ohne bisherige Nutzung und eine gelegentlich nutzende Person aus einem ergänzenden Tätigkeitsbereich. Die Auswahl, Dauer, Fassung, tatsächliche Kommunikationsform und verbleibende Probleme protokollieren. Ziel ist eine begrenzte formative Nachprüfung der Änderungen; ein positives Ergebnis oder Vollständigkeit der Fehlersuche wird nicht vorweggenommen.

Die bestehende `score.py` ist an die Referenz GARI-DE-0.1 gebunden. Daten der Forms-Fassungen nicht durch Änderung des Versionsfelds passend machen. Ein späterer produktiver Import benötigt einen ausdrücklich geprüften und versionierten Adapter bzw. ein passendes Codebuch. Für die zwei Verständlichkeitstests genügt die dokumentierte Prüfung der Antworten und Rückmeldungen.

## Quellen

Google. (o. D.-a). *Fragetyp für das Formular auswählen*. Google Docs-Editoren-Hilfe. Abgerufen am 17. Oktober 2026, von https://support.google.com/docs/answer/7322334?hl=de

Google. (o. D.-b). *Regeln für Formulare festlegen*. Google Docs-Editoren-Hilfe. Abgerufen am 17. Oktober 2026, von https://support.google.com/docs/answer/3378864?hl=de

Die Auswahl der konkreten Darstellung, freiwilligen Felder und Prüffragen ist eine begründete Projektentscheidung; die Google-Hilfe bestätigt die verwendeten Funktionen.
