# GARI-DE-0.1 im Modus ANWENDEN: Befragungsfassung für den Demonstrationsfall S1

**Laufangaben**

| Angabe | Wert |
|---|---|
| Datum | 18. Oktober 2026 |
| System und Modell | Claude; Modellkennung laut Laufumgebung `claude-opus-5-5`. Temperatur und weitere Systemparameter: NICHT_VERFUEGBAR |
| Promptversion | Masterprompt 0.5 vom 17. Oktober 2026 |
| Betriebsart | ANWENDEN (ausdrücklich angegeben) |
| Szenario | S1, `kontextart: FIKTIVE_DEMONSTRATION` |
| Referenzbank | `instrument/Itembank_GARI_DE_0.1.json`, Version GARI-DE-0.1 vom 29. September 2026, 34 Item-IDs |
| Codebuch | `instrument/Codebuch.md`, GARI-DE-0.1, Projektpaket 0.2, Stand 29. September 2026 (redaktionell fortgeschrieben am 17. Oktober 2026) |
| Quellenstand | `Quellen_APA.md`, Stand 17. Oktober 2026 |
| Fragebogenversion (Kern) | GARI-DE-0.1, unverändert |
| Erhebungsfassung (Umsetzungskennung) | S1-DEMO-ONLINE-E1 (in diesem Lauf vergeben, nur organisatorische Rahmentexte) |
| Datenart | Keine Antwortdaten vorhanden (`antwortdaten_vorhanden: false`) |
| Berechnungsstatus | NICHT_BERECHNET |
| Freigabestatus der Onlineoberfläche | OFFEN |

Gleiche Prompts garantieren keine identischen LLM-Ausgaben. Dieser Lauf ist keine unabhängige Begutachtung des Instruments.

---

## 1. Kurzbeschreibung, Annahmen und Rückfragen

### 1.1 Ziel, Zielgruppe, Kontext

**Demonstration.** Das Unternehmen ist laut Briefing fiktiv: ein Dienstleistungsbetrieb mit 40 Beschäftigten. Es gibt keine realen Daten. Alle unternehmensbezogenen Angaben in diesem Dokument stammen ausschließlich aus `briefing.json`. Weitere Unternehmensmerkmale werden nicht ergänzt.

Prüfung der Pflichtangaben aus dem Briefing (unverändert übernommen):

| Prüfpunkt | Angabe im Briefing | Folge für diesen Lauf |
|---|---|---|
| Zweck | Status quo beschreiben; Hinweise auf Weiterbildungsbedarf ableiten; betriebliche Voraussetzungen gesondert erfassen | Deckt sich mit dem Zweck von GARI-DE-0.1 (Profil plus C- und W-Fragen zu Zugang, Regeln, Hindernissen) |
| Zielpopulation | Mitarbeitende aller Tätigkeitsbereiche einschließlich Personen ohne bisherige GenAI-Nutzung | Passt: alle Fragen werden allen gezeigt, Nichtnutzung erzeugt keinen Fehlwert |
| Tätigkeitsbereiche | Verwaltung, Kundenkontakt, Operative Tätigkeit | C01 erfasst nur Büro/Bildschirm, andere Arbeit, gemischt. Keine 1:1-Zuordnung zu den drei Bereichen (siehe P-03) |
| Sprache | Deutsch | Passt |
| Bezug auf generative KI | Generative KI | Passt; Definition wird unverändert übernommen |
| Bisherige Nutzungsmöglichkeiten | Heterogene GenAI-Erfahrung; ein freigegebenes Chat-Werkzeug für Büroarbeitsplätze | Zugang ist vermutlich nicht für alle Tätigkeiten gleich. C04 und W02 = ACCESS sind daher zentral für die Interpretation |
| Zugelassene Anwendungen | Ein freigegebenes Chat-Werkzeug für Büroarbeitsplätze; Name, Funktionsumfang und Regeln: unbekannt | Unbekannt bleibt unbekannt. Kein Werkzeugname im Fragebogen (Kern unverändert) |
| Aufgabenbezug | Nicht näher angegeben | Wird über C06, W02 = TASK_FIT und W03 erhoben |
| Betrachtungszeitraum | Im Briefing nicht angegeben; im Kern festgelegt: C02 vergangene vier Wochen, A und I nächste drei Monate | Kernzeitbezüge bleiben unverändert |
| Bisherige Nutzung | Unbekannt, mit dem Fragebogen zu erheben | C02, C03 |
| Gewünschte Ausgabe | Nicht ausdrücklich angegeben; aus Betriebsart abgeleitet | Unternehmensbezogene Befragungsfassung mit unverändertem Kern |
| Art der Daten | Keine Antwortdaten; Erhebungsweg Onlineformular, Zugang über Link, freiwillig | Keine Auswertung möglich; Auswertung wird vorbereitet |

### 1.2 Getroffene Annahmen

| Nr. | Annahme | Begründung | Folge, falls falsch |
|---|---|---|---|
| AN-01 | Der Kern GARI-DE-0.1 wird unverändert übernommen; geändert werden nur organisatorische Rahmentexte (Untertitel, Einleitung, Datenschutz-/Kontakthinweis, Abschluss) | Auftrag ANWENDEN, `context_changes_allowed` und `frozen_text_note` der Bank | Jede weitere Änderung erfordert eine neue Fragebogenversion |
| AN-02 | Die organisatorische Pretest-Einleitung darf für eine Vollbefragung ersetzt werden, wenn die Erhebungsfassung gesondert gekennzeichnet ist | Wörtlich in `frozen_text_note` | Kennung S1-DEMO-ONLINE-E1 wurde vergeben |
| AN-03 | Die Befragung erfolgt mit einer noch nicht festgelegten Onlineplattform | Briefing nennt nur „Onlineformular“ | Plattformspezifischer Abgleich bleibt offen |
| AN-04 | Ergebnisse werden auf Betriebsebene berichtet; Gruppenberichte nur nach einer vorab festgelegten Mindestgröße | Codebuch: aggregierte Berichte; 40 Beschäftigte machen Untergruppen klein | Siehe Rückfrage 2 |

### 1.3 Rückfragen (höchstens drei, gebündelt)

Es besteht in diesem Lauf keine Antwortmöglichkeit. Alle ohne Antwort möglichen Teile sind unten bereits erstellt. Die Antworten verändern nur die markierten Platzhalter und den Freigabestatus, nicht den Kern.

1. **Plattform und Anonymität:** Welches Onlinewerkzeug wird verwendet, und ist bestätigt, dass es weder Name, E-Mail-Adresse, Anmeldekonto noch IP-Adresse speichert? Davon hängt ab, ob im Einleitungstext Variante A oder B eingesetzt wird. Ohne Bestätigung gilt Variante B.
2. **Gruppenberichte:** Soll außer dem Betriebsergebnis nach C01 (Büro/Bildschirm, andere Arbeit, gemischt) berichtet werden, und welche Mindestzahl gültiger Antworten pro Gruppe wird vor der Erhebung festgelegt? Bei 40 Beschäftigten und freiwilliger Teilnahme können Gruppen sehr klein werden.
3. **Betriebliche Ausgangslage für die Interpretation (nicht für den Fragebogen):** Gibt es schriftliche Regeln zur Nutzung generativer KI, wer ist zuständig, und welche Tätigkeitsgruppen haben tatsächlich Zugang zum freigegebenen Chat-Werkzeug? Diese Angaben werden nur für die spätere Einordnung von C04, C05 und W02 gebraucht. Im fiktiven Fall bleiben sie unbekannt und werden nicht erfunden.

---

## 2. Quellen- und Konstruktregister mit Evidenzgrenzen

### 2.1 Quellenregister (für den eingesetzten Kern)

Grundlage sind `source_register` der Bank und `Quellen_APA.md`. In diesem Lauf wurden keine Originalquellen erneut eingesehen. Die Spalte „Prüfstand“ gibt den dokumentierten Stand des Projekts wieder, nicht eine Prüfung in diesem Lauf.

