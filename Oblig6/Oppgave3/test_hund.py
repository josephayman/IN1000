from hund import Hund
def hovedprogram():
    hund = Hund(3, 5)
    print("Vekt:", hund.hent_vekt())
    hund.spring()
    print("Vekt:", hund.hent_vekt())
    hund.spis(2)
    print("Vekt:", hund.hent_vekt())
    hund.spring()
    print("Vekt:", hund.hent_vekt())
    hund.spis(3)
    print("Vekt:", hund.hent_vekt())

hovedprogram()
