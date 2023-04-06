def fil_til_liste(filNavn):                     #oppretter en funksjon som leser inn filen med daglige temperaturer
    fil = open(filNavn, "r")                   #åpner filen
    startdato = ""                                #oppretter en tom variabel som vil vise startdatoen av varmebølgen
    sluttdato = ""                                #oppretter en tom variabel som vil vise sluttdatoen av varmebølgen

    start = False                                #oppretter variabelen start som er False i starten
    count = 0                                     #oppretter en teller med verdien 0 i starten
    for linje in fil:                                #for-løkke for å iterere gjennom filen
        data = linje.strip().split(",")       #splitter hver linje i filen
        dato = data[0] + " " + data[1]   #definererer dato som vil bestå av verdiene på den første og den andre indeksen.
        temperatur = float(data[2])      #definerer variabelen temperatur som består av flytteverdien på den tredje indeksen.
        if temperatur > 25:                  #bruker en if-sjekk som vil sjekke om temperaturen er høyere enn 25.
            count += 1                          #hvis temperaturen er høyere enn 25 vil telleren øke med 1 for hver dag som har   temperaturen høyere enn 25
            if start == False:                 #og registrere startdatoen av varmebølgen.
                startdato = dato
            start = True
        else:
            if count > 5:                        #hvis telleren blir større enn 5, vil programmet skrive ut en melding i terminalen
                                                       #om registrert varmebølge.
                print(f"Det er registrert en varmebølge med startdato {startdato} og sluttdato {sluttdato}")
            count = 0                            #etter slutt av varmebølgen vil telleren blir 0 igjen.
            start = False
        sluttdato = dato                      #variabelen sluttdato blir dato etter if-sjekket for å registrere riktig sluttdato

    fil.close()

fil_til_liste('max_daily_temperature_2018.csv')