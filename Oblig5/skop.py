# Beskriv med ord hva som vil skje om følgende program kjøres. 
def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)
    
def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)
    
hovedprogram()

# Først defineres funksjonen minFunksjon. Den tar ikke imot noen parametere. 
# Deretter defineres prosedyren hovedprogram, som heller ikke tar noen parametere. 
# Deretter kalles hovedprogram. Inne i hovedprogram defineres variablene a med verdien 42 og b med verdien 0.
# Deretter printes verdien til b, som er 0. Deretter settes b lik a, som er 42. Deretter kalles minFunksjon.
# Inne i minFunksjon har vi en for-løkke som kjører 2 ganger.
# Inne i løkken defineres variabelen c med verdien 2. Deretter printes verdien til c, som er 2. Deretter økes c med 1, slik at c nå er 3.
# Deretter defineres variabelen b med verdien 10. Deretter økes b med a og her får vi en feilmelding, siden a ikke er definert inne i minFunksjon.
# Den burde defineres eller blir tatt imot some en parameter.
# Den returnerer no value.
# Programmet avsluttes.