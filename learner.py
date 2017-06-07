class Learner(object):
    #Assegnamo ad una classe che contiene un oggeto il nomer Learner
    def __init__(self, name, surname, level=0, classes=0):
        #inizializiamo una funzione della classe, che contiene gli argomenti relativi ai degli studenti
        self.name = name
        self.surname = surname
        self.full_name = name +" "+ surname
        self.level = 3 if abs(level > 3) else abs(level)
        self.classes = abs (classes)
        self.days = self._calc_days(self.level, self.classes)
        #assegniamo agli argomenti della funzione le variabili per cui dovrà lavorare
    def __repr__(self):
        return "Learner {}:\nlevel->{}\nclasses->{}\ndays{}".format(self.full_name, self.level, self.classes, self.days)
        #per rappresentare la i risultati della funzione inizializiamo un'altra funzione che riprende gli
        #argomenti del metodo self e che ritorna attraverso una stringa il suo risultato
    def add_data (self, level=0, classes=0):
        self.__init__(self.name, self.surname, level, classes)
        #inizializziamo una funzione che permette l'aggiunta dei dati attraverso il metodo .self
    def _calc_days (self, level, classes):
        if level==0:
            return None
        else:
            if classes == 0:
                return round(400/level, 0)
            else:
                return round((400/level)-(classes*2/24))
        #creiamo una funzione che grazie al modulo IF permette di calcolare quante ore e livelli sono necessari per diventare Master

# alan = Learner("Alan","Marazzi", 3, 5)
# alan.add_data(2,1000)
#
# print(alan)
