# Bewertungsbogen_Erstellerin

# Bewertungsbogen: menschliche Stichprobe

Zweck: Ein menschliches Urteil neben die Bewertung durch die Modelle stellen. Das ist der einzige Abgleich in der Evaluation, der nicht von einer KI stammt.

Bewertet werden zwei NotebookLM-Antworten: **N-A1** (Anwendung) und **N-A2** (Entwicklung, Phase 1). Zeitbedarf etwa 30 Minuten.

## Vorher

1. **Abschnitt 11 des Evaluationsprotokolls nicht vorher lesen.** Sonst bewertest du mein Urteil mit, nicht die Antwort.
2. Öffne nebeneinander: die Antwort, die Referenzbank (`Itembank_GARI_DE_0.1.json`) und den Masterprompt v0.6.
3. Bewerte nur, was in der Antwort steht. Keine Rückfragen an NotebookLM.

Skala je Kriterium: **E** = erfüllt · **T** = teilweise · **N** = nicht erfüllt · **?** = nicht prüfbar. Bei T und N bitte die Stelle kurz notieren.

## Teil 1: N-A1 Anwendung (etwa 20 Minuten)

| Nr | Kriterium | Worauf du achtest | Urteil | Stelle / Notiz |
| --- | --- | --- | --- | --- |
| K1 | Quellenbezug | Wird etwas behauptet, das nicht in Briefing, Bank oder Codebuch steht? Stichprobe: 3 Aussagen aus Abschnitt 1 nachschlagen | E |  |
| K2 | Unveränderter Kern | Stichprobe: 5 Items deiner Wahl Wort für Wort mit der Bank vergleichen, dazu bei 2 Items alle Antwortoptionen. Abweichungen bei Instruktionen und Einleitung notieren | E |  |
| K3 | Konstruktabdeckung | Alle Bereiche C, U, K, L, G, A, I, W vorhanden? | E |  |
| K4 | Umgang mit Nichtnutzung | Wird irgendwo nahegelegt, dass Nichtnutzung eine niedrige Kompetenz bedeutet? NB-Hinweis vorhanden? | E |  |
| K5 | Vollständiger Ablauf | Kurzbeschreibung, Befragungsfassung, Zusatzmodul, Manifest, Freigabestatus vorhanden? | E |  |
| K6 | Daten- und Rechenregeln | Wird etwas berechnet oder ein Wert erfunden, obwohl keine Daten vorliegen? | E |  |
| K7 | Begründete Maßnahmen | In A1 nicht verlangt. Nur notieren, falls trotzdem Empfehlungen auftauchen | ? |  |
| K8 | Korrekter Status | Behauptet die Antwort Validität, Vergleichbarkeit oder einen erfolgreichen Formularabgleich, der nicht stattgefunden hat? Achte auf das Manifest | E |  |
| Z | Zusatzmodul | Steht Z01 außerhalb des Kerns, mit eigener Version und Begründung? Ist die Frage sinnvoll für einen 40-Personen-Betrieb? | E |  |

**Gesamturteil N-A1:** Würdest du diese Befragungsfassung so an ein Formularwerkzeug geben? Ja

## Teil 2: N-A2 Theorieteil (etwa 10 Minuten)

| Nr | Frage | Urteil | Notiz |
| --- | --- | --- | --- |
| T1 | Passt die gewählte Theorie (RAA, TTF) fachlich zur Frage nach KI-Readiness von Beschäftigten? | E |  |
| T2 | Sind Theorie, Messinstrument und Methode sauber getrennt? | E |  |
| T3 | Sind die Hypothesen gerichtet, verständlich und aus der genannten Theorie ableitbar? Prüfe 2 Hypothesen genauer | E |  |
| T4 | Wird klar gesagt, dass die Hypothesen nicht getestet werden? | E |  |
| T5 | Nutzt die Antwort Quellen, die laut Prompt ausgeschlossen waren (Referenzbank, Codebuch)? Achte auf „GARI“, G01 bis G03, C01 bis C06 | N | GARI-Eigenitems und Kernkontext wurden übernommen; Anwenderfehler, da Quellen nicht über das Häckchen ausgeschlossen wurden |
| T6 | Fällt dir als Fachperson ein inhaltlicher Fehler auf, den ein Modell schwer erkennt? | E |  |

## Danach

1. Bogen ausfüllen und speichern.
2. Erst dann Abschnitt 11 im Evaluationsprotokoll lesen.
3. Übereinstimmungen und Abweichungen in einer Zeile je Kriterium notieren, zum Beispiel „K8: ich T, Modell T, gleiche Stelle“.
4. Bring den ausgefüllten Bogen hierher. Ich trage die Gegenüberstellung als Abschnitt 12 ins Protokoll ein und übernehme sie in Kapitel 5 der Hausarbeit.

Hinweis für die Hausarbeit: Eine Person, zwei Antworten. Das ist eine Plausibilitätsprüfung, keine Interrater-Reliabilität.