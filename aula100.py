matriz = []
m = int(input("Digite o número de linhas da matriz:"))
n = int(input("Digite o número de colunas da matriz:"))
j = 0
i = 0

def constroiMatriz(m,n,matriz):
    for i in range(1,m+1):
        for j in range(1,n+1):
            linha = []
            x = int (input("Digite o elemento %i%i da matriz:"))
            linha.append(x)
        
        matriz.append(linha) 

constroiMatriz(m,n,matriz)
print(matriz)