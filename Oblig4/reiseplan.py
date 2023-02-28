# Del 1
steder = []

for i in range(5):
    steder.append(input("Skriv inn et sted: "))

# Del 2
klesplagg = []
avreisedatoer = []

# Lager om for loopen til en funksjon siden det blir brukt flere ganger
def fyllListe(liste, tekst):
    for i in range(5):
        liste.append(input(f"{tekst}: "))

fyllListe(klesplagg, "Skriv inn klesplagg: ")
fyllListe(avreisedatoer, "Skriv inn avreisedato: ")

# Del 3
reiseplan = [steder, klesplagg, avreisedatoer]

# Del 4
for i in reiseplan:
    print(i)

# Del 5 a & b
index1 = int(input("Skriv inn et tall mellom 1 og 3: "))-1
index2 = int(input("Skriv inn et tall mellom 1 og 5: "))-1

if index1 < 1 or index1 > 3 or index2 < 1 or index2 > 5:
    print("Ugyldig indeksverdi")
else:
    print(reiseplan[index1][index2])
