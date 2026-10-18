# GARI-DE-0.1 im Modus ANWENDEN: Onlinefassung für den fiktiven Demonstrationsbetrieb S1

**Achtung: Das ist eine fiktive Demonstration.** Laut `briefing.json` (kontextart FIKTIVE_DEMONSTRATION) ist das Unternehmen erfunden. Es liegen keine realen Daten vor, und für diesen Fall werden auch keine erzeugt.

## 0 Laufangaben

| Angabe | Wert |
|---|---|
| Datum | 18. Oktober 2026 |
| System und Modell | Claude (Anthropic). Angezeigte Modellbezeichnung: „Opus 5.5“, Kennung `claude-opus-5-5`. Temperatur und weitere Parameter: NICHT_VERFUEGBAR |
| Promptversion | Masterprompt 0.5 vom 17. Oktober 2026 |
| Betriebsart | ANWENDEN, laut Auftrag ausdrücklich angegeben |
| Eingaben | `briefing.json` (Briefing 0.1, Szenario S1), `instrument/Itembank_GARI_DE_0.1.json` (Stand 29.09.2026), `instrument/Codebuch.md` (Stand 29.09.2026, redaktionell fortgeschrieben 17.10.2026), `Quellen_APA.md` (Stand 17.10.2026) |
| Referenzbank und Codebuch | GARI-DE-0.1 / GARI-DE-0.1. Die Versionen passen zusammen. |
| Fragebogenversion | Kern GARI-DE-0.1, unverändert. Neue Kennung für die Umsetzung: **GARI-DE-0.1/ONLINE-S1-E1**. Das ist eine Erhebungsfassung mit geänderter organisatorischer Einleitung, kein neuer Kern. |
| Datenart | Es gibt keine Antwortdaten (`antwortdaten_vorhanden: false`). |
| Berechnungsstatus | NICHT_BERECHNET. Ohne Daten gibt es nichts zu berechnen. `auswertung/score.py` gehört nicht zu den Eingaben dieses Laufs und wurde nicht ausgeführt. |
| Ausgeführter Code | Zwei eigene Python-3.13-Skripte im Arbeitsordner, beide mit Exitstatus 0: (1) die Onlinefassung aus `frozen_participant_text` erzeugen und automatisch mit der Bank abgleichen, (2) Register- und Umsetzungstabellen direkt aus der Bank erzeugen. |

Wenn derselbe Prompt noch einmal läuft, kann die Ausgabe anders aussehen. Die Kerntexte unten stammen nicht aus freier Formulierung. Sie wurden per Skript aus der Bank kopiert und automatisch abgeglichen.

## 1 Ziel, Zielgruppe, Kontext und Annahmen

**Übernommen aus dem Briefing, unverändert:**

- Zweck: Status quo beschreiben, Hinweise auf Weiterbildungsbedarf ableiten, betriebliche Voraussetzungen gesondert erfassen.
- Zielpopulation: Mitarbeitende aller Tätigkeitsbereiche eines fiktiven Dienstleistungsbetriebs mit 40 Beschäftigten, auch Personen, die GenAI bisher nicht nutzen.
- Tätigkeitsbereiche: Verwaltung, Kundenkontakt, operative Tätigkeit.
- Sprache: Deutsch. Technologie: generative KI.
- Zugang: GenAI-Erfahrung ist unterschiedlich. Es gibt ein freigegebenes Chat-Werkzeug für Büroarbeitsplätze.
- Bisherige Nutzung: unbekannt, wird mit dem Fragebogen erhoben (C02, C03).
- Erhebungsweg: Onlineformular, Zugang über Link, freiwillige Teilnahme.
- Antwortdaten: keine.

**Prüfung der Anfangsangaben:**

| Angabe | Status |
|---|---|
| Zweck, Zielpopulation, Tätigkeitsbereiche, Sprache, GenAI-Bezug | im Briefing vorhanden |
| Zugelassene Anwendungen | teilweise: „ein freigegebenes Chat-Werkzeug für Büroarbeitsplätze“. Der Name des Werkzeugs, die Regeln für Nicht-Büroarbeitsplätze und die zulässigen Dateneingaben sind unbekannt. |
| Aufgabenbezug | wird über C06 und W03 erhoben. Darüber hinaus ist er unbekannt. |
| Betrachtungszeitraum | im Kern festgelegt: C02 fragt nach den vergangenen vier Wochen, A und I nach den nächsten drei Monaten. Ein Erhebungszeitraum (Feldzeit) ist unbekannt. |
| Gewünschte Ausgabe | aus der Betriebsart abgeleitet: eine unternehmensbezogene Befragungsfassung mit unverändertem Kern |
| Art der Daten | keine Daten. Für den Datenschutz und die Anonymität des Onlineformulars gibt es keine Angaben. |
| Plattform des Onlineformulars | unbekannt |

**Annahmen dieses Laufs (eigene Entscheidungen):**

1. Die Erhebung läuft online und ohne Begleitgespräch. Deshalb werden die Pretest-Teile der Word-Einleitung ersetzt: Testkürzel und Datum, der Hinweis auf das Gespräch und die Begründung der fehlenden Anonymität im begleiteten Test. Das ist nach `frozen_text_note` erlaubt, „nur als gesondert dokumentierte Erhebungsfassung“. Die Dokumentation folgt in Abschnitt 3.2.
2. Weil es um ein fiktives Unternehmen geht, werden keine Werkzeugnamen, Regeln, Ansprechpersonen oder Gruppengrößen erfunden. Diese Stellen bleiben als ausgewiesene Platzhalter außerhalb der Items stehen.
3. Die Fassung ist plattformneutral beschrieben. Den Abgleich mit der tatsächlichen Oberfläche kann dieser Lauf nicht leisten.

### Rückfragen (höchstens drei, gebündelt)

Es gibt keine Möglichkeit, Rückfragen zu stellen. Deshalb sind alle Teile, die ohne Antworten möglich sind, unten bereits erstellt. Die drei Fragen betreffen nur die Platzhalter und die Gruppenauswertung.

1. **Datenschutz und Gruppengröße:** Welche Daten erfasst das Onlineformular technisch, zum Beispiel E-Mail-Adresse, Anmeldung oder Zeitstempel? Wer sieht die Rohdaten? Ab welcher Mindestgruppengröße dürfen Ergebnisse berichtet werden? Bis das beantwortet ist, sagt die Einleitung keine Anonymität zu. Bei 40 Beschäftigten können Teilgruppen sehr klein werden.
2. **Tätigkeitsbereiche:** Sollen Ergebnisse getrennt nach Verwaltung, Kundenkontakt und operativer Tätigkeit berichtet werden? Der Kern unterscheidet über C01 nur Büro-/Bildschirmarbeit, andere Arbeit und gemischt. Eine Abfrage der drei Briefingbereiche wäre eine dokumentierte Ergänzung außerhalb des Kerns. Sie bekäme eine eigene Kennung, zum Beispiel ONLINE-S1-E2, und eine eigene Datenschutzprüfung. Ich empfehle sie nur, wenn die Gruppen groß genug sind.
3. **Plattform und Kontakt:** Mit welcher Formularplattform wird erhoben? Wer ist Ansprechperson für Rückfragen? Davon hängen die konkrete Umsetzung der NB/KA-Optionen, die Höchstzahl bei W01/W02 und das Exportformat ab.

## 2 Quellen- und Konstruktregister mit Evidenzgrenzen

Im Modus ANWENDEN wird keine neue Quellenprüfung durchgeführt. Die Angaben unten stammen aus `Quellen_APA.md` und dem `source_register` der Bank. In diesem Lauf habe ich keine Originalquelle selbst eingesehen. Alle Aussagen zu Quellen sind also Angaben der Projektdokumentation, keine erneute Prüfung durch mich.

### 2.1 Quellenregister (Projektangaben)

