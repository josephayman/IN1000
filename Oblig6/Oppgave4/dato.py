class Dato:
    def __init__(self, ny_dag, ny_maaned, nytt_aar):
        self.dag = ny_dag
        self.maaned = ny_maaned
        self.aar = nytt_aar

    def hent_aar(self):
        return self.aar

    def dato_tekst(self):
        return f"{self.dag}.{self.maaned}.{str(self.aar)[-2:]}"

    def er_dagen(self, dag):
        return self.dag == dag

    def er_for_kommet(self, annen_dato):
        if self.aar != annen_dato.aar:
            return self.aar < annen_dato.aar
        elif self.maaned != annen_dato.maaned:
            return self.maaned < annen_dato.maaned
        else:
            return self.dag < annen_dato.dag

    def neste_dag(self):
        if self.maaned in [1, 3, 5, 7, 8, 10] and self.dag == 31:
            self.dag = 1
            self.maaned += 1
        elif self.maaned in [4, 6, 9, 11] and self.dag == 30:
            self.dag = 1
            self.maaned += 1
        elif self.maaned == 2:
            if self.er_skuddaar() and self.dag == 29:
                self.dag = 1
                self.maaned += 1
            elif not self.er_skuddaar() and self.dag == 28:
                self.dag = 1
                self.maaned += 1
        elif self.maaned == 12 and self.dag == 31:
            self.dag = 1
            self.maaned = 1
            self.aar += 1
        else:
            self.dag += 1

    def er_skuddaar(self):
        if self.aar % 4 == 0:
            if self.aar % 100 == 0:
                if self.aar % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
