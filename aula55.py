num = int(input("Digite um numero:"))

i,j,k = 1,2,3


while  i * j * k <num:
     i += 1
     j += 1
     k += 1

while i * j* k == num:
    print(num,"É triangular")
else:
    print(num," Não é triangular")
