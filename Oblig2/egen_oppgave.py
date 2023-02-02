# Oppgave 5 del 1

## Lag et quiz-program som stiller spørsmål til bruker og gir tilbakemelding på om svarene er korrekte.

def quiz():
    score = 0                           # Teller hvor mange poeng brukeren har
    # Spørsmål 1
    print("Hva er hovedstaden i Norge?")# Skriver ut spørsmålet
    print("1. Oslo")                    # Skriver ut alternativ 1
    print("2. Bergen")                  # Skriver ut alternativ 2
    print("3. Trondheim")               # Skriver ut alternativ 3
    svar = input("Svar: ").casefold()   # casefold() gjør at vi kan skrive inn store og små bokstaver
    
    if svar == "1" or svar == "oslo":   # Sjekker om svaret er 1 eller "oslo"
        score += 1                      # Hvis svaret er riktig, øker score med 1
        print("Riktig!")
    else:
        print("Feil!")

    # Spørsmål 2
    print("Hva er hovedstaden i Sverige?")
    print("1. Oslo")
    print("2. Stockholm")
    print("3. Trondheim")
    svar = input("Svar: ").casefold() 

    if svar == "2" or svar == "stockholm":
        score += 1
        print("Riktig!")
    else:
        print("Feil!")

    # Spørsmål 3
    print("Hva er hovedstaden i Danmark?")
    print("1. Oslo")
    print("2. Bergen")
    print("3. København")
    svar = input("Svar: ").casefold()
    if svar == "3" or svar == "københavn":
        score += 1
        print("Riktig!")
    else:
        print("Feil!")

    print("Du fikk " + str(score) + " poeng!")

quiz()