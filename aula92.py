a = [1,2,3,4,5]
aux = a[:]
b = []
print("lista =",a)

while len(b) != len(a):
    menor = aux[0]
    for ele in aux:
        if ele < menor:
            menor = ele

    b.append(ele)
    aux.remove(ele)

a = b
print("lista =",a)
