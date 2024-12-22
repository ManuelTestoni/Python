import oggetto

class utente:
    def __init__(self, nome, magazzino):
        self.__nome = nome
        self.__magazzino = magazzino

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str) and nome != " ":
            self.__nome = nome

        else:
            print("Il nome non può essere una stringa vuota")

    @property
    def magazzino(self):
        return self.__magazzino

    @magazzino.setter
    def magazzino(self, magazzino):
        self.__magazzino = magazzino


    def addMagazzino(self, magazzino):
        self.__magazzino = magazzino

    def getMagazzino(self):
        return self.__magazzino

    def addOgg(self, other):
        self.magazzino.append(other)
