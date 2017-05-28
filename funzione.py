x=1
y=2
n=5

if x == y:
  print (x, "e", y, "sono uguali")
else:
  if x < y:
    print (x, "e' minore di", y)
  else:
    print (x, "e' maggiore di", y)

print (x, y)


def ContoAllaRovescia(n):
  if n == 0:
    print ("Partenza!")
  else:
    print (n)
    ContoAllaRovescia(n-1)
ContoAllaRovescia(n)
