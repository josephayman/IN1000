# Skriv et beregningsprogram for skreddere med en
# funksjon som leser inn en fil (som du lager selv og leverer sammen med de andre
# filene) der hver linje beskriver et navn på et mål og selve målet i tommer.
# La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi
# og returner ordboken. Lag deretter en prosedyre som tar imot en liste av mål og
# benytter seg av tommerTilCm som du skrev tidligere for å skrive ut målene i
# centimeter.

from regnefunksjoner import tommerTilCm

def lesMalinger(filnavn):
    ordbok = {}
    innfil = open(filnavn)
    for linje in innfil:
        linje = linje.strip()
        mal = linje.split(',')
        ordbok[mal[0]] = tommerTilCm(float(mal[1]))
    innfil.close()
    return ordbok

print(lesMalinger('maaler.csv'))
