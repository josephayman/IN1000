# del 4 & 5
from motorsykkel import Motorsykkel
def hovedprogram():
    # lag 3 motorsykler
    sykkel1 = Motorsykkel("Yamaha", "AB12345")
    sykkel2 = Motorsykkel("Honda", "CD67890")
    sykkel3 = Motorsykkel("Harley", "EF23456")

    sykkel1.kjor(100)
    assert sykkel1.hent_kilometerstand() == 100 # del 8

    sykkel1.skriv_ut()
    sykkel2.skriv_ut()
    sykkel3.skriv_ut()
    # del 7
    sykkel3.kjor(10)
    assert sykkel3.hent_kilometerstand() == 10 # del 8

    sykkel3.skriv_ut()

if __name__ == "__main__":
    hovedprogram()