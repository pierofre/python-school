import timeit
import numpy as np


calcolo = range(10000)#range crea una lista di valore che vanno da 0 al numero all'interno della parentesi
#dentro range posso inserire anche dei salti, esempio range(5,10,2) "vai da 5 a 10 saltando di 2"
def loop_grow():
    risultato=[]
    for i in calcolo:
        risultato.append(i**2)
    return risultato

def loop_float():
    risultato = [i**2 for i in calcolo] #list comprehension. Lo stesso di sopra
    return risultato

def mapping():
    risultato = list(map(lambda x: x**2, calcolo))
    #map applica una funzione ad ogni elemento dell'oggetto che tu gli passi
    #lambda è una funzione di calcolo
    return risultato

def vector():
    risultato = np.array(calcolo) **2
    return risultato

print("Regular loop: ", timeit.timeit(loop_grow, number=1000))
print("List Comprehension: ", timeit.timeit(loop_flat, number=1000))
print("Map Function: ", timeit.timeit(mapping, number=1000))
print("Vectorization: ", timeit.timeit(vector, number=1000))
