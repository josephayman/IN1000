def fahrenheit_celsius():
    fahrenheit = float(input("Skriv inn temperaturen i Fahrenheit: ")) # Validering med float for å kunne ha desimaler
    celsius = (fahrenheit - 32) * 5/9
    print("Temperaturen i Celsius er: " + str(celsius))

# Kjører kun hvis dette er hovedprogrammet
if __name__ == "__main__":
    fahrenheit_celsius()
