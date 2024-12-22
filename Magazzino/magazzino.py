class Magazzino:
    def __init__(self, nome, oggetti):
        self.__nome = nome
        self.__oggetti = oggetti

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
    def ogetti(self):
        return self.__oggetti

    @ogetti.setter
    def ogetti(self, ogetti):
        if isinstance(ogetti, list):
            self.__oggetti = ogetti
        else:
            print("Errore")

    def addOggetto(self, oggetto):
        self.__oggetti.append(oggetto)

    def delOggetto(self, index):
        self.__oggetti.pop(index)