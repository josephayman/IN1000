import datetime
  
mnd1 = int(input("Skriv en måned (tall)\n")) ## \n starter en ny linje
dag1 = int(input("Skriv en dag\n"))

mnd2 = int(input("Skriv en senere måned (tall)\n"))
dag2 = int(input("Skriv en annen dag\n"))

d1 = datetime.datetime(2020, mnd1, dag1) # året spiller ingen rolle så lenge den er lik på begge datoene
d2 = datetime.datetime(2020, mnd2, dag2)

if d1 < d2:
    print("Riktig rekkefølge!")
elif d1 == d2:
    print("Samme dato!")
else:
    print("Feil rekkefølge!")

# Se dato2.py for input validering og bedre kode