| Quellen-ID | Nachweis | Dokumentierter Prüfstand | Fundstelle | Zielgruppe der Quelle, Sprache | Funktion im Instrument | Grenzen |
|---|---|---|---|---|---|---|
| MAILS_DE_2023 | Carolus et al. (2023); deutscher Autorenfragebogen | Laut Projekt: publizierter Volltext und deutscher Originalfragebogen geprüft (3 Seiten, 34 Items) | Items 1–6 (U), 7–12 (K), 26–28 (L); Zuordnung und Mittelwertregel Seite 3 | 300 deutschsprachige Erwachsene; allgemeine KI; Selbstbericht; Deutsch | U01–U06, K01–K06, L01–L03 (ADAPTIERT) | Gilt für allgemeine KI, nicht für GenAI am Arbeitsplatz. Fehlwertoptionen ergänzt. Die Regel, nur vollständige Fälle auszuwerten, ist eine Projektregel und stammt nicht aus MAILS. Die Rechte an der öffentlichen Nachnutzung der veränderten Items sind ungeklärt. |
| MAILS_KURZ_2024 | Koch et al. (2024) | Laut Projekt: Volltext eingesehen, Abschnitte 2.1 und 3.4 | – | – | wird nicht eingesetzt | Die Kurzfassung enthält KI-Entwicklung. Laut Artikel ist weitere Validierung nötig. |
| POWERPILOT_2025 | Wichmann et al. (2025), HICSS-58, S. 961–970; Itemsammlung Datensatz_v1.docx | Paper und bereitgestellte Itemsammlung geprüft | Questionnaire 2 / PowerPilot: 2 – Attitude, Items 1–4; 1 – Intention to use, Items 1–3 | Energiemonitoring-Anwendung; Deutschland; englischer Itemwortlaut | A01–A04, I01–I03 (ADAPTIERT) | **Der OSF-Anhang (doi:10.17605/OSF.IO/GEBK9) war am 29.09.2026 und beim erneuten Abruf nicht zugänglich. Der direkte Vergleich des Wortlauts mit diesem Anhang bleibt offen.** Der Anwendungskontext wurde übertragen. |
| Ajzen o. J. | Constructing a TPB questionnaire | Laut Projekt: Originaldokument (7 S.) eingesehen | – | – | Verhalten über Ziel, Handlung, Kontext und Zeit definieren (A/I: berufliche Aufgaben, drei Monate) | ohne Erscheinungsjahr |
| Peffers et al. 2007 | DSR-Methodik | Laut Projekt: Volltextabschnitte geprüft | – | – | Entwicklungsmethode, keine Messgrundlage | – |
| Boateng et al. 2018; NCHS 2024; Venable et al. 2016 | Skalenentwicklung, kognitive Interviews, DSR-Evaluation | Laut Projekt: Volltext bzw. offizielle Beschreibung | – | – | Pretest- und Evaluationslogik | Sie belegen keine Validität von GARI-DE. |
| Paetow et al. 2026; Do Khac et al. 2025; Wichmann et al. 2024, 2026 | bereitgestellte empirische Studien | laut Projekt bereitgestellt | – | VR, Entscheidungstragende, Gesundheit, virtuelle Meetings | Einordnung; keine Items im Kern | Sie belegen nicht, dass sich ihre Items auf GenAI übertragen lassen. |

### 2.2 Konstrukte im Kern (aus Codebuch und Bank)

| Teilbereich | Konstrukt | Art | Grundlage | Auswertung | Grenze |
|---|---|---|---|---|---|
| C01–C06 | Tätigkeit, Nutzung (4 Wochen, privat), Zugang, Kenntnis der Regeln, Aufgabenpassung | berichtetes Verhalten und wahrgenommene betriebliche Bedingungen | NEU_ENTWICKELT | jede Frage einzeln | nicht empirisch geprüft |
| U | selbst eingeschätzte Anwendung | persönliche Voraussetzung, Selbsteinschätzung | MAILS 1–6 | vorläufiger Mittelwert, nur bei vollständigen Antworten | Selbstbericht, kein Leistungsnachweis |
| K | selbst eingeschätztes Verständnis | Selbsteinschätzung | MAILS 7–12 | wie U | wie U |
| L | Zutrauen in das eigene Lernen | Selbstwirksamkeit, Selbsteinschätzung | MAILS 26–28 | wie U | wie U |
| G01–G03 | Prüfen von Ergebnissen, Prüfen von Quellen, zulässige Eingaben | Selbsteinschätzung | NEU_ENTWICKELT | drei Einzelitems, **kein G-Wert** | nicht empirisch geprüft |
| A | Einstellung zur arbeitsbezogenen Nutzung (bedingte Bewertung) | Einstellung | PowerPilot Attitude 1–4 | vorläufiger Mittelwert, nur bei vollständigen Antworten | OSF-Abgleich offen |
| I | Nutzungsabsicht unter tatsächlich erwarteten Bedingungen | Absicht | PowerPilot Intention 1–3 | wie A | wie A; kein hypothetisch zugesicherter Zugang |
| W01–W03 | Lernwünsche, Hindernisse, Wunschaufgabe | geäußerter Wunsch und wahrgenommene Bedingungen | NEU_ENTWICKELT | Häufigkeiten bzw. qualitative Zuordnung | nicht empirisch geprüft |

Es gibt keinen Gesamtwert, keinen Wert für G, C oder W und keine Reifegradklassen. 0–10-Werte und 1–7-Werte werden nicht gemeinsam gereiht. Die Kombination der Items ist **nicht psychometrisch validiert**. Auch der Originalwortlaut ist nicht für alle Items vollständig an Primärquellen geprüft. Den Prüfstand je Item zeigt Abschnitt 3.3.

## 3 Befragungsfassung, Itemregister und Codebuch

### 3.1 Befragungsfassung GARI-DE-0.1/ONLINE-S1-E1 (Ansicht für Befragte)

Diese Fassung wurde per Skript aus `frozen_participant_text` erzeugt. Kernwortlaut, Reihenfolge, IDs, Anker, NB/KA-Optionen und Instruktionen sind unverändert. Die Seitenumbrüche folgen den Abschnittsüberschriften der Word-Fassung. Die ID-Präfixe wie C01 oder U01 stehen auch in der Word-Fassung. In der Oberfläche können sie stehen bleiben. Werden sie ausgeblendet, ist das im Manifest zu vermerken. Ein Kreis „( )“ bedeutet Einzelwahl, ein Kästchen „[ ]“ Mehrfachwahl.


### Fragebogen zum Umgang mit generativer KI

Onlinebefragung · GARI-DE-0.1 · Erhebungsfassung ONLINE-S1-E1

Dieser Fragebogen erfasst Ihre Erfahrungen, Einschätzungen und Weiterbildungswünsche zu generativer KI bei der Arbeit. Die Ergebnisse werden nur zusammengefasst für das gesamte Unternehmen oder für Gruppen ab [PLATZHALTER_MINDESTGRUPPE] Personen berichtet. Sie dienen dazu, Weiterbildungsangebote und betriebliche Voraussetzungen wie Zugang und Regeln zu planen. Es geht dabei nicht um die Bewertung Ihrer Arbeitsleistung. Geschätzte Dauer für den Fragebogen: 10 bis 15 Minuten.

Generative KI erzeugt oder bearbeitet auf Eingaben hin Inhalte, zum Beispiel Texte, Bilder, Audio, Videos oder Programmcode. Gemeint sind sowohl eigenständige Anwendungen als auch entsprechende Funktionen in anderen Programmen.

Die Teilnahme ist freiwillig. Sie können einzelne Fragen auslassen oder die Befragung beenden. Bitte tragen Sie keine Namen, Personalnummern oder vertraulichen Informationen ein. [PLATZHALTER_DATENSCHUTZ: Angabe, welche Daten das Onlineformular technisch erfasst, wer die Rohdaten einsehen kann und ob Anonymität gewährleistet ist. Bis zur Klärung wird keine Anonymität zugesagt.]


---

*[Seite 1 von 5]*

### Ihre Tätigkeit und bisherige Nutzung

Bitte wählen Sie pro Frage genau eine Antwort.

**C01**  Wie sieht Ihre hauptsächliche Tätigkeit aus?

- ( ) Überwiegend Büro- oder Bildschirmarbeit
- ( ) Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst
- ( ) Etwa gleich große Anteile beider Bereiche
- ( ) Keine Angabe

**C02**  An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt?

- ( ) An keinem Tag
- ( ) An 1 bis 3 Tagen
- ( ) An 4 bis 9 Tagen
- ( ) An 10 bis 15 Tagen
- ( ) An 16 oder mehr Tagen
- ( ) Kann ich nicht einschätzen
- ( ) Keine Angabe

**C03**  Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt?

- ( ) Ja
- ( ) Nein
- ( ) Ich bin mir nicht sicher
- ( ) Keine Angabe

**C04**  Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen?

- ( ) Ja
- ( ) Nein
- ( ) Ich weiß es nicht
- ( ) Keine Angabe

**C05**  Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit?

- ( ) Ja
- ( ) Teilweise
- ( ) Nein
- ( ) Ich weiß nicht, ob es solche Regeln gibt
- ( ) Keine Angabe

**C06**  Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre?

- ( ) Ja
- ( ) Nein
- ( ) Kann ich noch nicht beurteilen
- ( ) Keine Angabe


---

*[Seite 2 von 5]*

