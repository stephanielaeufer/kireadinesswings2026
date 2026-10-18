# NotebookLM: Demonstration und Prüfung

Zwei getrennte Notebooks. Nicht mischen: Das Prüf-Notebook soll nicht vom Demonstrationslauf beeinflusst werden, und der Demonstrationslink soll nur das Artefakt zeigen.

## Notebook A „GARI Demonstration Masterprompt v0.6“

**Quellen hochladen**
- Alle 5 Dateien aus `A_Demonstration/`
- Datensatz_v1 (als PDF exportieren oder Original-.docx, falls NotebookLM es annimmt)
- Paper Fragebogen 1 bis 5 (PDF)

Die JSON-Dateien tragen die Endung `.txt`, damit NotebookLM sie sicher annimmt. Der Inhalt ist unverändert.

**Vor dem ersten Prompt:** In der Chat-Konfiguration, falls angeboten, die Antwortlänge auf „länger“ stellen. Den Masterprompt nicht in das Feld für eigene Anweisungen kopieren. Er ist zu lang und bleibt als Quelle.

### Prompt A1 · Anwendung (ANWENDEN, Szenario S1)

```
Arbeite strikt nach der Quelle 01_MASTERPROMPT_v0.6.md. Betriebsart: ANWENDEN.
Eingaben: Briefing 04_Briefing_S1_fiktiv, Referenzbank 02_Referenzbank_GARI_DE_0.1, Codebuch 03_Codebuch_Rev0.6. Andere Quellen in diesem Schritt nicht verwenden.

Liefere in dieser Reihenfolge:
1. Kurzbeschreibung und Annahmen (max. 8 Zeilen), inkl. Abweichungen zwischen Briefing und Referenzbank.
2. Die vollständige Befragungsfassung: Einleitung, Definition, alle 34 Kernfragen mit ID, exaktem Wortlaut aus der Referenzbank und allen Antwortoptionen inkl. NB/KA. Nichts umformulieren, nichts kürzen.
3. Falls nötig ein Zusatzmodul nach den Regeln der Phase 3 (IDs Z01 ff.).
4. Begleitmanifest und Freigabestatus.

Wenn die Antwort zu lang wird, höre nach einem vollständigen Abschnitt auf und schreibe „FORTSETZUNG FOLGT“.
```

Bei „FORTSETZUNG FOLGT“ einfach senden: `Weiter, ab dem nächsten Abschnitt, gleiche Regeln.`

### Prompt A2 · Entwicklung aus der Datenbasis (ENTWICKELN, nur Phase 1)

Neuer Chat oder Chatverlauf löschen.

```
Arbeite strikt nach der Quelle 01_MASTERPROMPT_v0.6.md. Betriebsart: ENTWICKELN.
Eingaben: Briefing 05_Briefing_Entwicklung_fiktiv, die Itemsammlung Datensatz_v1 und die Studien Paper Fragebogen 1 bis 5. Die Referenzbank und das Codebuch in diesem Schritt NICHT verwenden.

Liefere nur Phase 1:
1a Theorievorschlag, Abgrenzung Theorie/Instrument/Methode, Forschungsmodell, nummerierte Hypothesen mit Quelle und Prüfbarkeit, Zuordnung Hypothese → Itemblock.
1b Quellenregister mit Zugangsstatus und Konstruktmatrix, inkl. Nähe zwischen Items der Itemsammlung und geplanten Eigenitems.

Nenne fehlende Quellen aus dem Briefing ausdrücklich. Erfinde keine Items, Seitenzahlen oder Quellen.
```

### Prompt A3 · Itementwurf zu Phase 1 (optional, gleicher Chat)

```
Erstelle jetzt Phase 2 als kurzen Entwurf: für jeden Itemblock aus 1a höchstens 4 Items mit ID, Wortlaut, Status (ORIGINAL/UEBERSETZT/ADAPTIERT/NEU_ENTWICKELT), Quelle mit Fundstelle und Antwortskala. Keine Wiederholung von Phase 1.
```

**Danach:** Notebook teilen. Zugriff nur für bestimmte Personen (Prüfende), nicht „jeder mit Link“, weil Lehrunterlagen und Studien enthalten sind. Den Link für Hausarbeit und Repo notieren.

## Notebook B „GARI Prüfung Gesamtpaket“

**Quellen hochladen**
- Alle 7 Dateien aus `B_Pruefung/`
- Pruefungsleistung_v2.pdf, Study Guide Praxisseminar, EV-Bogen Praxismodul
- Hausarbeitsentwurf als PDF
- Paper Fragebogen 1 bis 5 und Datensatz_v1

Bewusst nicht dabei: mein Prüfbericht. So prüft NotebookLM unabhängig, und wir vergleichen danach beide Ergebnisse.

### Prompt B1 · Prüfung gegen Anforderungen und Konsistenz

```
Rolle: kritische Gutachterin für eine Hausarbeit im Master Digital Commerce, Marketing & Psychology. Du prüfst, du lobst nicht. Jeder Befund braucht eine Fundstelle in den Quellen.

Gegenstand: das DSR-Artefakt (01_MASTERPROMPT_v0.6 mit Referenzbank, Codebuch, Evaluation, Projektkontext) und der Hausarbeitsentwurf.

Prüfe:
1. Erfüllt das Paket die Anforderungen aus Pruefungsleistung_v2, Study Guide und EV-Bogen? Je Anforderung: erfüllt / teilweise / fehlt, mit Fundstelle.
2. Widersprüche zwischen den Dateien: Itemanzahl, Skalen, Fehlwertregeln, Versionen, Evaluationsumfang, Forschungsfrage.
3. Stimmen Herkunftsangaben der Items in der Referenzbank mit Datensatz_v1 und den Papers überein? Nenne jede Abweichung.
4. Werden irgendwo Validität, Reliabilität oder Vergleichbarkeit behauptet, die die Evaluation nicht trägt?
5. Stimmen Zitate im Hausarbeitsentwurf mit 07_Quellen_APA überein (beide Richtungen)?

Ausgabe als Tabelle: Nr | Quelle/Stelle | Befund | Beleg | Schwere (kritisch/wichtig/kosmetisch) | Vorschlag. Danach die 5 wichtigsten Punkte als Liste.
```

### Prompt B2 · Gegenprobe zur Evaluation (gleicher Chat)

```
Lies 05_Masterprompt_Evaluation. Welche Schlussfolgerungen dort sind durch die beschriebenen Läufe gedeckt, welche gehen darüber hinaus? Welche Grenze der Evaluation ist am schwerwiegendsten für die Forschungsfrage, und wie ließe sie sich bis 1. November mit vertretbarem Aufwand verringern?
```

## Was du hierher zurückbringst

1. Alle Antworten im Wortlaut (kopieren oder als Notiz speichern und exportieren). Keine Zusammenfassung.
2. Screenshot der Quellenliste beider Notebooks.
3. Datum, Uhrzeit und ob ein Modellname angezeigt wurde. Wenn nicht: „nicht angezeigt“.
4. Den Freigabelink von Notebook A.
5. Ob du nachgefragt oder etwas korrigiert hast, und was.

Daraus mache ich: Vergleich Claude gegen NotebookLM (systemübergreifende Prüfung), Abgleich beider Prüfberichte und den Abschnitt zur NotebookLM-Demonstration für die Hausarbeit.
