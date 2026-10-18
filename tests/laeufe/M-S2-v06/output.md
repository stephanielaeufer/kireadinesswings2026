# GARI-DE-0.1 im fiktiven Produktionsbetrieb (Szenario S2): Befragungsfassung, Prüfbericht und Auswertungsregeln

> **DEMONSTRATION.** Das Briefing beschreibt ausdrücklich einen fiktiven Produktionsbetrieb („Fiktives Unternehmen für eine Verfahrensdemonstration. Keine realen Daten.“). Alle betriebsbezogenen Angaben in diesem Dokument stammen aus dem Briefing oder sind als offene Eingabe in eckigen Klammern markiert. Es wurden keine Antwortdaten erhoben, erzeugt oder berechnet.

## 0 Ergebniskopf

| Angabe | Wert |
|---|---|
| Datum | 18. Oktober 2026 |
| System und Modell | Claude (Anthropic), Modellbezeichnung laut Systemangabe „Opus 5.5“ (Kennung claude-opus-5-5). Temperatur, Kontextparameter und weitere Systemparameter: NICHT_VERFUEGBAR |
| Promptversion | Masterprompt für GenAI Readiness und Weiterbildungsbedarf, Version 0.6 vom 18. Oktober 2026 |
| Betriebsart | ANWENDEN (im Auftrag und im Briefing ausdrücklich angegeben, keine Annahme nötig) |
| Eingaben | briefing.json (Briefing-Version 0.1, Szenario S2); instrument/Itembank_GARI_DE_0.1.json (Bankversion GARI-DE-0.1 vom 29. September 2026, SHA-256 12582782e64397d3460e88c2f4b2425b062f1f1c33725fc2d9953f5067afd050); instrument/Codebuch.md (Fragebogen GARI-DE-0.1, Codebuch-Revision 0.6 vom 18. Oktober 2026); Quellen_APA.md (Stand 17. Oktober 2026) |
| Quellenstand | Laut Quellen_APA.md vom 17. Oktober 2026 und Quellenregister der Bank. Die Quellen selbst lagen in dieser Sitzung nicht vor und wurden von mir nicht eingesehen |
| Fragebogenversion (Kern) | GARI-DE-0.1, unverändert |
| Erhebungsfassung | GARI-DE-0.1-S2-ONLINE-E1 (ersetzt nur die organisatorische Pretest-Einleitung, siehe 4.1) |
| Zusatzmodul | Z-S2-0.1 (eigene Modulversion, Status Entwurf, ungetestet) |
| Datenart | Keine Daten vorhanden (`antwortdaten_vorhanden: false`). Spätere echte Erhebung: `data_kind = SURVEY` |
| Berechnungsstatus | NICHT_BERECHNET (keine Daten; Auswertungsskript nicht unter den Eingaben) |
| Freigabestatus Onlineoberfläche | OFFEN (es existiert noch keine umgesetzte Oberfläche, die abgeglichen werden konnte) |

Gleiche Prompts garantieren keine identischen LLM-Ausgaben. Die Prüfungen in diesem Dokument sind Selbstprüfungen desselben Modells beziehungsweise von mir geschriebene und ausgeführte Vergleichsskripte. Sie sind kein unabhängiges Gutachten.

## 1 Kurzbeschreibung, Eingangsprüfung und Annahmen

### 1.1 Ziel, Zielgruppe, Kontext

Ziel ist die Anwendung der eingefrorenen Referenzbank GARI-DE-0.1 in einem fiktiven Produktionsbetrieb mit 400 Beschäftigten. Ergebnis ist eine betriebsbezogene Onlinefassung mit unverändertem Kern, ein gekennzeichnetes Zusatzmodul für betriebliche Voraussetzungen, die zugehörigen Codebuchergänzungen, ein Soll-Ist-Abgleich und der vorab festgelegte Auswertungs- und Maßnahmenplan.

### 1.2 Eingangsprüfung des Briefings

| Prüfpunkt | Angabe im Briefing | Behandlung |
|---|---|---|
| Zweck | Status quo beschreiben; Hinweise auf Weiterbildungsbedarf ableiten; betriebliche Voraussetzungen gesondert erfassen | Übernommen. „Gesondert erfassen“ begründet das Zusatzmodul (4.3) |
| Zielpopulation | Mitarbeitende aller Tätigkeitsbereiche einschließlich Personen ohne bisherige GenAI-Nutzung | Übernommen; deckt sich mit der filterlosen Bank (alle Fragen für alle Personen) |
| Tätigkeitsbereiche | Schichtarbeit Produktion, Logistik, Verwaltung, Führung | Kern erfasst nur C01 (Büro, andere Arbeit, gemischt). Bereiche nur über Zusatzmodul Z01/Z02 |
| Sprache | Deutsch | Übernommen; Bank ist deutsch |
| Bezug | Generative KI | Übernommen; Definition der Bank unverändert |
| Bisherige Nutzung | Unbekannt, mit dem Fragebogen zu erheben | Über C02, C03 |
| Nutzungsmöglichkeiten | Nicht alle haben einen eigenen PC oder freigegebene KI-Werkzeuge | C04 erfasst Zugang zu freigegebener GenAI; Gerätezugang nur über Zusatzmodul Z03 |
| Zugelassene Anwendungen | Nicht angegeben | Bleibt unbekannt. Nicht ergänzt |
| Aufgabenbezug | Nicht näher angegeben | Über C06, W02 (TASK_FIT), W03 |
| Betrachtungszeitraum | Nicht angegeben | Es gilt die Bank: vergangene vier Wochen (C02), nächste drei Monate (A01–A04, I01–I03) |
| Gewünschte Ausgabe | Befragungsfassung laut Betriebsart ANWENDEN | Abschnitte 4 bis 8 |
| Art der Daten | Keine Antwortdaten | Keine Auswertung; Regeln vorbereitet |
| Erhebungsweg | Onlineformular, Link, freiwillig; teilweise Tablet im Pausenraum | Eigene Erhebungseinleitung, Umsetzungsvorgaben und Prüfpunkte für geteilte Geräte (4.1, 4.2, 5.3) |
| Versionen | Kernbank GARI-DE-0.1, Codebuch GARI-DE-0.1 | Stimmt mit Bank (`version: GARI-DE-0.1`) und Codebuch (Fragebogen GARI-DE-0.1, Revision 0.6) überein |

### 1.3 Abweichungen zwischen Briefing und Referenzbank

1. **Tätigkeitsbereiche.** Das Briefing nennt vier Bereiche, die Bank kennt in C01 nur drei grobe Tätigkeitsarten. C01 bleibt unverändert. Die Bereiche werden nicht in C01 eingebaut, sondern als Z01 im Zusatzmodul erfragt.
2. **Führung.** Das Briefing führt Führung als Tätigkeitsbereich. Führung ist aber eine Rolle, die in Produktion, Logistik oder Verwaltung vorkommen kann. Ich trenne sie deshalb in Z02 (eigene Planungsentscheidung, siehe 4.3).
3. **Betrachtungszeitraum.** Im Briefing nicht festgelegt. Die Bank legt vier Wochen und drei Monate fest. Diese gelten.
4. **Gerätezugang.** Der Briefing-Hinweis auf fehlende eigene PCs wird vom Kern nicht erfasst. C04 fragt nur nach dem Zugang zu freigegebener generativer KI. Ergänzung über Z03.
5. **Erhebungssituation.** Der eingefrorene Befragtentext der Bank ist eine Pretest-Fassung („Fassung für den Verständlichkeitstest“, „Im anschließenden Gespräch …“, Testkürzel, Hinweis auf begleiteten Test). Für die Onlinebefragung wird diese organisatorische Einleitung laut `frozen_text_note` der Bank als gesondert dokumentierte Erhebungsfassung ersetzt.
6. **Medienbruch in Kerninstruktionen.** Die Kerninstruktionen enthalten Papierformulierungen („Kreisen Sie pro Aussage eine Zahl ein“, „Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein“, „Bitte fahren Sie auf der nächsten Seite fort“). Sie bleiben in ANWENDEN wortgleich, weil jede Änderung eine neue Version erzeugt. Siehe Rückfrage R3 und Prüfbericht P-04.

### 1.4 Getroffene Annahmen

- A-1: Die Bank ist laut Briefing „geprüft“. Ihr eigener Status lautet: „Fuer erste Pretestrunde festgehalten; inhaltliche Quellenpruefung mit dokumentierter Grenze bei POWERPILOT_2025; keine psychometrische Validierung.“ Ergebnisse des im Codebuch erwähnten Pretests (drei reale Personen, zwei Claude-Personas) liegen mir nicht vor. Ich setze nichts über deren Befunde voraus.
- A-2: Die Bank verbietet Zusatzmodule nicht ausdrücklich. `context_changes_allowed` regelt nur Kontaktangaben und organisatorische Hinweise außerhalb des Fragebogens und schließt Änderungen an Definition, Items, Skalen, Reihenfolge und Zeitbezügen aus. Ein Modul nach dem vollständigen Kern ändert keines davon. Es ist deshalb nach den Regeln des Masterprompts zulässig.
- A-3: Mindestgruppengröße 10 für alle Gruppenberichte. Das ist eine Planungsentscheidung, keine belegte Schwelle.
- A-4: Erhebungsplattform, gespeicherte technische Daten, Zugriffsrechte, Kontaktperson und Erhebungszeitraum sind unbekannt. Sie werden nicht erfunden, sondern als Eintragsfelder markiert.

### 1.5 Gebündelte Rückfragen an die Auftraggebenden

Alles, was ohne diese Antworten möglich ist, ist in diesem Dokument bereits erstellt.

