# Del 1 & 2
liste = []
tall = int(input("Tast inn et tall: ")) # Definerer variabelen tall før løkken
while tall != 0:
    tall = int(input("Tast inn et tall: "))
    liste.append(tall)

liste.pop() # Fjerner siste elementet som er null i det tilfelle

# Del 3
for i in liste:
    print(i)

# Del 4
minSum = 0
for i in liste:
    minSum += i
print("Summen av tallene er lik: ", minSum)

# Del 5
# Løsning med to for loops (nested) O(n^2)
minsteTall = liste[0]
for i in liste:
    for j in liste:
        if i < j:
            minsteTall = i
        else:
            minsteTall = j
print("Minste tallet er: ", minsteTall)

# Løsning med en for loop O(n)
storsteTall = 0
for i in liste:
    if i > storsteTall:
        storsteTall = i
print("Største tallet er: ", storsteTall)





