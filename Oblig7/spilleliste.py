from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def __str__ (self):
        return self._navn + ": " + str(len(self._sanger)) + " sanger"
    
    def lesFraFil(self, filnavn):
        innfil = open(filnavn)
        for linje in innfil:
            linje = linje.strip()
            ord = linje.split(';')
            nySang = Sang(ord[0], ord[1])
            self._sanger.append(nySang)
        innfil.close()


    def leggTilSang(self, nySang):
        self._sanger.append(nySang)
    
    def fjernSang(self, sang):
        self._sanger.remove(sang)
    
    def spillSang(self, sang):
        sang.spill()
    
    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    def finnSang(self, title):
        for sang in self._sanger:
            if sang.sjekkTittel(title):
                return sang
        return None
    
    def hentArtistUtvalg(self, artistnavn):
        utvalg = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                utvalg.append(sang)
        return utvalg
    