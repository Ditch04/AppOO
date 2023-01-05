class Pot:
    def __init__(self, total, monthly_total):
        self.__total = total
        self.__month = monthly_total

    @property
    def total(self):
        return self.__total

    @property
    def month(self):
        return self.__month