### Anwendung und Verständnis

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**U01**  Ich kann eine generative KI bedienen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**U02**  Ich kann mir berufliche Aufgaben durch generative KI erleichtern.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**U03**  Ich kann generative KI gezielt für meine Arbeitsziele einsetzen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**U04**  Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**U05**  Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**U06**  Ich kann generativer KI verständlich mitteilen, was ich brauche.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**K01**  Ich kenne die zentralen Konzepte generativer KI.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**K02**  Ich kann erklären, was generative KI bedeutet.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**K03**  Ich kann Chancen und Grenzen generativer KI einschätzen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**K04**  Ich kann Vor- und Nachteile generativer KI beurteilen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**K05**  Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**K06**  Ich kann mir künftige Anwendungen generativer KI vorstellen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  


---

*[Seite 3 von 5]*

### Lernen und Prüfen

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**L01**  Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**L02**  Ich kann mich über Neuerungen bei generativer KI informieren.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**L03**  Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**G01**  Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**G02**  Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

**G03**  Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf.

`0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 ·    NB ·    KA`  

Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.


---

*[Seite 4 von 5]*

### Einstellung und geplante Nutzung

Wie sehr stimmen Sie den folgenden Aussagen zu? Gemeint ist die Nutzung für Ihre beruflichen Aufgaben in den kommenden drei Monaten. „Freigegeben“ bedeutet, dass Ihr Unternehmen die betreffende Nutzung erlaubt.

1 = stimme überhaupt nicht zu   ·   7 = stimme vollständig zu

NB = nicht beurteilbar   ·   KA = keine Angabe. Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein.

**A01**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft.

`1 · 2 · 3 · 4 · 5 · 6 · 7 ·    NB ·    KA`  

**A02**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend.

`1 · 2 · 3 · 4 · 5 · 6 · 7 ·    NB ·    KA`  

**A03**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig.

`1 · 2 · 3 · 4 · 5 · 6 · 7 ·    NB ·    KA`  

**A04**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm.

`1 · 2 · 3 · 4 · 5 · 6 · 7 ·    NB ·    KA`  

Für die folgenden drei Aussagen: Denken Sie an die Bedingungen, die Sie in den nächsten drei Monaten tatsächlich erwarten. Setzen Sie keinen gesicherten Zugang voraus, wenn dieser unklar ist. Fehlender Zugang bedeutet jedoch nicht automatisch, dass Sie nicht antworten können.

**I01**  Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

`1 · 2 · 3 · 4 · 5 · 6 · 7 ·    NB ·    KA`  

**I02**  Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

`1 · 2 · 3 · 4 · 5 · 6 · 7 ·    NB ·    KA`  

**I03**  Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen.

`1 · 2 · 3 · 4 · 5 · 6 · 7 ·    NB ·    KA`  


---

*[Seite 5 von 5]*

### Weiterbildung und Unterstützung

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
> [Textfeld, mehrzeilig]

---

Vielen Dank für Ihre Teilnahme. [PLATZHALTER_KONTAKT: Ansprechperson für Rückfragen zur Befragung]


### 3.2 Dokumentierte Änderungen außerhalb des Kerns (Erhebungsfassung ONLINE-S1-E1)

`context_changes_allowed` in der Bank: „Kontaktangaben und organisatorischer Erhebungshinweis außerhalb des Fragebogens; keine Änderung der Definition, Items, Skalen, Reihenfolge oder Zeitbezüge.“ `frozen_text_note`: Die organisatorische Pretest-Einleitung darf „nur als gesondert dokumentierte Erhebungsfassung ersetzt werden; Kerninstruktionen bleiben unverändert“.

| Nr. | Zeile in frozen_participant_text | Ursprünglicher Text | Neuer Text | Begründung | Art |
|---|---|---|---|---|---|
| E1 | 1 | „Fassung für den Verständlichkeitstest · GARI-DE-0.1 · 29. September 2026“ | „Onlinebefragung · GARI-DE-0.1 · Erhebungsfassung ONLINE-S1-E1“ | Keine Pretest-Kennzeichnung mehr; die Versionsangabe bleibt sichtbar. | organisatorisch |
| E2 | 2 | „… Im anschließenden Gespräch prüfen wir, ob die Fragen verständlich sind. …“ | Der Satz zum Gespräch wird ersetzt durch: Ergebnisse werden zusammengefasst für das Unternehmen oder für Gruppen ab [PLATZHALTER_MINDESTGRUPPE] Personen berichtet; sie dienen der Planung von Weiterbildung und betrieblichen Voraussetzungen. Erster Satz, Satz zur Leistungsbewertung und Zeitangabe bleiben wörtlich. | Eine Onlinebefragung hat kein Begleitgespräch. Der Masterprompt verlangt, Zweck und Ausgabeebene zu beschreiben. | organisatorisch, Platzhalter |
| E3 | 4 | „… den Test beenden … Beim begleiteten Test kennt die durchführende Person Sie; eine vollständige Anonymität wird deshalb nicht zugesagt.“ | „… die Befragung beenden …“ plus [PLATZHALTER_DATENSCHUTZ]. Bis zur Klärung wird keine Anonymität zugesagt. | Die Begründung aus dem Pretest passt online nicht. Ob online Anonymität besteht, ist unbekannt, also wird sie nicht behauptet. Die Regel zum Auslassen („Sie können einzelne Fragen auslassen“) bleibt wörtlich. | organisatorisch, Platzhalter |
| E4 | 5 | „Testkürzel: ____ Datum: ____“ | entfernt | Die Auswertung braucht keine Namen oder Kürzel. Die technische Respondenten-ID und den Zeitpunkt vergibt die Plattform. | organisatorisch |
| E5 | 113 | „Vielen Dank. Im Gespräch können Sie jetzt …“ | „Vielen Dank für Ihre Teilnahme.“ plus [PLATZHALTER_KONTAKT] | Kein Gespräch; nach der Bank sind Kontaktangaben zulässig. | Kontakt, Platzhalter |
| E6 | – | Word-Darstellung „Kreisen Sie … ein“ (Zeilen 21, 49, 68) | **unverändert gelassen** | Die Instruktionen gehören zum Kern. Die Formulierung passt zwar nicht zum Anklicken. Sie anzupassen wäre aber eine Änderung der Instruktion und bräuchte eine neue Fragebogenversion (siehe P3). | keine Änderung, offener Punkt |

**Kontrollierte Platzhalter:** [PLATZHALTER_MINDESTGRUPPE], [PLATZHALTER_DATENSCHUTZ] und [PLATZHALTER_KONTAKT] stehen ausschließlich in der organisatorischen Einleitung und im Abschluss. Im Kernregister der Bank ist kein Platzhalter für Itemtexte vorgesehen, deshalb steht keiner davon in Items, Definitionen oder Kerninstruktionen. Beim Befüllen dürfen keine erfundenen Angaben eingesetzt werden. Bis die Platzhalter befüllt sind, darf die Fassung nicht ins Feld.

**Keine Ergänzung von Unternehmensbeispielen:** Der Kern enthält keine Platzhalter für betriebliche Beispiele. Der Werkzeugname des freigegebenen Chat-Werkzeugs wird deshalb nicht in Items oder in die Definition eingesetzt. Ein Hinweis auf das Werkzeug ginge nur als gesondert dokumentierter organisatorischer Hinweis außerhalb des Fragebogens. Das würde allerdings Antworten zu Zugang (C04) und Regeln (C05) vorwegnehmen, deshalb empfehle ich es nicht.

### 3.3 Itemregister Teil A: Herkunft und Prüfstand

Der Prüfstand wurde aus der Bank übernommen. Bei MAILS-Items enthält die Bank absichtlich keinen Originalwortlaut, sondern verweist auf die Fundstelle („hier über Fundstelle referenziert“). Ich habe ihn auch nicht ergänzt.


