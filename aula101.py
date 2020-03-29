import random 

matriz = []
def geraMatriz(matriz):
    lista = list(range(16)):
    while len(lista) > 0:
        linha = []
        for i in range(4):
            x = range.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)

for i in range(3):
    geraMatriz(matriz)
    print(matriz)
    matriz = []
    