- **R1 Datenschutz und Plattform.** Welche Plattform wird verwendet? Speichert sie Anmeldedaten, E-Mail-Adressen, IP-Adressen oder Zeitstempel? Wer sieht Einzelantworten? Wer ist Kontaktperson? Wie lange läuft die Erhebung? Kann ein begonnener, nicht abgesendeter Fragebogen am Pausenraum-Tablet zuverlässig verworfen werden? Ohne diese Angaben bleibt die Einleitung mit Eintragsfeldern und ohne Anonymitätszusage.
- **R2 Gruppenberichte.** Sollen Ergebnisse nach Bereich (Z01) und Führungsrolle (Z02) berichtet werden? Ist die Mindestgruppengröße 10 akzeptiert? Wie viele Beschäftigte gehören zu jedem Bereich (für die Rücklaufquote)? Werden keine Gruppenberichte gewünscht, entfallen Z01 und Z02 aus Gründen der Datensparsamkeit.
- **R3 Papierformulierungen in Kerninstruktionen.** Soll die Onlinefassung die Instruktionen „Kreisen Sie … ein“ wortgleich unter GARI-DE-0.1 behalten (meine Voreinstellung in diesem Dokument) oder soll eine neue Version GARI-DE-0.2 mit onlinegerechter Instruktion entstehen? Eine neue Version braucht eine eigene Bank, ein angepasstes Codebuch und einen eigenen Abgleich. Gleichwertigkeit mit 0.1 ist dann nicht ohne Prüfung zu behaupten.

## 2 Theoretische Grundlage und Forschungsmodell

In ANWENDEN wird ein mitgeliefertes Forschungsmodell unverändert übernommen. Weder die Bank noch das Codebuch enthalten ein Forschungsmodell oder Hypothesen. Ich erfinde keines. Die theoretische Herleitung des Instruments muss in der Begleitdokumentation von GARI-DE-0.1 zu finden sein.

Was die Eingaben selbst dazu sagen, ohne daraus ein Modell abzuleiten:

- Das Codebuch nennt die MAILS-Auswertungszuordnung als Motivation für U, K und L und die siebenstufige Zustimmung der bereitgestellten Itemsammlung für A und I.
- Quellen_APA.md führt Ajzen (o. J.) als Grundlage für die Definition des Verhaltens über Ziel, Handlung, Kontext und Zeit sowie Carolus et al. (2023) als Kompetenzbezug. Ob und wie diese Quellen in einem Forschungsmodell verbunden wurden, geht aus den Eingaben nicht hervor.
- Hypothesen: keine in den Eingaben. Es werden keine Hypothesen geprüft oder formuliert.

## 3 Quellen- und Konstruktregister mit Evidenzgrenzen

### 3.1 Quellenregister

Die Spalte „Geprüfter Dokumentstand“ gibt wieder, was Bank und Quellen_APA.md dokumentieren. Ich selbst habe in dieser Sitzung keine Quelle eingesehen. Zugang für mich: nur über die Metadaten und Prüfvermerke der Eingabedateien.

| Quellen-ID | Nachweis (APA) | Geprüfter Dokumentstand laut Eingaben | Fundstelle | Zielgruppe der Quelle | Sprache | Konstrukt / Items | Instrument | Relevante Grenzen |
|---|---|---|---|---|---|---|---|---|
| MAILS_DE_2023 | Carolus et al. (2023) | Publizierter Autoren-Volltext und deutscher Originalfragebogen geprüft (34 Items, 3 Seiten, Auswertungszuordnung) | Deutscher Autorenfragebogen, Items 1–6, 7–12, 26–28; Zuordnung und Mittelwertregel Seite 3 | 300 deutschsprachige Erwachsene | Deutsch (Fragebogen), Englisch (Artikel) | U01–U06, K01–K06, L01–L03 | MAILS, Teilbereiche | Evidenz betrifft allgemeine KI und Selbstberichte. Adaptierte Fassung im Projekt nicht empirisch geprüft. Fehlwertregel „vollständige Antworten“ ist Projektregel, nicht MAILS-Vorgabe. Nachnutzungsrechte bearbeiteter Items vor öffentlicher Veröffentlichung klären |
| POWERPILOT_2025 | Wichmann et al. (2025) | Paper und bereitgestellte Itemsammlung (Datensatz_v1.docx). OSF-Anhang GEBK9 am 29.09.2026 und bei erneutem Abruf nicht zugänglich | Datensatz_v1.docx, Questionnaire 2 / PowerPilot, „1 – Intention to use“ Items 1–3, „2 – Attitude“ Items 1–4 | Laut Titel Bezug auf Deutschland; Stichprobe in den Eingaben nicht beschrieben | Englisch | A01–A04, I01–I03 | Messmodell der Studie zur Energie-Monitoring-App | Exakter Originalwortlaut im OSF-Anhang nicht verifiziert. Energieanwendungskontext. Übersetzung, Technologiewechsel, Arbeitskontext und Zeitraum sind Anpassungen. Nutzungsbedingungen der Originalitems vor Veröffentlichung prüfen |
| Q02 (Ajzen) | Ajzen (o. J.) | Siebenseitiges Originaldokument eingesehen; kein Erscheinungsjahr | Gesamtdokument | Methodenanleitung, keine Stichprobe | Englisch | Verhaltensdefinition (Ziel, Handlung, Kontext, Zeit) | Konstruktionsanleitung für TPB-Fragebögen | Liefert keine Items von GARI-DE. In der Bank keinem Item als Quelle zugeordnet |
| KOCH_2024 | Koch et al. (2024) | Volltext eingesehen, Abschnitte 2.1 und 3.4 | Abschnitte 2.1, 3.4 | In den Eingaben nicht beschrieben | Englisch | Alternative Kurzfassung MAILS | MAILS-Kurzfassung | Wird nicht eingesetzt. Fordert weitere Validierung der Kurzfassung |
| Weitere Studien | Wichmann et al. (2024); Paetow et al. (2026); Do Khac et al. (2025); Wichmann et al. (2026) | Laut Quellen_APA.md als PDF bereitgestellt | Keine Itemfundstelle in der Bank | Gesundheit, VR, Entscheidungstragende, virtuelle Meetings | Englisch | Keinem GARI-DE-Item zugeordnet | Keine | Liefern in dieser Fassung keine Items. Keine Übertragbarkeit belegt |
| Methode | Peffers et al. (2007); Venable et al. (2016); Boateng et al. (2018); National Center for Health Statistics (2024); Bisbee et al. (2024) | Laut Quellen_APA.md eingesehen | Siehe Quellen_APA.md | Methodenquellen | Englisch | Entwicklungs- und Evaluationsmethode | Keine | Begründen Vorgehen, nicht Messqualität |

### 3.2 Konstruktregister (aus Bank und Codebuch übernommen)

| Bereich | Bezeichnung laut Bank/Codebuch | Items | Diagnosezweck | Herkunft | Zulässige Zusammenfassung | Evidenzgrenze |
|---|---|---|---|---|---|---|
| C | Tätigkeit, Nutzung, Zugang, Regeln, Aufgabenrelevanz | C01–C06 | Kontext für die Deutung aller anderen Antworten; organisatorische Hindernisse erkennen | NEU_ENTWICKELT | Jede Frage einzeln | Nicht empirisch geprüft |
| U | Selbst eingeschätzte Anwendung | U01–U06 | Selbstbericht zur Anwendungsfähigkeit | ADAPTIERT aus MAILS 1–6 | Vollständiger Teilbereichsmittelwert U | Selbsteinschätzung, kein Leistungsnachweis |
| K | Selbst eingeschätztes Verständnis | K01–K06 | Selbstbericht zum Verständnis | ADAPTIERT aus MAILS 7–12 | Vollständiger Teilbereichsmittelwert K | wie U |
| L | Zutrauen in das eigene Lernen | L01–L03 | Selbstbericht zum Mithalten mit Veränderungen | ADAPTIERT aus MAILS 26–28 | Vollständiger Teilbereichsmittelwert L | wie U |
| G | Prüfen von Ergebnissen und zulässigen Eingaben | G01–G03 | Selbstbericht zu Ergebnisprüfung und verantwortlicher Eingabe | NEU_ENTWICKELT | Drei Einzelitems, kein G-Mittelwert | Nicht empirisch geprüft |
| A | Einstellung zur Nutzung | A01–A04 | Bewertung einer bedingten Nutzung freigegebener GenAI | ADAPTIERT aus POWERPILOT_2025 Attitude 1–4 | Vorläufiger Mittelwert A | Wortlautvergleich mit OSF offen |
| I | Berichtete Nutzungsabsicht | I01–I03 | Absicht unter tatsächlich erwarteten Bedingungen | ADAPTIERT aus POWERPILOT_2025 Intention 1–3 | Vorläufiger Mittelwert I | wie A |
| W | Weiterbildungswünsche, Hindernisse, Freitext | W01–W03 | Geäußerter Lernwunsch und wahrgenommene Hindernisse | NEU_ENTWICKELT | Häufigkeiten je Option; qualitative Zuordnung | Nicht empirisch geprüft |

Abgleich mit der Prüfliste des Masterprompts (Phase 1b), nur als Zuordnung, nicht als Faktorenstruktur: Verständnis und Anwendung → U, K; Bewertung von Ergebnissen und verantwortlicher Umgang → G01–G03; Selbstwirksamkeit → in der Bank nicht als eigener Bereich bezeichnet, am nächsten L (Zutrauen in das eigene Lernen); Einstellung und Nutzungsabsicht → A, I; Nutzungserfahrung → C02, C03; Aufgabenpassung → C06, W02 TASK_FIT; Zugang und Unterstützung → C04, C05, W02, ergänzt durch Z03; Lernwünsche → W01, W03.

Die Bank enthält keinen Gesamtwert, keine Gewichtung und keine Reifegradklassen. Das Codebuch schließt sie ausdrücklich aus.

## 4 Befragungsfassung, Zusatzmodul, Itemregister und Codebuch

### 4.1 Erhebungsfassung GARI-DE-0.1-S2-ONLINE-E1 (Text für Befragte)

