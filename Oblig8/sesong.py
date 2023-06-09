from kamp import Kamp
from tabell import Tabell
from lagliste import lagliste

class Sesong:
    def __init__(self, lagliste):
        self._lagliste = lagliste
        self._runder = []
        self._tabell = Tabell(lagliste)

        nrunder = (len(lagliste) - 1)*2 # runder per sesong
        nkamper = len(lagliste)//2      # kamper per runde

        # Round-robin-algoritme
        # https://en.wikipedia.org/wiki/Round-robin_tournament#Circle_method
        lagliste1 = self._lagliste[:nkamper] # deler laglisten i to
        lagliste2 = self._lagliste[nkamper:] # slik at ett lag fra hver del møtes
        for runde in range(nrunder):
            kamper = []

            for i in range(nkamper):
                hjemmelag = lagliste1[i]
                bortelag = lagliste2[i]

                if runde % 2 == 0:
                    kamper.append(Kamp(hjemmelag, bortelag))
                else:
                    kamper.append(Kamp(bortelag, hjemmelag))

            self._runder.append(kamper)

            lagliste2.insert(0, lagliste1.pop())
            lagliste1.append(lagliste2.pop())

    def tabell(self):
        return self._tabell

    # Denne metoden simulerer en sesong
    # Alle kampene spilles, og tabellen oppdateres etter hver kamp
    def simuler(self):
        for runde in self._runder:
            for kamp in runde:
                kamp.spill()
                self._tabell.legg_til_resultat(kamp)
        

        self._tabell.oppdater_rangering() # oppdaterer rekkefølgen i tabellen til slutt

    # Skriver ut alle serierundene (med resultater om kampene er spilt)
    def print_runder(self):
        # self._runder er en liste hvor elementene er lister med Kamp-objekter
        for i in range(len(self._runder)): # trenger indeks her
            kamper = self._runder[i]
            print()
            print("Runde", str(i + 1).rjust(2)) # indeks 0 --> runde 1, osv.
            print("--------")
            print()
            for kamp in kamper:
                hjemmelag = kamp.hjemmelag()
                bortelag = kamp.bortelag()
                mål_hjemme = kamp.mål_hjemme()
                mål_borte = kamp.mål_borte()
                # kampstr (en streng) inneholder først og fremst lagene som møtes
                # (se print_tabell for en forklaring av .ljust() og .rjust(), hvis du lurer)
                kampstr = (hjemmelag.navn() + " - " + bortelag.navn()).ljust(30)
                # legg til resultatet i kampstr dersom kampen er spilt og har et resultat
                if (mål_hjemme is not None) and (mål_borte is not None):
                    kampstr += (str(mål_hjemme).rjust(2) + " - " + str(mål_borte).ljust(2))
                print(kampstr)

# Testkode (kjøres ikke når klassen importeres, kun når sesong.py kjøres)
if __name__ == "__main__":
    testsesong = Sesong(lagliste)       # sett opp sesongen
    testsesong.simuler()                # spill alle kampene
    testsesong.print_runder()           # print alle rundene (med resultater)
    testsesong.tabell().print_tabell()  # skriv ut tabellen etter siste runde