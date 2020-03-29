comeco = int(input("Começo = "))
fim = int(input("Fim = "))

for i in range(comeco,fim+1):
    print("Para o",i)
    for j in range(comeco,fim+1):
        print("%dX%d =%d"%(i,j,i*j))

print("") 
       