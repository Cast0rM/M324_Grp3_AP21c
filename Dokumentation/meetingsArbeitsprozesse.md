## Tasks
Jeder Task soll ein Label, ein Projekt, ein Titel und Beschreibung, einen Status und eine Gewichtung haben. Die Gewichtung soll per Label angefügt werden.

Die Subtasks werden wie normale Tasks erstellt und dann mit einem Hashtag in der Beschreibung des Parenttasks referenziert. 

## Git board
In unserem Projekt "Musikplatform" haben 5 Spalten. Vier davon repräsentiert einen Status.
Und eine Spalte ist für die Tasks die keinen Status haben. 

Die Spalte für Stories ohne Status heisst "Backlog". 
Backlog bedeuted, dass diese Story nicht nocht behandelt wird. Sie soll erst in Zukunft bearbeited werden.

Die Stories in der Spalte "Todo" werden als nächstes behandelt. Die Stories in Todo müssen an jemanden zugewiesen.

Die Spalte für den Status "In Progress" beinhaltet die Stories, die gerade in bearbeitung sind. 

Die Stories in "Review Testing" sind schon bearbeited worden, müssen jedoch noch von einem anderem Teammitglied überprüft werden. 
Die changes die gemacht wurden sind in einem Merge Request. Dort können sie dann einfach überprüft werden.
Bei Fehlern kann dies Rückgemeldet werden. Wenn es keine Fehler hat, kann man den Merge Request annehmen und die Storie kommt in die nächste Spalte.
Nur bei Code wird reviewed. 

In der Spalte "Done" landen die Stories die fertig sind. Wenn eine Storie in diesem Status ist, soll sie nie mehr berabeited werden müssen.

## Meetings
### Daily
Beschreibung:

Um 9:30 Uhr haben wir unser Daily. In diesem Meeting besprechen wir unsere nächsten Schritte und unser Standpunkt. Bei möglichen Problemen,
soll man in diesem Meeting Zeit haben dies anzusprechen. Ebenso kann man Theorie Tasks besprechen, damit alle auf gleichem stand sind.

Ablauf:

Zuerst erzählt jeder was er als nächstes macht. Dann gibt es die zusamenfassungen. Danach werden, wenn nötig, die Gewichtungen für die nächsten Tasks definiert. 

### Review
Beschreibung:

Das Review ist ein optionales Meeting, welches nur durchgeführt wird, wenn man es braucht um etwas zu besprechen, was man an diesem Tag gemacht hat oder ob es Probleme gibt/gab.

Ablauf:

Jeder der etwas Präsentieren kann präsentiert seine Arbeit. Code muss nicht präsentiert werden. Wenn es nichts zu präsentieren gibt, wird das Meeting übersprungen.

### Daily-Meeting 05.12.2024

Wir haben alle Tasks die den Status "In Progress" oder "Done" haben besprochen, Wichtig hier war zu wissen wer was gemacht hat und wie weit sie sind. Den Austausch der Theorie die Bearbeitet wurde haben wir auch gemacht. Danach haben wir alle neue Tasks erstellt, ihre subtasks erstellt und das Besprochen was nötig war, damit alles funktioniert. Zum schluss haben wir noch eine Zeiteinschätzung gemacht.

#### Entscheidungen die Getroffen wurden.
- **SQL:** Jeder hat auf seinem Gerät einen einzelnen Docker Container worauf die SQL-Test Datenbank läuft.
- **API:** Die Struktur des Projektes wird auf Docker gepusht damit, jeder den gleichen Stand der Applikation hat und die nicht immer neu Installieren muss.
Branching Strategie wurde definiert, wir nutzen die GitHub Flow Branching Strategie. Beispiel: feature/CreateDB
Für das Pushen der Dokumentations Dateien ist das Branching nicht nötig.
#### Tasks
- API-Endpoints Programmieren
- Dockerfile erstellen.
- Subtasks erstellt
- Zeiteinschätzung

### Daily-Meeting 16.01.2025

Heute haben wir kein guten Meeting gemacht, zu kurz un präzise und die Organisation der verschiedenen Contributors wurden fast vergessen. Dadurch dass Herr Nussle eingegrifen und ein Feedback gegeben hat, haben wir gewisse Tasks erstellen und zuweisen können. Wir haben auch mit der Zuweisung der Meeting Dokumentations Rolle fehlgeschlagen, da niemand diese Dokumentationen gemacht hat.

#### Entscheidungen die Getroffen wurden
An diesem Tag wurden keine Entscheidungen getroffen, wir haben uns daran erinnert, dass wir unser deployment auf ein Cluster mit Kubernetes machen wollten.

#### Tasks
- System Tests mit Postman
- CD Prozess umsetz
- TestKonzept anpassung
- Code Quality mit sonar / flake8

### Daily-Meeting 23.01.2025
Wir haben die CD-Pipeline gemacht anhand eines Selfrunners, testkonzept ist für unit-tests und code quality check fertig muss aber noch für restliche integrationtests gemacht werden. Heute im Meeting haben wir auch noch die Zeiteinschätzung der verschiedene Tasks gemacht.

#### Entscheidungen die Getroffen wurden
keine

#### Tasks
- Integration test
- Kennzahlen
- CD-Prozess machen
- DB Bands erstellen
- CI/CD Dokumentation