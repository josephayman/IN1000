from lag import Lag

# dette er listen over lag som skal spille (representert ved Lag-objekter)
lagliste = []
# mål for/mot et gjennomsnittlig lag hentet fra
# https://projects.fivethirtyeight.com/soccer-predictions/eliteserien/
lagliste.append(Lag("Bodø/Glimt", 2.0, 1.3))
lagliste.append(Lag("Molde", 1.7, 1.3))
lagliste.append(Lag("Rosenborg", 1.7, 1.6))
lagliste.append(Lag("Vålerenga", 1.2, 1.7))
lagliste.append(Lag("Lillestrøm", 1.1, 1.6))
lagliste.append(Lag("Odd", 1.1, 1.7))
lagliste.append(Lag("Viking", 1.2, 1.8))
lagliste.append(Lag("Sarpsborg 08", 1.2, 1.8))
lagliste.append(Lag("Brann", 1.0, 1.7))
lagliste.append(Lag("Tromsø", 1.0, 1.7))
lagliste.append(Lag("Haugesund", 1.0, 1.9))
lagliste.append(Lag("Strømsgodset", 1.0, 1.9))
lagliste.append(Lag("Aalesund", 0.8, 1.7))
lagliste.append(Lag("HamKam", 0.8, 1.8))
lagliste.append(Lag("Stabæk", 0.8, 1.8))
lagliste.append(Lag("Sandefjord", 0.8, 2.2))

# print("Lagliste:", lagliste[1].mål_for(), lagliste[1].mål_mot())