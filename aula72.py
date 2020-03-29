n = int(input("Digite o valor de n:"))

soma = 0.0

for i in range(1,n+1):
    soma = i/(n- i + 1)

print("A soma vale",soma)
