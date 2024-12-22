import paziente
import farmaco

#lista che tiene in memoria ipotetici pazienti per il programma
Pazienti = []
Farmaci = []
pazienteSelezioato = " "
paz = paziente.Paziente("Manuel", 21, [])
farm = farmaco.Farmaco("xanax", 4)
Farmaci.append(farm)
paz.__setattr__("farmaci", Farmaci)
Pazienti.append(paz)



def main():

    auth = False
    while(auth != True):
        print("Ciao user, benvenuto al software per l'ospedale Testoni")
        print("\n1: Scegli paziente \n2: Crea Pazeiente ")
        scelta = int(input())
        if scelta == 1:
            if len(Pazienti) != 0:
                print("Benvenuto, qua sotto sono stampati gli utenti presenti nel nostro database, scrivi quello")
                print("su cui vuoi loggarti: \n ")
                print(list(Pazienti))
                scelta_paziente = input()
                for i in Pazienti:
                    if i.nome.__contains__(scelta_paziente):
                        print("Autenticazione effettuata con successo")
                        auth = True
                        pazienteSelezionato = scelta_paziente
                    else:
                        print("Mi dispiace autenticazione fallita, ri provare")
            else:
                print("Mi dispiace non ci sono pazienti registrati al momento, crea un nuovo paziente!")
                auth = False
        elif scelta == 2:
            print("Benvenuto, inserisci il nome del tuo nuovo paziente e l'eta")
            newPaz()
            auth = True
        else:
            print("Valore inserito non valido, ri provare, non siamo soggetti a questo tipo di vulnerabilità banali")

    scelta = 0
    while scelta != 8:
        print("1: Per inserire dei farmaci per il paziente selezioanto")
        print("2: Stampare i farmaci del paziente selezionato")
        print("3: Rimuovere un farmaco per il paziente")
        print("4: Vedere la terapia odierna del paziente")
        print("5: Vedere la terapia del paziente tra un numero preciso di giorni")
        print("6: Salvare i pazienti e la terapia odierna su file")
        print("7 Caricare i pazienti e la loro terapia odierna su file")
        print("8: per uscire dal programma")
        scelta = int(input())
        if scelta == 1:
            addFarmaco()
        elif scelta == 2:
            printFarmaci()
        elif scelta == 3:
            delFarmaco()
        elif scelta == 4:
            viewTerapia()
        elif scelta == 5:
            print("Vuoi controllare la terapia del paziente tra quanti giorni?")
            giorni = int(input())
            viewTerapiaDay(giorni)
        elif scelta == 6:
            scriviBackUp()
        elif scelta == 7:
            pass
        elif scelta == 8:
            print("Grazie per aver utilizzato il nostro programma!")
        else:
            print("Scegi un opzione disponible")

    return

def newPaz():
    nome = str(input())
    eta = int(input())
    Paz = paziente.Paziente(nome, eta, Farmaci)
    Pazienti.append(Paz)
    pazienteSelezioato = Paz.nome

def addFarmaco():
    print("Inserisci il nome e la frequenza di assunzione del farmaco")
    nome = str(input())
    frequenza = int(input())

    farm = farmaco.Farmaco(nome, frequenza)
    for i in Pazienti:
        if i.nome == pazienteSelezioato:
            i.addFarmaco(farm)


def printFarmaci():
    if len(Farmaci) > 0:
        for i in Farmaci:
            print(i.nome + "", + i.frequenza)
    else:
        print("Non vi sono farmaci inseriti per il paziente selezionato, aggiungerne e riprovare")

def delFarmaco():
    if len(Farmaci) > 0:
        count = 0
        for i in Farmaci:
            count = count+1
            print(f"{count}: {i} ")
        print("inserisci il numero del farmaco che vuoi eleminare")
        cancella_farmaco = int(input())
        for i in Pazienti:
            if i.nome == pazienteSelezioato:
                i.delFarmaco(cancella_farmaco-1)
    else:
        print("Non vi sono farmaci inseriti per questo paziente")


def viewTerapia():
    print("Questi sono tutti i farmaci che il paziente dovrà prendere oggi")
    print(str(Farmaci))

def viewTerapiaDay(giorni):
    for i in Farmaci:
        if i.frequenza % giorni == 0:
            print(i.nome, i.frequenza)
        else:
            pass
    print(f"Questi sono tutti i farmaci che il paziente dovrà prendere in terapia tra: {giorni} giorni")


def scriviBackUp():
    with open("terapia.txt", "w") as f:
        for i in Pazienti:
            f.write(i.nome + " " + str(i.eta) + " ")
            Farmaci = i.getFarmaci()
            for j in Farmaci:
                f.write(j.nome + " " + str(j.frequenza) + " \n")

if __name__ == "__main__":
    main()