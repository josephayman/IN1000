from random import randint, choice, random
from lag import Lag


class Kamp:
    def __init__(self, hjemmelag, bortelag):
        self._hjemmelag = hjemmelag
        self._bortelag = bortelag
        self._mål_hjemme = None
        self._mål_borte = None

    def hjemmelag(self):
        return self._hjemmelag

    def bortelag(self):
        return self._bortelag

    def mål_hjemme(self):
        return self._mål_hjemme

    def mål_borte(self):
        return self._mål_borte

    def spill(self):
        hjemme_mål_for = self._hjemmelag.mål_for()
        hjemme_mål_mot = self._hjemmelag.mål_mot()

        borte_mål_for = self._bortelag.mål_for()
        borte_mål_mot = self._bortelag.mål_mot()

        hjemme_fordel = 1.2  # Juster denne for å endre hjemmefordelen

        hjemme = hjemme_mål_for * hjemme_fordel * borte_mål_mot * random()
        borte = borte_mål_for * hjemme_mål_mot * random()

        self._mål_hjemme = randint(0, round(hjemme))
        self._mål_borte = randint(0, round(borte))


# Testkode (kjøres ikke når klassen importeres, kun når kamp.py kjøres)
if __name__ == "__main__":
    lag1 = Lag("Molde", 1.7, 1.3)
    lag2 = Lag("Rosenborg", 1.7, 1.6)
    Kamp(lag1, lag2).spill()
    pass  # <--- instruksjon om å gjøre ingenting - fjern denne linjen
    #      når du begynner å skrive testkode
