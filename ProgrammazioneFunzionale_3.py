from functools import reduce

def somma_cifre(n):
    return sum(int(cifra) for cifra in str(n))

def somma_totale_cifre(numeri):
    # Converte ogni stringa in un intero e calcola la somma delle cifre per ciascun numero
    somme_cifre = map(lambda x: somma_cifre(int(x)), numeri)
    # Usa reduce per sommare tutte le somme delle cifre
    return reduce(lambda x, y: x + y, somme_cifre)

# Esempio di utilizzo
numeri = ["123", "456", "789"]
risultato = somma_totale_cifre(numeri)
print("Il totale cumulativo delle somme delle cifre è:", risultato)
