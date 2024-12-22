#importazione dei moduli necessari
import pickle
import Utente
import Ricetta
import time
#creazione varaibili di test
Ut = Utente.Utente("Prova", [])
ingredienti = {"Burro" : 10, "Panna" : 2}
Ricetta_prova = Ricetta.Ricetta("Mascarpone", ingredienti, "Medio", 20-12-2024, "Semplicemente il mascarpone")
Ut.addRicetta(Ricetta_prova)
lista_utenti = []
lista_utenti.append(Ut)
lista_difficolta = ["Facile", "Medio", "Difficile"]

#implementazione del menù di log-in
def main():
    auth = False
    while (auth != True):
        print("Ciao user, benvenuto al software per Gestione Ricette di Manuel Testoni")
        print("\n1: Log in \n2: Sign Up ")
        scelta = int(input())
        if scelta == 1:
            print("Benvenuto, qua sotto sono stampati gli utenti presenti nel nostro database, scrivi quello")
            print(" su cui vuoi loggarti: \n ")
            for i in lista_utenti:
                print(i.nome)
            scelta_utente = str(input())
            for i in lista_utenti:
                if i.nome == scelta_utente:
                    print("Autenticazione effettuata con successo!")
                    auth = True
                    Ut = i
                else:
                    print("Mi dispiace autenticazione non riuscita, riprovare")
                    auth = False
                    return
        elif scelta == 2:
            print("Benvenuto, inserisci il nome del tuo utente da registrare")
            nome = str(input())
            Ut = Utente.Utente(nome, [])
            auth = True
            print("Autenticazione effettuata con successo!")

            scelta = 0
        #implementazione del menu di scelta opzioni una volta loggati
        while scelta != 8:
            print("\t 1: Crea nuova ricetta")
            print("\t 2: Ricerca ricetta")
            print("\t 3: Stampa ricette utente")
            print("\t 4: Salvare l'archivio delle ricette su file (pickle)")
            print("\t 5: Caricare l'archivio delle ricette da file (pickle)")
            print("\t 6: Salvare l'archivio delle ricette su file (.txt)")
            print("\t 7: Caricare l'archivio delle ricette da file (.txt)")
            print("\t 8: Per uscire dal programma'")
            scelta = int(input())

            if scelta == 1:
                dec_calc_temp(addRicetta(Ut))
            elif scelta == 2:
                recipes_list = filtraRicetta(Ut)
                for i in recipes_list:
                    print(f"{i.nome}")
            elif scelta == 3:
                viewRicette(Ut)
            elif scelta == 4:
                scriviBackUp(Ut)
            elif scelta == 5:
                leggiBackUp(Ut)
            elif scelta == 6:
                esportaRecipes(Ut)
            elif scelta == 7:
                importaRecipes(Ut)
            elif scelta == 8:
                print("Buona giornata")
                return
            else:
                print("Valore non previsto, riprovare")

        else:
            print("Errore durante l'accesso, riprovare")
            auth = False

#funzione per aggiungere ricette
def addRicetta(Ut):
    print("Inserisci il nome, lista_ingredienti, difficolta, data_creazione, descrizione")
    nome = str(input())
    print("Di quanti ingredienti è composta la ricetta?")
    n_ingredienti = int(input())
    ingredienti = {}
    for i in range(n_ingredienti):
        print("inserisci il nome dell'ingrediente e la sua quantità")
        nome_ingr = str(input())
        qta = int(input())
        ingredienti[nome_ingr] = qta

    difficolta = str(input())
    if difficolta not in lista_difficolta:
        print("Difficoltà inserita non valida")
        return
    data_creazione = time.time()
    descrizione = str(input())

    ricetta = Ricetta.Ricetta(nome,ingredienti,difficolta,data_creazione,descrizione)
    Ut.addRicetta(ricetta)


#decoratore per il calcolo del tempo della aggiunta di una ricetta
def dec_calc_temp(addRicetta):
    def calc_temp():
        start = time.time()
        value = addRicetta()
        end = time.time()
        print("ci ha messo ", end - start, " secondi")
        return value
    return calc_temp

#funzione che usa filter() per ritornare una lista ridotta di ricette attraverso paradigma funzionale
def filtraRicetta(Ut):
    lista_ricette = Ut.ricette
    print("Queste sono le ricette disponibili per l'utente corrente, filtriamole per difficoltà")
    for i in lista_ricette:
        print(i.nome)
    print("Per che difficoltà si vuole filtrare?")
    print("\t 1: Facile")
    print("\t 2: Medio")
    print("\t 3: Difficile")
    scelta_diff = int(input())
    lista_difficolta = []
    for i in lista_ricette:
        lista_difficolta.append(i.difficolta)
    if scelta_diff == 1:
        return filter(lambda x: x.difficolta == "Facile", lista_ricette)
    elif scelta_diff == 2:
        return filter(lambda x: x == "Medio", lista_ricette)
    elif scelta_diff == 3:
        return filter(lambda x: x == "Difficile", lista_ricette)
    else:
        print("Mi dispiace quello che hai inserito non è previsto")

#funzione per stampare le ricette dell'utente corrente
def viewRicette(Ut):
    lista_ricette = Ut.ricette
    count = 0
    for i in lista_ricette:
        count += 1
        print(f"Ricetta {count}: ", i.nome)


#funzione per caricare su file le ricette dell'utente attraverso pickle
def scriviBackUp(Ut):
    lista_ricette = Ut.ricette
    with open("Ricette.txt", 'wb') as f:
        pickle.dump(lista_ricette, f)
    print("Progetti caricati correttamente su file")

#funzione per caricare da file precedentemente esportato tramite pickle
def leggiBackUp(Ut):
    with open("Ricette.txt", 'rb') as f:
        lista_ricette = pickle.load(f)

    print("Ricette caricate correttamente")
    Ut.ricette = lista_ricette
    viewRicette(Ut)


#funzione per esportare le ricette su file txt
def esportaRecipes(Ut):
    print("1: Esporta intero ricettario \n 2: Esporta ricettario filtrato su difficolta")
    scelta = int(input())
    lista_ricette = Ut.ricette
    if scelta == 1:
        with open("RicetteEsportate.txt", 'w') as f:
            for i in lista_ricette:
                f.write(f"{i.nome}, {i.difficolta}, {i.ingredienti}, {i.descr} \n")

    elif scelta == 2:
        lista_ricette = filtraRicetta(Ut)
        with open("RicetteEsportate.txt", 'w') as f:
            for i in lista_ricette:
                f.write(f"{i.nome} \n {i.difficolta}\n {i.ingredienti}\n {i.descr} \n")
    else:
        print("Valore imprevisto riprovare")
        return


def importaRecipes(Ut):
    lista_ricette = Ut.ricette
    with open("RicetteEsportate.txt", 'r') as f:
        for line in f:
            nome = f.read()
            difficolta = f.read()
            ingredienti = f.read()
            descr = f.read()
            ricetta = Ricetta.Ricetta(nome, ingredienti,difficolta, time.time(), descr)
            Ut.addRicetta(ricetta)


if __name__ == '__main__':
    main()