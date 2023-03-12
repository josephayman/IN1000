def lesFil(filnavn):
    innfil = open(filnavn)
    ordbok = {}
    for linje in innfil:
        linje = linje.strip()
        if linje:
            verdier = linje.split()
            ordbok[verdier[0]] = float(verdier[1])
    return ordbok

ordbok = lesFil("max_temperatures_per_month.csv")
print(ordbok)
