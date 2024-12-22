import Lista
import OggettoSpesa

listaProva = []
lista = Lista.Lista(listaProva)
oggettoProva = OggettoSpesa.OggettoSpesa("Arance", 10, "Frutta")
lista.addOggetto(oggettoProva)
def main():
    scelta = 0

    while scelta != 9:
        print("Benvenuto nel programma di gestione della tua lista della spesa, premi:")
        print("\t1: Aggiungere un elemento alla tua lista della spesa")
        print("\t2: Rimuovere un eleemnto dalla lista della spesa")
        print("\t3: Visualizzare la lista della spesa completa")
        print("\t4: Modificare la quantità di un articolo esistente")
        print("\t5: Sapere la quantità totale di oggetti nella lista")
        print("\t6: Cercare un articolo per nome o categoria")
        print("\t7 Salvare la lista su file")
        print("\t8: Caricare la lista da file")
        print("\t9: Uscire dal programma")

        scelta = int(input())
        if scelta ==1:
            newObject()
        elif scelta == 2:
            delObject()
        elif scelta == 3:
            stampaLista()
        elif scelta == 4:
            modQta()
        elif scelta == 5:
            print("Il numero totale di elementi nella lista è: {len(listaProva)}")
        elif scelta == 6:
            searchObject()
        elif scelta == 7:
            saveList()
        elif scelta == 8:
            pass
            #readList()
        elif scelta == 9:
            return
        else:
            print("Errore, riprovare")




def newObject():
    print("inserisci il nome, la quantità e la categoria dell'oggetto:")
    nome = str(input())
    qta = int(input())
    categoria = str(input())

    nuovoOggetto = OggettoSpesa.OggettoSpesa(nome,qta, categoria)
    lista.addOggetto(nuovoOggetto)
    return

def delObject():
    print("Hai scelto di cancellare un oggetto, quindi di seguito verrà stampata la lista degli oggetti, scrivi il nome di quello che vuoi cancellare")
    lista_cancello = lista.getLista()
    oggetto = str(input())
    print(lista_cancello)
    if oggetto not in lista_cancello:
        print("mi dispiace quello che hai inserito non è valido")
    else:
        print("Oggetto cancellato correttamente")


def modQta():
    print("scrivi il numero corrispondente a quello che si vuole modificare")
    lista_oggetti = lista.getLista()
    for i in lista_oggetti:
        print("{i}: {lista_oggetti[i]}")
    oggetto = int(input())
    if oggetto > len(lista_oggetti):
        print("mi dispiace quello che hai inserito non è valido")
    elif oggetto < len(lista_oggetti):
        print("Mi dispiace non è valodi")
    else:
        print("Inserisci dunque la quantità dell'oggetto:")
        qta = int(input())
        lista_oggetti[oggetto].modQta(qta)
        print("Oggetto inserito correttamente")

def searchObject():
    lista_oggetti = lista.getLista()
    print("premi 1 per cercare per categoria")
    print("premi 2 per cercare per nome")
    scelta = int(input())
    if scelta == 1:
        print("Inserisci la categoria")
        categoria = str(input())
        for i in lista_oggetti:
            if i.categoria == categoria:
                print("Trovato! Ecco i suoi dettagli")
                print(i.getNome())
                print(i.getCategoria())
                print(i.getQta())
    elif scelta == 2:
        print("Inserisci il nome")
        nome = str(input())
        for i in lista_oggetti:
            if i.nome == nome:
                print("Trovato! Ecco i suoi dettagli")
                print(i.getNome())
                print(i.getCategoria())
                print(i.getQta())
    else:
        print("errore")
def stampaLista():
    listaStampa = lista.getLista()
    for i in range(0, len(listaStampa)):
        print(listaStampa[i].getNome(), listaStampa[i].getCategoria(), listaStampa[i].getQta())
    return

def saveList():
    with open("lista.txt", 'w') as fileWrite:
        lista_scrivi = lista.getLista()
        for i in lista_scrivi:
            fileWrite.write(str(i.getNome()) + "," + str(i.getCategoria() + "," + str(i.getQta()) + "\n"))

    print("Lista correttamente salvata su file!")

def readList():
    with open("lista.txt", 'r') as fileRead:
        lista_scrivi = fileRead.read()
        lista.setLista(lista_scrivi)



if __name__ == '__main__':
    main()