# Del 1
fruktliste  = ["eple", "eple", "banan", "banan", "banan"]
fruktmengde = {"eple", "eple", "banan", "banan", "banan"}
print(len(fruktliste) == len(fruktmengde))

# hvorfor blir False printet ut?
# Fordi listen har 5 elementer uavhengig av om det er flere av samme element.
# Mens mengden har 2 elementer, et for hvert unike element i ordboken.

# Del 2
frukt_dict = {
    "eple": 2,
    "banan": 3,
}

# Del 3
nyFrukt = input("Skriv inn en ny frukt: ")
antall = int(input("Skriv inn antall: "))

frukt_dict[nyFrukt] = antall # Legger til ny frukt i ordboken

# Del 4
if antall < 0 :
    print("Ugyldig input!")
elif nyFrukt not in frukt_dict:
    frukt_dict[nyFrukt] = antall
else:
    frukt_dict[nyFrukt] = antall

print(frukt_dict)

