numeri=[1,2,3,4,5,6]
numeri2=[3,4,5]
#a = 0
#for indice in numeri:
    #indice è una variabile di appoggio (la convenzione vuole che per ogni plurare utilizziamo il singolare per considerare i valori della lista)
#    a = indice
def somma(lista):
    risultato=0
    for i in lista:
        risultato+=i
    print(risultato)
x=somma(numeri)
print(x)


#def name (arg="default"):
    #arg nome dell'argomento mentre "deafult" è l'argomento
