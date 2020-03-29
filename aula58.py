n = int(input("Digite um numero menor do que 10:"))

aux = n
reverso  = 0

while aux !=0:
    reverso = reverso*10 + aux % 10
    aux // = 10

if reverso == n:
    print(n,"é palidromo")

else:
    print(n," não é palidromo")