| item_id | dim | Status | Quelle / Fundstelle | Originalwortlaut | Änderung | Wortlaut geprüft | Quellgrenze |
|---|---|---|---|---|---|---|---|
| C01 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| C02 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| C03 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| C04 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| C05 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| C06 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| U01 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 1, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | KI-Bezug auf generative KI eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| U02 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 2, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Erleichterung des Lebens auf berufliche Aufgaben eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| U03 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 3, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Zielbezug auf Arbeitsziele eingegrenzt; sinnvoll durch gezielt konkretisiert. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| U04 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 4, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Alltagsinteraktion auf Zusammenarbeit bei der Arbeit übertragen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| U05 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 5, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Gewinnbringende Zusammenarbeit über brauchbare Arbeitsergebnisse konkretisiert; Bedeutungsverschiebung im Pretest prüfen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| U06 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 6, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Gewinnbringende Kommunikation über verständliches Mitteilen konkretisiert; Ergebnisaspekt verengt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| K01 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 7, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Allgemeine KI auf generative KI eingegrenzt; Konzepte bleibt bewusst zur Verständlichkeitsprüfung erhalten. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| K02 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 8, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Kenntnis von Definitionen in selbst eingeschätzte Erklärfähigkeit übertragen; stärkere Anpassung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| K03 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 9, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| K04 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 10, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| K05 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 11, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Gegenstand eingegrenzt; Verwendungszwecke sprachlich vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| K06 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 12, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Gegenstand eingegrenzt; Satz verkürzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| L01 | L | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 26, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Gegenstand eingegrenzt; stets entfällt. Deutsche Itemnummer 26 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| L02 | L | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 27, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Gegenstand eingegrenzt; deutsche Itemnummer 27 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| L03 | L | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 28, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert. | Gegenstand eingegrenzt; sprachliche Verdichtung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ja | – |
| G01 | G | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| G02 | G | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| G03 | G | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| A01 | A | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | The use of PowerPilot would be … advantageous. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | ja | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| A02 | A | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | The use of PowerPilot would be … satisfactory. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | ja | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| A03 | A | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | The use of PowerPilot would be … important. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | ja | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| A04 | A | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 4; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | The use of PowerPilot would be … enjoyable. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | ja | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| I01 | I | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | I plan to use PowerPilot in the future. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | ja | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| I02 | I | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | I intend to use PowerPilot in the future. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | ja | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| I03 | I | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | I will definitely use PowerPilot in the future. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | ja | Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. |
| W01 | W | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| W02 | W | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |
| W03 | W | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenentwicklung ohne Originalitem. | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | nein (kein Original) | – |

**Zusammenfassung des Prüfstands:** 22 Items sind ADAPTIERT (15 nach MAILS, 7 nach PowerPilot), 12 sind NEU_ENTWICKELT (C01–C06, G01–G03, W01–W03). Kein Item ist ORIGINAL oder nur UEBERSETZT. Ausweitung von allgemeiner KI auf GenAI im Arbeitskontext, ergänzte NB/KA-Optionen, Übertragung von PowerPilot auf GenAI sowie Zeitraum und Kontext gelten durchgehend als inhaltliche Anpassung. Validierungsaussagen aus MAILS oder PowerPilot gelten deshalb nicht für GARI-DE-0.1. **POWERPILOT_2025: Der Wortlaut ist an der bereitgestellten Itemsammlung geprüft. Der direkte Vergleich mit dem OSF-Anhang bleibt offen.**

### 3.4 Itemregister Teil B: Befragungsformulierung, Skalen und Auswertung


| item_id | Deutsche Befragungsformulierung | Antwortformat und Anker | Originalskala | Rolle | Anzeige | Richtung | Fehlwertgründe | Teilbereich | Evidenz | Version |
|---|---|---|---|---|---|---|---|---|---|---|
| C01 | Wie sieht Ihre hauptsächliche Tätigkeit aus? | OFFICE = „Überwiegend Büro- oder Bildschirmarbeit“; OTHER_WORK = „Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst“; MIXED = „Etwa gleich große Anteile beider Bereiche“; zusätzlich KA; genau eine Antwort | – | FESTER_KERN | ALWAYS (alle Personen) | nominal, keine Richtung | KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| C02 | An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt? | D0 = „An keinem Tag“; D1_3 = „An 1 bis 3 Tagen“; D4_9 = „An 4 bis 9 Tagen“; D10_15 = „An 10 bis 15 Tagen“; D16_PLUS = „An 16 oder mehr Tagen“; UNKNOWN = „Kann ich nicht einschätzen“; zusätzlich KA; genau eine Antwort | – | FESTER_KERN | ALWAYS (alle Personen) | nominal, keine Richtung | KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| C03 | Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt? | YES = „Ja“; NO = „Nein“; UNKNOWN = „Ich bin mir nicht sicher“; zusätzlich KA; genau eine Antwort | – | FESTER_KERN | ALWAYS (alle Personen) | nominal, keine Richtung | KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| C04 | Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen? | YES = „Ja“; NO = „Nein“; UNKNOWN = „Ich weiß es nicht“; zusätzlich KA; genau eine Antwort | – | FESTER_KERN | ALWAYS (alle Personen) | nominal, keine Richtung | KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| C05 | Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit? | KNOWN = „Ja“; PARTLY = „Teilweise“; NOT_KNOWN = „Nein“; EXISTENCE_UNKNOWN = „Ich weiß nicht, ob es solche Regeln gibt“; zusätzlich KA; genau eine Antwort | – | FESTER_KERN | ALWAYS (alle Personen) | nominal, keine Richtung | KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| C06 | Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre? | YES = „Ja“; NO = „Nein“; UNKNOWN = „Kann ich noch nicht beurteilen“; zusätzlich KA; genau eine Antwort | – | FESTER_KERN | ALWAYS (alle Personen) | nominal, keine Richtung | KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U01 | Ich kann eine generative KI bedienen. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | U | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U02 | Ich kann mir berufliche Aufgaben durch generative KI erleichtern. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | U | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U03 | Ich kann generative KI gezielt für meine Arbeitsziele einsetzen. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | U | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U04 | Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | U | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U05 | Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | U | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| U06 | Ich kann generativer KI verständlich mitteilen, was ich brauche. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | U | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K01 | Ich kenne die zentralen Konzepte generativer KI. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | K | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K02 | Ich kann erklären, was generative KI bedeutet. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | K | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K03 | Ich kann Chancen und Grenzen generativer KI einschätzen. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | K | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K04 | Ich kann Vor- und Nachteile generativer KI beurteilen. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | K | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K05 | Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | K | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| K06 | Ich kann mir künftige Anwendungen generativer KI vorstellen. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | K | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| L01 | Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | L | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| L02 | Ich kann mich über Neuerungen bei generativer KI informieren. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | L | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| L03 | Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | L | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| G01 | Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | – | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| G02 | Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | – | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| G03 | Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf. | ABILITY_0_10: ganze Zahlen 0–10; 0 = „gar nicht oder kaum ausgeprägt“, 10 = „sehr gut oder (nahezu) perfekt ausgeprägt“; keine Zwischenanker; zusätzlich NB, KA | – | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| A01 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft. | AGREEMENT_1_7: ganze Zahlen 1–7; 1 = „stimme überhaupt nicht zu“, 7 = „stimme vollständig zu“; keine Zwischenanker; zusätzlich NB, KA | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | A | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| A02 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend. | AGREEMENT_1_7: ganze Zahlen 1–7; 1 = „stimme überhaupt nicht zu“, 7 = „stimme vollständig zu“; keine Zwischenanker; zusätzlich NB, KA | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | A | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| A03 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig. | AGREEMENT_1_7: ganze Zahlen 1–7; 1 = „stimme überhaupt nicht zu“, 7 = „stimme vollständig zu“; keine Zwischenanker; zusätzlich NB, KA | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | A | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| A04 | Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm. | AGREEMENT_1_7: ganze Zahlen 1–7; 1 = „stimme überhaupt nicht zu“, 7 = „stimme vollständig zu“; keine Zwischenanker; zusätzlich NB, KA | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | A | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| I01 | Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | AGREEMENT_1_7: ganze Zahlen 1–7; 1 = „stimme überhaupt nicht zu“, 7 = „stimme vollständig zu“; keine Zwischenanker; zusätzlich NB, KA | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | I | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| I02 | Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen. | AGREEMENT_1_7: ganze Zahlen 1–7; 1 = „stimme überhaupt nicht zu“, 7 = „stimme vollständig zu“; keine Zwischenanker; zusätzlich NB, KA | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | I | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| I03 | Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen. | AGREEMENT_1_7: ganze Zahlen 1–7; 1 = „stimme überhaupt nicht zu“, 7 = „stimme vollständig zu“; keine Zwischenanker; zusätzlich NB, KA | Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | FESTER_KERN | ALWAYS (alle Personen) | nicht umgepolt; höher = mehr Selbsteinschätzung/Zustimmung | NICHT_BEURTEILBAR, KEINE_ANGABE | I | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. | GARI-DE-0.1 |
| W01 | Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen. | BASICS = „Grundlagen generativer KI“; USE_CASES = „Passende Einsatzmöglichkeiten für meine Aufgaben“; PROMPTING = „Klare Eingaben formulieren und Ergebnisse verbessern“; VERIFY = „Antworten und Quellen überprüfen“; DATA_RULES = „Betriebliche Regeln und zulässige Dateneingaben“; KEEP_CURRENT = „Bei neuen Entwicklungen auf dem Laufenden bleiben“; OTHER = „Anderes Thema“; NONE = „Derzeit kein Weiterbildungswunsch“; UNKNOWN = „Ich kann meinen Bedarf noch nicht einschätzen“; zusätzlich KA; höchstens 3 Antworten; exklusiv: NONE, UNKNOWN | – | FESTER_KERN | ALWAYS (alle Personen) | nominal, keine Richtung | KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| W02 | Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen. | ACCESS = „Kein Zugang zu einem freigegebenen Werkzeug“; RULES = „Unklare betriebliche Regeln“; TIME = „Zu wenig Zeit zum Ausprobieren oder Lernen“; KNOWLEDGE = „Mir fehlt Wissen über die Nutzung“; TASK_FIT = „Ich erkenne keinen passenden Einsatz für meine Aufgaben“; RELIABILITY = „Unsicherheit über die Verlässlichkeit der Ergebnisse“; OTHER = „Etwas anderes“; NONE = „Derzeit nichts“; UNKNOWN = „Kann ich noch nicht einschätzen“; zusätzlich KA; höchstens 3 Antworten; exklusiv: NONE, UNKNOWN | – | FESTER_KERN | ALWAYS (alle Personen) | nominal, keine Richtung | KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |
| W03 | Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen. | Freitext; zusätzlich KA | – | FESTER_KERN | ALWAYS (alle Personen) | nominal, keine Richtung | KEINE_ANGABE | kein Teilbereich, Einzelitem | Noch nicht empirisch geprüft. | GARI-DE-0.1 |

