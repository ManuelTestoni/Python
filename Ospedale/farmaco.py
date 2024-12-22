class Farmaco:
    def __init__(self, nome, frequenza):
        self.__nome = nome
        self.__frequenza = frequenza

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str) and nome != " ":
            self.__nome = nome
        else:
            print("Errore nome mancante o scorretto")

    @property
    def frequenza(self):
        return self.__frequenza

    @frequenza.setter
    def frequenza(self, frequenza):
        if isinstance(frequenza, int) and frequenza > 0:
            self.__frequenza = frequenza
        else:
            print("La frequenza non può essere negativa o uguale a zero o mancante")

    def __repr__(self):
        return f"(nome='{self.__nome}', frequenza={self.__frequenza})"