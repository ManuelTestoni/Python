#priImplementare una funzione che riceva una lista di numeri e utilizzi map per elevare
#ogni numero al quadrato.
#Successivamente, con filter, selezionare solo i numeri il cui quadrato è divisibile per
#4 e restituirli.

import math

l = [1,2,3,4,5,6,7,8,9]

def lista_quadrata(l):
    g = map(lambda x:x*x, l)
    filtrato = filter(lambda x:x%4==0, g)
    quadrato_filtrato = map(lambda x:math.sqrt(x), filtrato)
    return quadrato_filtrato

quadratox = lista_quadrata(l)
print("I numeri da 1 a 9 i cui quadrati loro quadrati sono divisibili per 4 sono: ")
print(list(quadratox))