### 3.5 Codebuch GARI-DE-0.1 für die Erhebungsfassung ONLINE-S1-E1

Die Rechenregeln gelten unverändert aus `instrument/Codebuch.md`. Hier ist nur zusammengefasst, was für die Onlineumsetzung festgelegt sein muss.

**Datenformat:** JSON, UTF-8. Pflichtfelder auf Dateiebene: `data_kind` (genau PRETEST, SURVEY oder SYNTHETIC_DEMO) und `questionnaire_version` = „GARI-DE-0.1“. Auf Personenebene ist `questionnaire_version` ebenfalls Pflicht. Je Person müssen alle 34 Item-IDs vorkommen, jeweils mit `value` und `missing_reason`. Jede Respondenten-ID darf nur einmal vorkommen.

**Umgang mit der Umsetzungskennung:** Das bestehende Codebuch und die Rechenroutine verlangen `questionnaire_version` = GARI-DE-0.1. Laut Codebuch ändern geänderte Einleitungstexte den Kern nicht, sie brauchen aber eine dokumentierte Erhebungsfassung. Ich schlage deshalb vor, die Umsetzungskennung GARI-DE-0.1/ONLINE-S1-E1 in einem **separaten Feld** `implementation_id` und im Manifest zu führen. **Voraussetzung:** Der Oberflächenabgleich (Abschnitt 4.2) ist BESTANDEN. Ob die Rechenroutine ein zusätzliches Feld akzeptiert, konnte ich nicht prüfen, weil `score.py` nicht Teil der Eingaben ist. Erlaubt sie keine Zusatzfelder, gehört die Kennung ausschließlich ins Manifest. Weicht die Oberfläche im Kern ab, zum Beispiel durch fehlende NB/KA, geänderte Instruktionen, Schieberegler oder Pflichtfelder, ist die Fassung **nicht** GARI-DE-0.1. Dann ist eine eigene Versionskennung nötig, und die Daten dürfen nicht durch bloßes Umbenennen der Version in die Rechenroutine gelangen.

**Wertebereiche und Labels:**

| Items | Gültige `value` | Labels | Erlaubte `missing_reason` |
|---|---|---|---|
| C01 | OFFICE, OTHER_WORK, MIXED | siehe 3.4 | KEINE_ANGABE |
| C02 | D0, D1_3, D4_9, D10_15, D16_PLUS, UNKNOWN | siehe 3.4 | KEINE_ANGABE |
| C03, C04, C06 | YES, NO, UNKNOWN | siehe 3.4 | KEINE_ANGABE |
| C05 | KNOWN, PARTLY, NOT_KNOWN, EXISTENCE_UNKNOWN | siehe 3.4 | KEINE_ANGABE |
| U01–U06, K01–K06, L01–L03, G01–G03 | ganze Zahlen 0–10 (0 ist ein gültiger Wert) | 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt | NICHT_BEURTEILBAR, KEINE_ANGABE |
| A01–A04, I01–I03 | ganze Zahlen 1–7 | 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu | NICHT_BEURTEILBAR, KEINE_ANGABE |
| W01 | Liste mit 1–3 Codes aus BASICS, USE_CASES, PROMPTING, VERIFY, DATA_RULES, KEEP_CURRENT, OTHER, NONE, UNKNOWN; NONE und UNKNOWN nur allein; leere Liste unzulässig | siehe 3.4 | KEINE_ANGABE |
| W02 | Liste mit 1–3 Codes aus ACCESS, RULES, TIME, KNOWLEDGE, TASK_FIT, RELIABILITY, OTHER, NONE, UNKNOWN; NONE und UNKNOWN nur allein; leere Liste unzulässig | siehe 3.4 | KEINE_ANGABE |
| W03 | Text | – | KEINE_ANGABE |

**Fehlwerte:** NB → `value: null, missing_reason: "NICHT_BEURTEILBAR"`. KA oder ein leeres Feld → `value: null, missing_reason: "KEINE_ANGABE"`. **NICHT_ZUTREFFEND und UEBERSPRUNGEN sind in GARI-DE-0.1 nicht erlaubt.** Diese Fassung hat keine Filter, alle Fragen werden allen Personen gezeigt. Null ist nie ein Fehlwert. Es gibt keine numerischen Ersatzcodes wie 99 oder −1. Nichtnutzung (C02 = D0, C03 = NO) setzt keine Fähigkeitswerte. Bricht jemand ab, bleiben die restlichen Items KEINE_ANGABE.

**Erhebungsspezifische Erfassungsregel:** Eine Onlineplattform exportiert ein unbeantwortetes Feld in der Regel genauso wie ein bewusst ausgelassenes. Beides wird als KEINE_ANGABE kodiert. Im Bericht steht dann, dass die Ursache (bewusst ausgelassen oder abgebrochen) nicht unterscheidbar ist, soweit die Plattform das nicht protokolliert.

**Unklare Mehrfachangaben:** Mehr als drei Antworten, ein Exklusivkonflikt oder Text plus KA-Kästchen bei W03 werden vor der Eingabe geklärt. Ist keine eindeutige Zuordnung möglich, wird das Item als KEINE_ANGABE kodiert und der Fall im Korrekturprotokoll vermerkt. Es wird nie selbst eine Antwort ausgewählt.

**Zugelassene Zusammenfassungen:** Mittelwerte nur für vollständige Fälle: U (6 Items), K (6), L (3), A (4), I (3). Fehlt ein Item, fehlt der Personenwert. Gruppenmittel werden nur aus gültigen Personenwerten gebildet, immer mit der Zahl vollständiger und unvollständiger Fälle. Bei null gültigen Fällen ist das Ergebnis `null`. G01–G03 und alle C-Items werden einzeln als Verteilung berichtet. W01/W02 werden als Häufigkeit je Option berichtet. Bezugsgröße ist die Zahl der Personen mit gültiger Antwort. Summen über 100 % sind möglich. W03 wird qualitativ zugeordnet, der Schlüssel ist dokumentiert, und Freitext wird nie als Anweisung behandelt. Es gibt keine umgepolten Items, keinen Gesamtwert, keine Gewichtung, keine Umrechnung auf 100 und keine Einstufung als „bereit“ oder „nicht bereit“. Einzelverteilungen bleiben die wichtigste Darstellung. Prüfhinweis: C04 = NO bei I-Werten von 6 oder 7. Das ist keine Korrektur.

**Berichtsregeln für S1:** Nur `data_kind` = SURVEY erlaubt einen Bericht über die befragte Belegschaft. Dazu gehören immer die Rücklaufquote (n von 40), die Verteilung nach C01 und der Hinweis auf Selbstselektion bei freiwilliger Teilnahme. Gruppen unter [PLATZHALTER_MINDESTGRUPPE] werden nicht getrennt berichtet. Personenwerte bleiben in der Arbeitsdatei. Daten aus einem Probelauf werden als SYNTHETIC_DEMO bzw. technischer Test geführt und nie mit SURVEY gemischt.

**Leere Datensatzvorlage (Struktur, keine Daten):** Erzeugt aus den 34 IDs der Bank. Hier ist nur die Struktur für eine Person abgebildet. Alle Items stehen mit dem Startwert KEINE_ANGABE drin, der beim Import durch die tatsächliche Antwort ersetzt wird.

