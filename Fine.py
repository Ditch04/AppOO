class Fine:
    def __init__(self, titled, price, times=0):
        self.__titled = titled
        self.__price = price
        self.__times = times

    @property
    def titled(self):
        return self.__titled

    @property
    def price(self):
        return self.__price

    @property
    def times(self):
        return self.__times


oubli = Fine("oubli d'un équipement", 2)
carte_jaune = Fine("sanction par une carte jaune lors d'un match", 5)