Erzeugt per Skript direkt aus `frozen_participant_text` der Bank. Wortgleich übernommen: 109 von 114 Zeilen, darunter Definition, alle Instruktionen, alle 34 Items und alle Antwortoptionen. Ersetzt wurden ausschließlich die organisatorischen Pretest-Zeilen 1, 2, 4, 5 und 113 (Zählung ab 0), siehe Änderungsprotokoll in 8.1. Seitenumbrüche sind als **[Seite n]** markiert und gehören zur Umsetzungsvorgabe, nicht zum Befragtentext. Eckige Klammern sind vom Betrieb vor dem Start zu füllen.


**[Seite 1 · Einleitung]**

### Fragebogen zum Umgang mit generativer KI

Onlinebefragung · Fragebogenversion GARI-DE-0.1 · Erhebungsfassung GARI-DE-0.1-S2-ONLINE-E1 (Zusatzmodul Z-S2-0.1) · Erhebungszeitraum: [vom Betrieb einzutragen]

Dieser Fragebogen erfasst Ihre Erfahrungen, Einschätzungen und Weiterbildungswünsche zu generativer KI bei der Arbeit. Die Ergebnisse sollen zeigen, welche Weiterbildungen und welche betrieblichen Voraussetzungen sinnvoll sind. Es geht dabei nicht um die Bewertung Ihrer Arbeitsleistung. Geschätzte Dauer für den Fragebogen: 10 bis 15 Minuten.

Generative KI erzeugt oder bearbeitet auf Eingaben hin Inhalte, zum Beispiel Texte, Bilder, Audio, Videos oder Programmcode. Gemeint sind sowohl eigenständige Anwendungen als auch entsprechende Funktionen in anderen Programmen.

Die Teilnahme ist freiwillig. Sie können einzelne Fragen auslassen oder die Befragung beenden. Für jede Frage gibt es dafür auch die Antwort „Keine Angabe“. Bitte tragen Sie keine Namen, Personalnummern oder vertraulichen Informationen ein. Wir fragen nicht nach Ihrem Namen. Ergebnisse werden nur zusammengefasst berichtet, für Gruppen erst ab 10 Personen. Welche technischen Daten die Befragungsplattform speichert und wer Zugriff auf die Einzelantworten hat: [vom Betrieb vor dem Start einzutragen]. Eine vollständige Anonymität wird nicht zugesagt, solange diese Angaben nicht geklärt sind. Fragen zur Befragung: [Kontaktperson vom Betrieb einzutragen].

Wenn Sie das Tablet im Pausenraum nutzen: Bitte schließen Sie den Fragebogen bis zum Ende ab und senden Sie ihn ab, damit die nächste Person Ihre Antworten nicht sieht. Wenn Sie unterbrechen müssen: [vom Betrieb nach technischer Prüfung einzutragen, wie ein begonnener Fragebogen sicher verworfen wird].


**[Seite 2]**

#### Ihre Tätigkeit und bisherige Nutzung

Bitte wählen Sie pro Frage genau eine Antwort.

**C01**  Wie sieht Ihre hauptsächliche Tätigkeit aus?

> ☐ Überwiegend Büro- oder Bildschirmarbeit · ☐ Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst · ☐ Etwa gleich große Anteile beider Bereiche · ☐ Keine Angabe

**C02**  An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt?

> ☐ An keinem Tag · ☐ An 1 bis 3 Tagen · ☐ An 4 bis 9 Tagen · ☐ An 10 bis 15 Tagen · ☐ An 16 oder mehr Tagen · ☐ Kann ich nicht einschätzen · ☐ Keine Angabe

**C03**  Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt?

> ☐ Ja · ☐ Nein · ☐ Ich bin mir nicht sicher · ☐ Keine Angabe

**C04**  Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen?

> ☐ Ja · ☐ Nein · ☐ Ich weiß es nicht · ☐ Keine Angabe

**C05**  Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit?

> ☐ Ja · ☐ Teilweise · ☐ Nein · ☐ Ich weiß nicht, ob es solche Regeln gibt · ☐ Keine Angabe

**C06**  Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre?

> ☐ Ja · ☐ Nein · ☐ Kann ich noch nicht beurteilen · ☐ Keine Angabe


**[Seite 3]**

