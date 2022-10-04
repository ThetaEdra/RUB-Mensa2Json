# RUB-Mensa2Json
Spuckt die JSON Version der Speisepläne der RUB aus weil es bisher keine API o.ä. gibt.

## TODO
### Pläne die noch fehlen
- Mensa
- Rote Bete
- Pfannengerichte
- LittleQ
### Coding
- Python Code aufräumen, säubern und mehr an Konventionen halten
- Mehr Kontrolle über Name des Outputs

## Qwest
Der Speiseplan wird nach dem folgendem Schema erzeugt:
### Speiseplan
Ein Speiseplan hat einen Wochenplan und Informationen.
### Wochenplan
Ein Wochenplan hat mehrere Tage
### Tag
Ein Tag hat ein Datum und eine Liste der Gerichte, die an dem entsprechenden Tag angeboten werden.
### Gericht
Ein Gericht hat einen Namen, Informationen und Preise jeweils für Studenten und Gäste.
Wenn ein Tag keine Gerichte enthält, ist das Q-West vermutlich geschlossen.
### Informationen
Informationen beinhalten aktuell allgemeine Informationen, Allergene und Zusatzstoffe.