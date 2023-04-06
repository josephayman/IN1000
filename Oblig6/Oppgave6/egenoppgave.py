class Person:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        self.hobbyer = []
    
    def legg_til_hobby(self, hobby):
        self.hobbyer.append(hobby)
    
    def skriv_hobbyer(self):
        print(", ".join(self.hobbyer))
    
    def skriv_ut(self):
        print(f"{self.navn} ({self.alder} år)")
        print("Hobbyer:", end=" ")
        self.skriv_hobbyer()

# Testprogram
navn = input("Skriv inn navn: ")
alder = int(input("Skriv inn alder: "))
person = Person(navn, alder)

while True:
    hobby = input("Skriv inn en hobby (eller Enter for å avslutte): ")
    if hobby == "":
        break
    person.legg_til_hobby(hobby)

person.skriv_ut()