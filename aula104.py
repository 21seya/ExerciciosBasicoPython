def criaLista():
    lista = []

    m = int(input("Digite o tamanho da lista:"))

    for i in range(m):
        ele = float(input("Digite o elemento %i de %i "%(i+1,m)))
        lista.append(ele)

    return lista

def main():
    l1 = criaLista()

    n = int(input("Digite o numero de elementos que se deseja somar"))

    soma = 0
    for i in range(len(l1)):
        if i == n:
            break

        soma += l1[i]

    print("A soma é ",soma)

main()
