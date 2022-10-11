# RUB-Mensa2Json
Spuckt die RUB Speisepläne und Infos als JSON aus.

## Pläne die noch fehlen
- [Mensa](https://www.akafoe.de/gastronomie/speiseplaene-der-mensen/ruhr-universitaet-bochum)
- [Rote Bete](https://www.akafoe.de/gastronomie/speiseplaene-der-mensen/rote-bete)
- [Pfannengerichte](https://www.akafoe.de/pfannengerichte)
- [Little Q](https://little-q.de/)
- [Little B und Curry Q](https://www.akafoe.de/foodtrucks)
### Coding
- Python Code aufräumen, säubern und mehr an Konventionen anpassen
- Mehr Kontrolle über Name des Outputs und File/Konsole erlauben

## [Qwest](https://q-we.st/speiseplan/)
Der Speiseplan wird nach dem folgendem Schema erzeugt:
Ein Speiseplan hat einen Wochenplan und Informationen.
Ein Wochenplan hat mehrere Tage
Ein Tag hat ein Datum und eine Liste der Gerichte, die an dem entsprechenden Tag angeboten werden.
Ein Gericht hat einen Namen, Informationen und Preise jeweils für Studenten und Gäste.
Wenn ein Tag keine Gerichte enthält, ist das Q-West vermutlich geschlossen.
Informationen beinhalten aktuell allgemeine Informationen, Allergene und Zusatzstoffe.