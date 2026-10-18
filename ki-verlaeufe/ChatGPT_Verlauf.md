# Chatverlauf ChatGPT (GPT-6 Astra Max): Vorarbeit

Zeitraum September bis 17. Oktober 2026, Export am 18. Oktober 2026 · Datenart: von der Erstellerin direkt aus der ChatGPT-Oberfläche kopierter Text, in zwei Teilen zusammengeführt

**Hinweise zur Fassung**

- Der Text ist so übernommen, wie die Oberfläche ihn beim Kopieren ausgab. Rechtschreibung und Absätze sind unverändert. Hochgeladene Dateien erscheinen nur mit Dateinamen.
- Fünf Links zu Google-Formularen und Antworttabellen wurden durch Platzhalter ersetzt. Die Antworttabellen enthalten Angaben realer Testpersonen; die Formulare sollen keine neuen Antworten erhalten.
- ChatGPT hat zusätzlich eine eigene PDF erzeugt. Sie bezeichnet sich selbst als Teil-Export mit Lücken bei älteren Antworten und enthält die nicht entfernten Links. Sie wird deshalb nicht veröffentlicht und kann den Prüfenden auf Anfrage bereitgestellt werden.
- Ein vollständiger Wortlaut aller Zwischenantworten und Dateien des Chats ist mit den verfügbaren Exportwegen nicht sicher herzustellen. Die erzeugten Dateien sind in ihren späteren Fassungen im Repository enthalten (Projektpaket 0.5 und 0.6).

---



Pruefungsleistung_v2.pdf
PDF

Beispiel Design Science Research Peffers.pdf
PDF

Datensatz_v1.docx
Dokument

Paper Fragebogen 1.pdf
PDF

Paper Fragebogen 2.pdf
PDF

Paper Fragebogen 3.pdf
PDF

Paper Fragebogen 4.pdf
PDF

Paper Fragebogen 5.pdf
PDF

Foliensatz_v2.pdf
PDF
Ich wurde dazu beauftragt einen standardisierten Fragebogen zur Messung der KI-Readiness von MItarbeitenden in Unternehmen zu erstellen und zwar auf Basis des Design Science Research nach Peffers. Ziel ist es auf Basis von bereits erprobten wissenschaftlichen Modellen eine solide Lösung bereitzustellen und zwar so, dass es derartig robust ist, dass man quasi dann einen Masterprompt entwickelt, der für den Anlasszweck vom Unternehmen unabhängig eingesetzt weren kann und wirklich nachvollziehbare Ergebnisse hervorbringt. Ich habe dir hierzu schon mal sämtliche Unterlagen, die mir bislang zur Verfügung tehen bereitgestellt. Bitte recherchiere alle weiteren notwendigen Informationen, die du für die Lösungsfindung benötigst und komme auch gerne mit Fragen wieder auf mich zurück um ein optimales Ergebnis zu erzielen. Den Code/Prompt soll ich dann via Github bereitstellen, des weiteren eine Hausarbeit im Ausmaß von 10 inhaltstragenden Seiten, die den Vorgang der Lösungsfindung beschreibt. Aber lies dir mal bitte alle Infos durch, die ich dir hochgeladen habe.
Ich habe alle neun Unterlagen inhaltlich ausgewertet und ergänzend zu KI-Kompetenz, Fragebogenentwicklung und DSR-Evaluation recherchiert.
Mein vorläufiges Fazit: Wir sollten einen quellengebundenen Masterprompt mit festen Konstruktions- und Prüfregeln entwickeln. Damit lässt sich ein nachvollziehbarer Fragebogen erzeugen. Ob dieser Fragebogen KI-Readiness zuverlässig misst und Ergebnisse zwischen Unternehmen vergleichbar sind, muss zusätzlich empirisch geprüft werden. Diese Unterscheidung wird für die wissenschaftliche Qualität deiner Hausarbeit entscheidend sein.

Aus der 
Prüfungsaufgabe
 ergeben sich einige wichtige Vorgaben:

