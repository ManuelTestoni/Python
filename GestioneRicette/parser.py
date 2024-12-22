import argparse
from main import filtraRicetta
import Utente
import Ricetta

parser = argparse.ArgumentParser()
parser.add_argument("Nome", help="Nome dell'utente", nargs="?", default="Prova")
parser.add_argument("Difficoltà", help="Difficoltà delle ricette da filtrare", nargs="?", default="Facile")
parser.add_argument("NomeFile", help="File dove esportare", nargs="?", default="Argomenti.txt")
parse = parser.parse_args()

ingredienti = {"Burro" : 10, "Panna" : 2}
utente_Prova = Utente.Utente(parse.Nome, [])
Ricetta_prova1 = Ricetta.Ricetta("Mascarpone", ingredienti, "Facile", 20-12-2024, "Semplicemente il mascarpone")
Ricetta_prova2 = Ricetta.Ricetta("Tiramisu", ingredienti, "Medio", 20-12-2024, "Semplicemente il Tiramisu")
Ricetta_prova3 = Ricetta.Ricetta("Pan Brioches", ingredienti, "Difficile", 20-12-2024, "Semplicemente il Pan Brioches")
utente_Prova.addRicetta(Ricetta_prova1)
utente_Prova.addRicetta(Ricetta_prova2)
utente_Prova.addRicetta(Ricetta_prova3)

with open(parse.NomeFile, "w") as f:

        utente_Prova.ricette = filtraRicetta(utente_Prova)
        lista_ricette = utente_Prova.ricette
        for i in lista_ricette:
                f.write(f"{i.nome}, {i.difficolta}, {i.ingredienti}, {i.descr} \n")
