# Del 1

tall = [1,2,3]

tall += [4] # Legger til 4 i slutten av listen

print(tall)

# Del 2

navn = []
for i in range(4): # Legger til 4 navn i listen
    navn.append(input("Skriv inn et navn: "))

# Del 3

if "Josef" in navn:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

# Del 4

sumOgProdukt = []
# Vi kan bruke sum() funksjonen for å finne summen av en liste
print(sum(tall))
# Eller så lager vi en rekusriv funksjon for å finne summen av listen
def summ(liste):
    if len(liste) == 1: # Slutter rekursjonen når listen bare har ett element
        return liste[0]
    else:
        return liste[0] + summ(liste[1:])

print(summ(tall))
sumOgProdukt += [summ(tall)] # Legger til summen i listen

# Rekursiv funksjon for å finne produktet av en liste
def multi(liste):
    if len(liste) == 1: # Slutter rekursjonen når listen bare har ett element
        return liste[0]
    else:
        return liste[0] * multi(liste[1:])
    
print(multi(tall))
sumOgProdukt += [multi(tall)]

nyListe = tall + sumOgProdukt
print(nyListe)
nyListe = nyListe[:-2] # Fjerner de to siste elementene
print(nyListe)