import pickle

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

with open ("MatriceSuFile.txt", 'w') as file:
    file.write(str(matrice))

with open ("MatriceSuFile.txt", 'r') as file2:
    amatrice = file2.read()

print(amatrice)

with open ("MatriceSuFile.txt", 'wb') as file3:
    pickle.dump(matrice, file3)

with open( "MatriceSuFile.txt", 'rb') as file4:
    amatriciana = pickle.load(file4)

print(amatriciana)