| Quellen-ID | Nachweis (APA) | Dokumentierter Prüfstand | Fundstelle | Zielgruppe der Quelle | Sprache | Konstrukt / Instrument | Zugang | Grenzen |
|---|---|---|---|---|---|---|---|---|
| MAILS_DE_2023 | Carolus, Koch, Straka, Latoschik und Wienrich (2023); deutscher Autorenfragebogen (Download Universität Würzburg) | Publizierter Autoren-Volltext und deutscher Originalfragebogen (34 Items, 3 Seiten) laut Projektdokumentation geprüft | Items 1–6 (Anwenden), 7–12 (Verstehen), 26–28 (Lernen), Seiten 1–2; Zuordnung und Mittelwertregel Seite 3 | 300 deutschsprachige Erwachsene | Deutsch | KI-Kompetenz-Selbstbericht (MAILS) | Vollständig | Evidenz betrifft allgemeine KI und Selbstberichte. Eingrenzung auf generative KI, Arbeitskontext, Kürzung und NB/KA sind Anpassungen; keine Übertragung des Validierungsstatus. Lizenz für öffentliche bearbeitete Fassungen ungeklärt |
| POWERPILOT_2025 | Wichmann, Behn, Degirmenci, Leyer und Barros (2025), HICSS-58, S. 961–970 | Paper und bereitgestellte Itemsammlung (Datensatz_v1.docx, Questionnaire 2 / PowerPilot) | Attitude Items 1–4; Intention to use Items 1–3 | Laut Quellenstatus Energie-Monitoring-Anwendungen, Deutschland; Details zur Stichprobe in diesem Lauf nicht eingesehen | Englisch | Einstellung und Nutzungsabsicht (RAA-Bezug) | Paper vollständig; Itemwortlaut nur über Itemsammlung | **Der direkte Vergleich mit dem OSF-Anhang (doi 10.17605/OSF.IO/GEBK9) bleibt offen**; Anhang am 29.09. und 17.10.2026 nicht abrufbar. Kontextwechsel von Energie-App zu GenAI ist eine inhaltliche Anpassung |
| Q-AJZEN | Ajzen (o. J.), Constructing a TPB questionnaire | Siebenseitiges Originaldokument eingesehen | Ganzes Dokument | Methodenanleitung | Englisch | Verhaltensdefinition über Ziel, Handlung, Kontext, Zeit | Vollständig | Begründet die Spezifizierung von A und I (berufliche Aufgaben, drei Monate), nicht deren Validität |
| Q-PEFFERS | Peffers, Tuunanen, Rothenberger und Chatterjee (2007) | Abschnitte zu den sechs Aktivitäten im Volltext geprüft | Methodenteil | Methodenartikel | Englisch | DSR-Vorgehen | Auszugsweise vertieft | Entwicklungsmethode, kein Messinstrument |
| Q-KOCH | Koch, Carolus, Wienrich und Latoschik (2024) | Volltext, Abschnitte 2.1 und 3.4 | Abschnitte 2.1, 3.4 | In diesem Lauf nicht eingesehen | Englisch | MAILS-Kurzfassung | Auszugsweise | Kurzfassung nicht eingesetzt, weil sie KI-Entwicklung enthält; fordert weitere Validierung |

Eigenentwicklungen ohne Quelle: C01–C06, G01–G03, W01–W03 (12 Items, Status NEU_ENTWICKELT).

**Grenze, die auch bei jedem erneuten Einsatz anzugeben ist:** POWERPILOT_2025 ist anhand der bereitgestellten Itemsammlung geprüft; der direkte Vergleich mit dem OSF-Anhang bleibt offen. Es liegt weder eine vollständige Primärquellenprüfung aller Items noch eine psychometrische Validierung der Kombination vor.

### 2.2 Konstruktmatrix (übernommen, nicht neu entwickelt)

| Bereich | Definition im Projekt | Diagnosezweck | Grundlage | Items | Zusammenfassung | Ebene | Überschneidungen / Hinweise |
|---|---|---|---|---|---|---|---|
| C | Tätigkeit, Nutzung, Zugang, Regelkenntnis, Aufgabenrelevanz | Kontext und betriebliche Voraussetzungen | Eigenentwicklung | C01–C06 | Jede Frage einzeln | Berichtetes Verhalten (C02, C03), wahrgenommene betriebliche Bedingungen (C04, C05), Aufgabeneinschätzung (C06) | Trennt fehlenden Zugang von Fähigkeit |
| U | Selbst eingeschätzte Anwendung | Selbsteinschätzung der Nutzungsfähigkeit | MAILS (Anwenden) | U01–U06 | Vorläufiger Mittelwert U | Persönliche Voraussetzung, Selbsteinschätzung | Kein objektiver Leistungstest |
| K | Selbst eingeschätztes Verständnis | Selbsteinschätzung von Wissen und Bewertung | MAILS (Verstehen) | K01–K06 | Vorläufiger Mittelwert K | Persönliche Voraussetzung, Selbsteinschätzung | K03/K04 inhaltlich nahe beieinander |
| L | Zutrauen in das eigene Lernen | Lernbezogene Selbstwirksamkeit | MAILS (Lernen) | L01–L03 | Vorläufiger Mittelwert L | Persönliche Voraussetzung, Selbsteinschätzung | Nahe an W01 = KEEP_CURRENT, aber anderer Gegenstand (Fähigkeit vs. Wunsch) |
| G | Prüfen von Ergebnissen und zulässigen Eingaben | Verantwortlicher Umgang | Eigenentwicklung | G01–G03 | Drei Einzelitems, kein Mittelwert | Selbsteinschätzung | G03 hängt mit C05 zusammen (Regelkenntnis) |
| A | Einstellung zur arbeitsbezogenen Nutzung | Bewertung der Nutzung | RAA über POWERPILOT_2025; Ajzen | A01–A04 | Vorläufiger Mittelwert A | Einstellung | Bedingte Bewertung, keine Absicht |
| I | Absicht unter tatsächlich erwarteten Bedingungen | Nutzungsabsicht | RAA über POWERPILOT_2025; Ajzen | I01–I03 | Vorläufiger Mittelwert I | Absicht | Ausdrücklich keine hypothetische Bereitschaft bei garantiertem Zugang; Prüfhinweis bei C04 = NO und I ≥ 6 |
| W | Weiterbildungswünsche, Hindernisse, konkrete Aufgabe | Lernwunsch und Hindernisse | Eigenentwicklung | W01–W03 | Häufigkeiten bzw. qualitative Zuordnung | Lernwunsch, wahrgenommene Hindernisse | Grundlage der Maßnahmenmatrix |

Kein Gesamtwert über alle Bereiche, keine Werte für C, G und W, keine Gewichtung, keine Reifegradklasse.

---

## 3. Befragungsfassung, Itemregister und Codebuch

### 3.1 Abgleich mit der eingefrorenen Bank (ausgeführt)

Der Abgleich wurde mit Python 3 auf `instrument/Itembank_GARI_DE_0.1.json` ausgeführt (Exitstatus 0). Geprüft wurde die Bank gegen ihren eigenen eingefrorenen Teilnehmendentext und die erzeugte Befragungsfassung gegen beide.

| Prüfung | Ergebnis |
|---|---|
| Anzahl Item-IDs / eindeutig | 34 / ja |
| Jede ID genau einmal im eingefrorenen Text | ja |
| Reihenfolge Bank = Reihenfolge Text | ja |
| Itemwortlaut Bank = Text | ja, 34 von 34 |
| Antwortoptionen einschließlich KA bzw. NB/KA | ja, für alle 34 Items |
| Fehlwertgründe: numerisch NICHT_BEURTEILBAR und KEINE_ANGABE, sonst nur KEINE_ANGABE; kein NICHT_ZUTREFFEND, kein UEBERSPRUNGEN | ja |
| `display_if` = ALWAYS, keine Umkodierung, Rolle FESTER_KERN, Version GARI-DE-0.1 | ja, alle 34 |
| Teilbereiche U, K, L, A, I plus `not_a_scale` decken genau die 34 IDs ab | ja |
| Definition generativer KI identisch | ja |
| Status | 22 ADAPTIERT, 12 NEU_ENTWICKELT; kein ORIGINAL |
| Befragungsfassung S1-DEMO-ONLINE-E1: unveränderte Kernzeilen | 109 von 114 Textzeilen identisch und in gleicher Reihenfolge |

**Ersetzte Zeilen (nur organisatorischer Rahmen):**

