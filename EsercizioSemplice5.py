print("vuoi la stampa dei numeri pari o dispari, \n \t inserisci 0 per i pari, \n \t 2 per i dispari")
input = int(input())
if input == 0:
    for i in range(0,100,2):
        print(i)
else:
    for i in range(1,100,2):
        print(i)