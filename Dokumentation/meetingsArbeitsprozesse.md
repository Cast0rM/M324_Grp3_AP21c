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
soll man in diesem Meeting Zeit haben dies anzusprechen. 

Ablauf:

Zuerst erzählt jeder was er als nächstes macht. Danach werden, wenn nötig, die Gewichtungen für die nächsten Tasks definiert. 

### Review
Beschreibung:

Um 11:15 haben wir unser Review. Dort erzählen wir was wir gemacht haben. Hier hat man ebenfalls Zeit Probleme anzusprechen.

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