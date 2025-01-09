# P3: Continuous Integration Dokumentation 
## Pipeline Schritte Mikroservice 1 Bands
1. Der User pusht.
2. Der Code wird gebuildet.
3. Die Unit Tests laufen.
4. Die Integrationstests werden gestarted. Die API Endpunkte werden überprüft.
5. Code Quality mit Sonar zum Beispiel.
6. Build-Artefakte (Docker Images) werden erstellt und gespeichert.

## Pipeline Schritte Mikroservice 2 Alben
1. Der User pusht.
2. Der Code wird gebuildet.
3. Die Unit Tests laufen.
4. Die Integrationstests werden gestarted. Die API Endpunkte werden überprüft. Und die Verbindung mit Mikroservice 2.
5. API Contract Tests. Sicherstellen das Microservice 2 die erwarteten Antworten von Microservice 1 bekommen.
6. Code Quality mit Sonar zum Beispiel.
