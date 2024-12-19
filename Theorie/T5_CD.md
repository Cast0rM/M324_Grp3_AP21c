# T5: Continuous Deployment
## Was ist Continuous Deployment (CD) und wie wird es umgesetzt?
Für CD wird in der Regel ein Continuous-Integration-System verwendet, um Änderungen an der Codebasis automatisch zu erstellen und zu testen. 
Sobald die Änderungen alle Tests bestanden haben, werden sie automatisch in einer Produktionsumgebung bereitgestellt. 
Dies kann mit Unterstützung von Deployment-Pipelines erreicht werden.
### Umsetzung:

**Version Control System:** Verwendung von Tools wie Git, um Code zu verwalten.
**Build-Prozesse:** Nutzung von CI/CD-Tools wie Jenkins, GitHub Actions oder GitLab CI, um die Software zu bauen.<br>
**Automatisierte Tests:** Integration von Unit-, Integrations- und End-to-End-Tests in die Pipeline.<br>
**Automatische Bereitstellung:** Tools wie Kubernetes, AWS CodePipeline oder Docker Swarm führen die Bereitstellung durch.<br>
**Monitoring:** Tools wie Prometheus oder ELK-Stack überwachen die Bereitstellung und das Verhalten der Software nach dem Release.

## Was ist der Unterschied zwischen Continuous Deployment und Continuous Delivery?
### Continuous Delivery
Der Code wird  täglich aktualisiert und jede Änderung schnellstens integriert.
Ebenfalls wird möglichst früh ein Prototyp für de Kunden bereitgestellt. Der Fokus liegt auf dem 
Feedback des Kunden. Code der dem Kunden nicht gefällt kann agil angepasst werden.
### Continuous Deployment
Der Ansatz im CD ist ähnlich, jedoch werden bei diesem Verfahren automatisierte Tests genutzt,
die direkt in den Entwicklungsprozess eingebunden werden. Konkrete Unterschiede zu Continuous Delivery
sind, dass keine Zeitverzögerung zwischen Test- und Releasezeitpunkt des Codes vorhanden ist.
Aufgrund der ausführlichen Test-Frameworks müssen die Entwickler nicht einmal mehr auf das Feedback des Kunden warten,
sondern können ihren Teil-Code nach der Entwicklung direkt automatisiert bereitstellen. <br>
Kurzgesagt, ist bei CD alles automatisiert, mitsamt der Produktionsbereitstellung. 


## Vor- und Nachteile von Continuous Delivery und Continuous Deployment
### Continuous Delivery:
**Vorteile:**
Kontrolle über den Deployment-Prozess.<br>
Reduzierung von Fehlern durch manuelle Validierung.<br>
**Nachteile:**
Manuelle Eingriffe können Verzögerungen verursachen.

### Continuous Deployment:
**Vorteile:**
Schnellere Time-to-Market.<br>
Automatisierte und konsistente Prozesse.<br>
**Nachteile:**
Höheres Risiko bei unzureichender Testabdeckung.<br>
Mögliche Instabilität durch fehlende manuelle Prüfung.<br>

## Deployment Strategien

### Blue/Green Deployment
Bei Blue Green Deployment werden zwei Server verwaltet: ein „blauer“ und ein „grüner“ Server. 
Die beiden Server sind gleich, jedoch ist einer dieser Server Live und der andere nicht. 
Auf dem privaten nicht Live Server werden die Änderungen gemacht. Nachdem dieser getestet wurde, 
wird er mit dem Live Server getauscht und die Änderungen werden sind live und für den Kunden verwendbar.
Ein Vorteil davon ist, dass Rollbacks sehr einfach sind. <br>
Tools wie Kubernetes oder Nginx werden für diese Strategie verwendet.

### Canary Deployment
Canary Deployment bezeichnet die Praxis der stufenweisen Veröffentlichung.
Dabei wird eine Änderung zunächst an einen kleinen Teil der Benutzer verteilt,
damit diese sie testen und Feedback geben können. 
Sobald die Änderung akzeptiert wird, wird die Änderung für den Rest der Benutzer bereitgestellt.

## A/B Testing
A/B-Testing bedeutet, dass zwei Varianten einer Sache gegeneinander getestet und miteinander in ihrer Performance verglichen werden.
Variante A und Variante B werden jeweils einem Teil der Zielgruppe gezeigt. 
Die Variante, die die höhere Conversion Rate erreicht, gewinnt den Test.

## Was sind Feature Toggles?
Feature Toggles (Feature Flags) sind Mechanismen, mit denen Features in einer Anwendung aktiviert oder deaktiviert werden können,
ohne dass ein neuer Deployment-Zyklus erforderlich ist.

## Was sind Rollback Strategien?
Rollback Strategien bezeichnen die Vorgehensweise zur Wiederherstellung des vorherigen stabilen Zustands einer 
Softwareanwendung nach einem fehlgeschlagenen oder auch unerwünschten Update. Dies hat eine wichtige
Bedeutung für die Verfügbarkeit, Verlässlichkeit oder Zufriedenheit der Nutzer der Software.
Für eine effiziente Wartung können Rollback Strategien hilfreich sein.
### Beispiele
**Automatisiertes Rollback:** Deployment-Tools können automatisch auf die vorherige stabile Version zurücksetzen.<br>
**Blue/Green Rollback:** Zurückleiten des Traffics zur vorherigen Umgebung.<br>
**Feature-Toggle Rollback:** Deaktivieren fehlerhafter Funktionen.<br>

