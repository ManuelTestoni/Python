a = [1,2,3,4,5,6,7,8,9,10]

lista = list(filter(lambda a:a if a%2==0 else None, a))
print(lista)
lista = list(map(lambda a: a**2, lista))
print(lista)