from datetime import datetime, timedelta # for å kunne bruke datoer for del 5

def lesMaksTemp(filnavn):
    innfil = open(filnavn)
    ordbok = {}
    for linje in innfil:
        linje = linje.strip()
        ord = linje.split(',')
        ordbok[ord[0]] = float(ord[1])
    innfil.close() # husk å lukke filen
    return ordbok

# del 1
maksTemp = lesMaksTemp('max_temperatures_per_month.csv')
print(maksTemp)


# del 2 & 3
def oppdaterMaksTemp(filnavn, ordbok):
    innfil = open(filnavn)
    for linje in innfil:
        linje = linje.strip()
        nyTemp = linje.split(',')
        if nyTemp[0] in ordbok:
            if ordbok[nyTemp[0]] < float(nyTemp[2]): 
                print('Ny varmerekord',nyTemp[1] , nyTemp[0], nyTemp[2], "(gammel varmerekord var", ordbok[nyTemp[0]], "grader Celcius)")
                ordbok[nyTemp[0]] = float(nyTemp[2])
        else:
            ordbok[nyTemp[0]] = float(nyTemp[2])
    innfil.close()
    return ordbok

oppdaterMaksTemp('max_daily_temperature_2018.csv', maksTemp)
print(maksTemp)

# del 4 (bonus)
def skrivMaksTemp(filnavn, ordbok):
    utfil = open(filnavn, 'w') # 'w' for write mode (default is read mode
    for key in ordbok:
        utfil.write(key + ',' + str(ordbok[key]) + '\n') # \n for newline
    utfil.close()
skrivMaksTemp('utfil.csv', maksTemp)


# del 5 (bonus)
def varmebolge(filnavn):
    innfil = open(filnavn)
    data = []
    for linje in innfil:
        linje = linje.strip()
        temp = linje.split(',')
        if float(temp[2]) > 25:
            data.append(temp) # legger til alle dager med temperatur over 25 grader i en liste
    datoer = [datetime.strptime(d[0] + ' ' + d[1], '%b %d') for d in data] # lager en liste med datoer
    sekvenser = {}
    gjeldende = []
    for i in range(len(datoer)):
        # Hvis gjeldende dato er ikke den første i en sekvens, sjekk om den er en dag etter forrige dato
        if gjeldende and datoer[i] - gjeldende[-1] == timedelta(days=1):
            gjeldende.append(datoer[i])
        # hvis gjeldende dato er den første i en sekvens, start en ny sekvens
        else:
            # Hvis forrige sekvens var lang nok, legg den til i ordboken
            if len(gjeldende) >= 5:
                startdato = gjeldende[0].strftime('%b %d') # Gjeldene format har blitt funnet på nettet. Denne delen er kopiert
                sluttdato = gjeldende[-1].strftime('%b %d')
                sekvenser[startdato + ' til ' + sluttdato] = gjeldende
            gjeldende = [datoer[i]]
    print(sekvenser.keys()) # printer ut start- og sluttdato uten å printe ut hele sekvensen
    innfil.close()

varmebolge('max_daily_temperature_2018.csv')


