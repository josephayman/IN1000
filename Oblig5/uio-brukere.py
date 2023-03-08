# del 1 & del 6(bonus)
def lagBrukernavn(fulltNavn: str, ordbok: dict={}): 
    fornavn = fulltNavn.split(" ")[0] # Første element i navn liste
    etternavn = fulltNavn.split(" ")[1]
    brukernavn = (fornavn + etternavn[0]).lower() # Lager brukernavnet og gjør det til små bokstaver
    if brukernavn in ordbok:
        # make a for loop that adds the next letter in etternavn to brukernavn
        for i in etternavn[1:]:
            brukernavn += i
            if brukernavn not in ordbok:
                return brukernavn
    return brukernavn

print(lagBrukernavn("Anniken Banken")) #annikenb

# del 2
def lagEpost(brukernavn: str, suffix: str):
    return brukernavn + "@" + suffix

print(lagEpost("annikenb", "uio.no")) # annikenb@uio.no

# del 3
ordbok = {"olan": "ifi.uio.no", "karin": "student.matnat.uio.no"}

def skrivUtEposter(ordbok: dict):
    for bruker in ordbok:
        print(bruker, ":", ordbok[bruker])

skrivUtEposter(ordbok)

# del 4
tomOrdbok = {}
valg = ""
while valg != "s":
    valg = input("Velg ett av følgende alternativer:\n i for å legge til bruker \n p for å skrive ut eposter\n s for å avslutte\n ")
    if valg == "i":
        navn = input("Skriv inn fulltnavn: ")
        suffix = input("Skriv inn epost suffix: ")
        brukernavn = lagBrukernavn(navn, tomOrdbok)
        epost = lagEpost(brukernavn, suffix)
        tomOrdbok[brukernavn] = epost
    elif valg == "p":
        skrivUtEposter(tomOrdbok)
    elif valg == "s":
        break
    else:
        print("Ugyldig input")

# del 5
def test_lagBrukernavn():
    assert lagBrukernavn("Anniken Banken") == "annikenb"
    assert lagBrukernavn("Karin Olsen") == "karino"
    assert lagBrukernavn("Ola Nordmann") == "olan"

def test_lagEpost():
    assert lagEpost("annikenb", "uio.no") == "annikenb@uio.no"
    assert lagEpost("karino", "student.matnat.uio.no") == "karino@student.matnat.uio.no"
    assert lagEpost("olan", "ifi.uio.no") == "olan@ifi.uio.no"


