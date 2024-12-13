
class Animale():
    Specie = " "
    Colore = " "
    zampe = 4
    coda = True
    età = 0
    sesso = 'M'
    __malato = False
    __spavaldo = False

    def __init__(self, Specie, Colore, malato, spavaldo, zampe, coda, età, sesso):
        self.Specie = Specie
        self.Colore = Colore
        self.__malato = malato
        self.__spavaldo = spavaldo
        self.zampe = zampe
        self.coda = coda
        self.età = età
        self.sesso = sesso

    def set_malato(self, malato):
        if self.__spavaldo == True:
            self.__malato = False
        else:
            self.__malato = malato

    def set_spavaldo(self, spavaldo):
        self.__spavaldo = spavaldo

    def get_malato(self):
        return self.__malato

    def get_spavaldo(self):
        return self.__spavaldo

    def faiVerso(self):

        return(self.faiVerso())



