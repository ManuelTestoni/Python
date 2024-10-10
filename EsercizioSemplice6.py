dizio = {3894535346: "Manuel Testoni", 3278425360: "Marco Magni G**", 3428832688: "Riccardo Rimondi"}
inp = ""
while(inp != "fine"):
    print("Inserisci \n \t 1 per Inserire un numero nella rubrica; \n \t 2 per cancellare un numero dalla rubrica; \n \t 3 per stampare l'intera rubrica")
    inp = int(input())
    if inp == 1:
        print("Inserisci il numero e la persona da aggiungere in rubrica")
        numero = int(input())
        persona = input()
        dizio[numero] = persona
    elif inp == 2:
        print("inserisci il numero da cancellare in rubrica")
        numero = int(input())
        dizio.pop(numero)
    elif inp == 3:
        print(dizio)

    else :
        print("Valore non atteso, riprovare")



    print("Inserisci fine per uscire dalla rubrica; \n")