Das eigentliche DSR-Artefakt sind Leitlinien für ein großes Sprachmodell, die eine theoriegestützte Fragebogenerstellung ermöglichen. Der erzeugte Fragebogen dient zur Anwendung und Prüfung dieser Leitlinien.
Google NotebookLM ist ausdrücklich vorgesehen. Wir sollten den späteren Prompt deshalb dort demonstrieren und evaluieren.
Die theoretische Herkunft der Fragen und der Entwicklungsprozess einschließlich Verbesserungen müssen nachvollziehbar sein.
GitHub dient zur Bereitstellung des Codes beziehungsweise Links. Eine vollständige Softwareanwendung ist dafür zunächst nicht erforderlich.
Die Aufgabenbeschreibung nennt einmal fünf Prozessschritte; die Abbildung und der Foliensatz zeigen die sechs Aktivitäten nach Peffers. Für die Arbeit würde ich alle sechs berücksichtigen: Problemidentifikation, Zieldefinition, Entwicklung, Demonstration, Evaluation und Kommunikation.
Die Unterlagen liefern eine brauchbare Grundlage, erfüllen dabei aber unterschiedliche Funktionen:

Unterlage	Beitrag zu deinem Vorhaben	Grenze der Übertragbarkeit
Paper Fragebogen 1: KI-Akzeptanz im Gesundheitswesen	Zeigt die theoriegestützte Verbindung von Einstellungen, sozialen Einflüssen und Nutzungsabsicht.	Krankheits-, Behandlungs- und Bedrohungsfragen sind stark an den Gesundheitskontext gebunden.
Paper Fragebogen 2: Energiemonitoring-Anwendungen	Liefert mit Reasoned Action Approach, UTAUT2 und Selbstwirksamkeit Ansatzpunkte für Nutzungsbereitschaft.	Energiebezogene Motive und Rahmenbedingungen benötigen eine neue Operationalisierung für KI.
Paper Fragebogen 3: Task-Technology Fit bei Virtual Reality	Hilft zu erfassen, ob eine Technologie zu konkreten Arbeitsaufgaben passt.	Aufgabenpassung und erwartete Leistung bilden persönliche KI-Kompetenz nur begrenzt ab.
Paper Fragebogen 4: Vertrauen in generative KI	Liefert unmittelbar KI-bezogene Konstrukte und Fragen zu Vertrauen und Nutzungsabsicht.	Untersucht Führungskräfte; einige Vertrauensfragen bewerten die Bereitschaft zur unbeaufsichtigten Nutzung. Das wäre als positives Readiness-Merkmal problematisch.
Paper Fragebogen 5: Virtuelle Meetings und Arbeitsengagement	Unterstützt die Betrachtung technischer und sozialer Arbeitsbedingungen.	Misst keine KI-Readiness; eignet sich eher für ergänzende Kontextfragen.
Der Datensatz_v1.docx ist eine Sammlung von Fragebogenitems, teilweise mit Übersetzungen. Für statistische Untersuchungen der Messqualität fehlen bislang Antworten von Mitarbeitenden. Außerdem unterscheiden sich Antwortskalen und Untersuchungskontexte. Eine Vereinheitlichung auf beispielsweise fünf Antwortstufen wäre eine methodische Veränderung, die wir dokumentieren müssten.
Das hochgeladene DSR-Beispiel ist eine Anwendung der Methode auf Ortungssysteme in Krankenhäusern, nicht der ursprüngliche Methodenaufsatz von Peffers. Es ist als Muster hilfreich: Anforderungen aus Quellen ableiten, ein Artefakt entwickeln, dieses praktisch prüfen und Änderungen begründen. Der Foliensatz unterstützt diesen Ablauf und nennt verschiedene Prompting-Verfahren als mögliche Werkzeuge.

Die größte inhaltliche Lücke betrifft die KI-Kompetenz. Die fünf Studien behandeln überwiegend Akzeptanz, Nutzungsabsicht, Vertrauen und Arbeitsbedingungen. Mitarbeitende können KI gerne einsetzen wollen und gleichzeitig Schwierigkeiten haben, fehlerhafte Ergebnisse zu erkennen. Umgekehrt kann eine kompetente Person eine konkrete KI-Anwendung begründet ablehnen.

Daher halte ich folgende Ergänzungen für besonders relevant:

