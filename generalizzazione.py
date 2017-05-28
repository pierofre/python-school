#stampa i primi 6 multipli di n
def StampaMultipli(n):
  i = 1
  while i <= 6:
    print (n*i, '\t')
    i= i + 1 #perché?
  print ()

StampaMultipli(6)
#generalizzazione 6*6
def TabellaMoltiplicazioneGenerica(Grandezza):
  i = 1
  while i <= Grandezza:
    StampaMultipli(i)
    i = i + 1

#generalizzazione7*7
def StampaMultipli(n, Grandezza):
  i = 1
  while i <= Grandezza:
    print (n*i, '\t')
    i = i + 1
  print(n, '\t', Grandezza)

def TabellaMoltiplicazioneGenerica(Grandezza):
  i = 1
  while i <= Grandezza:
    StampaMultipli(i, Grandezza)
    i = i + 1

TabellaMoltiplicazioneGenerica(7)