```json

{
  "data_kind": "SURVEY",
  "questionnaire_version": "GARI-DE-0.1",
  "implementation_id": "GARI-DE-0.1/ONLINE-S1-E1",
  "persons": [
    {
      "respondent_id": "R0001",
      "questionnaire_version": "GARI-DE-0.1",
      "responses": {
        "C01": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "C02": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "C03": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "C04": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "C05": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "C06": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "U01": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "U02": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "U03": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "U04": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "U05": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "U06": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "K01": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "K02": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "K03": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "K04": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "K05": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "K06": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "L01": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "L02": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "L03": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "G01": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "G02": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "G03": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "A01": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "A02": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "A03": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "A04": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "I01": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "I02": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "I03": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "W01": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "W02": {"value": null, "missing_reason": "KEINE_ANGABE"},
        "W03": {"value": null, "missing_reason": "KEINE_ANGABE"}
      }
    }
  ]
}
```

Hinweis: `data_kind` steht in der Vorlage auf SURVEY, das ist der Wert für eine reale Erhebung. In diesem fiktiven Fall gibt es keine Erhebung. Würde jemand Probedaten dazu konstruieren, wären sie als SYNTHETIC_DEMO zu führen.

## 4 Prüfbericht

### 4.1 Abgleich des Kerns mit der eingefrorenen Bank (ausgeführt)

Ein Skript (Python 3.13, Exitstatus 0) hat die Befragungsfassung aus 3.1 direkt aus `frozen_participant_text` erzeugt und gegen `items` und `scales` der Bank geprüft. Ergebnis:

| Prüfpunkt | Ergebnis |
|---|---|
| Alle 34 IDs je genau einmal als Zeile „ID + Itemtext“ vorhanden und wortgleich mit `items[].text` | 34 von 34, keine Abweichung |
| Reihenfolge der Items wie in der Bank | identisch |
| Antwortzeilen der Zahlen-Items: 0–10 bzw. 1–7 plus NB und KA | 25 von 25 identisch |
| Optionen der Einzelwahl-Items (Labels und Reihenfolge) plus „Keine Angabe“ | 6 von 6 identisch |
| Optionen W01/W02 plus „Keine Angabe“ | identisch |
| W03 mit KA-Option | vorhanden |
| Definition generativer KI wortgleich mit `definition` | identisch |
| Alle 109 nicht geänderten Zeilen des eingefrorenen Texts in unveränderter Reihenfolge | identisch |
| Geänderte Zeilen | 4 ersetzt (Zeilen 1, 2, 4, 113), 1 entfernt (Zeile 5). Alle organisatorisch, siehe 3.2 |
| Unbeabsichtigte Abweichungen | keine gefunden |

Zusätzlich anhand der Bank geprüft: Alle Items haben `display_if` = ALWAYS, `role` = FESTER_KERN und `reverse_coded` = false. Als Fehlwertgründe kommen nur KEINE_ANGABE oder NICHT_BEURTEILBAR/KEINE_ANGABE vor. Die Domänen U, K, L, A und I stimmen mit dem Codebuch überein. G, C und W sind als `not_a_scale` geführt.

**Grenze dieses Abgleichs:** Er betrifft nur die Textfassung in diesem Dokument. Die Word-Fassung und eine tatsächliche Onlineoberfläche lagen in diesem Lauf nicht vor und wurden nicht verglichen.

### 4.2 Abgleich der tatsächlich verwendeten Oberfläche

**Freigabestatus: OFFEN.** Es gibt noch kein Onlineformular. Ohne dokumentierten Abgleich wird BESTANDEN nicht vergeben. Meine Beschreibung unten ist ein Umsetzungsvorschlag und kein Nachweis, dass ein Formular korrekt umgesetzt wurde. Auch eine Selbstauskunft des Systems, das später das Formular erzeugt, ist kein solcher Nachweis.

**Umsetzungsvorgabe je Item** (von der Bank abgeleitet; keine Frage ist Pflichtfeld, weil die Einleitung das Auslassen ausdrücklich erlaubt):


| Pos. | item_id | Seite | Fragetyp in der Oberfläche | Auswählbare Optionen (Reihenfolge) | Pflichtfeld | Regel | Exportwert → Codebuch |
|---|---|---|---|---|---|---|---|
| 1 | C01 | 1 | Einzelwahl (Optionsfelder) | Überwiegend Büro- oder Bildschirmarbeit · Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst · Etwa gleich große Anteile beider Bereiche · Keine Angabe | nein | genau eine Auswahl | Label → Code (OFFICE, OTHER_WORK, MIXED); Keine Angabe oder leer → null/KEINE_ANGABE |
| 2 | C02 | 1 | Einzelwahl (Optionsfelder) | An keinem Tag · An 1 bis 3 Tagen · An 4 bis 9 Tagen · An 10 bis 15 Tagen · An 16 oder mehr Tagen · Kann ich nicht einschätzen · Keine Angabe | nein | genau eine Auswahl | Label → Code (D0, D1_3, D4_9, D10_15, D16_PLUS, UNKNOWN); Keine Angabe oder leer → null/KEINE_ANGABE |
| 3 | C03 | 1 | Einzelwahl (Optionsfelder) | Ja · Nein · Ich bin mir nicht sicher · Keine Angabe | nein | genau eine Auswahl | Label → Code (YES, NO, UNKNOWN); Keine Angabe oder leer → null/KEINE_ANGABE |
| 4 | C04 | 1 | Einzelwahl (Optionsfelder) | Ja · Nein · Ich weiß es nicht · Keine Angabe | nein | genau eine Auswahl | Label → Code (YES, NO, UNKNOWN); Keine Angabe oder leer → null/KEINE_ANGABE |
| 5 | C05 | 1 | Einzelwahl (Optionsfelder) | Ja · Teilweise · Nein · Ich weiß nicht, ob es solche Regeln gibt · Keine Angabe | nein | genau eine Auswahl | Label → Code (KNOWN, PARTLY, NOT_KNOWN, EXISTENCE_UNKNOWN); Keine Angabe oder leer → null/KEINE_ANGABE |
| 6 | C06 | 1 | Einzelwahl (Optionsfelder) | Ja · Nein · Kann ich noch nicht beurteilen · Keine Angabe | nein | genau eine Auswahl | Label → Code (YES, NO, UNKNOWN); Keine Angabe oder leer → null/KEINE_ANGABE |
| 7 | U01 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 8 | U02 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 9 | U03 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 10 | U04 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 11 | U05 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 12 | U06 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 13 | K01 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 14 | K02 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 15 | K03 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 16 | K04 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 17 | K05 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 18 | K06 | 2 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 19 | L01 | 3 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 20 | L02 | 3 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 21 | L03 | 3 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 22 | G01 | 3 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 23 | G02 | 3 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 24 | G03 | 3 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 25 | A01 | 4 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 26 | A02 | 4 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 27 | A03 | 4 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 28 | A04 | 4 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 29 | I01 | 4 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 30 | I02 | 4 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 31 | I03 | 4 | Einzelwahl mit 13 bzw. 9 Optionen (Zahlen plus NB, KA), waagrecht; kein Schieberegler, keine lineare Skala ohne NB/KA | 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA | nein | genau eine Auswahl | Zahl → value (Ganzzahl); NB → null/NICHT_BEURTEILBAR; KA oder leer → null/KEINE_ANGABE |
| 32 | W01 | 5 | Mehrfachwahl (Kästchen) | Grundlagen generativer KI · Passende Einsatzmöglichkeiten für meine Aufgaben · Klare Eingaben formulieren und Ergebnisse verbessern · Antworten und Quellen überprüfen · Betriebliche Regeln und zulässige Dateneingaben · Bei neuen Entwicklungen auf dem Laufenden bleiben · Anderes Thema · Derzeit kein Weiterbildungswunsch · Ich kann meinen Bedarf noch nicht einschätzen · Keine Angabe | nein | höchstens 3; NONE, UNKNOWN und Keine Angabe nur allein; Höchstzahl technisch blockierend umsetzen und Exklusivität im Datencheck prüfen | Labels → Liste der Codes; nur Keine Angabe oder leer → null/KEINE_ANGABE; >3 oder Exklusivkonflikt → KEINE_ANGABE + Korrekturprotokoll |
| 33 | W02 | 5 | Mehrfachwahl (Kästchen) | Kein Zugang zu einem freigegebenen Werkzeug · Unklare betriebliche Regeln · Zu wenig Zeit zum Ausprobieren oder Lernen · Mir fehlt Wissen über die Nutzung · Ich erkenne keinen passenden Einsatz für meine Aufgaben · Unsicherheit über die Verlässlichkeit der Ergebnisse · Etwas anderes · Derzeit nichts · Kann ich noch nicht einschätzen · Keine Angabe | nein | höchstens 3; NONE, UNKNOWN und Keine Angabe nur allein; Höchstzahl technisch blockierend umsetzen und Exklusivität im Datencheck prüfen | Labels → Liste der Codes; nur Keine Angabe oder leer → null/KEINE_ANGABE; >3 oder Exklusivkonflikt → KEINE_ANGABE + Korrekturprotokoll |
| 34 | W03 | 5 | Absatztext plus separates Kästchen | Textfeld (lang) · Kästchen „Keine Angabe“ | nein | keine Längenbegrenzung festgelegt | Text → value (String); Kästchen KA oder leer → null/KEINE_ANGABE; Text und KA zugleich → Korrekturprotokoll |

