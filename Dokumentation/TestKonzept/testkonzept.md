# Testkonzept für die Applikation `app`

## 1. Zielsetzung
Das Ziel des Testkonzepts ist die Sicherstellung der Funktionalität der API und der Datenbankoperationen der `app`. Dabei wird ein besonderer Fokus auf die korrekte Interaktion zwischen den Services und die Vermeidung ungewollter Datenbankaufrufe gelegt.

---

## 2. Testbereiche
Basierend auf dem Code können die folgenden Testbereiche identifiziert werden:

1. **Session Management:**
   - Sicherstellen, dass die Sessions (`mock_album_session`, `mock_bands_session`) korrekt initialisiert werden und keine unerwarteten Datenbankaufrufe erfolgen.

2. **CRUD-Operationen:**
   - Überprüfung der Leseoperationen für Alben (`Album`) und Bands (`Bands`).
   - Validierung der Funktionalität, eine Band über die ID zu lesen.

3. **Mock-Integration:**
   - Verifikation, dass Datenbankoperationen durch Mocking simuliert werden, um die echte Datenbank nicht zu belasten.

4. **Datenkonsistenz:**
   - Sicherstellen, dass die zurückgegebenen Objekte den erwarteten Attributwerten entsprechen.

---

## 3. Testfälle

### 3.1 Session Management
- **Testfall:** Validierung der Album-Session.
  - **Voraussetzung:** `mock_album_session` und `mock_album_engine` sind bereitgestellt.
  - **Schritte:** 
    1. Initialisiere `mock_album_session`.
    2. Verifiziere, dass keine Datenbankabfragen ausgeführt wurden.
  - **Erwartetes Ergebnis:** `mock_album_session.execute` wird nicht aufgerufen.

- **Testfall:** Validierung der Bands-Session.
  - **Voraussetzung:** `mock_bands_session` und `mock_bands_engine` sind bereitgestellt.
  - **Schritte:** 
    1. Initialisiere `mock_bands_session`.
    2. Verifiziere, dass keine Datenbankabfragen ausgeführt wurden.
  - **Erwartetes Ergebnis:** `mock_bands_session.execute` wird nicht aufgerufen.

---

### 3.2 Lesen von Alben
- **Testfall:** Abrufen aller Alben.
  - **Voraussetzung:** `mock_album_session` ist bereitgestellt.
  - **Schritte:** 
    1. Simuliere eine Abfrage mit `mock_album_session.query(models.Album).all()`.
    2. Überprüfe, dass `query` und `all` korrekt aufgerufen werden.
    3. Simuliere eine Rückgabewertliste mit mindestens einem Album.
    4. Validiere die zurückgegebenen Werte (z. B. Titel, Preis).
  - **Erwartetes Ergebnis:**
    - `query` wird einmal aufgerufen.
    - `all` liefert korrekte Attribute (z. B. `title="Test Album"`, `price=10.25`).

---

### 3.3 Lesen von Bands
- **Testfall:** Abrufen aller Bands.
  - **Voraussetzung:** `mock_bands_session` ist bereitgestellt.
  - **Schritte:** 
    1. Simuliere eine Abfrage mit `mock_bands_session.query(models.Bands).all()`.
    2. Überprüfe, dass `query` und `all` korrekt aufgerufen werden.
    3. Simuliere eine Rückgabewertliste mit mindestens einer Band.
    4. Validere die zurückgegebenen Werte (z. B. Name, Genre).
  - **Erwartetes Ergebnis:**
    - `query` wird einmal aufgerufen.
    - `all` liefert korrekte Attribute (z. B. `name="Queen"`, `genre="Rock"`).

---

### 3.4 Lesen einer Band nach ID
- **Testfall:** Abrufen einer spezifischen Band über ID.
  - **Voraussetzung:** `mock_bands_session` ist bereitgestellt.
  - **Schritte:**
    1. Simuliere eine Abfrage mit `mock_bands_session.query(models.Bands).filter_by(band_id=<id>).first()`.
    2. Überprüfe, dass `query`, `filter_by` und `first` korrekt aufgerufen werden.
    3. Simuliere eine Rückgabe mit einer spezifischen Band.
    4. Validere die zurückgegebenen Werte (z. B. Name, Genre).
  - **Erwartetes Ergebnis:**
    - `query`, `filter_by` und `first` werden jeweils einmal aufgerufen.
    - Die zurückgegebene Band hat die erwarteten Werte (z. B. `name="Queen"`, `genre="Rock"`).

- **Testfall:** Abrufen einer nicht existierenden Band über ID.
  - **Voraussetzung:** `mock_bands_session` ist bereitgestellt.
  - **Schritte:**
    1. Simuliere eine Abfrage mit `mock_bands_session.query(models.Bands).filter_by(band_id=<id>).first()`.
    2. Überprüfe, dass keine Band gefunden wird.
  - **Erwartetes Ergebnis:**
    - `filter_by` liefert kein Ergebnis (Rückgabewert ist `None`).

---

## 4. Testansatz
- **Unit Tests:** Für jeden Bereich wird ein isolierter Test geschrieben, um die Funktionalität einzelner Komponenten zu verifizieren.
- **Mocking:** Verwenden von Mock-Objekten für Sessions und Datenbank-Engines, um echte Datenbankaufrufe zu vermeiden.
- **Datenvalidierung:** Überprüfung der Konsistenz der zurückgegebenen Mock-Daten.
- **Automatisierung:** Die Tests werden mit `pytest` automatisiert.

---

## 5. Qualitätskriterien
- 100% Abdeckung der im Testkonzept beschriebenen Szenarien.
- Simulierte Daten müssen den erwarteten Modellen entsprechen (`models.Album`, `models.Bands`).
- Es dürfen keine echten Datenbankaufrufe ausgeführt werden.
- Tests müssen deterministisch und reproduzierbar sein.

---

## 6. Nicht abgedeckte Bereiche
- Schreiboperationen (z. B. Erstellen, Aktualisieren, Löschen).
- Integrationstests mit einer echten Datenbank.

# Integration Tests
## 1. Code-Qualitätsprüfung mit Flake8

Dieser Integrationstest stellt sicher, dass der Code den PEP-8-Standards entspricht und keine kritischen Syntax- oder Importfehler aufweist. Dabei wird die Codebasis mithilfe von Flake8 analysiert, einem Tool zur statischen Code-Analyse für Python. Der Fokus liegt auf der Einhaltung von Code-Qualitätsrichtlinien, um Wartbarkeit und Lesbarkeit zu gewährleisten. Kritische Verstöße führen zum Fehlschlagen des Tests, und alle weniger schwerwiegenden Hinweise werden dokumentiert, um sie in späteren Iterationen zu adressieren.