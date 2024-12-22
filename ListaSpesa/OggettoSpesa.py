class OggettoSpesa:

    def __init__(self, nome,qta, categoria):
        self.nome = nome
        self.qta = qta
        self.categoria = categoria

    def setNome(self, nome):
        self.nome = nome

    def setCategoria(self, categoria):
        self.categoria = categoria

    def setQta(self, qta):
        self.qta = qta

    def getNome(self):
        return self.nome

    def getCategoria(self):
        return self.categoria

    def getQta(self):
        return self.qta

    def modQta(self, newQta):
        if newQta <= 0:
            return(print("hai inserito un valore non valido"))
        else:
            self.qta = newQta

