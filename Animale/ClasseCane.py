import ClasseAnimale
import random

class Cane(ClasseAnimale.Animale):
    razza = " "
    volte = 1 #Attributo di classe che conta quante volte la casse è stata istanziata
    luogo = ""


    def __init__(self, razza, malato, spavaldo, Specie, Colore, zampe, coda, età, sesso, luogo):
        self.razza = razza
        Cane.volte = Cane.volte + 1 #ogni volta che il metodo __init__ viene chiamato aumentiamo di 1 l'attributo
        #volte di classe
        self.luogo = luogo
        super().__init__(Specie, Colore, malato, spavaldo, zampe, coda, età, sesso)

    def abbaia(self):
        super().faiVerso()

    def get_razza(self):
        return self.razza

    def cammina(self):
        print("PADRONE ANDIAMO A CAMMINARE TI PREGO")

    def corri(self):
        print("CORRIAMO PADRONE CORRIAMO WOF WOF")

    def volteChiamate(self): #metodo che ritorna il numero di volte che la classe è stata istanziata.
        return Cane.volte

    def __add__(self, other):
        if (self.età > 15):
            print("Il cane è troppo vecchio per fare figli")
        elif (self.età < 1):
            print("Il cane è troppo piccolo per fare figli")
        elif (self.sesso == other.sesso):
            print("I cani non possono esser froci")
        else:
            razze_posibili = [self.get_razza(), other.get_razza()]
            return Cane(random.choice(razze_posibili), False,True, "Canis", 'White', 4, True, 0, 'M')

    def faiVerso(self):
        print("BAU BAU")
        return 0

    def stessoLuogo(self,other):
        if(self.luogo == other.luogo):
            print("Si, possono vivere nello stesso luogo")
        else:
            print("No, non possono vivere nello stesso luogo")


def main():
    GoldenRetriever = Cane("GoldenRetriever", False, True, 'Canis', 'Panna', 4, True, 10, 'M', "tundra")
    GoldenRetriever.faiVerso()

if __name__ == "__main__":
    main()