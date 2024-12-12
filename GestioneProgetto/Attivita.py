class Attivita:
    def __init__(self, nome, iniz, state):
        self.__nome = nome
        self.__iniz = iniz
        self.__state = state

    def getNome(self):
        return self.__nome

    def getIniz(self):
        return self.__iniz

    def getState(self):
        return self.__state

    def setNome(self, nome):
        self.__nome = nome

    def setIniz(self, iniz):
        self.__iniz = iniz

    def setState(self, state):
        self.__state = state

    def modState(self, newState):
        self.__state = newState
        return self