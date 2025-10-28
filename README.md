# US Medical Insurance Costs Analysis

## Projektziele
Das Hauptziel dieses Projekts ist die Durchführung einer unabhängigen explorativen Datenanalyse (EDA) des "US Medical Insurance Costs Dataset", um die wichtigsten Prädiktoren für medizinische Kosten zu identifizieren.

Folgende Fragestellungne werden behandelt:

1. Rauchergewohnheiten: Wie hoch ist der durchschnittliche Unterschied bei den Kosten zwischen Rauchern und Nichtrauchern? 
2. Geografische Unterschiede: Gibt es signifikante Unterschiede bei den durchschnittlichen Kosten zwischen den vier Regionen (`northeast`, `northwest`, `southeast`, `southwest`)?
3. Körperliche Faktoren: Wie beeinflussen Alter und BMI (Body Mass Index) in Kombination mit anderen Faktoren (wie z.B. der Anzahl der Kinder) die individuellen Kosten

##  Datensatz-Übersicht
Der Datensatz (`insurance.csv`) enthält 7 Spalten:

| Spalte | Beschreibung | Datentyp |
| :--- | :--- | :--- |
| age | Alter des Hauptbegünstigten | Numerisch (Integer) |
| sex | Geschlecht des Versicherungsnehmers | Kategorial (Text) |
| bmi| Body Mass Index | Numerisch (Float) |
| children | Anzahl der vom Versicherungsplan abgedeckten Kinder/Abhängigen | Numerisch (Integer) |
| smoker | Raucherstatus | Kategorial (Text) |
| region | Die Wohnregion des Begünstigten in den USA (4 Regionen) | Kategorial (Text) |
| charges | Individuelle medizinische Kosten, die durch die Krankenversicherung in Rechnung gestellt werden | Numerisch (Float) |

## Geplante Methodik
1. Datenimport: Importieren der `insurance.csv` mit der Python `csv`-Bibliothek in eine Liste von Python-Dictionaries
2. Datenbereinigung/Transformation: Sicherstellen, dass numerische Daten korrekt als Zahlen behandelt werden.
3. Analyse: Entwicklung von Funktionen zur Berechnung von:
    * Durchschnittswerten (nach Raucherstatus, Region etc.)
    * Häufigkeiten
    * Korrelationen (z.B. zwischen Alter und Kosten)
4.  Ergebnispräsentation: Zusammenfassung der Ergebnisse.
