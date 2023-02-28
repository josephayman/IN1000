# del 1
def adder(tall1, tall2):
    return tall1 + tall2

print(adder(2, 3)) # 5
print(adder(8583,7575)) # 16158


# del 2 & 3
streng = input("Skriv inn en streng: ")
bokstav = input("Skriv inn en bokstav: ")
def tellForekomst(minTekst, minBokstav):
    return minTekst.count(minBokstav)

print(tellForekomst(streng, bokstav))


