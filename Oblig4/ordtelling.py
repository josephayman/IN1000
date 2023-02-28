def antallBosktaver(ord):
    bokstaver = list(ord)
    antall = len(bokstaver)
    return antall

print(antallBosktaver("hei")) # 3

# Del 2
def antallOrd(tekst):
    ord = tekst.split()
    antall = len(ord)
    return antall

print(antallOrd("hei på deg")) # 3

# Del 3
def setningTilOrdbok(setning):
    ord = setning.split()
    ordbok = {}
    for i in ord:
        if i in ordbok:
            ordbok[i] += 1
        else:
            ordbok[i] = 1
    return ordbok  

print(setningTilOrdbok("hei hei på deg")) # {'hei': 2, 'på': 1, 'deg': 1}

# Del 4
# Funksjonen bruker funksjonene fra del 2 og 3
def ordtelling():
    setning = input("Skriv inn en setning: ")
    antallOrdISetning = antallOrd(setning)
    print(f"Det er {antallOrdISetning} ord i setningen din.")
    for ord in setningTilOrdbok(setning):
        print(f"Ordet '{ord}' forekommer {setningTilOrdbok(setning)[ord]} ganger, og har {antallBosktaver(ord)} bokstaver.")

ordtelling()

