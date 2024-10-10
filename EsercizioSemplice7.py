def stampa(*args, **kwargs):
    print(*args)
    print(**kwargs)

print("Inserisci valori")
val = []

while 1:
    a = input()
    val.append(a)
    if a == '#':
        break


stampa(val)
