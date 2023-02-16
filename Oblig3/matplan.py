# Del 1
matplan = {
    "Kari": {"brød", "egg", "pølser"},
    "Ola": {"yoghurt", "brød", "kjøttboller"},
    "Per": {"egg", "salat", "pizza"},
}

# Del 2
def nyMatplan():
    # for navn in matplan:
    #     print(navn)
    print(*matplan.keys())
    navn = input("Skriv inn navn: ")
    if navn in matplan:
        print(matplan[navn])
    else:
        print("Beboeren finnes ikke i matplanen.")

nyMatplan()

# Del 3
# Hvilken type samling (liste, mengde, ordbok) ville du brukt for å representere hver av de følgende eksemplene på data? Skriv litt om hvorfor, eventuelt med forbehold eller presiseringer.
# a. Brukernavn på alle IN1000 studentene
# b. Brukernavn og antall poeng på innlevering 3 for alle studentene på IN1000
# c. Alle vinnere i Lotto siste år (kun navn)
# d. All mat noen gjester i et selskap er allergisk mot (for å planlegge menyen)

# a. Liste
## Fordi vi ikke trenger å ha unike brukernavn, og vi kan ha flere brukere med samme brukernavn(Antar at validering av brukernavn kjøres på serveren)
# b. Ordbok
## Fordi vi trenger å ha unike brukernavn, og vi kan ha flere brukere med samme brukernavn(validering av brukernavn kjøres på serveren)
# c. Mengde
## Fordi vi ikke trenger å ha unike navn, og vi kan ha flere brukere med samme navn. Rekkefølgen på navnene er ikke viktig.
# d. Mengde
## Fordi Rekkefølgen på allergener er ikke viktig.


