import oggetto
import Utente

#lista che tiene in memoria ipotetici utenti per il programma
Manuel = Utente.utente("Manuel", [])
utenti = []
utenti.append(Manuel)

def main():
    UtenteScelto = Utente.utente("Scelto", [])
    auth = False
    while(auth != True):
        print("Ciao user, benvenuto al software per gestione progetti di Testoni srl")
        print("\n1: Log in \n2: Sign Up ")
        scelta = int(input())
        if scelta == 1:
            print("Benvenuto, qua sotto sono stampati gli utenti presenti nel nostro database, scrivi quello")
            print(" su cui vuoi loggarti: \n ")
            for i in utenti:
                print(f"{i.nome}")
            scelta_utente = input()
            for i in utenti:
                if i.nome.__contains__(scelta_utente):
                    Ut = Utente.utente(i.nome, i.magazzino)
                    print("Autenticazione effettuata con successo")
                    auth = True
                else:
                    print("Mi dispiace autenticazione fallita, ri provare")
        elif scelta == 2:
            print("Benvenuto, inserisci il nome del tuo nuovo utente da registrare nei nostri database")
            scelta_utente = input()
            Ut = Utente.utente(scelta_utente, [])
            utenti.append(Ut)
            print("Ciao " + scelta_utente + " grazie per esserti registrato sulla nostra piattaforma!")
            auth = True

        else:
            print("Valore inserito non valido, ri provare, non siamo soggetti a questo tipo di vulnerabilità banali")

    scelta = 0
    while scelta != 8:
        print("1: Per inserire uno o più oggetti in magazzino")
        print("2: Per visualizzare la quantità disponibile in magazzino di un oggetto")
        print("3: Per prelevare una determinata quantità di oggetti")
        print("4: Per depositare una determinata quantità di oggetti")
        print("5: Per visionare i movimenti di un oggetto")
        print("6: Per scrivere su file di backup")
        print("7 ")
        print("8: per uscire dal programma")
        scelta = int(input())
        if scelta == 1:
            print("Quanti oggetti vorresti inserire?")
            num_ogg = int(input())
            for i in range(num_ogg):
                addObj(Ut)
        elif scelta == 2:
            viewQta(Ut)
        elif scelta == 3:
            sceltaPrelievo(Ut)
        elif scelta == 4:
            sceltaPrelievo(Ut)
        elif scelta == 5:
            viewMovimenti(Ut)
        elif scelta == 6:
            backUp(Ut)
        elif scelta == 7:
            pass
        elif scelta == 8:
            print("Grazie per aver utilizzato il nostro programma!")
        else:
            print("Scegi un opzione disponible")

    return

def addObj(Ut):
    print("Inserisci il nome dell'oggetto e la quantità")
    nome = str(input())
    qta = int(input())

    ogg = oggetto.oggetto(nome, qta, [])
    Ut.addOgg(ogg)
    print(list(Ut.getMagazzino()))
    #Ut.addMagazzino(listaOgg)

def viewQta(Ut):
    print("Di seguito verranno stampati tutti gli oggetti del magazzino")
    print("Inserisci il numero corrispondente all'oggetto di cui vuoi sapere la quantità")
    count = 0
    for i in Ut.getMagazzino():
        count += 1
        print(f"{count} {i.nome}")
    scelta = int(input())
    lista = Ut.getMagazzino()
    print(f"in magazzino sono presenti {lista[scelta-1].qta} {lista[scelta-1].nome}")


def sceltaDeposito(Ut):
    print("Di seguito verranno stampati tutti gli oggetti del magazzino")
    print("Inserisci il numero corrispondente all'oggetto da depositare")
    count = 0
    for i in Ut.magazzino:
        count += 1
        print(f"{count} {i.nome}")
    scelta = int(input())
    print("Ora inserisci la quantità dell'oggetto")
    qta = int(input())
    lista = Ut.getMagazzino()
    lista[scelta-1].deposito(qta)


def sceltaPrelievo(Ut):
    print("Di seguito verranno stampati tutti gli oggetti del magazzino")
    print("Inserisci il numero corrispondente all'oggetto da prelevare")
    count = 0
    for i in Ut.magazzino:
        count += 1
        print(f"{count} {i.nome}")
    scelta = int(input())
    print("Ora inserisci la quantità dell'oggetto")
    qta = int(input())
    lista = Ut.getMagazzino()
    lista[scelta-1].prelievo(qta)

def viewMovimenti(Ut):
    print("Di seguito verranno stampati tutti gli oggetti del magazzino")
    print("Inserisci il numero corrispondente all'oggetto da prelevare")
    count = 0
    for i in Ut.magazzino:
        count += 1
        print(f"{count} {i.nome}")
    scelta = int(input())
    with open("movimenti.txt", 'r') as file:
        for line in file:
            print(f"{line}")

def backUp(Ut):
    print("Preparati, stiamo per caricare su un file di back up tutti gli utenti e i loro magazzini!")
    with open("backUp.txt", 'w') as file:
        for i in utenti:
            print(f"{i.nome}", file=file)
            listaOgg = i.magazzino
            for j in listaOgg:
                print(f"{j.nome}", file=file)
                print(f"{j.qta}", file=file)
                movimenti = j.movimenti
                for k in movimenti:
                    print(f"{k}",  file=file)

if __name__ == "__main__":
    main()