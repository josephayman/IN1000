# be bruker skrive et tall fra 5 til 10
# lage en for løkke som setter inn alle tallene helt til det tallet bruker skrev inn

tall = int(input("Skriv inn et tall fra 5 til 10: "))
liste = []
for i in range(tall):
    liste.append(i+1)
print(liste)

# lag en funksjon som tar inn en et tall ofd fjerner er mindre enn det tallet fra liste

def fjernTall(liste, tall):
    for i in liste:
        if i < tall:
            liste.remove(i)
    return liste

print(fjernTall(liste, 5))

# lag en funksjon som tar inn et tall fra bruker og legger det til i listen

def leggTilTall(liste, tall):
    liste.append(tall)
    return liste

print(leggTilTall(liste, 11))