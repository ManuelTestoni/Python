class Lista:

    def __init__(self, lista):
        self.lista = lista

    def addOggetto(self, other):
        self.lista.append(other)

    def delOggetto(self, str):
        self.lista.remove(str)

    def getLista(self):
        return self.lista

    def setLista(self, lista):
        Lista.lista = lista

    def __repr__(self):
        return f"Lista(nome='{self.nome}', qta={self.qta}, categiria={self.categoria})"