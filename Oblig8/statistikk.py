class Statistikk:
    def __init__(self, lagliste):
        self._plasseringer = {}               # ordbok med Lag som nøkkel og liste over
                                        # [ antall førsteplasser, antall andreplasser, ... , antall sisteplasser ]
                                        # for dette laget i løpet av de simulerte sesongene
        for lag in lagliste:
            # til å begynne med er listen [0, 0, 0, ..., 0]
            self._plasseringer[lag] = [0]*len(lagliste)

    # Lagrer rangering av lagene i statistikken etter at en sesong er spilt
    def lagre_rangering(self, rangering):
        # rangering er en liste over Lag-objekter (0 = 1. plass, 1 = 2. plass, osv.)
        for j in range(len(rangering)):     # for hver plassering:
            lag = rangering[j]                  # finn ut hvilket lag som fikk denne plasseringen
            self._plasseringer[lag][j] += 1     # registrer at dette laget fikk en slik plassering denne sesongen

    # Skriver ut statistikken etter at alle sesongene er spilt
    def print_plasseringer(self):
        print()
        for lag in self._plasseringer: # for hvert lag
            print()
            print(lag.navn())    # skriv ut lagets navn
            print("-"*len(lag.navn()))
            plasseringsliste = self._plasseringer[lag] # hent listen med plasseringer for dette laget
            # bruker indeksen j som løkkevariabel slik at vi også kan skrive ut
            # hvilken plass det er snakk om (0 = 1.plass, 1 = 2.plass, osv.)
            for j in range(len(plasseringsliste)):
                antall = plasseringsliste[j] # antall plasseringer av denne typen
                print(str(j + 1).ljust(2), str(antall).rjust(5))