| Zeile im eingefrorenen Text | Bisher | Neu | Begründung |
|---|---|---|---|
| Untertitel | „Fassung für den Verständlichkeitstest · GARI-DE-0.1 · 29. September 2026“ | „Onlinebefragung · Fragebogen GARI-DE-0.1 · Erhebungsfassung S1-DEMO-ONLINE-E1 · fiktive Demonstration“ | Kennzeichnung der Erhebungsfassung |
| Einleitung | Verwies auf das anschließende Gespräch im Pretest | Zweck der Befragung, Berichtsebene, kein Leistungsbezug, unveränderte Dauerangabe 10 bis 15 Minuten | Gespräch findet nicht statt; Briefing-Zweck |
| Freiwilligkeit/Anonymität | „…den Test beenden… Beim begleiteten Test kennt die durchführende Person Sie…“ | „…die Befragung beenden…“ plus Platzhalter für geprüfte Anonymitätsaussage und Kontaktstelle | Begleiteter Test entfällt; Anonymität darf nur nach Prüfung zugesagt werden |
| Testkürzel/Datum | Eintragungsfelder | entfernt | Online nicht nötig; keine Personenkennungen erfragen |
| Abschluss | Hinweis auf das Gespräch | Dank und Hinweis auf Absenden | Gespräch entfällt |

Unverändert bleiben insbesondere: Definition, alle Abschnittsinstruktionen, Endanker, NB/KA-Hinweise, der Satz „Sie können einzelne Fragen auslassen“ (konsistent mit KA in jeder Frage), der Seitenhinweis vor dem Skalenwechsel und die Regeln zu W01/W02.

**Kontrollierte Platzhalter:** Die Bank weist ausdrücklich nur „Kontaktangaben und organisatorischer Erhebungshinweis außerhalb des Fragebogens“ als zulässige Kontextänderung aus. Die eckigen Klammern in der Einleitung (Mindestgruppengröße, Anonymitätsvariante, Kontaktstelle) fallen darunter. Sie müssen vor dem Versand ausgefüllt sein.

### 3.2 Befragungsfassung für Befragte (Erhebungsfassung S1-DEMO-ONLINE-E1)

> **Demonstration mit fiktivem Unternehmen.** Kern: GARI-DE-0.1, unverändert. Darstellung hier als Text; die Umsetzung im Onlinewerkzeug muss nach Abschnitt 4.2 abgeglichen werden. Die Zeilen „Antwortoptionen:“ zeigen die anzubietenden Auswahlmöglichkeiten; jede Option muss im Formular einzeln auswählbar sein.

### Fragebogen zum Umgang mit generativer KI

Onlinebefragung · Fragebogen GARI-DE-0.1 · Erhebungsfassung S1-DEMO-ONLINE-E1 · fiktive Demonstration

Dieser Fragebogen erfasst Ihre Erfahrungen, Einschätzungen und Weiterbildungswünsche zu generativer KI bei der Arbeit. Die Ergebnisse sollen zeigen, wo Weiterbildung sinnvoll sein kann und welche betrieblichen Voraussetzungen, etwa Zugang oder verständliche Regeln, noch fehlen. Berichtet werden nur zusammengefasste Ergebnisse für den gesamten Betrieb und gegebenenfalls für Gruppen mit mindestens [Mindestgruppengröße festlegen] Antworten, nicht für einzelne Personen. Es geht nicht um die Bewertung Ihrer Arbeitsleistung. Geschätzte Dauer: 10 bis 15 Minuten.

Generative KI erzeugt oder bearbeitet auf Eingaben hin Inhalte, zum Beispiel Texte, Bilder, Audio, Videos oder Programmcode. Gemeint sind sowohl eigenständige Anwendungen als auch entsprechende Funktionen in anderen Programmen.

Die Teilnahme ist freiwillig. Sie können einzelne Fragen auslassen oder die Befragung beenden. Bitte tragen Sie keine Namen, Personalnummern oder vertraulichen Informationen ein.

[VOR FREIGABE EINE DER BEIDEN FASSUNGEN EINSETZEN, je nach geprüfter Einstellung des Befragungswerkzeugs. Variante A, nur wenn technisch und organisatorisch bestätigt: „Das Befragungswerkzeug speichert weder Ihren Namen noch Ihre E-Mail-Adresse.“ Variante B: „Eine vollständige Anonymität kann nicht zugesagt werden, weil [konkreten Grund eintragen]. Ihre Antworten werden nur zusammengefasst ausgewertet.“]

Bei Fragen zur Befragung: [Kontaktstelle eintragen].

#### Ihre Tätigkeit und bisherige Nutzung

Bitte wählen Sie pro Frage genau eine Antwort.

**C01**  Wie sieht Ihre hauptsächliche Tätigkeit aus?

Antwortoptionen: Überwiegend Büro- oder Bildschirmarbeit · Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst · Etwa gleich große Anteile beider Bereiche · Keine Angabe

**C02**  An wie vielen Tagen haben Sie in den vergangenen vier Wochen generative KI für berufliche Aufgaben genutzt?

Antwortoptionen: An keinem Tag · An 1 bis 3 Tagen · An 4 bis 9 Tagen · An 10 bis 15 Tagen · An 16 oder mehr Tagen · Kann ich nicht einschätzen · Keine Angabe

**C03**  Haben Sie generative KI schon einmal außerhalb Ihrer Arbeit selbst genutzt?

Antwortoptionen: Ja · Nein · Ich bin mir nicht sicher · Keine Angabe

**C04**  Haben Sie aktuell Zugang zu einer generativen KI, die Sie für Ihre Arbeit nutzen dürfen?

Antwortoptionen: Ja · Nein · Ich weiß es nicht · Keine Angabe

**C05**  Kennen Sie die betrieblichen Regeln für den Einsatz generativer KI bei Ihrer Arbeit?

Antwortoptionen: Ja · Teilweise · Nein · Ich weiß nicht, ob es solche Regeln gibt · Keine Angabe

**C06**  Gibt es in Ihrem Aufgabenbereich Tätigkeiten, für die generative KI aus Ihrer Sicht sinnvoll wäre?

Antwortoptionen: Ja · Nein · Kann ich noch nicht beurteilen · Keine Angabe

#### Anwendung und Verständnis

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**U01**  Ich kann eine generative KI bedienen.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**U02**  Ich kann mir berufliche Aufgaben durch generative KI erleichtern.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**U03**  Ich kann generative KI gezielt für meine Arbeitsziele einsetzen.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**U04**  Ich kann die Zusammenarbeit mit generativer KI so gestalten, dass sie meine Arbeit vereinfacht.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**U05**  Ich kann mit generativer KI zu brauchbaren Arbeitsergebnissen kommen.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**U06**  Ich kann generativer KI verständlich mitteilen, was ich brauche.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**K01**  Ich kenne die zentralen Konzepte generativer KI.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**K02**  Ich kann erklären, was generative KI bedeutet.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**K03**  Ich kann Chancen und Grenzen generativer KI einschätzen.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**K04**  Ich kann Vor- und Nachteile generativer KI beurteilen.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**K05**  Ich kann mir neue Einsatzmöglichkeiten für generative KI überlegen.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**K06**  Ich kann mir künftige Anwendungen generativer KI vorstellen.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

#### Lernen und Prüfen

Wie stark sind Ihre Fähigkeiten derzeit ausgeprägt? Kreisen Sie pro Aussage eine Zahl ein. Auch ohne bisherige Nutzung dürfen Sie sich einschätzen.

0 = gar nicht oder kaum ausgeprägt   ·   10 = sehr gut oder (nahezu) perfekt ausgeprägt

NB = nicht beurteilbar   ·   KA = keine Angabe. Verwenden Sie NB, wenn Ihnen eine Grundlage für die Einschätzung fehlt. 0 ist eine tatsächliche Fähigkeitseinschätzung.

**L01**  Ich kann bei den schnellen Veränderungen generativer KI auf dem Laufenden bleiben.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**L02**  Ich kann mich über Neuerungen bei generativer KI informieren.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**L03**  Ich kann mein Wissen und Können trotz neuer generativer KI-Anwendungen aktuell halten.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**G01**  Ich kann erkennen, wann ich eine Antwort generativer KI mit einer unabhängigen Quelle überprüfen muss.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**G02**  Ich kann überprüfen, ob die von generativer KI genannten Quellen die behaupteten Aussagen tatsächlich belegen.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