**Prüfliste für den späteren Oberflächenabgleich.** Jeden Punkt einzeln prüfen und den geprüften Schritt protokollieren. Grundlage ist eine ungesendete Testsitzung oder ein klar gekennzeichneter technischer Probelauf, getrennt von echten Antworten.

| Nr. | Prüfpunkt | Sollwert | Status |
|---|---|---|---|
| O1 | Alle 34 IDs und Wortlaute, zeichengenau gegen 3.1 | identisch | OFFEN |
| O2 | Reihenfolge der Items und Seiten | wie 3.1 / 4.2 | OFFEN |
| O3 | Einleitung, Definition, alle Instruktionen einschließlich Skalenwechsel-Hinweis vor Seite 4 | wörtlich wie 3.1 | OFFEN |
| O4 | Endanker 0/10 und 1/7 sichtbar, keine zusätzlichen Zwischenanker | wie Bank | OFFEN |
| O5 | NB und KA bei allen 25 Zahlen-Items **auswählbar** (ein Hinweistext reicht nicht) | auswählbar | OFFEN |
| O6 | „Keine Angabe“ bei C01–C06, W01–W03 auswählbar | auswählbar | OFFEN |
| O7 | Kein Pflichtfeld | alle optional | OFFEN |
| O8 | W01/W02: eine vierte Auswahl wird **beim Fortsetzen tatsächlich blockiert** (nicht nur als Hinweis angezeigt) | blockiert | OFFEN |
| O9 | W01/W02: Exklusivität von NONE, UNKNOWN und KA technisch erzwungen oder im Datencheck abgefangen; Weg dokumentieren | dokumentiert | OFFEN |
| O10 | Exportierter Datentyp: Zahlen als Ganzzahlen, NB/KA als eigene Textwerte, Mehrfachwahl trennbar | eindeutig zuordenbar | OFFEN |
| O11 | Endgültige Speicherung einer Testübermittlung (ein Seitenwechsel allein belegt das nicht) | ungeprüft, bis eine Übermittlung getestet ist | OFFEN |
| O12 | Technisch erfasste personenbezogene Daten (E-Mail, Anmeldung) entsprechen der Einleitung | übereinstimmend | OFFEN |
| O13 | Platzhalter befüllt, und zwar ohne erfundene Angaben | befüllt | OFFEN |

**Begleitmanifest (Vorlage, für diesen Lauf ausgefüllt):**

| Feld | Eintrag |
|---|---|
| Referenzbank | `instrument/Itembank_GARI_DE_0.1.json`, Version GARI-DE-0.1, Stand 2026-09-29 |
| Codebuch | `instrument/Codebuch.md`, GARI-DE-0.1, Stand 29.09.2026 / 17.10.2026 |
| Fragebogen-/Umsetzungskennung | GARI-DE-0.1/ONLINE-S1-E1 (Entwurf) |
| Erhebungsrunde | S1, fiktive Demonstration; keine Feldphase |
| Plattform | NICHT_DOKUMENTIERT (unbekannt) |
| Datum des Oberflächenabgleichs | keins; Abgleich nicht durchgeführt |
| Tatsächlich geprüfte Stellen | nur der Textabgleich nach 4.1 (Textfassung gegen Bank) |
| Offene Abweichungen | keine im Text; die Oberfläche ist insgesamt ungeprüft (O1–O13) |
| Erstellung: Prompt | Masterprompt 0.5 (17.10.2026), Betriebsart ANWENDEN |
| Erstellung: Eingabedateien | briefing.json, Itembank_GARI_DE_0.1.json, Codebuch.md, Quellen_APA.md |
| Manuelle Änderungen | E1–E5 nach 3.2 |
| System/Modell | Claude, angezeigt „Opus 5.5“ (`claude-opus-5-5`); weitere Parameter NICHT_VERFUEGBAR |
| Freigabestatus | OFFEN |

**Erzeugungsprompt für eine spätere KI-gestützte Formularübertragung** (vollständige Vorgabe, kein Rückgriff auf ältere Fassungen):

> Lege ein Onlineformular exakt nach der beigefügten Befragungsfassung GARI-DE-0.1/ONLINE-S1-E1 (Abschnitt 3.1) und der Umsetzungstabelle (Abschnitt 4.2) an. Übernimm alle Texte zeichengenau. Ändere keine Wortlaute, Reihenfolgen, Anker oder Instruktionen. Setze keine Frage auf Pflicht. Bilde bei den 25 Zahlen-Items 0–10 bzw. 1–7 plus NB und KA als auswählbare Einzelwahl ab. Verwende keine Schieberegler und keine lineare Skala ohne NB/KA. Ergänze überall die Option „Keine Angabe“, wo sie in 3.1 steht. Begrenze W01 und W02 technisch auf höchstens drei Auswahlen. Fehlt eine Referenzdatei oder lässt sich ein Element nicht abbilden, melde das und erfinde keinen Ersatz. Fehlen die Platzhalterinhalte, lass die Platzhalter sichtbar stehen.

Dieser Prompt ist ein Vorschlag. Erst der Abgleich O1–O13 zeigt, ob die Umsetzung gelungen ist.

### 4.3 Offene Probleme und Risiken

| ID | Problem | Folge | Vorschlag |
|---|---|---|---|
| P1 | Der Abgleich der Oberfläche fehlt | Keine Freigabe, keine reguläre Auswertung unter GARI-DE-0.1 | Formular bauen, O1–O13 prüfen, Manifest ergänzen |
| P2 | Datenschutz, Anonymität und Mindestgruppe sind unbekannt | Die Einleitung bleibt unvollständig. Bei 40 Beschäftigten droht Re-Identifikation in Teilgruppen | Rückfrage 1 klären. Bis dahin keine Anonymitätszusage und keine Teilgruppen |
| P3 | Die Kerninstruktion „Kreisen Sie … ein“ ist für ein Onlineformular nur bedingt passend | Möglicherweise kleine Irritation | Im Kern **nicht** ändern. Eine Anpassung, etwa zu „Wählen Sie …“, wäre eine Instruktionsänderung und bräuchte eine neue Fragebogenversion samt angepasstem Codebuch. Die Entscheidung bleibt der Projektleitung überlassen |
| P4 | Die C01-Kategorien passen nicht 1:1 zu den Briefingbereichen Verwaltung, Kundenkontakt und operative Tätigkeit | Keine Auswertung nach Briefingbereichen möglich | Siehe Rückfrage 2. Eine Zusatzfrage nur als dokumentierte Ergänzung außerhalb des Kerns mit eigener Kennung |
| P5 | Der Zugang ist laut Briefing nur für Büroarbeitsplätze freigegeben | A/I-Werte von Personen ohne Zugang hängen von Erwartungen ab. C04 = NO bei I ≥ 6 wird nur als Prüfhinweis markiert | Zusammen mit C01/C04 interpretieren; nicht als fehlende Readiness werten |
| P6 | Bearbeitungszeit nur geschätzt (10–15 Min., „noch nicht gemessen“) | Die Zeitangabe in der Einleitung ist unbelegt | Ein Absendezeitstempel ergibt keine Dauer. Messen nur bei protokollierter Start- und Endzeit |
| P7 | Die Rechte an der öffentlichen Nachnutzung veränderter MAILS- und PowerPilot-Items sind ungeklärt | Betrifft Veröffentlichung, nicht die interne Erhebung | Vor einer Veröffentlichung klären |
| P8 | `score.py` liegt diesem Lauf nicht vor | Ob die Routine `implementation_id` akzeptiert, ist ungeprüft | Mit der Routine testen, bevor Daten anfallen |
| P9 | Pretestbefunde früherer Runden (R1–R3) lagen nicht vor | Bekannte Verständnisprobleme konnten nicht berücksichtigt werden. Der Kern bleibt laut Auftrag trotzdem unverändert | Abschlussdokumentation `pretest/Abschluss_Evaluation_R3.md` vor dem Feldeinsatz sichten |

Mehrere Prüfperspektiven (Quellen, Fragebogen, Codebuch) habe ich nacheinander im selben Modell eingenommen. Das ist eine Selbstprüfung und kein unabhängiges Gutachten.

## 5 Auswertungsbericht

