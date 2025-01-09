# Testkonzept für die Musikplattform

## Ziel des Testkonzepts
Das Ziel des Testkonzepts ist die Sicherstellung der Funktionalität, Validität und Interoperabilität der beiden Mikroservices **Verwaltung von Bands** und **Verwaltung von Alben**. Dies erfolgt durch strukturierte Unit- und Integrationstests, um die Anforderungen aus den User Stories abzudecken.

---

## Testumfang

### Mikroservice 1: Verwaltung von Bands
- **Funktionalität zur Erfassung neuer Bands**: Validierung und Speicherung der Eingabedaten, Generierung einer eindeutigen ID und Rückgabe der vollständigen Daten.
- **Funktionalität zum Abrufen aller Bands**: Anzeige der Bandübersicht mit vollständigen Daten, inklusive Performanztests bei großen Datenmengen.

### Mikroservice 2: Verwaltung von Alben
- **Funktionalität zur Erfassung neuer Alben**: Validierung der Eingabedaten, Verknüpfung eines Albums mit einer bestehenden Band (über Mikroservice 1) und Speicherung der Albumdaten.

---

## Teststrategie

### Unit Tests
- **Ziel**: Testen einzelner Funktionen und Komponenten der Mikroservices in Isolation.
- **Methodik**: Tests werden gegen die Business-Logik, Validierungen und Datenpersistierung ausgeführt.
- **Werkzeuge**: Tools wie JUnit (Java), pytest (Python) oder ähnliche je nach Programmiersprache.

### Integrationstests
- **Ziel**: Sicherstellen der korrekten Zusammenarbeit zwischen den beiden Mikroservices und ihrer Abhängigkeiten.
- **Methodik**: Fokus auf API-Kommunikation, Datenflüsse und Fehlerhandling bei Service-Interaktionen.
- **Werkzeuge**: REST-Assured, Postman oder vergleichbare Tools für API-Tests.

---

## Testfälle

### Unit Tests

#### Mikroservice 1: Verwaltung von Bands

| **Testfall-ID** | **Funktion**                  | **Positiver Testfall**                                | **Negativer Testfall**                                |
|------------------|-------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| UT-MS1-01        | Validierung: Name             | Gültiger Name wird akzeptiert.                        | Leerer Name gibt Fehlermeldung zurück.                |
| UT-MS1-02        | Validierung: Genre            | Gültiges Genre wird akzeptiert.                       | Leeres Genre gibt Fehlermeldung zurück.               |
| UT-MS1-03        | Validierung: Gründungsdatum   | Gültiges Datum wird akzeptiert.                       | Ungültiges Datum führt zu Fehlermeldung.              |
| UT-MS1-04        | Validierung: Bandmitglieder   | Positive Zahl wird akzeptiert.                        | Negative Zahl gibt Fehlermeldung zurück.              |
| UT-MS1-05        | Validierung: Auflösungsdatum  | Datum nach Gründungsdatum wird akzeptiert.            | Auflösungsdatum vor Gründungsdatum gibt Fehlermeldung.|
| UT-MS1-06        | Persistierung: Bands speichern| Banddaten werden korrekt gespeichert.                 | Fehlerhafte Speicherung führt zu einer Fehlermeldung. |

#### Mikroservice 2: Verwaltung von Alben

| **Testfall-ID** | **Funktion**                  | **Positiver Testfall**                                | **Negativer Testfall**                                |
|------------------|-------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| UT-MS2-01        | Validierung: Titel            | Gültiger Titel wird akzeptiert.                       | Leerer Titel gibt Fehlermeldung zurück.               |
| UT-MS2-02        | Validierung: Preis            | Positiver Preis wird akzeptiert.                      | Negativer Preis gibt Fehlermeldung zurück.            |
| UT-MS2-03        | Validierung: Veröffentlichungsdatum | Gültiges Datum wird akzeptiert.                       | Ungültiges Datum führt zu Fehlermeldung.              |
| UT-MS2-04        | Validierung: Band-Existenz    | Band wird erfolgreich durch Mikroservice 1 validiert. | Ungültige Band-ID führt zu Fehlermeldung.             |

---

### Integrationstests

| **Testfall-ID** | **Schnittstelle**                        | **Positiver Testfall**                                | **Negativer Testfall**                                |
|------------------|------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| IT-MS1-MS2-01    | Band-Validierung bei Album-Erfassung     | Gültige Band-ID wird durch Mikroservice 1 validiert.  | Ungültige Band-ID führt zu Fehlermeldung.             |
| IT-MS1-MS2-02    | Abrufen aller Bands                     | Alle Bands werden korrekt und vollständig angezeigt.  | Fehlerhafte Abfrage liefert Fehlermeldung.            |
| IT-MS2-03        | Verknüpfung Album mit Band              | Album wird erfolgreich mit bestehender Band verknüpft.| Album wird nicht gespeichert, wenn Band-ID ungültig.  |

## Testumgebung
- **Entwicklungssprachen**: Die Unit- und Integrationstests berücksichtigen unterschiedliche Sprachen für die Mikroservices (z. B. Java für MS1, Python für MS2).
- **Datenbanken**: Separate Datenbanken werden verwendet, mit Testdatensätzen für jede Mikroservice-Umgebung.
- **Testtools**:
  - Unit Testing: JUnit, pytest
  - API Testing: Postman, REST-Assured
  - Mocking: Mockito, WireMock

---

## Testdurchführung
1. **Unit Tests**
   - Durchführung in der Entwicklungsumgebung.
   - Tests werden als Teil der CI/CD-Pipeline ausgeführt.
2. **Integrationstests**
   - Ausführung in einer isolierten Testumgebung mit Mock-Daten und getrennten Instanzen der Mikroservices.

---

## Abschlusskriterien
- Alle Unit Tests und Integrationstests müssen erfolgreich bestanden sein.
- Bei negativem Testfall müssen aussagekräftige Fehlermeldungen angezeigt werden.
- Performanztests für große Datenmengen (Bands und Alben) müssen innerhalb der akzeptablen Grenzwerte liegen.

---

Dieses Testkonzept bietet eine umfassende Grundlage für die Überprüfung der Funktionalität und Interoperabilität der Musikplattform.
