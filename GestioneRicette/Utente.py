class Utente():
    def __init__(self, nome, ricette):
        self.__nome = nome
        self.__ricette = ricette

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str) and nome != " ":
            self.__nome = nome
        else:
            print("Errore")

    @property
    def ricette(self):
        return self.__ricette

    @ricette.setter
    def ricette(self, ricette):
        self.__ricette = ricette

    def addRicetta(self, other):
        self.__ricette.append(other)

