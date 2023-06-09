class Lag:
    def __init__(self, navn: str, mål_for: float, mål_mot: float):
        self._navn = navn
        self._mål_for = mål_for
        self._mål_mot = mål_mot

# Attributtet _navn er privat, så vi må lage en metode for å få tilgang til det. osv.
    def navn(self) -> str:
        return self._navn
    
    def mål_for(self) -> float:
        return self._mål_for
    
    def mål_mot(self) -> float:
        return self._mål_mot

    def __gt__(self, other: 'Lag') -> bool:
        return self._navn > other._navn
    
    def __lt__(self, other: 'Lag') -> bool:
        return self._navn < other._navn

# Testkode (kjøres ikke når klassen importeres, kun når lag.py kjøres)
if __name__ == "__main__":
    # TODO: Her kan koden testes
    lag1 = Lag("Molde", 1.7, 1.3)
    lag2 = Lag("Rosenborg", 1.7, 1.6)

    print(lag1.navn())  # Skal skrive ut "Molde"
    print(lag1.mål_for())  # Skal skrive ut 1.7
    print(lag2.mål_mot())  # Skal skrive ut 1.6

    print(lag1 > lag2)  # Skal skrive ut False (alfabetisk sortering)
    print(lag1 < lag2)  # Skal skrive ut True (alfabetisk sortering)


    # pass # <--- instruksjon om å gjøre ingenting - fjern denne linjen
         #      når du begynner å skrive testkode