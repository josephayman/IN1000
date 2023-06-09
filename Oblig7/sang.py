class Sang:
    def __init__(self, artist, title):
        self._artist = artist
        self._title = title

    def spill(self):
        print("Spiller " + self._title + "av " + self._artist)

    def sjekkArtist(self, navn):
        for word in navn.split():
            if word in self._artist.split():
                return True
        return False

    def sjekkTittel(self, title: str):
        if (self._title.lower() == title.lower()):
            return True
        else:
            return False

    def sjekkArtistOgTittel(self, artist, title):
        return self.sjekkArtist(artist) and self.sjekkTittel(title) # sjekker om artist og tittel er i sangen
        
    def __str__(self):
        return self._title + " av " + self._artist
