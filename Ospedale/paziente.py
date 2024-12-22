class Paziente:
    def __init__(self, nome, eta, farmaci):
        self.__nome = nome
        self.__eta = eta
        self.__farmaci = farmaci

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str) and nome != " ":
            self.__nome = nome
        else:
            print("Il nome non può esser vuoto o nome errato")

    @property
    def eta(self):
        return self.__eta

    @eta.setter
    def eta(self, eta):
        if isinstance(eta, int) and eta >= 0:
            self.__eta = eta
        else:
            print("Il paziente non può avere un età negativa")

    @property
    def farmaci(self):
        return self.__farmaci

    def getFarmaci(self):
        return self.__farmaci

    @farmaci.setter
    def farmaci(self, farmaci):
        if isinstance(farmaci, list):
            self.__farmaci = farmaci

    def __repr__(self):
        return f"Paziente(nome='{self.__nome}', qta={self.__eta}, terapia={self.__farmaci})"

    def setFarmaci(self, farmaci):
        self.__farmaci = farmaci

    def addFarmaco(self, farmaco):
        self.__farmaci.append(farmaco)

    def delFarmaco(self, index):
        self.__farmaci.pop(index)