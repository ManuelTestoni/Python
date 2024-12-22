#lista che tiene in memoria ipotetici utenti per il programma
utenti = ["Manuel", "Professore"]


def main():

    auth = False
    while(auth != True):
        print("Ciao user, benvenuto al software per gestione progetti di Testoni srl")
        print("\n1: Log in \n2: Sign Up ")
        scelta = int(input())
        if scelta == 1:
            print("Benvenuto, qua sotto sono stampati gli utenti presenti nel nostro database, scrivi quello")
            print(" su cui vuoi loggarti: \n ")
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
        print("1: ")
        print("2: ")
        print("3: ")
        print("4: ")
        print("5: ")
        print("6: ")
        print("7 ")
        print("8: per uscire dal programma")
        scelta = int(input())
        if scelta == 1:

        elif scelta == 2:

        elif scelta == 3:

        elif scelta == 4:

        elif scelta == 5:

        elif scelta == 6:

        elif scelta == 7:

        elif scelta == 8:
            print("Grazie per aver utilizzato il nostro programma!")
        else:
            print("Scegi un opzione disponible")

    return


if __name__ == "__main__":
    main()