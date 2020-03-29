idades = []
alturas = []

for i in range(1,6):
    idade = int(input("Digite a idade da pessoa %i de 5:"%i))
    altura = float(input("Digite a altura (m) da pessoa %i de 5: "%i))

    idades.append(idade)
    alturas.append(altura)

    idades_invertida = idades[::-1]
    alturas_invertida = alturas[::-1]

    for i in range(5):
        print("Idade %i: %i "%(5-i,idades_invertida[i]))
        print("Altura %i: %.2f" %(5-i,alturas_invertida))

        
