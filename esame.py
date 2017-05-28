numeri=[1,2,3,4]
def somma(lista):
    risultato=0
    for i in lista:
        if i%2==0 or i==3:
            risultato+=i

    return risultato
x=somma(numeri)
print(x)
