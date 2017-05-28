import csv
from collections import Counter
with open('sacramento_crime.csv', 'r') as esercizi:
    crime = csv.reader(esercizi)
    #nome della lista: stats
    stats = []
    for row in crime:
        #"append" metodo inserisce gli elementi in una lista.
        stats.append(row)
crime_type =[]
for row in stats:
    crime_type.append(row[5])

c = Counter (crime_type).most_common(10)
with open('ex.csv', 'w') as p:
    risultato = csv.writer(p)
    for row in c:
        risultato.writerow([row[0],row[1]])
        #writerow metodo per scrivere una riga
