class Learner(object):
    def __init__(self, name, surname, level=0, classes=0):
        self.name = name
        self.surname = surname
        self.full_name = name +" "+ surname
        self.level = 3 if abs(level > 3) else abs(level)
        self.classes = abs (classes)
        self.days = self._calc_days(self.level, self.classes)

    def __repr__(self):
        return "Learner {}:\nlevel->{}\nclasses->{}\ndays{}".format(self.full_name, self.level, self.classes, self.days)

    def add_data (self, level=0, classes=0):
        self.__init__(self.name, self.surname, level, classes)

    def _calc_days (self, level, classes):
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