**G03**  Ich kann beurteilen, welche Informationen ich in eine generative KI eingeben darf.

Antwortoptionen: 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · NB · KA

*Bitte fahren Sie auf der nächsten Seite fort. Dort wechselt die Antwortskala.*

--- *Seitenumbruch im Onlineformular* ---

#### Einstellung und geplante Nutzung

Wie sehr stimmen Sie den folgenden Aussagen zu? Gemeint ist die Nutzung für Ihre beruflichen Aufgaben in den kommenden drei Monaten. „Freigegeben“ bedeutet, dass Ihr Unternehmen die betreffende Nutzung erlaubt.

1 = stimme überhaupt nicht zu   ·   7 = stimme vollständig zu

NB = nicht beurteilbar   ·   KA = keine Angabe. Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein.

**A01**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich vorteilhaft.

Antwortoptionen: 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA

**A02**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich zufriedenstellend.

Antwortoptionen: 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA

**A03**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich wichtig.

Antwortoptionen: 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA

**A04**  Die Nutzung freigegebener generativer KI für meine beruflichen Aufgaben in den nächsten drei Monaten wäre für mich angenehm.

Antwortoptionen: 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA

Für die folgenden drei Aussagen: Denken Sie an die Bedingungen, die Sie in den nächsten drei Monaten tatsächlich erwarten. Setzen Sie keinen gesicherten Zugang voraus, wenn dieser unklar ist. Fehlender Zugang bedeutet jedoch nicht automatisch, dass Sie nicht antworten können.

**I01**  Ich plane, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

Antwortoptionen: 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA

**I02**  Ich habe die Absicht, in den nächsten drei Monaten freigegebene generative KI für meine beruflichen Aufgaben zu nutzen.

Antwortoptionen: 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA

**I03**  Ich werde in den nächsten drei Monaten auf jeden Fall freigegebene generative KI für meine beruflichen Aufgaben nutzen.

Antwortoptionen: 1 · 2 · 3 · 4 · 5 · 6 · 7 · NB · KA

#### Weiterbildung und Unterstützung

Bei W01 und W02 sind jeweils höchstens drei Antworten möglich. „Kein Weiterbildungswunsch“, „derzeit nichts“, „kann ich noch nicht einschätzen“ und „keine Angabe“ dürfen innerhalb einer Frage nur allein gewählt werden.

**W01**  Zu welchen Themen wünschen Sie sich derzeit Weiterbildung? Bitte höchstens drei Themen auswählen.

- Grundlagen generativer KI

- Passende Einsatzmöglichkeiten für meine Aufgaben

- Klare Eingaben formulieren und Ergebnisse verbessern

- Antworten und Quellen überprüfen

- Betriebliche Regeln und zulässige Dateneingaben

- Bei neuen Entwicklungen auf dem Laufenden bleiben

- Anderes Thema

- Derzeit kein Weiterbildungswunsch

- Ich kann meinen Bedarf noch nicht einschätzen

- Keine Angabe

**W02**  Was erschwert Ihnen derzeit den sinnvollen Einsatz generativer KI bei der Arbeit? Bitte höchstens drei Antworten auswählen.

- Kein Zugang zu einem freigegebenen Werkzeug

- Unklare betriebliche Regeln

- Zu wenig Zeit zum Ausprobieren oder Lernen

- Mir fehlt Wissen über die Nutzung

- Ich erkenne keinen passenden Einsatz für meine Aufgaben

- Unsicherheit über die Verlässlichkeit der Ergebnisse

- Etwas anderes

- Derzeit nichts

- Kann ich noch nicht einschätzen

- Keine Angabe

**W03**  Welche konkrete berufliche Aufgabe würden Sie gerne mit generativer KI bearbeiten lernen? Hier können Sie auch „Anderes“ aus W01 oder W02 erläutern. Bitte keine Namen oder vertraulichen Informationen nennen.

- Keine Angabe

*[Freitextfeld]*

Vielen Dank für Ihre Teilnahme. Mit dem Absenden werden Ihre Antworten übermittelt.
### 3.3 Wissenschaftliches Itemregister GARI-DE-0.1 (Begleitdokumentation, nicht für Befragte)

Alle 34 Items: Rolle FESTER_KERN, Anzeige ALWAYS für alle Personen und alle Tätigkeitsbereiche, Version GARI-DE-0.1, Prüfstatus „im Projekt noch nicht empirisch geprüft“ (Pretest R1–R3 ist explorativ und kein Validitätsnachweis). Höhere Zahlen bedeuten höhere Selbsteinschätzung bzw. Zustimmung. Bei den MAILS-Items ist der Originalwortlaut laut Bank am Dokument geprüft und wird über die Fundstelle referenziert, nicht abgedruckt (Rechte für öffentliche Wiedergabe ungeklärt). Der deutsche Befragungswortlaut steht unverändert in 3.2.

