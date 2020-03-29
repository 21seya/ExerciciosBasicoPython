n = int(input("Digite o tamanho da seuqencia:"))
ant= int(input("Digite o numero 1:"))
cont = seg = 1

while cont <n:
    prox = int(input("Digite o numero %i " %(cont+1)))
    if prox != ant :
        seg += 1
        ant = prox
        cont += 1

print("A sequencia tem %i segmentos " %seg)
        