MAILS – Meta AI Literacy Scale: Erfasst verschiedene Facetten selbst eingeschätzter KI-Kompetenz sowie unter anderem KI-bezogene Selbstwirksamkeit. Die Entwicklung wurde an deutschsprachigen Erwachsenen untersucht; der modulare Aufbau ist für unser Vorhaben interessant. Die Skala misst Selbsteinschätzungen, weshalb wir daraus keinen objektiven Kompetenznachweis ableiten sollten. Originalarbeit von Carolus et al.
AICOS – AI Competency Objective Scale: Kommt ergänzend infrage, falls der Fragebogen tatsächliches KI-Wissen prüfen soll. Dafür müssten wir Wissensaufgaben und Selbsteinschätzungen getrennt auswerten. Originalarbeit von Markus et al.
Public Employees Artificial Intelligence Readiness Scale: Eine 2026 veröffentlichte Readiness-Skala untersucht Selbstwirksamkeit und Optimismus bei Beschäftigten im öffentlichen Dienst. Sie ist ein relevanter Vergleichspunkt; ihre Übertragbarkeit auf deutschsprachige Unternehmen müsste geprüft werden. Originalstudie von Bilgiç
Als vorläufige theoretische Grundlage bietet sich damit der Reasoned Action Approach für Nutzungsbereitschaft, ergänzt um passende MAILS-Teilskalen für KI-Kompetenz und Selbstwirksamkeit, an. Aufgabenpassung und wahrgenommene betriebliche Unterstützung könnten eigene Zusatzmodule bilden. Die endgültige Auswahl hängt davon ab, was „Readiness“ in deinem Auftrag genau umfassen soll.
Für die angestrebte Robustheit würde ich sechs Regeln festlegen:

Readiness ausdrücklich definieren. Als Arbeitsdefinition schlage ich vor: die individuelle Fähigkeit und Bereitschaft, KI im eigenen Arbeitskontext sachgerecht und verantwortungsvoll einzusetzen. Betriebliche Voraussetzungen werden gesondert erfasst.
Einen festen Kern und kontrollierte Zusatzmodule verwenden. Unternehmensübergreifende Wiederverwendung verlangt stabile Kernfragen. Anpassbare Felder betreffen beispielsweise KI-Anwendung, Tätigkeitsgruppe und Nutzungssituation. Die Bedeutung einer präzisen Verhaltens- und Kontextdefinition betont auch Ajzens Anleitung zur Fragebogenkonstruktion. Ajzens Leitfaden
Jedes Item rückverfolgbar machen. Zu jeder Frage gehören Konstrukt, Quelle, Originalformulierung, Anpassung, Antwortskala und Auswertungsregel. Originale, Übersetzungen, Anpassungen und neu entwickelte Fragen erhalten unterschiedliche Kennzeichnungen.
Validierungsstatus korrekt ausweisen. Übernommene Einzelitems machen einen neu zusammengestellten Fragebogen noch nicht zu einem validierten Instrument. Inhaltsprüfung, Verständlichkeit, Reliabilität und weitere Validitätsevidenz sind eigene Entwicklungsschritte. Boateng et al. zur Skalenentwicklung
Zunächst ein Profil je Dimension ausgeben. Für einen Gesamtwert von 0–100, Gewichtungen oder Schwellen wie „KI-ready“ fehlt derzeit eine begründete Grundlage. Hohe Nutzungsbereitschaft sollte beispielsweise geringe Kompetenz nicht rechnerisch verdecken.
Prompt, Quellen und Ergebnisse versionieren. Gleiche Eingaben garantieren bei Sprachmodellen keine identischen Ausgaben. Dokumentierte Quellenstände, Promptversionen, Testfälle und Prüfkriterien machen Abweichungen nachvollziehbar.
Bei der Evaluation sollten wir zwei Ebenen unterscheiden: Erzeugt der Masterprompt fachlich nachvollziehbare Fragebögen? Und messen diese Fragebögen tatsächlich das beabsichtigte Merkmal?
Die erste Ebene lässt sich im Rahmen der Hausarbeit durch festgelegte Unternehmensszenarien, wiederholte NotebookLM-Durchläufe und einen Vergleich zwischen Ausgangsprompt und verbesserten Versionen untersuchen. Bewertet werden etwa Quellenkorrektheit, Konstruktzuordnung, Verständlichkeit, Vollständigkeit und Stabilität des Kernfragebogens. Jede Änderung wird mit einem beobachteten Problem begründet. Ein solcher Wechsel zwischen Entwicklung und Evaluation entspricht dem DSR-Gedanken. FEDS-Evaluationsrahmen