| ID | Dim. | Status | Quelle und Fundstelle | Originalwortlaut | Änderung | Skala/Optionen | Fehlwerte | Richtung | Evidenz |
|---|---|---|---|---|---|---|---|---|---|
| C01 | C | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | OFFICE = Überwiegend Büro- oder Bildschirmarbeit; OTHER_WORK = Überwiegend andere Arbeit, zum Beispiel Produktion, Service oder Außendienst; MIXED = Etwa gleich große Anteile beider Bereiche | KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| C02 | C | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | D0 = An keinem Tag; D1_3 = An 1 bis 3 Tagen; D4_9 = An 4 bis 9 Tagen; D10_15 = An 10 bis 15 Tagen; D16_PLUS = An 16 oder mehr Tagen; UNKNOWN = Kann ich nicht einschätzen | KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| C03 | C | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | YES = Ja; NO = Nein; UNKNOWN = Ich bin mir nicht sicher | KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| C04 | C | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | YES = Ja; NO = Nein; UNKNOWN = Ich weiß es nicht | KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| C05 | C | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | KNOWN = Ja; PARTLY = Teilweise; NOT_KNOWN = Nein; EXISTENCE_UNKNOWN = Ich weiß nicht, ob es solche Regeln gibt | KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| C06 | C | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | YES = Ja; NO = Nein; UNKNOWN = Kann ich noch nicht beurteilen | KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| U01 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 1, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | KI-Bezug auf generative KI eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| U02 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 2, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Erleichterung des Lebens auf berufliche Aufgaben eingegrenzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| U03 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 3, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Zielbezug auf Arbeitsziele eingegrenzt; sinnvoll durch gezielt konkretisiert. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| U04 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 4, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Alltagsinteraktion auf Zusammenarbeit bei der Arbeit übertragen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| U05 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 5, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Gewinnbringende Zusammenarbeit über brauchbare Arbeitsergebnisse konkretisiert; Bedeutungsverschiebung im Pretest prüfen. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| U06 | U | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 6, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Gewinnbringende Kommunikation über verständliches Mitteilen konkretisiert; Ergebnisaspekt verengt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K01 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 7, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Allgemeine KI auf generative KI eingegrenzt; Konzepte bleibt bewusst zur Verständlichkeitsprüfung erhalten. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K02 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 8, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Kenntnis von Definitionen in selbst eingeschätzte Erklärfähigkeit übertragen; stärkere Anpassung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K03 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 9, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K04 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 10, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Gegenstand eingegrenzt; Satz vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K05 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 11, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Gegenstand eingegrenzt; Verwendungszwecke sprachlich vereinfacht. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| K06 | K | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 12, Seite 1; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Gegenstand eingegrenzt; Satz verkürzt. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| L01 | L | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 26, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Gegenstand eingegrenzt; stets entfällt. Deutsche Itemnummer 26 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| L02 | L | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 27, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Gegenstand eingegrenzt; deutsche Itemnummer 27 verwenden. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| L03 | L | ADAPTIERT | MAILS_DE_2023; Deutscher Autorenfragebogen, Item 28, Seite 2; Zuordnung und Mittelwertregel Seite 3. | Am Dokument geprüft, über Fundstelle referenziert, hier nicht wiedergegeben | Gegenstand eingegrenzt; sprachliche Verdichtung. Zusätzlich: Nicht beurteilbar und Keine Angabe ergänzt; Originalanker beibehalten. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original: Ganzzahlen 0–10; zwei Endanker, keine Zwischenanker. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| G01 | G | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original:  | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| G02 | G | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original:  | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| G03 | G | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | ABILITY_0_10: 0–10 ganzzahlig; 0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker. Original:  | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| A01 | A | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | The use of PowerPilot would be … advantageous. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | AGREEMENT_1_7: 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| A02 | A | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | The use of PowerPilot would be … satisfactory. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | AGREEMENT_1_7: 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| A03 | A | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | The use of PowerPilot would be … important. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | AGREEMENT_1_7: 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| A04 | A | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 2 – Attitude, Item 4; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | The use of PowerPilot would be … enjoyable. | Englisch ins Deutsche übertragen; PowerPilot durch freigegebene generative KI ersetzt; berufliche Aufgaben und Zeitraum drei Monate ergänzt. Zusätzliche Fehlwertoptionen. Einstellung bleibt bedingte Bewertung, keine tatsächliche Nutzungsabsicht. | AGREEMENT_1_7: 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| I01 | I | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 1; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | I plan to use PowerPilot in the future. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | AGREEMENT_1_7: 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| I02 | I | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 2; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | I intend to use PowerPilot in the future. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | AGREEMENT_1_7: 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| I03 | I | ADAPTIERT | POWERPILOT_2025; Datensatz_v1.docx, Questionnaire 2 / PowerPilot, 1 – Intention to use, Item 3; Paper Fragebogen 2.pdf, Messmodell und Verweis auf Online-Anhang. Grenze: Itemwortlaut aus bereitgestellter Itemsammlung; dortige Zuordnung mit Paper abgeglichen. Original-Online-Anhang OSF GEBK9 am 29.09.2026 nicht abrufbar; direkte Gleichheit mit dessen Fassung bleibt offen. | I will definitely use PowerPilot in the future. | Englisch ins Deutsche übertragen; Technologie, Arbeitskontext und Zeitraum drei Monate spezifiziert. Tatsächlich erwartete Bedingungen, kein hypothetisch garantierter Zugang. Zusätzliche Fehlwertoptionen. | AGREEMENT_1_7: 1–7 ganzzahlig; 1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker. Original: Siebenstufige Zustimmung; Endanker strongly disagree / totally agree laut bereitgestellter Itemsammlung. | NICHT_BEURTEILBAR, KEINE_ANGABE | keine Umkodierung | Adaptierte Selbstberichtsfassung; im Projekt noch nicht empirisch geprüft. |
| W01 | W | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | BASICS = Grundlagen generativer KI; USE_CASES = Passende Einsatzmöglichkeiten für meine Aufgaben; PROMPTING = Klare Eingaben formulieren und Ergebnisse verbessern; VERIFY = Antworten und Quellen überprüfen; DATA_RULES = Betriebliche Regeln und zulässige Dateneingaben; KEEP_CURRENT = Bei neuen Entwicklungen auf dem Laufenden bleiben; OTHER = Anderes Thema; NONE = Derzeit kein Weiterbildungswunsch; UNKNOWN = Ich kann meinen Bedarf noch nicht einschätzen. Höchstens 3; exklusiv: NONE, UNKNOWN | KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| W02 | W | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | ACCESS = Kein Zugang zu einem freigegebenen Werkzeug; RULES = Unklare betriebliche Regeln; TIME = Zu wenig Zeit zum Ausprobieren oder Lernen; KNOWLEDGE = Mir fehlt Wissen über die Nutzung; TASK_FIT = Ich erkenne keinen passenden Einsatz für meine Aufgaben; RELIABILITY = Unsicherheit über die Verlässlichkeit der Ergebnisse; OTHER = Etwas anderes; NONE = Derzeit nichts; UNKNOWN = Kann ich noch nicht einschätzen. Höchstens 3; exklusiv: NONE, UNKNOWN | KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |
| W03 | W | NEU_ENTWICKELT | Eigenentwicklung, keine Quelle | Entfällt (NEU_ENTWICKELT) | Eigenes Einzelitem für den Projektzweck; keine etablierte Skala. | Freitext | KEINE_ANGABE | keine Umkodierung | Noch nicht empirisch geprüft. |

### 3.4 Codebuch für die Erhebungsfassung S1-DEMO-ONLINE-E1

Das Codebuch GARI-DE-0.1 gilt unverändert. Es wird hier für diese Erhebung vollständig in seinen anwendungsrelevanten Regeln wiedergegeben und um die für die Onlineumsetzung nötigen Begleitfelder ergänzt. Die Ergänzungen sind als solche gekennzeichnet und ändern keine Rechenregel.

**Datenformat.** JSON, UTF-8. Pflichtfelder auf Dateiebene: `data_kind` (genau PRETEST, SURVEY oder SYNTHETIC_DEMO) und `questionnaire_version` = `GARI-DE-0.1`. Auf Personenebene: `questionnaire_version` = `GARI-DE-0.1`, ein je Datei eindeutiges Kürzel (zufällig vergeben, keine Personalnummer, kein Name) und alle 34 Item-IDs, auch bei fehlender Antwort. Jede Antwort hat die Felder `value` und `missing_reason`.

**Ergänzende Begleitfelder (Erhebungsmanifest, außerhalb der Rechendatei; Ergänzung dieses Laufs):** `erhebungsfassung` = S1-DEMO-ONLINE-E1, `plattform`, `oberflaechenabgleich_datum`, `oberflaechenabgleich_status` (BESTANDEN, OFFEN, ABWEICHUNG). Ob `score.py` zusätzliche Felder in der Eingabedatei akzeptiert, ist in diesem Lauf nicht geprüft (Skript nicht beigefügt). Deshalb gehören sie in das separate Manifest.

**Datenart für diesen Fall:** Echte Antworten von Beschäftigten eines realen Betriebs wären SURVEY. Da S1 fiktiv ist, sind alle Daten, die für diese Demonstration erzeugt würden, ausschließlich SYNTHETIC_DEMO. Ein synthetisches Rechenergebnis darf nie als Befragungsergebnis berichtet werden.

**Wertebereiche und Labels**

| Items | Typ | Zulässige Werte (`value`) | Zulässige `missing_reason` |
|---|---|---|---|
| C01 | Einzelwahl | OFFICE, OTHER_WORK, MIXED | KEINE_ANGABE |
| C02 | Einzelwahl | D0, D1_3, D4_9, D10_15, D16_PLUS, UNKNOWN | KEINE_ANGABE |
| C03 | Einzelwahl | YES, NO, UNKNOWN | KEINE_ANGABE |
| C04 | Einzelwahl | YES, NO, UNKNOWN | KEINE_ANGABE |
| C05 | Einzelwahl | KNOWN, PARTLY, NOT_KNOWN, EXISTENCE_UNKNOWN | KEINE_ANGABE |
| C06 | Einzelwahl | YES, NO, UNKNOWN | KEINE_ANGABE |
| U01–U06, K01–K06, L01–L03, G01–G03 | Ganzzahl | 0 bis 10 (0 = gar nicht oder kaum ausgeprägt; 10 = sehr gut oder (nahezu) perfekt ausgeprägt; keine Zwischenanker) | NICHT_BEURTEILBAR, KEINE_ANGABE |
| A01–A04, I01–I03 | Ganzzahl | 1 bis 7 (1 = stimme überhaupt nicht zu; 7 = stimme vollständig zu; keine Zwischenanker) | NICHT_BEURTEILBAR, KEINE_ANGABE |
| W01 | Mehrfachwahl, Liste | BASICS, USE_CASES, PROMPTING, VERIFY, DATA_RULES, KEEP_CURRENT, OTHER, NONE, UNKNOWN; 1 bis 3 Einträge; NONE und UNKNOWN nur allein | KEINE_ANGABE |
| W02 | Mehrfachwahl, Liste | ACCESS, RULES, TIME, KNOWLEDGE, TASK_FIT, RELIABILITY, OTHER, NONE, UNKNOWN; 1 bis 3 Einträge; NONE und UNKNOWN nur allein | KEINE_ANGABE |
| W03 | Freitext | Zeichenkette | KEINE_ANGABE |

Labels der Einzelwahl- und Mehrfachwahlcodes: siehe Itemregister 3.3.

**Fehlwerte**

