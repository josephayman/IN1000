import datetime
  
# Funksjon for å hente dato
def get_date():
    mnd = int(input("Skriv en måned (tall)\n")) ## \n starter en ny linje
    dag = int(input("Skriv en dag\n"))
    # Validering
    if mnd < 1 or mnd > 12:
        print("Ugyldig måned!")
        exit()
    if dag < 1 or dag > 31:
        print("Ugyldig dag!")
        exit()
    return datetime.datetime(2020, mnd, dag)

# Funksjon for å hente to datoer
def get_dates():
    d1 = get_date()
    d2 = get_date()
    return d1, d2

# Funksjon for å sammenligne datoer
def compare_dates(d1, d2):
    if d1 < d2:
        print("Riktig rekkefølge!")
    elif d1 == d2:
        print("Samme dato!")
    else:
        print("Feil rekkefølge!")

# Hovedprogram
def main():
    d1, d2 = get_dates()
    compare_dates(d1, d2)

# Kjører kun hvis dette er hovedprogrammet
if __name__ == "__main__":
    main()