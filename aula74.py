num = float (input("Digite um numero:"))

if num != int(num):
    decimal = num - int(num)
    arredondado = int(num)

    if decimal >= 0.5 :
        arredondado += 1

    print(num,"é decimal")
    print("Arrendondado:",arredondado)
else:
    print(num,"é inteiro")
