from dato import Dato

# Oppretter et Dato-objekt
d1 = Dato(15, 3, 2023)

# Tester metoden hent_aar()
assert d1.hent_aar() == 2023

# Tester om det er lønningsdag eller ny måned
if d1.er_dagen(15):
    print("Lønningsdag!")
elif d1.er_dagen(1):
    print("Ny måned, nye muligheter")

# Tester metoden dato_tekst()
print(d1.dato_tekst())

# Endrer til neste dag og skriver ut på nytt
d1.neste_dag()
print(d1.dato_tekst())

# Leser inn en ny dato fra bruker og sammenligner
ny_dato = input("Skriv inn en dato på formatet dd.mm.åååå: ")
ny_dato_liste = ny_dato.split(".")
ny_dato_objekt = Dato(int(ny_dato_liste[0]), int(ny_dato_liste[1]), int(ny_dato_liste[2]))
