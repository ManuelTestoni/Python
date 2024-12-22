class oggetto:
    def __init__(self, nome, qta, movimenti):
        self.__nome = nome
        self.__qta = qta
        self.__movimenti = movimenti

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str) and nome != " ":
            self.__nome = nome
        else:
            print("nome inserito non è valido")

    @property
    def qta(self):
        return self.__qta

    @qta.setter
    def qta(self, qta):
        if isinstance (qta, int) and qta > 0:
            self.__qta = qta
        else:
            print("impossibile aggiungere oggetti con quantità negativa")

    @property
    def movimenti(self):
        return self.__movimenti

    @movimenti.setter
    def movimenti(self, movimenti):
        if isinstance(movimenti, list):
            self.__movimenti = movimenti
        else:
            print("Errore")

    def prelievo(self, qta_prelevo):
        if self.__qta > qta_prelevo:
            self.__qta -= qta_prelevo
            print("prelevo effettuato con successo!")
            self.__movimenti.append(f"Prelevo effettuato per: {self.__nome}, {self.__qta}")
            with open("movimenti.txt", 'a') as movimento:
                movimento.write(f"Prelevo effettuato per: {self.__nome}, {self.__qta}")
        else:
            print("Mi dispiace prelievo non possibile, quantità inserita troppo elevata")

    def deposito(self, qta_deposito):
        self.__qta += qta_deposito
        self.__movimenti.append(f"Deposito effettuato per: {self.__nome}, {self.__qta}")
        with open("movimenti.txt", 'a') as movimento:
            movimento.write(f"Effettuato deposito per: {self.__nome}, {self.__qta}")

