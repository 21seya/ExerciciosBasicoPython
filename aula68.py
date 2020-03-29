n = int(input("Digite o numero de sequencias: "))
print("")
for i in range(n):
    print("sequencia %i:" % (i+1))
    num = int(input("Digite um numero da seuqencia:"))
    soma = 0
    while num != 0:
        if num % 2 == 0:
            soma += num
        num = int(input("Digite um numero da seuqencia:"))
    
    print("A soma da seuqencia %i e %i " %(i,soma))
print("")
