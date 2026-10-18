# Ergänzender synthetischer Test mit Claude

Dokumentiert am 17. Oktober 2026 · Datenart SYNTHETIC_DEMO · Ursprung LLM_PERSONA

## Protokoll

| Feld | Dokumentierter Stand |
|---|---|
| Zweck | Technische Erprobung der Forms-Umsetzung und Gewinnung von Prüfhypothesen |
| Erstellerin/Bedienung | Durch die Projektbearbeiterin ausgeführt; Ablauf von ihr mitgeteilt |
| Antwortsystem | Claude im Browser; Angabe der Erstellerin: „Claude Opus Mittel 5.5“; technische Modell-ID nicht belegt |
| Formular | GARI-DE-0.1-FORMS-R2, neuer von der Erstellerin bereitgestellter Link |
| Anzahl | Zwei synthetische Antwortzeilen; keine zusätzlichen echten Testpersonen |
| Sitzungen | Jeweils ein eigener Chat im Browser; nach Angabe der Erstellerin unabhängig voneinander gestartet |
| Werkzeugablauf | Kein vollständiges Claude-Browseraktionsprotokoll vorliegend |
| Ausgangsprompts | Von der Erstellerin mitgeteilte Texte, unten dokumentiert |
| Datenstatus | Originalexport separat gesichert; keine Überschreibung und keine Ergänzung leerer Zellen |
| Rechenprüfung | `auswertung/audit_synthetic_forms.py` am real vorliegenden synthetischen Export ausgeführt; keine Readiness-Scores |
| Ergebnis | 46 Zahlenwerte im zulässigen Bereich; vier NB-Antworten; drei leere Kontextfelder im ersten Fall; 20 nichtleere Feedbackfelder |
| Verbleibende Probleme | Gebündelte Prüffragen, unvollständig angepasste Hinweise und beim Seitenwechsel nicht erzwungene Höchstzahl |
| Abschließender Umfang | Drei reale Personen plus diese zwei synthetischen Fälle; weitere reale Tests nicht vorgesehen |

Die Zuordnung SYN01/SYN02 zu Bau/Marketing ist eine nachträgliche Dokumentationszuordnung anhand Reihenfolge und Inhalte. Modellparameter, nicht angezeigte Versionen oder Sitzungsdaten werden nicht erfunden. Die zwei Rollenläufe waren nicht Teil des vorab festgelegten kontrollierten Baselinevergleichs. Ihr ergänzender Einsatz wird deshalb ausdrücklich als nachträglich hinzugefügter Entwicklungsschritt bezeichnet.

## Von der Erstellerin mitgeteilte Prompts

Die Platzhalter `[FORMULARLINK_R2]` ersetzen ausschließlich den konkreten URL-Verweis. Beide Prompts verwiesen auf dieselbe neue Forms-Fassung. Die Inhaltsvorgaben werden unverändert wiedergegeben; die Bezeichnung der ausgefüllten Rollen als synthetisch bleibt in der wissenschaftlichen Dokumentation erhalten.

### Prompt 1

```text
Stell dir folgende einmalige Situation vor, du bist ein ca. 45 Jähriger Facharbeiter am Bau (hauptsächlich Bau von Ziegelmassivhäusern) und sollst diesen Fragebogen ausfüllen: [FORMULARLINK_R2]
Du hattest davor noch nicht wirklich mit ChatGPT & Co gearbeitet, nur aus dem Radio und Fernsehen davon gehört. Interessant findest du es schon, aber auch gruselig. Fülle unter diesen Voraussetzungen bitte den Fragebogen unter dem Link aus.
```

### Prompt 2

```text
Stell dir folgende einmalige Situation vor, du bist eine ca. 40 Jährige Angestellte im Bereich Marketing (hauptsächlich Digitales Marketing und Social Media) und sollst diesen Fragebogen ausfüllen: [FORMULARLINK_R2]
Du arbeitest regelmäßig mit ChatGPT & Co und hast auch an Schulungen zu diesem Thema teilgenommen. Privat nutzt du deine Accounts auch täglich. Einerseits sparst du durch die Anwendung von KI sehr viel Zeit ein, andererseits hast du manchmal auch Bedenken hinsichtlich Datenschutz. Fülle unter diesen Voraussetzungen bitte den Fragebogen unter dem Link aus.
```

## Bewusst offene Prompts

Die Erstellerin bestätigte am 17. Oktober 2026, dass die Rollenbeschreibungen absichtlich Interpretationsspielraum ließen. Dieser explorative Zuschnitt wird beibehalten. Die Prompts werden nicht rückwirkend zu standardisierten kontrollierten Szenarien erklärt. Unterschiedliche Erfahrungen und Haltungen waren teilweise vorgegeben; nicht vorgegebene Unternehmensmerkmale sind vom Modell ergänzt. Die getrennten Chats vermeiden eine direkte Übernahme des Gesprächsverlaufs zwischen den Rollen, machen die Fälle aber nicht zu unabhängigen menschlichen Bewertungen.

## Interpretation

Die Persona-Vorgaben legen Erfahrung und Haltung teilweise schon fest. Entsprechende Unterschiede in den ausgefüllten Werten sind daher keine Prüfung der Trennschärfe des Instruments. Nicht vorgegebene Unternehmensmerkmale in den Antworten sind Ergänzungen des Modells, keine unabhängig erhobenen Kontextdaten. Aussagen über Bau- oder Marketingbeschäftigte dürfen daraus nicht abgeleitet werden.

Die originären Antworten und die direkte Antworttabellenadresse werden im aktuellen Arbeitsstand separat vom Repositorypaket bereitgestellt. Für eine spätere bewusste Veröffentlichung synthetischer Beispiele wäre eine eigene, eindeutig gekennzeichnete und von realen Daten getrennte Beispieldatei geeignet. Im aktuellen Paket werden nur Verfahren, Prompts, aggregierte Prüfergebnisse und der Prüfcode dokumentiert.
