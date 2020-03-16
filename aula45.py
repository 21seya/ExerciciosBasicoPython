area = int(input("Digite a área ser pintada:"))

litros = area/3
if area % 3 >0:
    litros = litros + 1
print(litros)
