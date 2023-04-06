# del 1
class Motorsykkel:
    def __init__(self, merke, regnr):
        self.merke = merke
        self.regnr = regnr
        self.kmstand = 0
    # del 2
    def kjor(self, km):
        self.kmstand += km
    # del 3
    def hent_kilometerstand(self):
        return self.kmstand
    # del 6
    def skriv_ut(self):
        print("Merke: ", self.merke)
        print("Regnr: ", self.regnr)
        print("Kilometerstand: ", self.kmstand)
    