n = int(input("Digite o tamanho da sequencia:"))
ant = int(input("Digite o primeiro numero:"))
cont = seg = segMAX =  1
while cont < n :
    prox = int(input("Digite o numero %i:" %(cont+1)))
    if prox > ant:
        seg += 1
    else:
        if seg > segMAX:
            segMAX = seg    
    cont +=1
    ant = prox    

print("O maior segmento crescente da sequencia e:",segMAX)