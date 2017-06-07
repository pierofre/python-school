class Learner(object):
    """Learner serve al calcolo e allo storage di
    informazioni riguardo ai learner iscritti
    """

    def __init__(self, name, surname, level=0, classes=0):
        """inizializzazione di Learner che contiene
        gli argomenti relativi ai dati degli studenti
        """

        # assegniamo agli argomenti della funzione le variabili per cui dovrà lavorare
        self.name = name
        self.surname = surname
        self.full_name = name +" "+ surname
        self.level = 3 if abs(level > 3) else abs(level)
        self.classes = abs (classes)
        self.days = self._calc_days(self.level, self.classes)

    def __repr__(self):
        """Metodo di rappresentazione della classe, stampa:
        `Learner <full_name>:
        level-><level reached>
        classes-><classes missing>
        days-><days missing>`
        """

        return "Learner {}:\nlevel->{}\nclasses->{}\ndays{}".format(self.full_name, self.level, self.classes, self.days)

    def add_data(self, level=0, classes=0):
        """Aggiungi dati rispetto alla creazione di Learner
        senza bisogno di reinizializzazione
        """

        self.__init__(self.name, self.surname, level, classes)

    def _calc_days (self, level, classes):
        """Metodo per calcolare il numero di giorni
        mancanti al Learner per diventare un Python
        master.
        """

        if level==0:
            return None
        else:
            if classes == 0:
                return round(400/level, 0)
            else:
                return round((400/level)-(classes*2/24))


# alan = Learner("Alan","Marazzi", 3, 5)
# alan.add_data(2,1000)
#
# print(alan)