- NB bei numerischen Fragen: `value: null`, `missing_reason: "NICHT_BEURTEILBAR"`.
- KA oder leeres Feld: `value: null`, `missing_reason: "KEINE_ANGABE"`. Motive werden nicht ergänzt.
- Null ist bei 0–10 ein gültiger Skalenwert und nie ein Fehlwertcode. Gültige 0-Antworten bleiben stets erhalten.
- Unsicherheitsoptionen in C01–C06 (z. B. UNKNOWN, EXISTENCE_UNKNOWN) sind reguläre Antwortkategorien und werden mitgezählt und ausgewiesen.
- W01/W02: NONE und UNKNOWN sind reguläre, exklusive Kategorien. Eine leere Liste ist unzulässig und bedeutet nicht „keine Wünsche“.
- NICHT_ZUTREFFEND und UEBERSPRUNGEN sind in GARI-DE-0.1 nicht erlaubt (keine Filter; alle Fragen für alle).
- Mehrfachmarkierung bei Einzelwahl, mehr als drei Antworten bei W01/W02 oder exklusive Option zusammen mit anderen: vor Eingabe klären. Ist keine eindeutige Zuordnung möglich, KEINE_ANGABE und Vermerk im Korrekturprotokoll. Nie selbst eine Antwort auswählen.
- Abgebrochene Formulare: nur tatsächlich vorliegende Angaben übertragen, übrige Items KEINE_ANGABE.
- Nichtnutzung (C02 = D0, C03 = NO) erzeugt keinen Fehlwert und setzt Fähigkeitswerte nicht auf null.

**Zugelassene Zusammenfassungen**

| Teilbereich | Items | Bereich | Regel |
|---|---|---|---|
| U | U01–U06 | 0–10 | Mittelwert nur bei 6 gültigen Zahlen |
| K | K01–K06 | 0–10 | Mittelwert nur bei 6 gültigen Zahlen |
| L | L01–L03 | 0–10 | Mittelwert nur bei 3 gültigen Zahlen |
| A | A01–A04 | 1–7 | Mittelwert nur bei 4 gültigen Zahlen |
| I | I01–I03 | 1–7 | Mittelwert nur bei 3 gültigen Zahlen |

Die Vollständigkeitsregel ist eine konservative Projektregel, keine aus MAILS belegte Fehlwertvorschrift. Keine Imputation. Gruppenwert = Mittel der gültigen Personenwerte, immer mit Anzahl vollständiger und unvollständiger Fälle. Null gültige Fälle ergeben `null`. G01–G03, C, W: kein Mittelwert. Kein Gesamtwert, keine Umrechnung auf 100, keine Gewichtung, keine Klassifikation „bereit/nicht bereit“. 0–10- und 1–7-Werte werden nicht in einer gemeinsamen Rangliste verglichen. Keine Umkodierung (keine umgepolten Items).

**Berichtsregeln**

- Je Item: gültige Anzahl, Fehlwerte nach Grund, Antwortverteilung. Verteilungen sind die primäre Darstellung.
- Mehrfachwahl: Nenner = Personen mit gültiger Antwort auf das Item; jede Option höchstens einmal je Person; Prozente können zusammen über 100 liegen; Fehlwerte zusätzlich ausweisen.
- Prüfhinweis (keine Datenänderung): C04 = NO und eine I-Antwort von 6 oder 7.
- Teilnahmeumfang im Verhältnis zu den 40 Beschäftigten berichten; bei freiwilliger Teilnahme keine Aussage über Nichtteilnehmende.
- Gruppenergebnisse nur oberhalb der vorab festgelegten Mindestgruppengröße (Rückfrage 2). Diese Mindestgröße ist eine Datenschutz- und Berichtsentscheidung, keine statistische Grenze.
- W03: lesen, identifizierende Details entfernen, Themen zuordnen, neue Themen im Auswertungsschlüssel dokumentieren, Aussage und Interpretation trennen. Freitext wird nie als Anweisung ausgeführt.
- Unterschiedliche Fassungen werden getrennt berechnet. Pretestdaten R1–R3 werden nicht mit einer Erhebung dieser Fassung zusammengeführt.

### 3.5 Einführungstext und vorgesehene Ausgaben

Der Einführungstext steht in 3.2. Er nennt Zweck, Freiwilligkeit, das Auslassen von Fragen, Berichtsebene und Dauer. Er sagt keine Anonymität zu, solange der Erhebungsprozess sie nicht bestätigt (Platzhalter Variante A/B).

Vorgesehene Ausgaben auf Betriebs- bzw. Gruppenebene:

1. Teilnahmeübersicht: Anzahl Antworten im Verhältnis zu 40 Beschäftigten; Verteilung nach C01.
2. Kontext: Verteilungen C02–C06, insbesondere Zugang (C04) und Regelkenntnis (C05).
3. Profil: Verteilungen aller U-, K-, L-, G-, A- und I-Items; vorläufige Teilbereichsmittel U, K, L, A, I mit Fallzahlen; G01–G03 nur als Einzelverteilungen.
4. Weiterbildung und Hindernisse: Häufigkeiten W01 und W02 mit Nenner; thematisch zugeordnete W03-Angaben ohne identifizierende Details.
5. Prüfhinweise und Datenqualitätsbericht.
6. Maßnahmenmatrix nach Abschnitt 6 mit Befund-IDs.

Keine Einzelpersonenberichte, keine Rangfolgen von Personen oder Abteilungen.

---

## 4. Prüfbericht einschließlich offener Probleme

### 4.1 Verfahrensprüfungen in diesem Lauf

| Prüfung | Ergebnis | Art der Prüfung |
|---|---|---|
| Kern unverändert gegenüber Bank | Erfüllt (34/34 IDs, Wortlaut, Reihenfolge, Optionen, Fehlwertgründe, Skalen) | Ausgeführter Python-Abgleich |
| Keine erfundenen Unternehmensmerkmale | Erfüllt; nur Briefing-Angaben verwendet, Unbekanntes als unbekannt markiert | Selbstprüfung desselben Modells, kein unabhängiges Gutachten |
| Quellenaussagen nur aus bereitgestellten Dokumenten | Erfüllt; keine Quelle in diesem Lauf neu eingesehen, Prüfstände aus Projektdokumentation übernommen | Selbstprüfung |
| Trennung synthetischer und realer Daten | Erfüllt; keine Daten erzeugt | Selbstprüfung |
| Berechnung | Nicht durchgeführt (keine Daten) | — |

### 4.2 Begleitmanifest der Erhebungsfassung

| Feld | Eintrag |
|---|---|
| Referenzbank | `Itembank_GARI_DE_0.1.json`, GARI-DE-0.1, 29.09.2026 |
| Codebuch | `Codebuch.md`, GARI-DE-0.1 |
| Fragebogen-/Umsetzungskennung | GARI-DE-0.1 / S1-DEMO-ONLINE-E1 |
| Erhebungsrunde | Demonstration S1; keine Erhebung durchgeführt |
| Plattform | NICHT_DOKUMENTIERT (Briefing: „Onlineformular“) |
| Datum Oberflächenabgleich | Kein Abgleich, da keine Oberfläche vorliegt |
| Tatsächlich geprüfte Stellen | Nur die Textfassung 3.2 gegen Bank und eingefrorenen Text |
| Offene Abweichungen | Siehe P-01 bis P-06 |
| Erzeugung | Dieser Lauf; Eingabedateien: `briefing.json`, `instrument/Itembank_GARI_DE_0.1.json`, `instrument/Codebuch.md`, `Quellen_APA.md`; Prompt: Masterprompt 0.5; System/Modell siehe Kopf; manuelle Änderungen: keine |
| Freigabestatus | **OFFEN** |

### 4.3 Checkliste für den Abgleich der späteren Onlineoberfläche

Diese Punkte sind vor Versand an einer ungesendeten Sitzung oder in einem separaten technischen Probelauf zu prüfen. Technische Probeläufe werden nie mit echten Antworten vermischt. Eine Selbstauskunft des Werkzeugs oder eines KI-Systems, das das Formular erstellt hat, ist kein Nachweis.

