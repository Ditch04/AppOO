class Player:
    def __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