## Was ist Continuous Monitoring und wie wird es umgesetzt?
Continuous Monitoring bezeichnet die kontinuierliche Überwachung von Systemen,
Anwendungen und Infrastruktur zur Identifikation von Problemen in Echtzeit.
### Umsetzung
Zuerst muss entschieden werden, was überwacht werden soll. Nicht alle Systeme sollen überwacht werden, weil 
dies kostenintensiv und komplex sein kann. Ebenfalls muss entschieden werden, wie die Systeme überwacht werden sollen.
Danach kann man mit der Hilfe von Tools wie z.B xmcyber oder crowdstrike die Sicherheitskontrollen durchgeführt werden.

## Wie werden Passwörter sicher gespeichert?

**Hashing:** Nutzung von Algorithmen wie bcrypt, Argon2 oder PBKDF2.<br>
**Salt:** Zufällige Werte für jedes Passwort.<br>
**Secret Management:** Verwendung von Tools wie AWS Secrets Manager oder Azure Key Vault.<br>

## Arten von Deployment
### Basic Deployment
Alle Nodes in der Zielumgebung werden gleichzeitig aktualisiert, um eine neue Version einzuführen.<br>

### Multi-Service-Deployment
Ebenfalls werden hier alle Nodes in der Zielumgebung aktualisiert. Diese Methode birgt weniger Risiken und ist für 
Anwendungen mit Versions- oder Serviceabhängigkeiten nützlich.

### Blue/Green-Deployment
Bei einem Blue/Green-Deployment werden zwei Versionen der Anwendung gleichzeitig bereitgestellt. 
Die aktuelle Version (Blue) und die neue Version (Green) werden in getrennten Umgebungen ausgeführt, 
wobei immer nur eine Live-Version zur Verfügung steht. Die Blue-Version läuft weiter, 
während die Green-Version getestet wird. Wenn die neue Version fertig ist, 
kann der Datenverkehr umgestellt werden, wobei die alte Version entweder außer Betrieb genommen
oder für ein späteres Rollback aufbewahrt wird. Manchmal wird die Blue Umgebung die in diesem Fall die alte ist, 
zur neuen Version und aktualisiert. 

### Move fast, fail often
Täglich werden mehrere neue Funktionen hinzugefügt. Die neuen Features werden an eine ausgewählte Gruppe
von Nutzern und Nutzerinnen gepusht. Nach und nach erhalten immer mehr User den Zugriff auf die neuen Funktionen.
Dadurch können schnell Fehler identifiziert werden. 

### Canary Deployment
Die Canary Deployment Methode ist sehr ähnlich zur Move fast, fail often Methode. Der einzige Unterschied 
besteht darin, dass die neuen Features an eine kleine Gruppe von Users gesendet wird. 

### Container via Docker Deployment
**Voraussetzungen** <br>
Laufender Ubuntu Server 18.04 mit installiertem Docker. <br>
Ein Benutzerkonto, das Mitglied der Docker-Gruppe ist (zur Ausführung von Docker-Befehlen ohne sudo). <br>
**Beschreibung**
Mit Docker kann man Deployment mit einem Kommando seine changes pushen. Man kann in einem in sich geschlossenes System
seine Änderungen machen. <br>
Mit Docker kann man in wenigen Schritten eine vollständige Anwendung bereitstellen, ohne sich mit der Installation
und Konfiguration von Software und Betriebssystem auseinandersetzen zu müssen.

### Container via Docker swarm Deployment
**Voraussetzungen** <br>
Docker ist auf allen beteiligten Hosts installiert.
Mindestens zwei Hosts (einer als Manager, die anderen als Worker).
Zugriff auf die Hosts und deren Netzwerk. <br>
**Vorteile** <br>
Einfache Skalierung: Durch Replikate oder Scale-Befehle.<br>
Hohe Verfügbarkeit: Container werden automatisch auf verfügbare Nodes verteilt.<br>
Rolling Updates: Services können ohne Downtime aktualisiert werden.<br>
Declarative Configurations: Mit stack.yml-Dateien kannst du Services deklarativ definieren.<br>
**Beschreibung**<br>
Mit Swarm kann man Anwendungen als sogenannte Services definieren, skalieren und verwalten, die in Containern laufen.




### Quellen
[computerweekly.com](https://www.computerweekly.com/de/definition/Continuous-Deployment) <br>
[ionos.com](https://www.ionos.de/digitalguide/websites/web-entwicklung/continuous-integration-vs-continuous-delivery-vs-continuous-deployment/)<br>
[wikipedia.com](https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment)<br>
[semaphoreci.com](https://semaphoreci.com/blog/what-is-canary-deployment)<br>
[agile-academy.com](https://www.agile-academy.com/de/agiles-lexikon/a-b-testing/)<br>
[appmaster.io](https://appmaster.io/de/glossary/rollback-strategie-fur-die-bereitstellung)<br>
[crowdstrike.com](https://www.crowdstrike.com/de-de/cybersecurity-101/next-gen-siem/continuous-monitoring/)<br>
[thenewstack.io](https://thenewstack.io/containers/how-to-deploy-a-container-with-docker/)<br>
[docs.docker.com](https://docs.docker.com/engine/swarm/services/)<br>