Für die zweite Ebene wären Rückmeldungen echter Mitarbeitender und anschließend geeignete Befragungsdaten erforderlich. Simulierte Befragte oder eine zweite KI können zusätzliche Prüfhinweise liefern; ihre Rückmeldungen belegen keine psychometrische Messqualität.

Für die zehn inhaltstragenden Seiten würde ich deshalb die begründeten Entwicklungsentscheidungen und die tatsächlich durchgeführte Evaluation in den Mittelpunkt stellen. Vollständige Items, Promptversionen, Quellenzuordnungen und Testprotokolle können ergänzend im GitHub-Projekt dokumentiert werden.

Bevor wir das Messmodell und die erste Promptversion festlegen, helfen mir diese fünf Antworten:

Welche KI ist gemeint? Generative KI wie ChatGPT und Copilot oder auch andere KI-Systeme?
Wer soll befragt werden und wozu? Beispielsweise Büro- und Wissensarbeitende, sämtliche Beschäftigte einschließlich Produktion – und sollen daraus vor allem Weiterbildungsbedarfe, Einführungsentscheidungen oder Unternehmensvergleiche entstehen?
Welche praktische Evaluation ist möglich? Hast du Zugang zu Mitarbeitenden für einen kurzen Verständlichkeitstest oder zu Fachpersonen für eine inhaltliche Prüfung? Ist eine echte Befragung vorgeschrieben?
Wie weit soll der Masterprompt reichen? Nur bis zum Fragebogen oder auch bis zu Auswertungsregeln und einem Ergebnisbericht aus späteren Antworten?
Welche formalen Vorgaben gelten zusätzlich? Abgabetermin, Zitierstil, Bewertungsraster und Regelungen dazu, ob Tabellen und Abbildungen zu den zehn Seiten zählen.
Mit diesen Antworten können wir die Breite des Vorhabens so festlegen, dass das Ergebnis wissenschaftlich nachvollziehbar und innerhalb der Hausarbeit tatsächlich überprüfbar bleibt.

Pruefungsleistung_v2.pdf
PDF

Formatvorlage Master CMP_2023_V3_Fend.docx
Dokument

