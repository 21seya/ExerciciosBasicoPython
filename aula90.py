a = [1,2,3,4,5]

print(a)

indice = int(input("Digite o indice (de 0 até %i) do elemento a ser removido:"%(len(a)-1)))

print("Elemento:",a[indice])

a.remove(a[indice])

b = []

for i in range(len(a)):
    if i != indice:
        b.append(a[i])

a = b

print(a)
