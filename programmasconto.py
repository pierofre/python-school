percentuale=()
incremento=()
formula= (str.lower(input("percentuale o incremento? ")))
if formula == "percentuale":
     numero1=int(input ("da quale numero devi effettuare il calcolo percentuale? "))
     percentuale1=int(input("quale percentuale vuoi eliminare?(inserisci numero intero) "))
     risultato1= ((numero1*percentuale1)/100)
     print (risultato1)
elif formula == "incremento":
     numero2= int(input ("di quale numero vuoi calcolare l'incremento? "))
     percentuale2=int(input("di quanto lo vuoi incrementare? "))
     risultato=(numero2+((numero2*percentuale2)/100))
     print (risultato)
else:
    print ("non posso effettuare altre operazioni")
