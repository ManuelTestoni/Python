from datetime import datetime
import pickle

import Progetto
import Attivita


utenti = ["Manuel", "Professore"]
progetti_utente = {}
stati_attività = ["Da fare", "In corso", "Completata"]
progetto = Progetto.Progetto("prova", 2024-12-20, 2025-3-20)
att = Attivita.Attivita("nome", 2024-12-25, "Da fare")
progetto.addActivity(att)

prOggetti = []
prOggetti.append(progetto)
attivita = []
attivita.append(att)

def main():


    auth = False
    while(auth != True):
        print("Ciao user, benvenuto al software per gestione progetti di Testoni srl")
        print("\n1: Log in \n2: Sign Up ")
        scelta = int(input())
        if scelta == 1:
            print("Benvenuto, qua sotto sono stampati gli utenti presenti nel nostro database, scrivi quello")
            print( " su cui vuoi loggarti: \n ")
            print(list(utenti))
            scelta_utente = input()
            if utenti.__contains__(scelta_utente):
                print("Autenticazione effettuata con successo")
                auth = True
            else:
                print("Mi dispiace autenticazione fallita, ri provare")
        elif scelta == 2:
            print("Benvenuto, inserisci il nome del tuo nuovo utente da registrare nei nostri database")
            scelta_utente = input()
            utenti.append(scelta_utente)
            print("Ciao " + scelta_utente + " grazie per esserti registrato sulla nostra piattaforma!")
            auth = True

        else:
            print("Valore inserito non valido, ri provare, non siamo soggetti a questo tipo di vulnerabilità banali")

    scelta = 0
    while scelta != 8:
        print("1: per inserire un nuovo progetto")
        print("2: per inserire una nuova attività")
        print("3: per visualizzare le attività di un progetto")
        print("4: per cambiare lo stato ad un'attività")
        print("5: per salvare i progetti su un file di backup")
        print("6: per caricare i progetti salvati da file")
        print("7 per esporare il progetto e tutte le sue attività su un file testuale")
        print("8: per uscire dal programma")
        scelta = int(input())
        if scelta == 1:
            scelta_utente = ''
            while(scelta_utente != 'N' or scelta_utente != 'n'):
                print("Vuoi creare un nuovo progetto? Inserisci il carattere 'Y' per confermare, 'N' per fermare l'operazione")
                scelta_utente = input()
                if scelta_utente == "Y" or scelta_utente == 'y':
                    progetto = newProject(scelta_utente)
                    prOggetti.append(progetto)
                elif scelta_utente == "N" or scelta_utente == 'n':
                    print("Mi dispiace che non siamo riusciti ad esserti d'aiuto, buona giornata")
                    break
                else:
                    print("Basta, come posso dimostrarti che non soffriamo questo tipo di banalità?")
                    pass
        elif scelta == 2:
            scelta_attivita = ''
            while (scelta_attivita != 'N' or scelta_attivita != 'n'):
                print(
                    "Per aggiungere un attività inserisci il carattere 'Y', 'N' per fermare l'operazione")
                scelta_attivita = input()
                if scelta_attivita == "Y" or scelta_attivita == 'y':
                    print("I progetti disponibili attualmente sono: \n")
                    cont = 1
                    for i in prOggetti:
                        print(f"{cont} : " + i.getNome())
                        cont= cont+1
                    print("Inserisci il numero corrispondente al progetto di cui vuoi sapere i dettagli")
                    indice = int(input())
                    newActivity(prOggetti[indice-1])
                elif scelta_attivita == "N" or scelta_attivita == 'n':
                    print("Mi dispiace che non siamo riusciti ad esserti d'aiuto, buona giornata")
                    break
                else:
                    print("Basta, come posso dimostrarti che non soffriamo questo tipo di banalità?")
                    pass
        elif scelta == 3:
            print("Ecco a lei le attività del progetto:\n")
            print("I progetti disponibili attualmente sono: \n")
            for i in prOggetti:
                print(i.getNome())

            print("Inserisci il numero corrispondente al progetto di cui vuoi sapere i dettagli")
            indice = int(input())
            print(printAct(prOggetti[indice]))

        elif scelta == 4:
            print("Inserisci il nuovo stato dell'attività tra i seguenti:\n")
            print("\t - In corso\n")
            print("\t - Da fare\n")
            print("\t - Completato\n")
            stato = input()
            if stato not in stati_attività:
                print("Seleziona uno tra quei valori...")
            else:
                print("di quale attività vuoi modificare lo stato?")
                cont = 0
                for i in attivita:
                    print("{cont} : "+ i.getNome())
                scelta_attivita = int(input)
                attivita[scelta_attivita-1].modState(stato)
        elif scelta == 5:
            with open("Progetti.txt", 'wb') as file_write:
                pickle.dump(prOggetti, file_write)

            print("Oggetto correttamente scritto su file")

        elif scelta == 6:
            with open("Progetti.txt", 'rb') as file_read:
                progetti_caricati = pickle.load(file_read)

            print("Oggetto correttamente letto da file")
            print(progetti_caricati)

        elif scelta == 7:
            print("Seleziona il progetto che vuoi esportare tra quelli presenti:")
            cont = 1
            for i in prOggetti:
                print(f"{cont} + : " + i.getNome())
                cont = cont+1
            print("Inserisci il numero corrispettivo al progetto da esportare")
            scelta_progetto = int(input())

            with open("Progetti.txt", 'w') as file_write:
                file_write.write(str(prOggetti[scelta_progetto-1]))

        elif scelta == 8:
            print("Grazie per aver utilizzato il nostro programma!")

        else:
            print("Scegi un opzione disponible")




    return


def newProject(scelta_utente):
    print("Inserisci il nome, la data di inizio e la data di scadenza")
    nome = input()
    data1_input = input("Inserisci la prima data (formato YYYY-MM-DD): ")
    data = datetime.strptime(data1_input, "%Y-%m-%d").date()
    data2_input = input("Inserisci la prima data (formato YYYY-MM-DD): ")
    scadenza = datetime.strptime(data2_input, "%Y-%m-%d").date()

    prog = (Progetto.Progetto(nome, data, scadenza))
    print("Oggetto creato con successo: \n" )
    print("\tnome: " + prog.getNome() + " \n\tdata inizio: " + str(prog.getIniz())+ "\n\tdata di scadenza: " + str(prog.getExp()))

    progetti_utente.update({scelta_utente: prog})
    return prog


def newActivity(progetto):
    inserimento = False
    while inserimento != True:

        print("Inserisci il nome, la data di completamento e lo stato dell'attività")
        nome = input()
        data3_input = input("Inserisci la prima data (formato YYYY-MM-DD): ")
        data_compl = datetime.strptime(data3_input, "%Y-%m-%d").date()
        stato = input()

        if data_compl <= progetto.getIniz():
            print("Data non valida")
        elif stato not in stati_attività:
            print("Valore dello stato non previsto")
        else:
            att = Attivita.Attivita(nome, data_compl, stato)
            print("Attività creata con successo: \n")
            print(
                "\tnome: " + att.getNome() + " \n\tdata inizio: " + str(att.getIniz()) + "\n\tdata di scadenza: " + att.getState())
            attivita.append(att)
            inserimento = True

    return 0

def printAct(progetto):
    print(progetto.getActivity())

if __name__ == "__main__":
    main()