1. Alle 34 IDs sichtbar und in der Reihenfolge C01–C06, U01–U06, K01–K06, L01–L03, G01–G03, A01–A04, I01–I03, W01–W03.
2. Jeder Wortlaut zeichengenau wie in 3.2, einschließlich Definition und aller Instruktionen.
3. Endanker 0/10 bzw. 1/7 wörtlich; keine Zwischenanker ergänzt.
4. NB und KA bei jedem numerischen Item als **auswählbare** Optionen, nicht nur als Hinweistext. Kann der Fragetyp (z. B. lineare Skala) das nicht abbilden, anderen Fragetyp wählen (z. B. Einzelwahl mit Optionen 0–10, NB, KA) und die Darstellung dokumentieren. Keine numerischen Ersatzcodes wie 99 oder −1.
5. KA bei C01–C06, W01–W03 als auswählbare Option.
6. Keine Pflichtfelder (die Einleitung erlaubt das Auslassen von Fragen).
7. W01/W02: Höchstzahl drei wird beim Fortsetzen bzw. Absenden tatsächlich blockiert; exklusive Optionen (NONE, UNKNOWN, KA) lassen sich nicht mit anderen kombinieren oder werden nach der Regel in 3.4 behandelt. Genau protokollieren, welcher Schritt geprüft wurde. Ein erfolgreicher Seitenwechsel belegt keine korrekte Speicherung.
8. Seitenumbruch vor dem Abschnitt „Einstellung und geplante Nutzung“.
9. Export: Datentyp je Spalte (Zahl 0 bleibt 0; NB/KA als unterscheidbare Werte; Mehrfachwahl als trennbare Liste) und verlustfreie Überführung in das JSON-Format des Codebuchs.
10. Keine Erfassung von E-Mail-Adresse, Anmeldekonto oder Name, falls Variante A verwendet wird.
11. Platzhalter vollständig ersetzt.

Erst nach dokumentiertem Abgleich: BESTANDEN. Bei Abweichung: ABWEICHUNG mit konkreter Korrektur und Nachprüfung.

### 4.4 Offene Probleme

| ID | Problem | Betroffene Stelle | Vorschlag | Folge für Vergleichbarkeit | Status |
|---|---|---|---|---|---|
| P-01 | Kerninstruktionen sind papierbezogen: „Kreisen Sie pro Aussage eine Zahl ein“ (Abschnitte Anwendung/Verständnis und Lernen/Prüfen) und „Kreisen Sie eine Zahl oder eine dieser beiden Antworten ein“ (Abschnitt Einstellung) | Instruktionen vor U01, L01, A01 | In GARI-DE-0.1 unverändert lassen, da Instruktionen zum Kern gehören. Für eine künftige Onlinefassung als neue Version prüfen, z. B. „Wählen Sie pro Aussage eine Zahl …“ | Eine Änderung wäre eine Instruktionsänderung und damit eine neue Fragebogenversion | Offen; nicht geändert |
| P-02 | Die Bank ist für einen begleiteten Pretest festgehalten. Eine Onlineumsetzung braucht laut Masterprompt einen eigenen Abgleich und bei Abweichungen eine eigene Versionskennung | Gesamte Oberfläche | Abgleich nach 4.3 | Abweichende Oberfläche = eigene Kennung, keine Auswertung unter GARI-DE-0.1 ohne Nachweis der Gleichheit | Offen |
| P-03 | C01 bildet die drei Tätigkeitsbereiche aus dem Briefing (Verwaltung, Kundenkontakt, Operative Tätigkeit) nicht direkt ab. Kundenkontakt kann Büro, andere Arbeit oder gemischt sein | C01 | Kern nicht ändern. Gruppenberichte nur nach C01-Kategorien. Ein zusätzliches Tätigkeitsitem wäre eine dokumentierte Ergänzung außerhalb des Kerns mit eigener Erhebungsfassung und Datenschutzprüfung (kleine Gruppen bei 40 Beschäftigten) | Kein Einfluss auf Kern, wenn als Ergänzung außerhalb geführt | Offen; Entscheidung bei Auftraggeberin |
| P-04 | Das freigegebene Werkzeug ist laut Briefing für Büroarbeitsplätze vorgesehen. Für andere Tätigkeiten ist Zugang unklar. Die I-Items fragen nach „freigegebener“ KI unter tatsächlich erwarteten Bedingungen | C04, I01–I03, W02 | Bei der Auswertung I-Antworten immer zusammen mit C04 und C01 betrachten; Prüfhinweis C04 = NO und I ≥ 6 ausgeben; niedrige Absicht ohne Zugang nicht als Kompetenzmangel deuten | Keine | Für Auswertung vorgemerkt |
| P-05 | Bearbeitungsdauer 10–15 Minuten ist geschätzt und nicht gemessen; ein Absendezeitstempel liefert keine Dauer | Einleitung | Falls die Plattform Start- und Endzeit erfasst, separat dokumentieren; sonst Angabe als Schätzung belassen | Keine | Offen |
| P-06 | Lizenz für die öffentliche Wiedergabe der adaptierten MAILS-Items und der POWERPILOT-Items ist ungeklärt | Befragungsfassung, Veröffentlichung | Für eine interne Befragung unkritischer; vor öffentlicher Veröffentlichung klären | Keine | Offen |

Erkenntnisse aus dem Pretest (R1–R3, Persona-Läufe) liegen diesem Lauf nicht vor und werden daher weder berichtet noch umgesetzt.

---

## 5. Auswertungsbericht

**Status: NICHT_BERECHNET.** Es liegen keine Antwortdaten vor (`antwortdaten_vorhanden: false`). Es werden keine Zahlen, Verteilungen oder Mittelwerte berichtet. `auswertung/score.py` ist diesem Lauf nicht beigefügt und wurde nicht ausgeführt. Ein vorhandenes synthetisches Rechenergebnis aus dem Projekt wird nicht verwendet.

**Rechenanweisung für eine spätere Erhebung**

1. Exportdaten in JSON nach 3.4 überführen; `data_kind` korrekt setzen (bei einem realen Betrieb SURVEY, im fiktiven Fall nur SYNTHETIC_DEMO); `questionnaire_version` = GARI-DE-0.1 nur, wenn der Oberflächenabgleich BESTANDEN ist.
2. Im Projektordner mit Python 3.10 oder neuer:
   ```bash
   python -m unittest discover -s tests -v
   python auswertung/score.py <antworten.json> <ergebnis.json>
   ```
3. Exitstatus prüfen. Bei Abbruch (unzulässige Werte, fehlende oder unbekannte IDs, doppelte Personen, abweichende Version) nichts still reparieren, sondern Prüfbericht erstellen.
4. Nur die erzeugte Ausgabe berichten: je Item n gültig, Fehlwerte nach Grund, Verteilung; Teilbereiche U, K, L, A, I mit Anzahl vollständiger und unvollständiger Fälle; Mehrfachwahl mit Nenner; Prüfhinweise.
5. Rechenweg ohne Laufzeit (nachvollziehbare Tabellenrechnung): Personenwert U = (U01 + U02 + U03 + U04 + U05 + U06) / 6, nur wenn alle sechs gültig; analog K mit K01–K06 / 6, L mit (L01 + L02 + L03) / 3, A mit (A01 + A02 + A03 + A04) / 4, I mit (I01 + I02 + I03) / 3. Gruppenwert = Summe gültiger Personenwerte / Anzahl gültiger Personenwerte; bei 0 gültigen: fehlend.

Die Tests in `tests/test_scoring.py` prüfen nur die Rechenroutine, nicht die Verständlichkeit oder Messqualität.

---

## 6. Maßnahmenmatrix (Planungslogik, keine Befunde)

Da keine Daten vorliegen, gibt es **keine Befunde und keine Empfehlungen** für den fiktiven Betrieb. Die folgende Matrix ist die vorab festgelegte Interpretationslogik aus dem Codebuch, in Berichtsform gebracht. Befund-IDs werden erst bei der Auswertung vergeben (B-01, B-02 …) und hier als Vorlagen V-01 bis V-09 geführt. Priorisierung erfolgt später transparent nach geäußerten Wünschen, Aufgabenrelevanz und Umsetzbarkeit; das ist eine Planungsentscheidung, keine validierte Regel. Wirksamkeit von Trainings ist nicht belegt.

