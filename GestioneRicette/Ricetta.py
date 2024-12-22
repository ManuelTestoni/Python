class Ricetta():
    def __init__(self, nome, ingredienti, difficolta, data_crea, descr):
        self.__nome = nome
        self.__ingredienti = ingredienti
        self.__difficolta = difficolta
        self.__data_crea = data_crea
        self.__descr = descr

    @property
    def data(self):
        return self.__data_crea

    @data.setter
    def data(self, data_crea):
        self.data_crea = data_crea

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
    def ingredienti(self):
        return self.__ingredienti

    @ingredienti.setter
    def ingredienti(self, ingredienti):
        if isinstance(ingredienti, dict):
            self.__ingredienti = ingredienti
        else:
            print("Errore")

    @property
    def difficolta(self):
        return self.__difficolta

    @difficolta.setter
    def difficolta(self, difficolta):

        if isinstance(difficolta, list):
            self.__difficolta = difficolta
        else:
            print("Errore")

    @property
    def descr(self):
        return self.__descr

    @descr.setter
    def descr(self, descr):
        if isinstance(descr, str) and descr != " ":
            self.__descr = descr
        else:
            print("Errore")

    def __repr__(self):
        return f"Ricetta(nome='{self.__nome}', ingredienti={self.__ingredienti}, difficolta={self.__difficolta}, data_crea={self.__data_crea}, descr={self.__descr})"
