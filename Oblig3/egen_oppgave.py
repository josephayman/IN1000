# Lag en quiz ved hjelp av dictionaries. Bruk input() for å spørre brukeren om svar. Bruk en for-løkke for å gå gjennom svarene og sjekke om de er riktige. Bruk en if-setning for å sjekke om svaret er riktig. Print ut resultatet.

quiz = {
    "Hva er hovedstaden i Norge?": "oslo",
    "Hva er hovedstaden i Sverige?": "stockholm",
    "Hva er hovedstaden i Danmark?": "københavn",
}

score = 0

for spørsmål, svar in quiz.items():
    svar = input(spørsmål).casefold()
    if svar == svar:
        score += 1
        print("Riktig!")
    else:
        print("Feil!")

print("Du fikk " + str(score) + " poeng!")
