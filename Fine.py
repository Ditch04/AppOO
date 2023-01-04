class Fine:
    def __init__(self, titled, price):
        self.__titled = titled
        self.__price = price

    @property
    def titled(self):
        return self.__titled

    @property
    def price(self):
        return self.__price