EV Bogen_Praxismodul.pdf
PDF
Ja beschränken wir uns auf generative KI; Ziel soll sein den Status Quo und Weiterbildungsbedarf aufzudecken im gesamte Unternehmen; eine echte Befragung ist nicht vorgeschrieben, ich würde es aber 5 testpersonen geben zur evaluierung. der masterprompt soll komplett den ganzen prozess abdecken. formale vorgaben der wings; zitierstil nach apa, abgabetermin ist der 1. november; themeneintragung bis spätestens 18. oktober. evaluationsbogen findest du im anhang (es ist aber keine verteidigung vorgesehen dieses semester; tabellen und abbildungen sofern sie zur erklärung beitragen gehören zum inhalt der 10 seiten also von der einleitung bis zum fazit. github ist dann der fokus, wenn nötig können wir auch ein readme erstellen, im letzten tutorium wurde noch gesagt, dass wir nicht zwingend notebooklm nutzen müssen, aber können. wir können sämtliche ki-systeme, agenten, etc. heranziehen wenn es notwendig ist und zur praktischen lösung beiträgt.
Ich habe deine Festlegungen und die beiden neuen Anhänge in eine erste Projektfassung mit Masterprompt, Evaluationsplan und README überführt. NotebookLM ist darin optional; die Plattformwahl richtet sich nach den benötigten Funktionen.
Die Dateien findest du hier:

GenAI_Readiness_Projektpaket_v0.1.zip
 – vollständiges Paket mit acht Dateien.
Projektgrundlage.md
 – Thema, Forschungsfrage, Messmodell, Gliederung und Zeitplan.
MASTERPROMPT.md
 – erste Arbeitsfassung für den gesamten Prozess.
Evaluation.md
 – konkrete Prüfungen und Leitfaden für die fünf Testpersonen.
Für die Themeneintragung empfehle ich diesen Titel:
Entwicklung und formative Evaluation eines theoriegestützten Masterprompts zur Erfassung der Readiness für generative KI und des Weiterbildungsbedarfs von Mitarbeitenden

Die zentrale Forschungsfrage dazu lautet:

Wie lässt sich ein theoriegestützter Masterprompt gestalten und formativ evaluieren, der unternehmensübergreifend standardisierte Fragebögen zur Readiness für generative KI erstellt und aus erhobenen Antworten nachvollziehbare Hinweise auf Weiterbildungsbedarf ableitet?

„Formative Evaluation“ beschreibt dabei die Prüfung während der Entwicklung, aus der konkrete Verbesserungen entstehen. Das passt zum geplanten Umfang und vermeidet ein Validierungsversprechen, das wir mit fünf Personen nicht einlösen können.

Der Masterprompt führt durch mehrere Arbeitsschritte:

Schritt	Ergebnis
Unternehmenskontext und Quellen prüfen	Dokumentierte Ausgangslage und geeignete Konstrukte
Fragebogen entwickeln	Fragen mit nachvollziehbarer Herkunft und gekennzeichneten Anpassungen
Anwendung vorbereiten	Fester Fragebogenkern, Kontextmodule und Auswertungsregeln
Pretest verarbeiten	Befunde und begründete Änderungen
Antworten auswerten	Nachvollziehbare Berechnungen und getrennte Dimensionsprofile
Maßnahmen ableiten	Hinweise auf Weiterbildung und organisatorischen Handlungsbedarf
Besonders wichtig für dein Ziel ist die Trennung zwischen Lernbedarf und betrieblichen Hindernissen. Wer kein freigegebenes Werkzeug nutzen kann, benötigt möglicherweise zuerst Zugang. Wer Ergebnisse schwer beurteilen kann, könnte von einer entsprechenden Lernaufgabe profitieren. Der Bericht soll deshalb jede Empfehlung auf konkrete Antworten zurückführen. Selbsteinschätzungen bleiben dabei als solche erkennbar.
Für die fünf Testpersonen habe ich zwei Runden mit drei und zwei Personen vorgesehen. Nach der ersten Runde können wir problematische Formulierungen überarbeiten und anschließend erneut prüfen. Im Protokoll bleibt ausdrücklich stehen, welche Fassung von welchen Personen getestet wurde.

Die Personen sollen nicht nur ankreuzen, ob ihnen der Fragebogen gefällt. Mit kurzen Nachfragen prüfen wir, wie sie einzelne Aussagen verstanden haben und wie sie zu ihrer Antwort gekommen sind. Das entspricht dem Ansatz kognitiver Interviews. Die fünf Personen ermöglichen eine begrenzte explorative Prüfung; Repräsentativität oder statistische Messqualität können wir daraus nicht ableiten. Methodenbeschreibung des NCHS

Zusätzlich enthält der Evaluationsplan einen Vergleich zwischen einem einfachen Ausgangsprompt und dem entwickelten Masterprompt. Beide erhalten dieselben Quellen und Eingaben. Geprüft werden unter anderem Quellenkorrektheit, unveränderte Kernfragen und der Umgang mit fehlenden Daten. Die fünf Testpersonen allein würden die Funktionsfähigkeit des gesamten Prozesses noch nicht prüfen.

Aus deinen Anhängen ergeben sich außerdem zwei Konsequenzen:

Der Bewertungsbogen betont wissenschaftliche Herleitung, praktische Lösungsqualität und begründete Evaluation. Diese Kriterien berücksichtige ich; seine Präsentations- und Disputationsanteile übertrage ich entsprechend deiner aktuellen Vorgabe nicht auf die Arbeit.
Die Word-Datei enthält bereits eine andere Hausarbeit. Ihre Formatierung dient als Ausgangspunkt; Titelblatt, Verzeichnisse und modulbezogene Angaben müssen für dieses Projekt angepasst werden.
Das Seitenbudget ist auf zehn Seiten einschließlich erklärender Tabellen und Abbildungen ausgelegt. Der Zeitplan berücksichtigt die Themeneintragung spätestens am 18. Oktober 2026 und die Abgabe am 1. November 2026.
Die Dateien sind eine erste Entwicklungsfassung. Die konkrete Itembank und die tatsächlichen Testergebnisse stehen noch aus. Der nächste fachliche Schritt ist deshalb der genaue Abgleich geeigneter Originalitems und ihrer Anpassungen an generative KI. Daraus entsteht die erste Befragungsfassung, die du anschließend deinen fünf Testpersonen geben kannst.

Projektgrundlage.md
Dokument

MASTERPROMPT.md
Dokument

Evaluation.md
Dokument
Okay, ich hab mir alle Unterlagen durchgesehen, dann lass uns bitte mit dem nächsten Schritt fortfahren
Die erste Fragebogenfassung mit 34 Fragen ist fertig. Dazu habe ich Herkunft und Anpassungen jeder Frage dokumentiert, Auswertungsregeln festgelegt und den Masterprompt aktualisiert.
Für den nächsten Schritt brauchst du diese Dateien:

Fragebogen_GARI_DE_0.1.docx
 – Befragungsfassung, geschätzte Bearbeitungszeit 10–15 Minuten.
Pretestleitfaden_und_Notizbogen.docx
 – Gesprächsanleitung und Protokollvorlage.
GenAI_Readiness_Projektpaket_v0.2.zip
 – vollständiges Paket mit Itemregister, Codebuch, Masterprompt und technisch geprüfter Python-Auswertung.
Die MAILS-Grundlage erfasst Selbsteinschätzungen zu allgemeiner KI. Unsere Anpassung auf generative KI und die neue Kombination sind deshalb noch nicht psychometrisch validiert.  Ein noch offener Originalquellenabgleich bei den PowerPilot-Items ist im Register ausgewiesen.
Jetzt starten wir mit drei Testpersonen. Plane jeweils ungefähr 30 Minuten einschließlich Nachgespräch ein und verwende bei allen dieselbe Fassung. Schick mir anschließend die Notizbögen ohne Namen. Daraus leiten wir dokumentierte Änderungen ab und prüfen die überarbeitete Fassung mit den beiden weiteren Personen.

Fragebogen_GARI_DE_0.1.docx
Word

Pretestleitfaden_und_Notizbogen.docx
Word
Hier findest du nun die Antworten der drei Testpersonen: [Link entfernt: Antworttabelle R1]
Ich bin folgendermaßen vorgegangen: Ich habe den Pretestleitfaden sowie den Fragebogen an Google Forms übermittelt und daraus via Google Forms das Formular zum Fragebogen erstellen lassen (Prompt: Kannst du mir bitte unter Berücksichtigung des Dokuments „Pretestleitfaden_und_Notizbigen_docx“ folgenden Fragebogen erstellen „ Fragebogen_GARI_DE_0.1.docx")„: [Link entfernt: Formular R1] Beschreibungen, Hinweise, etc. habe ich lt. Pretestleitfaden manuell ergänzt. Das geplante Gespräch jeweils nach Beantwortung der Fragen habe ich vereinfacht in Form von einem "Virtuellen Gespräch" nach Beantwortung der Fragen durchgeführt. Was wir berücksichtigen müssen bei der Erstellung realer Fragebögen: Google Forms war nicht in der Lage bei den skalenbasierten Antworten vom z.B Abschnitt Anwendung und Verständnis die Bedingungen KA und NB hinzuzufügen.
Ich habe die drei Antworten und das Formular geprüft. Die erste Runde liefert verwertbare Befunde für die Weiterentwicklung. Vor den zwei weiteren Tests sollten wir die Forms-Umsetzung korrigieren.
Die wichtigsten Ergebnisse:

NB und KA fehlen tatsächlich bei allen 25 Zahlenfragen. Google Forms kann diese Optionen grundsätzlich abbilden: als Multiple-Choice-Einzelwahl mit den Zahlen sowie „Nicht beurteilbar“ und „Keine Angabe“. Die Einschränkung betrifft den verwendeten Fragetyp „Lineare Skala“.
Einige Pflichtfelder passen nicht zum vorgesehenen Ablauf. Insbesondere I02 erzwingt eine Zahlenantwort. Auch W03 und die Rückfrage speziell an Nichtnutzende sind verpflichtend.
Die schriftlichen Rückfragen müssen getrennt werden. Antworten wie „Ja“ auf drei gleichzeitig gestellte Fragen lassen sich nicht eindeutig interpretieren. Für die Hausarbeit beschreiben wir dein Vorgehen als schriftliche Nachbefragung mit kognitiven Prüffragen.
Alle drei Personen nutzen bereits GenAI. Für Runde 2 sollte möglichst eine Person ohne bisherige Nutzung hinzukommen.
Inhaltlich wünschen sich zwei Personen Weiterbildung zum Formulieren von Eingaben; zwei nennen fehlende Zeit als Hindernis. Das sind konkrete Angaben dieser Testgruppe, noch kein Unternehmensprofil.
Ich habe daraus folgende Dateien erstellt:

Pretest_Runde1_Auswertung.md
 – Befundmatrix, Interpretationsgrenzen und Textbaustein für die Hausarbeit.
GoogleForms_Runde2_Anleitung.md
 – konkrete Einstellungen, Kopierprompt und einzeln formulierte Rückfragen.
GenAI_Readiness_Projektpaket_v0.3.zip
 – aktualisierter Masterprompt, Evaluationsdokumentation und README.
Als Nächstes: eine Formularkopie nach der Anleitung anpassen, prüfen und anschließend mit den zwei weiteren Personen testen.
Eine Frage zur korrekten Dokumentation: Hast du das Formular nach den drei Teilnahmen noch verändert? Davon hängt ab, ob wir die heute beobachteten Pflichtfeldeinstellungen sicher dem damaligen Test zuordnen können.

Pretest_Runde1_Auswertung.md
Dokument

GoogleForms_Runde2_Anleitung.md
Dokument
Nein das Formular habe ich nach den drei Teilnahmen nicht mehr verändert. Erst jetzt zu deinen Anweisungen. Wie von dir vorgeschlagen, habe ich deinen Prompt genutzt um den Fragebogen in der neuen Fassung zu erstellen: [Link entfernt: Formular R2] Anweisungen und Beschreibungen habe ich wieder händisch ergänzt. Zur Überprüfung habe ich dieses Mal mit Claude im Browser gearbeitet und zwei fiktive Personas erstellt, die den Fragebogen beantworten sollen.  Prompt 1: Stell dir folgende einmalige Situation vor, du bist ein ca. 45 Jähriger Facharbeiter am Bau (hauptsächlich Bau von Ziegelmassivhäusern) und sollst diesen Fragebogen ausfüllen: [Link entfernt: Formular R2]
Du hattest davor noch nicht wirklich mit ChatGPT & Co gearbeitet, nur aus dem Radio und Fernsehen davon gehört. Interessant findest du es schon, aber auch gruselig. Fülle unter diesen Voraussetzungen bitte den Fragebogen unter dem Link aus.

Prompt 2:
Stell dir folgende einmalige Situation vor, du bist eine ca. 40 Jährige Angestellte im Bereich Marketing (hauptsächlich Digitales Marketing und Social Media) und sollst diesen Fragebogen ausfüllen: 
Du arbeitest regelmäßig mit ChatGPT & Co und hast auch an Schulungen zu diesem Thema teilgenommen. Privat nutzt du deine Accounts auch täglich. Einerseits sparst du durch die Anwendung von KI sehr viel Zeit ein, andererseits hast du manchmal auch Bedenken hinsichtlich Datenschutz. Fülle unter diesen Voraussetzungen bitte den Fragebogen unter dem Link aus.

Das sind die Antworten: 
…
Ich habe die neue Formularfassung und beide Antwortdatensätze geprüft. NB/KA sind jetzt bei allen 25 skalenbasierten Fragen vorhanden; auch das Überspringen freiwilliger Fragen funktioniert. Deine Bestätigung zur unveränderten ersten Formularfassung ist ebenfalls dokumentiert.
Vor den nächsten echten Teilnahmen bleiben drei gezielte Korrekturen:

Rückmeldungsfragen entflechten: PF03–PF10 bündeln weiterhin mehrere Fragen. Die aktualisierte Anleitung enthält die zehn vorgesehenen Rückmeldungsfragen jetzt vollständig im kopierbaren Prompt.
Auswahlgrenze prüfen: Bei W01 und W02 konnte ich jeweils vier Optionen auswählen und zur nächsten Seite weitergehen, obwohl höchstens drei vorgesehen sind. Google Forms unterstützt dafür eine Antwortvalidierung „Höchstens auswählen: 3“. Nach dem Einstellen bitte nochmals prüfen.
Hinweise vereinheitlichen: Formulierungen wie „im anschließenden Gespräch“ und „Kreisen Sie … ein“ passen noch nicht zum schriftlichen Feedback und digitalen Formular.
Die Claude-Durchläufe sind als ergänzende synthetische Tests brauchbar. Im Export stehen 46 gültige Zahlenwerte und vier NB-Antworten. Beim Bauarbeiter bleiben allerdings drei Kontextfragen leer – darunter die Nutzungshäufigkeit, obwohl im späteren Freitext „an keinem Tag“ genannt wird. Diese Lücken dürfen wir nicht nachträglich aus der Rollenbeschreibung oder dem Freitext auffüllen.
Für die Hausarbeit bleibt der Evaluationsstand deshalb drei reale Testpersonen plus zwei synthetische Testfälle. Die KI-Antworten liefern Hinweise für weitere Prüfungen; sie belegen keine Verständlichkeit für tatsächliche Beschäftigte. Beispielsweise ergänzt die Marketing-Persona Unternehmensregeln, die dein Prompt gar nicht vorgibt.

Ich habe den Prüfbericht, den Masterprompt, die Evaluationsdokumentation und das GitHub-Projektpaket entsprechend aktualisiert:

GenAI_Readiness_Projektpaket_v0.4.zip
Der nächste Schritt sind diese Korrekturen in einer Formularkopie als R2.1, eine kurze Funktionsprüfung und anschließend die zwei noch geplanten echten Testpersonen. Ein vollständiger Neuaufbau ist dafür nicht erforderlich.
Für das Testprotokoll fehlen mir noch zwei Angaben: Welche Claude-Modellversion hast du verwendet, und liefen die Personas jeweils in einem eigenen neuen Chat?

Forms_R2_Claude_Pruefbericht.md
Dokument

GoogleForms_Runde2_Anleitung.md
Dokument
Claude Opus Mittel 5.5 jeweils eigene Chats im Browser, unabhängig voneinander. Die Prompts waren bewusst eher freier gestaltet um der KI Freiheit hinsichtlich der Interpretation zu geben. Echte Testpersonen sind nun keine mehr geplant. Es bleibt bei 3 + 2. Die Änderungen habe ich gerade manuell durchgeführt: [Link entfernt: Formular R3] Bitte lass uns nun weiter vorankommen
was ist passiert?
was ist passiert ?
Bist du noch da?
Ja, ich bin da. Entschuldige die lange Wartezeit. Die Dateien sind jetzt erstellt und geprüft:
Vollständiger Entwurf mit zehn Inhaltsseiten, zusätzlich Deckblatt, Verzeichnissen und APA-Literaturverzeichnis. Enthält DSR-Vorgehen, Entwicklung, Evaluation und Grenzen.

GenAI_Readiness_Projektpaket_v0.5.zip

Aktualisiertes Paket für GitHub mit Masterprompt, README, Fragebogenbasis, Auswertungscode und Evaluationsdokumentation.
Dokumentiert die Prüfung deiner neuesten Formularfassung und die verbliebenen Detailpunkte.
Deine Festlegung „3 reale Testpersonen + 2 KI-Personas“ ist übernommen. Beide Datenarten werden getrennt behandelt; weitere Testpersonen sind nicht eingeplant. Auch die getrennten Claude-Chats und die bewusst offenen Persona-Prompts sind dokumentiert.
Im neuen Formular habe ich die NB-/KA-Optionen, die zehn einzelnen Rückfragen und die funktionierende Begrenzung auf drei Antworten bestätigt.

Für den Abschluss bleiben die persönlichen Deckblattangaben, die dokumentierten Quellen- und Nachnutzungsfragen sowie die tatsächliche Veröffentlichung auf GitHub offen. Die Hausarbeit liegt damit als durchgehender Entwurf zur Endredaktion vor.

Hausarbeit_GenAI_Readiness_Entwurf.docx
Word

Abschluss_Evaluation_R3.md
Dokument
Bitte stelle mir den kompletten Verlauf dieses Chats inkl. aller Verwendeter Quellen als PDF zum Export zur Verfügung
Die PDF enthält die verfügbaren Originalnachrichten, das dokumentierte Quellenverzeichnis und 28 anklickbare Webadressen.
Es ist leider kein vollständiger Chat-Export: Ältere Assistentenantworten sind mir teilweise nicht mehr im Original zugänglich. Diese Lücken sind ausdrücklich gekennzeichnet; fehlende Nachrichten habe ich nicht erfunden.

Für den gewünschten lückenlosen Export benötige ich den vollständigen Originalchat als Text- oder HTML-Datei. Lade ihn bitte hier hoch, damit ich die PDF vervollständigen kann.

Chatverlauf_GenAI_Readiness_Teil_Export_2026-10-18.pdf
PDF
