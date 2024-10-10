print("Inserisci il numero del quale vuoi vedere i numeri dispari")
a = int(input())

lista = (x if x%2!=0 else None for x in range(a))
print(list(lista))



