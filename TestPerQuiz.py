#una variabile può cambiare tipo durante l'esecuzione
a = 30
print(a)
a = "ciao"
print(a)

#le stringe sono immutabili, ogni oeprazione ceh sembra le modifichi viene in realtà eseguita su un'altra stringa
b = a.replace("ciao", "ciaoioio")
print(a)
print(b)

#possiamo accedere ad elementi della lista tramite indici negativi
list1 = [1,2,3,4,5,6,7,8]
print(list1[-1])

#creazione di copia della lista tramite operatore ":"
list2 = list1[:]
print(list2)

x = 0

(x**2 for x in range(10))