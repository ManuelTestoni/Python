dizzonario = {1: "RED", 2: "GREEN", 3: "BLUE"}

while(1) :
    print("Inserisci la chiave del dizionario")
    input2 = int(input())
    print(dizzonario.get(input2,"Non trovato"))
    print("vuoi terminare? Inserire fine per terminare")
    input = input()
    if input == "fine":
        break