#### Anwendung und Verständnis

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**U01**  Ich kann eine generative KI bedienen.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**U02**  Ich kann mir berufliche Aufgaben durch generative KI erleichtern.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**U03**  Ich kann generative KI gezielt für meine Arbeitsziele einsetzen.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**U04**  Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**U05**  Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**U06**  Ich kann generativer KI verständlich mitteilen, was ich brauche.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**K01**  Ich kenne die zentralen Konzepte generativer KI.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**K02**  Ich kann erklären, was generative KI bedeutet.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**K03**  Ich kann Chancen und Grenzen generativer KI einschätzen.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**K04**  Ich kann Vor- und Nachteile generativer KI beurteilen.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**K05**  Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**K06**  Ich kann mir künftige Anwendungen generativer KI vorstellen.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`


**[Seite 4]**

#### Lernen und Prüfen

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**L01**  Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**L02**  Ich kann mich über Neuerungen bei generativer KI informieren.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**L03**  Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**G01**  Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**G02**  Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

**G03**  Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf.

> `0  1  2  3  4  5  6  7  8  9  10  NB  KA`

Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.


**[Seite 5]**

#### Einstellung und geplante Nutzung

Wie sehr stimmen Sie den folgenden Aussagen zu? Gemeint ist die Nutzung für Ihre beruflichen Aufgaben in den kommenden drei Monaten. „Freigegeben“ bedeutet, dass Ihr Unternehmen die betreffende Nutzung erlaubt.

1 = stimme überhaupt nicht zu   ·   7 = stimme vollständig zu

NB = nicht beurteilbar   ·   KA = keine Angabe. Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein.

**A01**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft.

> `1  2  3  4  5  6  7  NB  KA`

**A02**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend.

> `1  2  3  4  5  6  7  NB  KA`

**A03**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig.

> `1  2  3  4  5  6  7  NB  KA`

**A04**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm.

> `1  2  3  4  5  6  7  NB  KA`

Für die folgenden drei Aussagen: Denken Sie an die Bedingungen, die Sie in den nächsten drei Monaten tatsächlich erwarten. Setzen Sie keinen gesicherten Zugang voraus, wenn dieser unklar ist. Fehlender Zugang bedeutet jedoch nicht automatisch, dass Sie nicht antworten können.

**I01**  Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

> `1  2  3  4  5  6  7  NB  KA`

**I02**  Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

> `1  2  3  4  5  6  7  NB  KA`

**I03**  Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen.

> `1  2  3  4  5  6  7  NB  KA`


**[Seite 6]**

#### Weiterbildung und Unterstützung

Bei W01 und W02 sind jeweils höchstens drei Antworten möglich. „Kein Weiterbildungswunsch“, „derzeit nichts“, „kann ich noch nicht einschätzen“ und „keine Angabe“ dürfen innerhalb einer Frage nur allein gewählt werden.

**W01**  Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen.

> ☐ Grundlagen generativer KI

> ☐ Passende Einsatzmöglichkeiten für meine Aufgaben

> ☐ Klare Eingaben formulieren und Ergebnisse verbessern

> ☐ Antworten und Quellen überprüfen

> ☐ Betriebliche Regeln und zulässige Dateneingaben

> ☐ Bei neuen Entwicklungen auf dem Laufenden bleiben

> ☐ Anderes Thema

> ☐ Derzeit kein Weiterbildungswunsch

> ☐ Ich kann meinen Bedarf noch nicht einschätzen

> ☐ Keine Angabe

**W02**  Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen.

> ☐ Kein Zugang zu einem freigegebenen Werkzeug

> ☐ Unklare betriebliche Regeln

> ☐ Zu wenig Zeit zum Ausprobieren oder Lernen

> ☐ Mir fehlt Wissen über die Nutzung

> ☐ Ich erkenne keinen passenden Einsatz für meine Aufgaben

> ☐ Unsicherheit über die Verlässlichkeit der Ergebnisse

> ☐ Etwas anderes

> ☐ Derzeit nichts

> ☐ Kann ich noch nicht einschätzen

> ☐ Keine Angabe

**W03**  Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen.

> ☐ Keine Angabe

> ______________________________

> ______________________________

> ______________________________


**[Seite 7 · Zusatzmodul Z-S2-0.1, nicht Teil von GARI-DE-0.1]**

#### Zusatzfragen für diesen Betrieb

Die folgenden Fragen gehören nicht zum Kernfragebogen. Sie helfen, betriebliche Voraussetzungen einzuordnen. Bitte wählen Sie pro Frage genau eine Antwort. Sie können jede Frage auslassen.

**Z01**  In welchem Bereich arbeiten Sie hauptsächlich?

> ☐ Produktion im Schichtbetrieb · ☐ Logistik · ☐ Verwaltung · ☐ Anderer Bereich · ☐ Keine Angabe

**Z02**  Haben Sie Führungsverantwortung für andere Mitarbeitende?

> ☐ Ja · ☐ Nein · ☐ Keine Angabe

**Z03**  Steht Ihnen bei der Arbeit ein Gerät des Betriebs zur Verfügung, mit dem Sie Programme oder das Internet nutzen können, zum Beispiel PC, Laptop oder Tablet?

> ☐ Ja, ein Gerät, das nur ich nutze · ☐ Ja, ein Gerät, das ich mit anderen teile · ☐ Nein · ☐ Keine Angabe


**[Abschlussseite]**

Vielen Dank für Ihre Teilnahme. Bitte senden Sie den Fragebogen jetzt ab.


### 4.2 Umsetzungsvorgaben für das Onlineformular (Sollwerte für den Oberflächenabgleich)

Die Übertragung in ein Formular ist ein eigener Implementierungsschritt. Die folgenden Sollwerte sind die Prüfgrundlage für Abschnitt 5.3. Eine Selbstauskunft des Formularwerkzeugs oder eines erzeugenden KI-Systems ersetzt den Abgleich nicht.

| Nr. | Element | Sollwert |
|---|---|---|
| S-01 | Seiten | Sieben Fragebogenseiten plus Abschlussseite wie in 4.1 markiert. Ein Seitenwechsel nach G03 ist Pflicht, weil die Kerninstruktion „Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.“ sonst nicht zutrifft |
| S-02 | Reihenfolge | Exakt Bankreihenfolge C01–C06, U01–U06, K01–K06, L01–L03, G01–G03, A01–A04, I01–I03, W01–W03; danach Z01–Z03. Keine Zufallsreihenfolge von Fragen oder Optionen |
| S-03 | Item-IDs | Sichtbar vor jedem Wortlaut wie in der Bank (z. B. „U01“) und als Variablenname im Export |
| S-04 | C01–C06 | Einzelwahl (Optionsfeld) mit allen Optionen der Bank plus „Keine Angabe“ als auswählbare Option |
| S-05 | U, K, L, G | Pro Item eine Einzelwahl mit 13 Optionen in der Reihenfolge 0, 1, …, 10, NB, KA. Endanker nur als Instruktionstext über dem Block, keine Zwischenanker. Kein Schieberegler, keine Sternbewertung, keine Vorauswahl. Ein Raster ist nur zulässig, wenn jede Zeile genau eine Wahl erlaubt und NB/KA als eigene Spalten auswählbar sind |
| S-06 | A, I | Pro Item Einzelwahl mit 9 Optionen 1, …, 7, NB, KA. Sonst wie S-05 |
| S-07 | W01, W02 | Kontrollkästchen mit allen 9 Bankoptionen plus „Keine Angabe“ (10 Kästchen). Höchstzahl 3 muss beim Weiter-Klick tatsächlich blockieren, nicht nur als Hinweis erscheinen. Exklusivität von NONE, UNKNOWN und „Keine Angabe“ technisch erzwingen, falls die Plattform das kann; sonst dokumentieren und im Datencheck behandeln (4.5) |
| S-08 | W03 | Mehrzeiliges Textfeld plus Kontrollkästchen „Keine Angabe“ |
| S-09 | Pflichtfelder | Keine. Einleitung und Instruktionen sagen, dass Fragen ausgelassen werden können |
| S-10 | Kennung | Systemvergebene, zufällige Antwortkennung als `respondent_id`. Kein Namensfeld, keine Personalnummer, keine automatische E-Mail-Erfassung. Das Feld „Testkürzel/Datum“ der Pretestfassung entfällt |
| S-11 | Zwei Links | Getrennte Links für das Pausenraum-Tablet und für persönliche Geräte. Der Link bestimmt das Metadatum `erhebungskanal` (TABLET_PAUSENRAUM oder PERSOENLICHER_LINK). Keine Frage an die Befragten |
| S-12 | Tablet | Kein Anmelden mit persönlichem Konto. Nach dem Absenden zurück auf leere Startseite. Keine Zwischenspeicherung oder automatische Formularausfüllung durch den Browser. Ablauf beim Unterbrechen festlegen und in die Einleitung eintragen |
| S-13 | Darstellung Tablet | Die 13 Antwortoptionen der 0–10-Items müssen im Hoch- und Querformat vollständig sichtbar und einzeln tippbar sein. Wechsel zu einer anderen Darstellung nur dokumentiert und ohne Entfernen von Optionen |
| S-14 | Export | Je Item eine Spalte. Zahlen als ganze Zahlen exportiert, NB/KA als Text. Mehrfachwahl als vollständige Liste der gewählten Optionen. Codierung laut Tabelle in 4.5 |
| S-15 | Testantworten | Technische Probeläufe nur in einer Formularkopie oder in ungesendeten Sitzungen. Keine Testabsendungen im Erhebungsformular |

### 4.3 Zusatzmodul Z-S2-0.1 (Register)

Modulversion Z-S2-0.1, getrennt von Kernversion GARI-DE-0.1. Platz: nach W03, vor der Abschlussseite. Kernreihenfolge, Kerninstruktionen und Definition bleiben unverändert. Modulfragen fließen in keine Kernzusammenfassung ein und verändern keine Kernauswertung. Sie dürfen nur zur Gruppierung bereits regelgerecht berechneter Kernergebnisse und als eigene Häufigkeiten verwendet werden.

| ID | Wortlaut | Status | Begründung aus dem Briefing | Antwortoptionen (Code: Label) | Fehlwerte | Verwendung | Evidenz |
|---|---|---|---|---|---|---|---|
| Z01 | In welchem Bereich arbeiten Sie hauptsächlich? | NEU_ENTWICKELT | `taetigkeitsbereiche`: Schichtarbeit Produktion, Logistik, Verwaltung, Führung. C01 unterscheidet nur Büro, andere Arbeit und gemischt | PROD_SHIFT: Produktion im Schichtbetrieb; LOGISTICS: Logistik; ADMIN: Verwaltung; OTHER_AREA: Anderer Bereich | KEINE_ANGABE, UNGUELTIG_ERFASST | Gruppierung für Berichte, nur wenn R2 bestätigt. Mindestgruppengröße 10 | Ungetestet |
| Z02 | Haben Sie Führungsverantwortung für andere Mitarbeitende? | NEU_ENTWICKELT | Führung im Briefing als Bereich genannt. Getrennt, weil Führung in allen Bereichen vorkommen kann (Planungsentscheidung) | YES: Ja; NO: Nein | KEINE_ANGABE, UNGUELTIG_ERFASST | Gruppierung, nur wenn R2 bestätigt. Keine Kreuzung mit Z01 in Berichten | Ungetestet |
| Z03 | Steht Ihnen bei der Arbeit ein Gerät des Betriebs zur Verfügung, mit dem Sie Programme oder das Internet nutzen können, zum Beispiel PC, Laptop oder Tablet? | NEU_ENTWICKELT | `arbeitszugang_zu_genai`: „Nicht alle haben einen eigenen PC“; Zweck „Betriebliche Voraussetzungen gesondert erfassen“ | OWN_DEVICE: Ja, ein Gerät, das nur ich nutze; SHARED_DEVICE: Ja, ein Gerät, das ich mit anderen teile; NO_DEVICE: Nein | KEINE_ANGABE, UNGUELTIG_ERFASST | Häufigkeiten; gemeinsame Darstellung mit C04 und W02 ACCESS als organisatorischer Befund | Ungetestet |

Hinweise zum Modul:

- Mindestgruppengröße für alle Gruppenberichte (Z01, Z02, C01, `erhebungskanal`): 10 gültige Fälle je ausgewiesener Gruppe. Kleinere Gruppen werden mit „Anderer Bereich“ zusammengefasst oder nicht berichtet. Planungsentscheidung, keine empirisch belegte Schwelle.
- Keine Kreuztabellen Z01 × Z02 und keine Kombination mit W03-Freitexten auf Gruppenebene. Führungskräfte eines Bereichs wären sonst leicht erkennbar.
- Z03 misst Gerätezugang, nicht die Freigabe von GenAI-Werkzeugen. Die Freigabe erfasst C04.
- Die Wortlaute sind ungetestet. Eine kurze Verständlichkeitsprüfung mit Beschäftigten aus Schichtproduktion und Logistik am Tablet wird empfohlen (5.4).
- Entfällt der Wunsch nach Gruppenberichten (R2), werden Z01 und Z02 gestrichen und die Modulversion auf Z-S2-0.2 erhöht.

### 4.4 Wissenschaftliches Itemregister GARI-DE-0.1 (unverändert aus der Bank)

Für alle 34 Items gilt laut Bank: Rolle FESTER_KERN, Anzeigebedingung ALWAYS (keine Filter, alle Personen sehen alle Fragen, auch Nichtnutzende), keine Umpolung (`reverse_coded: false`), Version GARI-DE-0.1. Konstruktdefinitionen und Zweck: siehe 3.2. Für die MAILS-Items dokumentiert die Bank den Originalwortlaut nur über die Fundstelle (`original_text: null`, „Originalwortlaut am angegebenen Dokument geprüft; hier über Fundstelle referenziert“). Ich kann diesen Wortlaut nicht prüfen und gebe ihn nicht wieder. Für A und I gibt die Bank den englischen Wortlaut der bereitgestellten Itemsammlung wieder, mit der genannten Grenze zum OSF-Anhang. Ursprüngliche Skalen laut Bank: MAILS „Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker“; POWERPILOT „Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung“. Deutscher Befragungswortlaut: siehe 4.1.

UNGUELTIG_ERFASST steht nicht im Feld `missing_allowed` der Bank. Es ist seit Codebuch-Revision 0.6 als Erfassungsgrund für alle Items zugelassen und keine Antwortoption für Befragte. Die Bank bleibt dadurch laut Codebuch unverändert.

Originalwortlaute A/I laut Bank: A01 „The use of PowerPilot would be … advantageous.“; A02 „… satisfactory.“; A03 „… important.“; A04 „… enjoyable.“; I01 „I plan to use PowerPilot in the future.“; I02 „I intend to use PowerPilot in the future.“; I03 „I will definitely use PowerPilot in the future.“

| ID | Teilbereich | Status | Quelle und Fundstelle | Art der Änderung (laut Bank) | Antwortformat | Fehlwerte | Zusammenfassung |
|---|---|---|---|---|---|---|---|
| C01 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: OFFICE, OTHER_WORK, MIXED | KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Einzelverteilung |
| C02 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: D0, D1_3, D4_9, D10_15, D16_PLUS, UNKNOWN | KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Einzelverteilung |
| C03 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: YES, NO, UNKNOWN | KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Einzelverteilung |
| C04 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: YES, NO, UNKNOWN | KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Einzelverteilung |
| C05 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: KNOWN, PARTLY, NOT_KNOWN, EXISTENCE_UNKNOWN | KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Einzelverteilung |
| C06 | C | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Einzelwahl: YES, NO, UNKNOWN | KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Einzelverteilung |
| U01 | U | ADAPTIERT | MAILS_DE_2023, Item 1; Deutscher Autorenfragebogen, Item 1, Seite 1; Zuordnung und Mittelwertregel Seite 3. | KI-Bezug auf generative KI eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | U-Mittelwert (vollständig) |
| U02 | U | ADAPTIERT | MAILS_DE_2023, Item 2; Deutscher Autorenfragebogen, Item 2, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Erleichterung des Lebens auf berufliche Aufgaben eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | U-Mittelwert (vollständig) |
| U03 | U | ADAPTIERT | MAILS_DE_2023, Item 3; Deutscher Autorenfragebogen, Item 3, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Zielbezug auf Arbeitsziele eingegrenzt; sinnvoll durch gezielt konkretisiert. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | U-Mittelwert (vollständig) |
| U04 | U | ADAPTIERT | MAILS_DE_2023, Item 4; Deutscher Autorenfragebogen, Item 4, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Alltagsinteraktion auf Zusammenarbeit bei der Arbeit übertragen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | U-Mittelwert (vollständig) |
| U05 | U | ADAPTIERT | MAILS_DE_2023, Item 5; Deutscher Autorenfragebogen, Item 5, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gewinnbringende Zusammenarbeit über brauchbare Arbeitsergebnisse konkretisiert; Bedeutungsverschiebung im Pretest prüfen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | U-Mittelwert (vollständig) |
| U06 | U | ADAPTIERT | MAILS_DE_2023, Item 6; Deutscher Autorenfragebogen, Item 6, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gewinnbringende Kommunikation über verständliches Mitteilen konkretisiert; Ergebnisaspekt verengt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | U-Mittelwert (vollständig) |
| K01 | K | ADAPTIERT | MAILS_DE_2023, Item 7; Deutscher Autorenfragebogen, Item 7, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Allgemeine KI auf generative KI eingegrenzt; Konzepte bleibt bewusst zur Verständlichkeitsprüfung erhalten. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | K-Mittelwert (vollständig) |
| K02 | K | ADAPTIERT | MAILS_DE_2023, Item 8; Deutscher Autorenfragebogen, Item 8, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Kenntnis von Definitionen in selbst eingeschätzte Erklärfähigkeit übertragen; stärkere Anpassung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | K-Mittelwert (vollständig) |
| K03 | K | ADAPTIERT | MAILS_DE_2023, Item 9; Deutscher Autorenfragebogen, Item 9, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | K-Mittelwert (vollständig) |
| K04 | K | ADAPTIERT | MAILS_DE_2023, Item 10; Deutscher Autorenfragebogen, Item 10, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | K-Mittelwert (vollständig) |
| K05 | K | ADAPTIERT | MAILS_DE_2023, Item 11; Deutscher Autorenfragebogen, Item 11, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Verwendungszwecke sprachlich vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | K-Mittelwert (vollständig) |
| K06 | K | ADAPTIERT | MAILS_DE_2023, Item 12; Deutscher Autorenfragebogen, Item 12, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; Satz verkürzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | K-Mittelwert (vollständig) |
| L01 | L | ADAPTIERT | MAILS_DE_2023, Item 26; Deutscher Autorenfragebogen, Item 26, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; stets entfällt. Deutsche Itemnummer 26 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | L-Mittelwert (vollständig) |
| L02 | L | ADAPTIERT | MAILS_DE_2023, Item 27; Deutscher Autorenfragebogen, Item 27, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; deutsche Itemnummer 27 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | L-Mittelwert (vollständig) |
| L03 | L | ADAPTIERT | MAILS_DE_2023, Item 28; Deutscher Autorenfragebogen, Item 28, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Gegenstand eingegrenzt; sprachliche Verdichtung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | L-Mittelwert (vollständig) |
| G01 | G | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Einzelitem, kein G-Mittelwert |
| G02 | G | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Einzelitem, kein G-Mittelwert |
| G03 | G | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | 0–10 (gar nicht oder kaum ausgeprägt / sehr gut oder (nahezu) perfekt ausgeprägt) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Einzelitem, kein G-Mittelwert |
| A01 | A | ADAPTIERT | POWERPILOT_2025, Item 2 – Attitude, Item 1; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | 1–7 (stimme überhaupt nicht zu / stimme vollständig zu) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | A-Mittelwert (vollständig, vorläufig) |
| A02 | A | ADAPTIERT | POWERPILOT_2025, Item 2 – Attitude, Item 2; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | 1–7 (stimme überhaupt nicht zu / stimme vollständig zu) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | A-Mittelwert (vollständig, vorläufig) |
| A03 | A | ADAPTIERT | POWERPILOT_2025, Item 2 – Attitude, Item 3; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | 1–7 (stimme überhaupt nicht zu / stimme vollständig zu) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | A-Mittelwert (vollständig, vorläufig) |
| A04 | A | ADAPTIERT | POWERPILOT_2025, Item 2 – Attitude, Item 4; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 4; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | 1–7 (stimme überhaupt nicht zu / stimme vollständig zu) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | A-Mittelwert (vollständig, vorläufig) |
| I01 | I | ADAPTIERT | POWERPILOT_2025, Item 1 – Intention to use, Item 1; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | 1–7 (stimme überhaupt nicht zu / stimme vollständig zu) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | I-Mittelwert (vollständig, vorläufig) |
| I02 | I | ADAPTIERT | POWERPILOT_2025, Item 1 – Intention to use, Item 2; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | 1–7 (stimme überhaupt nicht zu / stimme vollständig zu) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | I-Mittelwert (vollständig, vorläufig) |
| I03 | I | ADAPTIERT | POWERPILOT_2025, Item 1 – Intention to use, Item 3; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. Quellengrenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | 1–7 (stimme überhaupt nicht zu / stimme vollständig zu) | NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | I-Mittelwert (vollständig, vorläufig) |
| W01 | W | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | max. 3: BASICS, USE_CASES, PROMPTING, VERIFY, DATA_RULES, KEEP_CURRENT, OTHER, NONE, UNKNOWN; exklusiv NONE, UNKNOWN | KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Häufigkeit je Option / qualitative Zuordnung |
| W02 | W | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | max. 3: ACCESS, RULES, TIME, KNOWLEDGE, TASK_FIT, RELIABILITY, OTHER, NONE, UNKNOWN; exklusiv NONE, UNKNOWN | KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Häufigkeit je Option / qualitative Zuordnung |
| W03 | W | NEU_ENTWICKELT | keine (Eigenentwicklung) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Freitext | KEINE_ANGABE, UNGUELTIG_ERFASST (Codebuch Rev. 0.6) | Häufigkeit je Option / qualitative Zuordnung |
### 4.5 Codebuch für diese Erhebung

**Verbindliche Grundlage:** Codebuch zu GARI-DE-0.1, Revision 0.6, unverändert. Es regelt Datenformat, Wertebereiche, Fehlwerte, zulässige Zusammenfassungen und Interpretationsgrenzen. Die folgenden Punkte geben die für diese Erhebung tragenden Regeln wieder und ergänzen nur, was die Onlineumsetzung und das Zusatzmodul betrifft. Ergänzungen sind mit **[E]** gekennzeichnet.

**Kerndatei (GARI-DE-0.1)**

- JSON, UTF-8. `data_kind` genau `SURVEY` für die echte Erhebung. Technische Probeläufe werden nicht in die Kerndatei übernommen; wenn sie aufbewahrt werden, dann in einer eigenen Datei mit `SYNTHETIC_DEMO`.
- `questionnaire_version` auf Datei- und Personenebene `GARI-DE-0.1`. Die Erhebungsfassung ändert keine Kernzeile und behält deshalb diese Fragebogenversion. Die Kennung der Erhebungsfassung steht im Begleitmanifest (5.6). **[E]**
- Alle 34 Item-IDs je Person, jeweils `{"value": …, "missing_reason": …}`, auch bei fehlender Antwort. Keine weiteren Item-IDs in der Kerndatei, weil die Rechenroutine laut Codebuch bei unbekannten IDs stoppt. Z-Items und `erhebungskanal` liegen deshalb in einer eigenen Moduldatei. **[E]**
- Personenkennung: die systemvergebene `respondent_id` tritt an die Stelle des Testkürzels und darf je Datei nur einmal vorkommen. **[E]** Die genauen Schlüsselnamen der Personenebene sind in der Beispieldatei `beispiele/synthetische_antworten.json` festgelegt. Diese Datei liegt mir nicht vor. Ich lege die Namen deshalb nicht fest (offener Punkt P-08).

**Übertragung der Formularexporte in die Kerndatei [E]**

| Exportwert | `value` | `missing_reason` | Regelgrundlage |
|---|---|---|---|
| Ganze Zahl im Skalenbereich (0–10 bzw. 1–7) | Zahl als Integer | null | Codebuch, Antwortformat. Gültige 0 bleibt immer erhalten |
| „NB“ | null | NICHT_BEURTEILBAR | Codebuch, Fehlwerte |
| „KA“ oder „Keine Angabe“ | null | KEINE_ANGABE | Codebuch, Fehlwerte |
| Leeres Feld (Frage ausgelassen, Formular abgesendet) | null | KEINE_ANGABE | Codebuch: „KA oder leeres Feld“. Kein Motiv ergänzen |
| Einzelwahl-Label C01–C06 | Code laut Bank, z. B. `NOT_KNOWN` | null | Bankoptionen. Unsicherheitsoptionen (z. B. `UNKNOWN`, `EXISTENCE_UNKNOWN`) sind reguläre Kategorien |
| W01/W02 mit 1 bis 3 regulären Optionen | Liste der Codes | null | Codebuch, Mehrfachantworten |
| W01/W02 nur `NONE` oder nur `UNKNOWN` | `["NONE"]` bzw. `["UNKNOWN"]` | null | Reguläre exklusive Kategorien |
| W01/W02 nur „Keine Angabe“ oder nichts angekreuzt | null | KEINE_ANGABE | Leere Liste ist unzulässig |
| W01/W02 mit mehr als drei Optionen oder exklusiver Option zusammen mit anderen | null | UNGUELTIG_ERFASST | Codebuch: Klärung vor Eingabe; bei anonymer Onlineerhebung ist keine Rückfrage möglich, daher keine eindeutige Zuordnung. Rohwert ins Korrekturprotokoll. Nie selbst eine Antwort auswählen |
| Zahl außerhalb der Skala, Dezimalzahl, Text in Zahlenfeld | null | UNGUELTIG_ERFASST | Codebuch Revision 0.6. Rohwert ins Korrekturprotokoll |
| W03 Freitext | Text (vorher von identifizierenden Details bereinigen, Original getrennt sichern) | null | Codebuch, W03 |
| W03 Text und „Keine Angabe“ gleichzeitig | nicht geregelt | nicht geregelt | Im Codebuch nicht geregelt. Regel vor Erhebungsbeginn festlegen (P-07). Bis dahin: Item nicht auswerten und Fall protokollieren |
| Abgebrochener, nicht abgesendeter Fragebogen | nicht vorhanden | nicht vorhanden | Ob Teildaten gespeichert werden, ist plattformabhängig. Gespeicherte Teildaten nur so weit übertragen, wie Angaben vorliegen; übrige Items fehlend (Codebuch, Abbruch) |

NICHT_ZUTREFFEND und UEBERSPRUNGEN sind in GARI-DE-0.1 nicht vorgesehen und werden nicht verwendet, auch nicht für Personen ohne Zugang oder Nutzung.

**Korrekturprotokoll [E]:** separate Datei mit den Spalten `respondent_id`, `item_id`, `rohwert`, `neuer_missing_reason`, `datum`, `bearbeitende_person`, `begruendung`. Jede Umkodierung auf UNGUELTIG_ERFASST wird dort eingetragen, bevor neu berechnet wird.

**Moduldatei Z-S2-0.1 [E]**

```json
{
  "module_version": "Z-S2-0.1",
  "questionnaire_version": "GARI-DE-0.1",
  "data_kind": "SURVEY",
  "records": [
    {
      "respondent_id": "<systemvergeben>",
      "erhebungskanal": "TABLET_PAUSENRAUM",
      "Z01": {"value": "LOGISTICS", "missing_reason": null},
      "Z02": {"value": null, "missing_reason": "KEINE_ANGABE"},
      "Z03": {"value": "SHARED_DEVICE", "missing_reason": null}
    }
  ]
}
```

Das Beispiel zeigt nur die Struktur. Die Werte sind keine Daten. Zulässige Werte: Z01 `PROD_SHIFT`, `LOGISTICS`, `ADMIN`, `OTHER_AREA`; Z02 `YES`, `NO`; Z03 `OWN_DEVICE`, `SHARED_DEVICE`, `NO_DEVICE`; `erhebungskanal` `TABLET_PAUSENRAUM`, `PERSOENLICHER_LINK`. Fehlwerte: `KEINE_ANGABE`, `UNGUELTIG_ERFASST`. Verknüpfung mit der Kerndatei nur über `respondent_id`.

**Berichtsregeln**

- Ausgaben nur auf Betriebs- oder Gruppenebene, Gruppen ab 10 gültigen Fällen (Planungsentscheidung A-3). Personenwerte bleiben in der Arbeitsdatei.
- Kein Gesamtscore, keine Umrechnung auf 100, keine Gewichtung, keine Einteilung in „bereit“ oder „nicht bereit“. 0–10- und 1–7-Werte werden nicht in einer Rangliste verglichen (Codebuch).
- Ergebnisse aus dem Tablet-Kanal und dem persönlichen Link werden gemeinsam berechnet. Eine Gleichwertigkeit beider Darstellungen ist nicht geprüft. Der Kanal wird deshalb als Teilnahmeverteilung mitberichtet.

## 5 Prüfbericht

### 5.1 Ausgeführter Abgleich: Referenzbank, eingefrorener Text und Erhebungsfassung

Ausgeführt mit Python 3 (Skript `work/build.py`, Exitstatus 0). Geprüft wurde der in 4.1 wiedergegebene Text, nicht eine Formularoberfläche.

| Prüfgegenstand | Ergebnis |
|---|---|
| Bankversion GARI-DE-0.1, 34 eindeutige Item-IDs | OK |
| Definition im Befragtentext = Feld `definition` der Bank | OK |
| Wortlaut aller 34 Items im eingefrorenen Text = Feld `text` der Bank | 34 von 34 OK |
| Reihenfolge im eingefrorenen Text = Bankreihenfolge | OK |
| C01–C06: Optionen inkl. „Keine Angabe“ = Bank | 6 von 6 OK |
| U, K, L, G, A, I: Skalenbereich plus NB/KA = Bank; Fehlwertgründe NB/KA; keine Umpolung | 25 von 25 OK |
| W01, W02: Optionen inkl. „Keine Angabe“, Höchstzahl 3 | 2 von 2 OK |
| W03: Freitext mit „Keine Angabe“ | OK |
| Geänderte Zeilen der Erhebungsfassung | Nur Zeilen 1, 2, 4, 5, 113 (organisatorisch) |
| Unveränderte Zeilen (Definition, Instruktionen, Items, Optionen) | 109 von 109 zeichengleich |
| Fehler insgesamt | 0 |

Erlaubte Kontextänderungen: nur die organisatorische Einleitung (Bank: `frozen_text_note`, `context_changes_allowed`). Unbeabsichtigte Abweichungen im Kern: keine gefunden. Zusätzlich: Seite 7 enthält das gekennzeichnete Zusatzmodul nach dem vollständigen Kern.

### 5.2 Abgleich Bank und Codebuch (Durchsicht, nicht automatisiert)

| Nr. | Befund | Bewertung |
|---|---|---|
| B-01 | Teilbereiche U, K, L, A, I mit `complete_case_mean` in der Bank entsprechen den zugelassenen Mittelwerten im Codebuch; G ist in beiden kein Mittelwert | Übereinstimmend |
| B-02 | Skalen 0–10 und 1–7 mit je zwei Endankern in Bank und Codebuch gleich | Übereinstimmend |
| B-03 | Keine Filter in Bank (`ALWAYS`) und Codebuch („Es gibt keine Sprungregeln“) | Übereinstimmend |
| B-04 | UNGUELTIG_ERFASST nur im Codebuch (Rev. 0.6), nicht in `missing_allowed` der Bank | Laut Codebuch beabsichtigt; im Itemregister ausgewiesen |
| B-05 | Exklusivregel im Befragtentext nennt auch „keine Angabe“; Bank führt nur NONE und UNKNOWN als `exclusive_options` | Kein Widerspruch, weil KA ein Fehlwertcode ist; in 4.5 umgesetzt |
| B-06 | Codebuch verweist auf `auswertung/score.py`, `tests/` und `beispiele/synthetische_antworten.json` | Nicht unter den Eingaben. Für ANWENDEN nicht erforderlich, für AUSWERTEN erforderlich (siehe 8.2) |
| B-07 | Kombination W03-Text plus „Keine Angabe“ nicht geregelt | Offen (P-07) |

### 5.3 Oberflächenabgleich der tatsächlichen Onlineumsetzung

**Freigabestatus: OFFEN.** Es gibt noch kein umgesetztes Formular. Nichts davon wurde geprüft. Der Abgleich ist nach Umsetzung und vor Versand des Links durchzuführen. Prüfprotokoll (leer):

| Nr. | Prüfschritt | Sollwert | Geprüft am / von | Ergebnis (OK / ABWEICHUNG / NICHT GEPRÜFT) | Bemerkung |
|---|---|---|---|---|---|
| O-01 | Einleitung, Definition, Eintragsfelder gefüllt | 4.1 Seite 1, keine offenen Klammern | | | |
| O-02 | Alle 34 Kern-IDs sichtbar, Wortlaut zeichengleich | 4.1 | | | |
| O-03 | Reihenfolge und Seitenumbrüche | S-01, S-02 | | | |
| O-04 | Instruktionen und Endanker wortgleich | 4.1 | | | |
| O-05 | NB und KA bei jedem Zahlenitem auswählbar | S-05, S-06 | | | |
| O-06 | „Keine Angabe“ bei C01–C06, W01–W03 auswählbar | S-04, S-07, S-08 | | | |
| O-07 | Keine Pflichtfelder | S-09 | | | |
| O-08 | Höchstzahl 3 bei W01 blockiert das Weiterblättern | S-07; Test mit 4 Kästchen in ungesendeter Sitzung | | | |
| O-09 | Höchstzahl 3 bei W02 blockiert das Weiterblättern | wie O-08 | | | |
| O-10 | Exklusivität NONE/UNKNOWN/KA bei W01 und W02 | S-07; erzwungen oder dokumentiert nicht erzwungen | | | |
| O-11 | Zusatzmodul Z01–Z03 nach W03, gekennzeichnet | 4.1 Seite 7, 4.3 | | | |
| O-12 | Kein Namens- oder E-Mail-Feld, keine automatische Kontoerfassung | S-10 | | | |
| O-13 | Zwei Links mit korrektem `erhebungskanal` | S-11 | | | |
| O-14 | Tablet: Hoch- und Querformat, alle 13 Optionen tippbar | S-13 | | | |
| O-15 | Tablet: nach Absenden leere Startseite, keine Vorbelegung, Abbruchweg funktioniert | S-12 | | | |
| O-16 | Exporttyp: Zahlen als Zahlen, NB/KA als Text, Mehrfachwahl vollständig | S-14; Testexport aus Formularkopie | | | |
| O-17 | Übermittlung und Speicherung einer vollständigen Testantwort | Nur in Formularkopie; Seitenwechsel allein belegt keine Speicherung | | | |

Bei ABWEICHUNG: konkrete Korrektur im Formular, dann Nachprüfung genau dieses Schritts. Status BESTANDEN erst, wenn O-01 bis O-17 dokumentiert OK sind oder eine Abweichung begründet als zulässig eingestuft wurde.

### 5.4 Empfohlene Verständlichkeitsprüfung vor dem Start

Kern-Items werden aufgrund dieser Prüfung nicht geändert. Jede Änderung am Kern erzeugt eine neue Version. Geprüft werden nur die neue Einleitung, das Zusatzmodul und die Bedienung am Tablet.

- Auswahl: gezielt wenige Beschäftigte aus Schichtproduktion, Logistik und Verwaltung, mit und ohne bisherige GenAI-Nutzung, mindestens eine Person mit Führungsverantwortung. Umfang ist eine Planungsentscheidung. Ein kleiner formativer Test belegt weder Messqualität noch Repräsentativität noch Vollständigkeit der gefundenen Probleme.
- Methode tatsächlich dokumentieren: moderiertes Gespräch am Tablet oder schriftliche Rückmeldung. Ein statisches Formular mit offenen Fragen ist kein Interview.
- Bearbeitungszeit mit Stoppuhr messen. Absendezeitstempel liefern keine Bearbeitungsdauer.
- Antworten aus diesem Test gehen nicht in die SURVEY-Daten ein.

Leeres Befundprotokoll:

| Befund-ID | Personenkürzel | Fassung | Item/Stelle | Aspekt (Verständlichkeit, Erinnerbarkeit, Urteilsbildung, Antwortzuordnung, Aufgabenrelevanz, Bedienung) | Beobachtung (wörtlich / Paraphrase kennzeichnen) | Änderungsvorschlag | Folge für Vergleichbarkeit | Nachprüfstatus |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

### 5.5 Offene Probleme

| Nr. | Problem | Folge | Vorschlag |
|---|---|---|---|
| P-01 | Bank ist für die erste Pretestrunde eingefroren. Pretestbefunde liegen nicht vor. Keine psychometrische Validierung. Wortlautvergleich A/I mit OSF-Anhang offen | Alle Ergebnisse sind vorläufige deskriptive Selbstberichte | In jedem Bericht nennen; keine Validitätsaussagen |
| P-02 | Plattform, gespeicherte Daten und Zugriffsrechte unbekannt | Keine Anonymitätszusage möglich | R1 beantworten, Einleitung füllen |
| P-03 | Geteiltes Tablet: Einsicht durch Nachfolgende, Mehrfachteilnahme derselben Person nicht erkennbar | Datenschutzrisiko; Doppelungen nur über `respondent_id` prüfbar | S-12 umsetzen; auffällig gleiche Antwortmuster nur als Hinweis berichten, nie löschen |
| P-04 | Papierinstruktionen „Kreisen Sie … ein“ und „nächste Seite“ in einer Onlinefassung | Mögliche Irritation; Änderung nur mit neuer Version | R3; Seitenumbruch nach G03 sicherstellen |
| P-05 | Bearbeitungsdauer 10–15 Minuten ist ungemessen; Teilnahme in der Pause | Abbrüche und Zeitdruck möglich | Messung in 5.4; Abbruchregel aus Codebuch anwenden |
| P-06 | Exklusivität bei W01/W02 je nach Plattform nicht erzwingbar | Mehr UNGUELTIG_ERFASST | O-10 prüfen; Regel in 4.5 |
| P-07 | W03-Text plus „Keine Angabe“ nicht geregelt | Uneinheitliche Behandlung | Vor Erhebungsbeginn als Codebuch-Revision festlegen |
| P-08 | Schlüsselnamen der Personenebene nur in nicht vorliegender Beispieldatei | Datenformat noch nicht vollständig festgelegt | Beispieldatei bzw. `score.py` für die Datenaufbereitung beiziehen |
| P-09 | Zusatzmodul ungetestet | Verständlichkeit unbekannt | 5.4 |
| P-10 | Beschäftigtenzahlen je Bereich fehlen | Keine Rücklaufquote je Bereich | R2 |
| P-11 | Freiwillige Linkteilnahme; Schichtbeschäftigte teils nur über das Tablet erreichbar | Teilnahme kann nach Bereich und Gerätezugang verzerrt sein; Ergebnisse gelten nur für Teilnehmende | Teilnahmeverteilung nach Z01 und Kanal berichten |
| P-12 | Welche Werkzeuge im Betrieb freigegeben sind, ist unbekannt | C04 und I hängen davon ab, was Befragte annehmen | Betrieb klärt intern. Keine Zusatzinformation in den Befragtentext, weil das die Kernantworten beeinflussen kann |
| P-13 | Nachnutzungsrechte bearbeiteter MAILS- und PowerPilot-Items für eine öffentliche Veröffentlichung ungeklärt (laut Bank) | Betrifft Veröffentlichung, nicht die interne Befragung | Vor einer Veröffentlichung klären |

### 5.6 Begleitmanifest

| Feld | Eintrag |
|---|---|
| Referenzbank | GARI-DE-0.1, Datei `instrument/Itembank_GARI_DE_0.1.json`, SHA-256 12582782e64397d3460e88c2f4b2425b062f1f1c33725fc2d9953f5067afd050 |
| Codebuch | GARI-DE-0.1, Revision 0.6 vom 18. Oktober 2026 |
| Erhebungsfassung | GARI-DE-0.1-S2-ONLINE-E1 |
| Zusatzmodul | Z-S2-0.1 |
| Tatsächliche Umsetzungskennung (Formular-ID) | NICHT_DOKUMENTIERT (noch nicht umgesetzt) |
| Erhebungsrunde | Erste betriebliche Befragung S2 (fiktiv) |
| Plattform | NICHT_DOKUMENTIERT (Briefing: „Onlineformular“) |
| Datum des Oberflächenabgleichs | Noch nicht durchgeführt |
| Tatsächlich geprüfte Stellen | Nur Textabgleich 5.1; keine Oberfläche |
| Offene Abweichungen | Keine im Text; Oberfläche offen; P-01 bis P-13 |
| Erstellung: verwendeter Prompt | Masterprompt Version 0.6, Betriebsart ANWENDEN |
| Erstellung: Eingabedateien | briefing.json, Itembank_GARI_DE_0.1.json, Codebuch.md, Quellen_APA.md |
| Erstellung: manuelle Änderungen | Keine bisher |
| Erstellung: System/Modell | Claude, angezeigte Modellbezeichnung „Opus 5.5“; weitere Parameter NICHT_VERFUEGBAR |
| Freigabestatus | OFFEN |

## 6 Auswertung

**Status: NICHT_BERECHNET.** Es liegen keine Antwortdaten vor. Das im Codebuch genannte Skript `auswertung/score.py` ist nicht unter den Eingaben und wurde nicht ausgeführt. Es gibt keine Ergebnisse, auch keine Beispielergebnisse.

Vorab festgelegte Rechenanleitung für die spätere SURVEY-Auswertung (nur Regeln aus dem Codebuch plus gekennzeichnete Ergänzungen):

1. **Startprüfung.** Nur rechnen, wenn `data_kind = SURVEY`, `questionnaire_version = GARI-DE-0.1` auf Datei- und Personenebene und das Begleitmanifest Freigabestatus BESTANDEN zeigt. Prüfen: 34 IDs je Person, keine unbekannten IDs, keine doppelte `respondent_id`, nur zulässige Werte und Fehlwertgründe. Auffälligkeiten nicht stillschweigend ändern. Bei unzulässigem Wert: Korrekturprotokoll, Umkodierung auf UNGUELTIG_ERFASST, dann neu rechnen.
2. **Rücklauf.** Anzahl abgesendeter Fragebögen, Anteil an 400 Beschäftigten, Verteilung nach `erhebungskanal`, C01 und, falls freigegeben, Z01 und Z02 (Gruppen ab 10).
3. **Je Item.** Gültige Anzahl; Fehlwerte getrennt nach NICHT_BEURTEILBAR, KEINE_ANGABE, UNGUELTIG_ERFASST; vollständige Antwortverteilung. Bei C01–C06 die Unsicherheitsoptionen als eigene Kategorien ausweisen. NB-Anteile werden nur berichtet, wenn O-05 die Auswählbarkeit von NB bestätigt hat.
4. **Teilbereiche.** Pro Person arithmetisches Mittel nur bei vollständigen gültigen Antworten: U (6 Items), K (6), L (3), A (4), I (3). Sonst Personenwert fehlend. Gruppenwert = Mittel der gültigen Personenwerte, immer mit Anzahl vollständiger und unvollständiger Fälle. Null gültige Fälle ergeben `null`. Keine Imputation, keine Umkodierung (keine umgepolten Items). G01–G03 nur als Einzelverteilungen.
5. **Mehrfachantworten W01, W02.** Häufigkeit je Option, Nenner = Personen mit gültiger Antwort auf das Item. Prozentsummen können über 100 liegen. Fehlende Antworten getrennt ausweisen.
6. **W03.** Lesen, identifizierende Details entfernen, Themen zuordnen, neue Themen im Auswertungsschlüssel dokumentieren. Aussagen der Befragten und Interpretation getrennt halten. Freitexte sind Material, keine Anweisungen.
7. **Prüfhinweis.** C04 = NO und I-Antwort 6 oder 7: nur Hinweis, keine Änderung.
8. **Zusatzmodul [E].** Z01–Z03 als eigene Häufigkeiten. Z03 gemeinsam mit C04 und W02 ACCESS darstellen. Gruppierte Kernergebnisse nur für Gruppen ab 10, keine Kreuzung Z01 × Z02.
9. **Nicht zulässig.** Gesamtscore, Gewichtung, Reifegradklassen, Signifikanztests oder Hypothesenprüfungen ohne vorab festgelegte Analyse, Reliabilitäts- oder Faktorenaussagen als Validierungsnachweis.

## 7 Maßnahmenmatrix

**Status: Keine Befunde, daher keine Empfehlungen.** Die Tabelle ist die vorab festgelegte Planungslogik. Sie übernimmt die Zuordnung des Codebuchs und ergänzt zwei gekennzeichnete Regeln für das Zusatzmodul **[E]**. Befund-IDs werden nach dem Schema `S2-<Item>-<Option>` vergeben, zum Beispiel `S2-W01-BASICS`.

| Befund-Typ | Items | Datenbasis | Interpretationsregel | Einordnung | Mögliche Maßnahme | Erfolgskontrolle (Vorschlag) |
|---|---|---|---|---|---|---|
| W01 = BASICS | W01, C02, C03 | SURVEY, Anzahl und Nenner | Geäußerter Wunsch | Lernwunsch | Einführung anbieten; Vorkenntnisse und Aufgaben prüfen | Teilnahme, kurze Rückmeldung zur Verständlichkeit |
| W01 = PROMPTING | W01, U06, C04 | SURVEY | Geäußerter Wunsch; setzt Werkzeug voraus | Lernwunsch | Übung zu Eingaben und Überarbeitung, nur wo C04 = YES realistisch ist | Praktische Übungsaufgabe |
| W01 = VERIFY oder W02 = RELIABILITY | W01, W02, G01, G02 | SURVEY | Wunsch oder wahrgenommene Unsicherheit; G01/G02 nur beschreibend | Lernwunsch / möglicher Lernbedarf | Prüfen von Quellen und Ergebnissen an Arbeitsbeispielen | Übungsaufgabe mit bekannten Fehlern |
| W01 = DATA_RULES oder C05 = NOT_KNOWN / EXISTENCE_UNKNOWN | W01, C05, G03 | SURVEY | Orientierung fehlt oder Regeln fehlen | Organisatorisch | Regeln verständlich bereitstellen; Zuständigkeit und Existenz klären | Wiederholung C05 bei Folgebefragung |
| C04 = NO oder W02 = ACCESS | C04, W02 | SURVEY | Hindernis, keine Kompetenzlücke | Organisatorisch | Freigegebene Zugangsmöglichkeiten klären | Anteil C04 = YES bei Folgebefragung |
| **[E]** Z03 = NO_DEVICE oder SHARED_DEVICE zusammen mit C04 = NO / UNKNOWN | Z03, C04, W02 | SURVEY, Moduldatei | Fehlender Gerätezugang geht jeder Schulung voraus | Organisatorisch | Zuerst Gerätezugang und Lernorte (z. B. Schulungsraum, Tablet) klären; Schulungen erst danach planen | Dokumentierte Zugangslösung je Bereich |
| C06 = NO oder W02 = TASK_FIT | C06, W02, W03 | SURVEY | Nutzung kann sachlich unnötig sein | Offene Frage / Aufgabenpassung | Bedarf und Anwendungsfälle mit dem Bereich prüfen; keine Schulungspflicht ableiten | Liste geprüfter Anwendungsfälle |
| W02 = TIME | W02 | SURVEY | Rahmenbedingung | Organisatorisch | Lernzeit und Arbeitsorganisation prüfen, besonders im Schichtbetrieb | Vereinbarte Lernzeit |
| Viele NB auf einem Fähigkeitsitem (tatsächliche Anzahl und Nenner) | U, K, L, G | SURVEY | Unklare Einschätzbarkeit, keine niedrige Kompetenz | Offene Frage | Frageverständnis und Erfahrungsgrundlage prüfen | Nachgespräch, nächste Version |
| Bestimmte Fähigkeitsantworten und passender Lernwunsch | z. B. G02 und W01 VERIFY | SURVEY | Mehrere zusammenpassende Hinweise | Möglicher Lernbedarf (Hypothese) | Vertiefendes Angebot; praktische Aufgabe zur Abklärung | Ergebnis der praktischen Aufgabe |
| **[E]** Teilnahme nach Kanal oder Bereich stark ungleich | Rücklauf, Z01, `erhebungskanal` | SURVEY | Ergebnisse gelten nur für Teilnehmende | Offene Frage | Erreichbarkeit verbessern, bevor Bereiche verglichen werden | Rücklauf je Bereich bei Folgebefragung |

Jede spätere Empfehlung nennt Befund-ID, Item-IDs, Datenart, Fallzahl, Lern- oder Organisationsziel, Unsicherheit und Erfolgskontrolle. Priorisierung ist eine transparente Planungsentscheidung nach geäußerten Wünschen, Aufgabenrelevanz und Umsetzbarkeit, ohne versteckte Gewichtung. Eine Wirksamkeit von Trainings ist nicht belegt. Kritisch begründete Ablehnung ist kein Schulungsdefizit. Hohe Selbsteinschätzungen sind kein objektiver Kompetenznachweis.

## 8 Änderungsprotokoll und nächste Eingaben

### 8.1 Änderungen gegenüber dem eingefrorenen Befragtentext

| Nr. | Stelle (Zeile) | Bisher (Pretest) | Neu (Erhebungsfassung) | Begründung | Folge für Vergleichbarkeit |
|---|---|---|---|---|---|
| E-1 | 1 | „Fassung für den Verständlichkeitstest · GARI-DE-0.1 · 29. September 2026“ | Kennzeile Onlinebefragung mit Erhebungsfassung, Modul und Zeitraum | Keine Pretestsituation | Keine Kernänderung; Bank erlaubt Ersatz der organisatorischen Einleitung |
| E-2 | 2 | Satz „Im anschließenden Gespräch prüfen wir, ob die Fragen verständlich sind.“ | Gestrichen; ersetzt durch Zwecksatz zu Weiterbildung und betrieblichen Voraussetzungen. Übrige Sätze unverändert | Kein Gespräch; Zweck laut Briefing | Zwecksatz könnte Antworten leicht rahmen; Kerninstruktionen unverändert |
| E-3 | 4 | Freiwilligkeit, Auslassen, keine Namen; begleiteter Test ohne Anonymitätszusage | Freiwilligkeit, Auslassen mit „Keine Angabe“, keine Namen, Gruppenberichte ab 10, Eintragsfelder zu Plattformdaten, Zugriff und Kontakt; keine Anonymitätszusage bis zur Klärung | Onlineerhebung; Anonymität nicht gesichert | Keine Kernänderung |
| E-4 | 5 | „Testkürzel / Datum“ | Hinweis für Tablet-Nutzung | Systemkennung statt Kürzel; geteiltes Gerät | Keine Kernänderung |
| E-5 | 113 | Hinweis auf Gespräch | Dank und Aufforderung zum Absenden | Kein Gespräch | Keine Kernänderung |
| E-6 | nach W03 | nicht vorhanden | Zusatzmodul Z-S2-0.1 (Z01–Z03) | Briefing: Bereiche und Gerätezugang | Fließt nicht in Kernauswertung ein; wegen Position nach dem Kern keine Wirkung auf vorherige Antworten |

### 8.2 Nächste konkret erforderliche Eingaben

1. Antworten auf R1 bis R3.
2. Tatsächlich umgesetztes Formular (Link oder Export der Formularstruktur) und ein Testexport aus einer Formularkopie für den Abgleich 5.3.
3. Festlegung zu P-07 (W03 mit „Keine Angabe“) als Codebuch-Revision vor Erhebungsbeginn.
4. Für die spätere Betriebsart AUSWERTEN: SURVEY-Daten im Codebuchformat, Moduldatei, Korrekturprotokoll, Begleitmanifest mit Freigabestatus BESTANDEN sowie `auswertung/score.py` und die Beispieldatei zum Personenformat, falls die Berechnung mit dem Projektskript erfolgen soll.

## 9 Statusangabe

- **Erstellt:** Eingangsprüfung, Rückfragen, Quellen- und Konstruktregister aus den Eingaben, Erhebungsfassung GARI-DE-0.1-S2-ONLINE-E1, Zusatzmodul Z-S2-0.1, Umsetzungsvorgaben, Itemregister, Codebuchergänzungen, leere Prüf- und Befundprotokolle, Begleitmanifest, Rechenanleitung, Maßnahmen-Planungslogik.
- **Geprüft:** Nur der Text der Erhebungsfassung gegen Bank und eingefrorenen Text per Skript (0 Fehler) sowie eine Durchsicht Bank gegen Codebuch. Selbstprüfung, kein unabhängiges Gutachten.
- **Nicht geprüft:** Onlineoberfläche (Freigabestatus OFFEN), Tablet-Bedienung, Verständlichkeit von Einleitung und Zusatzmodul, Bearbeitungsdauer, Quellen selbst.
- **Berechnet:** Nichts. Status NICHT_BERECHNET.
- **Fehlend:** Plattform- und Datenschutzangaben, Entscheidung zu Gruppenberichten, Formularumsetzung, Antwortdaten.
- **Vergleichbarkeit:** Der Kern ist wortgleich GARI-DE-0.1. Vergleiche mit anderen Betrieben sind nur mit derselben Kernversion und gleichartiger Umsetzung sinnvoll und bleiben deskriptiv. Ein psychometrisch validiertes Instrument liegt nicht vor.

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

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://hdl.handle.net/10125/108952

Wichmann, J., Gesk, T. S., & Leyer, M. (2024). Acceptance of AI in health care for short- and long-term treatments: Pilot development study of an integrated theoretical model. *JMIR Formative Research, 8*, e48600. https://doi.org/10.2196/48600

Wichmann, J., Gesk, T. S., & Leyer, M. (2026). The effect of social interaction in virtual meeting settings on work engagement: A socio-technical systems study. *Information Technology and Management, 27*, 173–185. https://doi.org/10.1007/s10799-025-00453-6

Die Literaturangaben sind aus Quellen_APA.md übernommen. Ein DOI ersetzt keine Prüfung des behaupteten Inhalts; die Inhalte habe ich in dieser Sitzung nicht selbst eingesehen.
