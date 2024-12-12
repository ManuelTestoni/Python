class Progetto():


    def __init__(self, nome, start, exp, attivita =[]):
        self.__nome = nome
        self.__start = start
        self.__exp = exp
        self.__attivita = []

    #Metodi Getter & Setter
    def getNome(self):
        return self.__nome

    def getIniz(self):
        return self.__start

    def getExp(self):
        return self.__exp

    def setNome(self, nome):
        self.__nome = nome

    def setIniz(self, start):
        self.__start = start

    def setExp(self, exp):
        self.__exp = exp

    #Metodo per aggiungere un attività
    def addActivity(self, other):
        self.__attivita.append(other)
        return self
    #Metodo per controllare le varie attività di un progetto.
    def getActivity(self):
        return self.__attivita

    def __repr__(self):
        return f"Progetto(nome='{self.__nome}', inizio={self.__start}, fine={self.__exp}, attivita={self.__attivita})"