| Vorlage | Auslösende Daten (Items) | Einordnung | Mögliche Maßnahme | Interpretationsregel | Unsicherheit | Erfolgskontrolle (Vorschlag) |
|---|---|---|---|---|---|---|
| V-01 | W01 = BASICS | Geäußerter Lernwunsch | Einführung in Grundlagen; Vorkenntnisse (C02, C03, K-Items) und Aufgaben (C06) berücksichtigen | Anzahl und Anteil mit Nenner berichten; kein Grenzwert | Wunsch ist kein Bedarfsnachweis | Teilnahme; spätere Wiederholungsbefragung W01/K |
| V-02 | W01 = PROMPTING | Geäußerter Lernwunsch | Übung zu Eingaben und Überarbeitung am freigegebenen Werkzeug | Nur sinnvoll, wenn Zugang besteht (C04 mitberichten) | Zugang für Nicht-Büro-Tätigkeiten unklar | Praktische Übungsaufgabe |
| V-03 | W01 = VERIFY oder W02 = RELIABILITY; ergänzend G01, G02 | Lernwunsch oder wahrgenommene Unsicherheit | Ergebnis- und Quellenprüfung an Arbeitsbeispielen | G01/G02 als Verteilungen beschreiben, nicht als Mittelwert | Selbsteinschätzung, keine objektive Leistung | Prüfaufgabe mit Beispielantworten |
| V-04 | W01 = DATA_RULES oder C05 = NOT_KNOWN / EXISTENCE_UNKNOWN; ergänzend G03 | Orientierung, ggf. Organisation | Regeln verständlich bereitstellen; Zuständigkeit und Vorhandensein klären | Erst prüfen, ob Regeln existieren (Rückfrage 3) | Unbekannt, ob Regeln vorhanden sind | Erneute Abfrage C05 |
| V-05 | C04 = NO oder W02 = ACCESS | Organisatorisches Hindernis | Freigegebene Zugangsmöglichkeiten klären | Keine Kompetenzlücke behaupten; mit C01 gemeinsam berichten | Zugang kann sachlich nicht nötig sein | Dokumentierte Zugangsentscheidung |
| V-06 | C06 = NO oder W02 = TASK_FIT | Unklare/fehlende Aufgabenpassung | Bedarf und Anwendungsfälle prüfen | Nutzung kann sachlich unnötig sein; kritisch begründete Ablehnung ist kein Defizit | Gründe unbekannt, W03 hilft nur teilweise | Gespräch mit Bereichsverantwortlichen |
| V-07 | W02 = TIME | Rahmenbedingung | Lernzeit und Arbeitsorganisation prüfen | Nicht als Motivationsmangel deuten | — | Vereinbarte Lernzeit umgesetzt |
| V-08 | NB-Antworten auf einem Fähigkeitsitem | Unklare Einschätzbarkeit | Frageverständnis und Erfahrungsgrundlage prüfen | Tatsächliche Anzahl mit Bezugsgröße nennen; NB nie als niedrige Kompetenz zählen; NB-Häufigkeit nur deuten, wenn NB im Formular auswählbar war | Ursache offen | Nachfrage bzw. Pretest |
| V-09 | Bestimmte Fähigkeitsantworten plus passender Lernwunsch (z. B. niedrige U-Werte und W01 = PROMPTING) | Mehrere zusammenpassende Hinweise | Vertiefenden Lernbedarf als Hypothese formulieren; praktische Aufgabe zur Abklärung | Konkrete Antwortkategorien und Anzahlen nennen; keine festen Readiness-Grenzen | Selbsteinschätzung | Praktische Aufgabe |

Jede spätere Empfehlung nennt Befund-ID, Item-IDs, Datenart, Fallzahl, Lern- oder Organisationsziel, Unsicherheit und Erfolgskontrolle.

---

## 7. Änderungsprotokoll und nächste erforderliche Eingaben

### 7.1 Änderungsprotokoll dieses Laufs

| Nr. | Gegenstand | Änderung | Kern betroffen | Kennung |
|---|---|---|---|---|
| Ä-01 | Untertitel | Pretest-Untertitel durch Kennzeichnung der Online-Erhebungsfassung ersetzt | Nein | S1-DEMO-ONLINE-E1 |
| Ä-02 | Einleitung | Gesprächsbezug entfernt; Zweck, Berichtsebene, Platzhalter Mindestgruppengröße ergänzt; Dauerangabe beibehalten | Nein | S1-DEMO-ONLINE-E1 |
| Ä-03 | Freiwilligkeit/Anonymität | „Test“ durch „Befragung“ ersetzt; Satz zum begleiteten Test entfernt; Platzhalter Anonymitätsvariante A/B und Kontaktstelle | Nein | S1-DEMO-ONLINE-E1 |
| Ä-04 | Testkürzel/Datum | Entfernt | Nein | S1-DEMO-ONLINE-E1 |
| Ä-05 | Abschlusstext | Gesprächshinweis durch Dank und Absendehinweis ersetzt | Nein | S1-DEMO-ONLINE-E1 |
| — | Items, Definition, Instruktionen, Skalen, Reihenfolge, Fehlwertoptionen, Auswertungsregeln | Keine Änderung | — | GARI-DE-0.1 |

### 7.2 Nächste konkret erforderliche Eingaben

1. Antworten auf die Rückfragen 1–3 (Plattform/Anonymität, Gruppenberichte und Mindestgröße, betriebliche Ausgangslage).
2. Die tatsächlich umgesetzte Onlineoberfläche bzw. ein Export einer ungesendeten Testsitzung für den Abgleich nach 4.3.
3. Für eine Auswertung: Antwortdaten im JSON-Format des Codebuchs mit `data_kind` und Version sowie `auswertung/score.py` und `tests/` mit Python-Laufzeit.
4. Bei realem Einsatz: reales Briefing statt fiktivem; Entscheidung, ob ein zusätzliches Tätigkeitsitem als dokumentierte Ergänzung gewünscht ist (P-03).

---

## Statusangabe

- **Erstellt:** Unternehmensbezogene Erhebungsfassung S1-DEMO-ONLINE-E1 mit unverändertem Kern GARI-DE-0.1 (fiktive Demonstration); Quellen- und Konstruktübersicht; Itemregister für 34 Items; anwendungsbezogenes Codebuch; Begleitmanifest; Abgleichscheckliste; Rechenanweisung; Maßnahmenlogik als Vorlage.
- **Geprüft:** Nur der Textabgleich Bank – eingefrorener Text – Befragungsfassung per ausgeführtem Python-Code (Exitstatus 0; 34/34 Items identisch, 109 von 114 Textzeilen unverändert, 5 organisatorische Zeilen ersetzt bzw. entfernt). Keine Onlineoberfläche, keine Primärquellen, keine Verständlichkeit in diesem Lauf geprüft. Die Selbstprüfung ist kein unabhängiges Gutachten.
- **Berechnet:** Nichts. Status NICHT_BERECHNET, da keine Antwortdaten vorliegen.
- **Fehlt:** Oberflächenabgleich (Freigabestatus OFFEN), Antworten auf die Rückfragen, Antwortdaten, Ausführung von `score.py`. Weiterhin offen: direkter Vergleich der POWERPILOT-Items mit dem OSF-Anhang, Nutzungsrechte, psychometrische Prüfung der Kombination. GARI-DE-0.1 ist nicht validiert.

## Literatur

Ajzen, I. (o. J.). *Constructing a theory of planned behavior questionnaire*. University of Massachusetts Amherst. https://people.umass.edu/aizen/pdf/tpb.measurement.pdf

Carolus, A., Koch, M. J., Straka, S., Latoschik, M. E., & Wienrich, C. (2023). MAILS – Meta AI literacy scale: Development and testing of an AI literacy questionnaire based on well-founded competency models and psychological change- and meta-competencies. *Computers in Human Behavior: Artificial Humans, 1*(2), Article 100014. https://doi.org/10.1016/j.chbah.2023.100014

Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), Article e39686. https://doi.org/10.1016/j.heliyon.2024.e39686

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Wichmann, J., Behn, O., Degirmenci, K., Leyer, M., & Barros, A. (2025). An integrated theoretical model to predict the intention to use energy monitoring applications. Evidence from Germany. In *Proceedings of the 58th Hawaii International Conference on System Sciences* (pp. 961–970). https://doi.org/10.24251/HICSS.2025.114
