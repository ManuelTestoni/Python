#Utilizzando functools.partial, creare una funzione parziale che fissi un argomento
#per una funzione di moltiplicazione. Definire una funzione che moltiplica due numeri
#e crea una versione parziale che fissa uno dei due fattori.
#Ad esempio, se fissi il primo argomento a 5, la funzione risultante deve moltiplicare
#ogni valore dato per 5.

l = [1,2,3,4,5,6,7,8,9]

def prodotto(x, y):
    return x*y

prodotto_lista = prodotto(l[3], y =5)
print(prodotto_lista)



