# del 1
def addisjon(tall1, tall2):
    return tall1 + tall2

def substraksjon(tall1, tall2):
    return tall1 - tall2

def divisjon(tall1, tall2):
    return tall1/tall2

# del 2
assert addisjon(2, 3) == 5
assert addisjon(-8583, -7575) == -16158
assert addisjon(54,-32) == 22

assert substraksjon(2, 3) == -1
assert substraksjon(-8583, -7575) == -1008
assert substraksjon(54,-32) == 86



# NOTAT! assert kan gi feil når det flyttall. 
# eksempel assert 1/6 == 0.6666666666666667 gir feil, 
# men 1/6 == 1/6 gir ikke feil

assert divisjon(9, 3) == 3
assert divisjon(-400, -20) == 20
assert divisjon(74,-2) == -37

# del 3
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer*2.54

print(tommerTilCm(10)) # 25.4

# del 4
def skrivBergninger():
    tall1 = float(input("Skriv tall 1: "))
    tall2 = float(input("Skriv ett tall 2: "))
    print(addisjon(tall1, tall2))
    print(substraksjon(tall1, tall2))
    print(divisjon(tall1, tall2))
    tommelTall = float(input("Skriv tall som skal konverteres fra tommel til centimeter: "))
    print(tommerTilCm(tommelTall))

skrivBergninger()