**NICHT_BERECHNET.** Es liegen keine Antwortdaten vor, weder reale noch synthetische. Es werden keine Verteilungen, Mittelwerte oder Fallzahlen berichtet. Ein synthetisches Rechenergebnis aus dem Projekt wäre ohnehin kein Ergebnis dieses Betriebs.

Die Rechenanleitung für später, unverändert aus dem Codebuch: Daten im Format 3.5 mit `data_kind` = SURVEY aufbereiten. Den Datencheck ausführen (IDs, Duplikate, Wertebereiche, Version, Fehlwertgründe, Mehrfachwahl-Regeln). Danach im Projektordner `python auswertung/score.py <daten>.json ergebnis.json` ausführen, den Exitstatus prüfen und ausschließlich die erzeugte Ausgabe berichten. Je Item gehören in den Bericht: gültiges n, Fehlwerte nach Grund (NB und KA getrennt) und die Verteilung. Für U, K, L, A und I zusätzlich der Mittelwert vollständiger Fälle mit der Zahl vollständiger und unvollständiger Fälle.

## 6 Maßnahmenmatrix (Planungslogik ohne Befunde)

Ohne Daten gibt es keine Befunde und deshalb noch keine Maßnahmenempfehlung. Die Matrix legt **vor der Erhebung** fest, wie Befunde später zu Maßnahmen führen. Sie stammt aus dem Codebuch und ist eine eigene, prüfbare Planungslogik ohne Grenzwerte. Die Befund-IDs sind Platzhalter für die spätere Auswertung.

| Befund-ID (später) | Items | Interpretationsregel | Einordnung | Mögliche Maßnahme / Ziel | Unsicherheit | Erfolgskontrolle (Vorschlag) |
|---|---|---|---|---|---|---|
| B-ZUGANG | C04, W02 = ACCESS, C01 | Anzahl C04 = NO/UNKNOWN, aufgeschlüsselt nach C01 | organisatorisch | Zuerst den Zugang klären, auch für Nicht-Büroarbeitsplätze. Keine Kompetenzlücke behaupten | Wahrgenommener und tatsächlicher Zugang können abweichen | Zugang dokumentiert; C04 in der Folgeerhebung |
| B-REGELN | C05 = NOT_KNOWN/EXISTENCE_UNKNOWN, W01 = DATA_RULES, W02 = RULES, G03 | Anzahlen je Kategorie | Orientierung / Organisation | Regeln verständlich bereitstellen, Zuständigkeit benennen, klären, ob es Regeln überhaupt gibt | Es kann auch sein, dass gar keine Regeln existieren | Regeln veröffentlicht; C05 in der Folgeerhebung |
| B-AUFGABE | C06 = NO/UNKNOWN, W02 = TASK_FIT, W03 | Anzahlen; W03 qualitativ | unklare Aufgabenpassung | Anwendungsfälle je Tätigkeitsbereich prüfen. Nutzung kann sachlich unnötig sein | Eine begründete Ablehnung ist kein Defizit | dokumentierte Anwendungsfälle |
| B-GRUNDLAGEN | W01 = BASICS/UNKNOWN, W02 = KNOWLEDGE, U, K | Lernwunsch zusammen mit Verteilungen von U/K, ohne Schwelle | geäußerter Wunsch bzw. möglicher Lernbedarf | Einführung anbieten, freiwillig, mit Bezug zu Aufgaben | Selbsteinschätzung ist kein Leistungsnachweis | Teilnahme; Lernziele an Übungsaufgabe prüfen |
| B-PROMPTING | W01 = PROMPTING, U06, U05 | wie oben | Lernwunsch | Übung zu Eingaben und Überarbeitung. Setzt Zugang voraus (B-ZUGANG) | wie oben | praktische Aufgabe vor/nach |
| B-PRUEFEN | W01 = VERIFY, W02 = RELIABILITY, G01, G02 | Anzahlen; G01/G02 als Einzelverteilungen | Lernwunsch / wahrgenommene Unsicherheit | Ergebnis- und Quellenprüfung an Arbeitsbeispielen | G-Items sind nicht empirisch geprüft | Prüfaufgabe mit realistischem Beispiel |
| B-ZEIT | W02 = TIME | Anzahl | Rahmenbedingung | Lernzeit und Arbeitsorganisation prüfen | – | vereinbarte Lernzeit |
| B-NB | NB-Anteile je Fähigkeitsitem | tatsächliche Anzahl/Bezugsgröße nennen, kein Grenzwert | unklare Einschätzbarkeit | Zuerst Frageverständnis und Erfahrungsgrundlage prüfen; nicht als niedrige Kompetenz zählen | Online kann man NB nur auswerten, wenn NB auswählbar war (O5) | – |
| B-VERTIEFUNG | hohe Selbsteinschätzungen in U/K/L plus passender W01-Wunsch | nur Kombination, als Hypothese | möglicher vertiefender Lernbedarf | Vertiefungsangebot | kein objektiver Kompetenznachweis | praktische Aufgabe |
| B-OFFEN | Muster ohne Erklärung, z. B. hohe A und niedrige I trotz Zugang | als offene Frage festhalten | offen | Gezielte, neutrale Nachfrage, etwa in einer Gruppenrunde | Die Daten erklären das Muster nicht | – |

Wie priorisiert wird, entscheidet die Projektleitung. Kriterien sind geäußerte Wünsche, Aufgabenrelevanz und Umsetzbarkeit, ohne versteckte Gewichtung. Für keine Maßnahme ist eine Wirksamkeit nachgewiesen.

## 7 Änderungsprotokoll und nächste Eingaben

**Änderungsprotokoll dieses Laufs**

| Datum | Objekt | Änderung | Version |
|---|---|---|---|
| 18.10.2026 | Organisatorische Einleitung und Abschluss | E1–E5 (3.2), 3 Platzhalter | GARI-DE-0.1/ONLINE-S1-E1 |
| 18.10.2026 | Kern (Items, Definition, Instruktionen, Skalen, Reihenfolge) | keine | GARI-DE-0.1 |
| 18.10.2026 | Codebuch | keine Regeländerung. Vorschlag: zusätzliches Feld `implementation_id` (ungeprüft gegen `score.py`) | GARI-DE-0.1 |

**Nächste konkret nötige Eingaben**

1. Antworten auf die Rückfragen 1–3 (Datenschutz und Mindestgruppe, Bereichsauswertung, Plattform und Kontakt).
2. Das umgesetzte Onlineformular bzw. ein Export einer ungesendeten Testsitzung für den Oberflächenabgleich O1–O13.
3. `auswertung/score.py` für einen Test des Datenformats mit `implementation_id`.
4. Für die spätere Auswertung: echte Antwortdaten (SURVEY) mit Manifest. Im fiktiven Fall S1 fallen keine an.

## Literatur (APA, laut Projektquellenliste)

Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. University of Massachusetts Amherst. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, Article 149. https://doi.org/10.3389/fpubh.2018.00149

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), Article e39686. https://doi.org/10.1016/j.heliyon.2024.e39686

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114

Die übrigen Nachweise (Venable et al., 2016; National Center for Health Statistics, 2024; Paetow et al., 2026; Do Khac et al., 2025; Wichmann et al., 2024, 2026; Bisbee et al., 2024) stehen vollständig in `Quellen_APA.md`. Hier dienen sie nur der Einordnung. Einen DOI anzugeben ersetzt nicht die Prüfung des Inhalts, und diese habe ich in diesem Lauf nicht selbst vorgenommen.

## Status

- **Erstellt:** die unternehmensbezogene Befragungsfassung GARI-DE-0.1/ONLINE-S1-E1 mit unverändertem Kern und drei Platzhaltern, das Itemregister (Herkunft und Anwendung) für alle 34 Items, ein Codebuch-Auszug für die Onlineerhebung samt Datensatzvorlage, eine Umsetzungsspezifikation, eine Prüfliste, das Manifest, Rückfragen und eine Planungsmatrix für Maßnahmen.
- **Geprüft:** der Kerntext gegen die eingefrorene Bank, per Skript, ohne Abweichung.
- **Nicht geprüft:** die tatsächliche Onlineoberfläche (Freigabestatus OFFEN), die Primärquellen (in diesem Lauf nicht eingesehen; der OSF-Abgleich zu POWERPILOT_2025 bleibt offen), die Kompatibilität mit `score.py`, die Bearbeitungszeit und die Verständlichkeit in der Onlinedarstellung.
- **Berechnet:** nichts (NICHT_BERECHNET), weil keine Daten vorliegen.
- **Keine Validierung:** GARI-DE-0.1 ist eine adaptierte, psychometrisch nicht validierte Kombination. Dieser Lauf ist eine fiktive Demonstration.
