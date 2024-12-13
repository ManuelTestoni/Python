from ctypes import *
so_file = "/Users/chad/Desktop/Documenti/Uni/3 Anno/Complementi_Di_Programmazione/Esercizi/ComplementiDiProgrammazione/prodottoMatrici.so"
prodottoMatrici = CDLL(so_file)

matrix3 = [
    [],
    [],
    []
]
#non funziona ma since non penso che sia una cosa così importante...
matrix3 = prodottoMatrici.multiplyMatrices()
print(matrix3)