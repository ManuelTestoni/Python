from itertools import groupby
def raggruppa_parole_per_lunghezza(parole):
    # Usa map per ottenere una lista di tuple (lunghezza, parola)
    lunghezze_parole = map(lambda parola: (len(parola), parola), parole)
    # Ordina le tuple per lunghezza della parola
    lunghezze_parole = sorted(lunghezze_parole, key=lambda x: x[0])
    # Usa groupby per raggruppare le parole per lunghezza e crea il dizionario
    dizionario = {lunghezza: list(map(lambda x: x[1], gruppo)) for lunghezza, gruppo in
                  groupby(lunghezze_parole, key=lambda x: x[0])}

    return dizionario


# Esempio di utilizzo
parole = ["ciao", "hello", "gatto", "amico", "piatto", "cane", "mela", "cia"]
risultato = raggruppa_parole_per_lunghezza(parole)
print("Dizionario delle parole raggruppate per lunghezza:", risultato)


