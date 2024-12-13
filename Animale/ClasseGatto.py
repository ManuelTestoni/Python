import ClasseAnimale

class Gatto(ClasseAnimale.Animale):
    razza = " "

    def __init__(self, razza, malato, spavaldo, Specie, Colore, zampe, coda, età, sesso):
        self.razza = razza
        super().__init__(Specie, Colore, malato, spavaldo, zampe, coda, età, sesso)

    def faiVerso(self):
        print("MIAO MIAO")
        return 0

def main():
    Sfinge = Gatto("Sfinge", False, True, "Felis", "Marroncino", 4, True, 3, 'F')
    Sfinge.faiVerso()

if __name__ == "__main__":
    main()