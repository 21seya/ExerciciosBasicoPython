num = int(input("Digite o numero de temperatura regiratradas:"))

soma = maior = menor = float(input("Digite a temperatura 1:"))

for i in range(2, num+1):
    temp = float(input("Digite a temperatura %d :"%i))

    if temp > maior:
        maior = temp

    if temp < menor:
        menor = temp
    
    soma += temp

print(" A maior temperatura e %6.2f  ºC "%maior)
print(" A menor temperatura e %6.2f ºC "%menor)
print("A media das temperaturas  é %6.2f"%(soma/num))

