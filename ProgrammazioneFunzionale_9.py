#Creare una funzione che prenda una lista di stringhe e ritorni una lista delle stesse
#stringhe, ma in ordine di lunghezza crescente.
#Utilizzare sorted con cmp_to_key di functools per trasformare una funzione di
#confronto della lunghezza delle stringhe in una chiave di ordinamento.

import functools

l =["Ciao", "Io", "Sono","L'uomo", "Focaccina"]

g = sorted(l, key=lambda x:len(x))
print(list(g))