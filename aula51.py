n = int(input("Digite n:"))

prod = n
cont = n-1
while cont > 1:
    prod = prod*cont
    cont = cont - 1

print(n,"! =" ,prod)
