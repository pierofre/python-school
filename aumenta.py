#funzione aumenta
def aumenta (numero=4):
    return numero+1 #"return" restituisce il valore della funzione nella sessione in cui ci troviamo
print (aumenta())
#facciamo una funzione che stampa il risultato di una funzione che non ha il print

def stampa_fun(fun):
    print(fun)

stampa_fun (aumenta(3))
