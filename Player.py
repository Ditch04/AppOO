from Team import Team


class Player:

    def __init__(self, firstname, fines={}, total=0):
        self.__firstname = firstname
        self.__fines = fines
        self.__total = total

    @property
    def firstname(self):
        return self.__firstname

    @property
    def fines(self):
        return self.__fines

    @property
    def total(self):
        return self.__total

    def __str__(self):
        return self.firstname + '\n' + "amendes : " + self.fines + '\n' + "total : " + self.total + '\n'

    def add_fine(self, fine):
        if fine.titled not in self.fines:
            self.fines.update(fine)
        else:
            self.fines[fine.times] += 1


