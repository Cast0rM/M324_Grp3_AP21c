Das beste Branching-Pattern, das sich für unsere Entwicklung der Applikation am meisten eignet ist ein Short-Lived pattern. Eine kurze Beschreibung beide Patterns.

# Long-lived branching

Langfristiges Branching ist eine gute Option für ein längerfristiges, tiefgreifend komplexes Projekt mit mehreren verteilten Entwicklungsteams. Ein langfristiger Branch ist eine Kopie oder ein Branch des Mainline-Codes, der zur Arbeit an einer Funktion verwendet wird. Ein langfristiges Branching-Muster funktioniert am besten mit einem Entwicklungsansatz zur Funktionsisolation.

# Short-lived branching

Das Kurzlebige-Branching-Muster bietet einen anderen Arbeitsansatz durch kurzlebige Branches. Im Gegensatz zum langfristigen Branching, das Wochen an Entwicklung beanspruchen kann, erfordert das kurzlebige Branching, dass Entwickler Feature-Updates innerhalb von Tagen integrieren. Dieser Branching-Stil eignet sich am besten für einen Entwicklungsansatz mit kontinuierlicher Integration.

Die Tendenz für das Short-Lived Pattern ist in unserem Fall Attraktiv, da die verschiedene User Stories nicht so gross sind und wir direkt auf einem MVP greifen können.

Für die Branching-Strategie ergab sich laut unsere Anforderungen die **GitHub Flow branching strategy**

# GitHub Flow branching strategy

Die GitHub-Flow-Branching-Strategie ist ein relativ einfacher Arbeitsablauf. Der Hauptzweig enthält Ihren produktionsreifen Code, und die anderen Zweige, sogenannte Funktionszweige, sollten die Arbeit an neuen Funktionen und Fehlerbehebungen enthalten. Diese werden wieder in den Hauptzweig zusammengeführt, sobald die Arbeit abgeschlossen und ordnungsgemäss überprüft wurde.

![Github Branching Diagramm.png](Github%20Branching%20Diagramm.png)

In unserem Fall wäre der Main Branch unser Hauptzweig mit dem produktionsreifen Code. Wir würden dann für jedes Feature ein Branch ziehen. Als Beispiel eine Erweiterung mit dem Namen 
feature_{Feature, das implementiert wird} : feature_DBConnection als Beispiel.
Für Theorie teile und Dokumentations Erweiterungen würde man das direkt in unserem Main Branch Deployen.



