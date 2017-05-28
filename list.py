#le liste sono sempre dentro le parentesi quadre

x=[1,2,3]
y=[4,5,6]
print (sum(x), sum(y))
z=x
print(sum(z))
#come facciamo a cambiare un valore all'interno della lista?
#all'interno della lista abbiamo delle posizioni, 0,1,2...
#soluzione
print(x[0])
#mi restituisce il primo valore della lista
print(x[0:])
# inserendo i 2 punti mi restituisce tutti i valori della lista
print (x[-1])
#inserendo il "(-1)" mi restituisce l'ultimo valore della lista, con -2 il penultimo e cosi via.
#per cambiare il valore dobbiamo assegnare un altro valore alla lista, in questa maniera
x[2]=7
print (z)

j=1
v=j
print(v)
j=2
print(v)
