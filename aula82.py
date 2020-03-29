lista = []

num = int(input("Digite um numero da sequencia:"))

while num != -1:
    lista.append(num)
    num = int(input("Digite um numero da sequencia:"))

elemento = int(input("Digite o elemento a ser procurado: ")) 

for i in range(len(lista)):
    if lista[i] == elemento:
        cont += 1

print(" O elemento %i aparece %i vezes na sequencia"%(elemento,cont))
        