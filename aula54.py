n = int(input("Digite o numero de empresas:"))
m = int(input("Digite o numero de meses:"))

empresa = 1
print("")
while empresa <= n:
    mes = 1
    balança = 0
    print("Empresa",empresa,":")
    while mes <= m:
        print("Mês",mes,":")
        ganho = int(input("Digite o ganho da empresa no mes:")) 
        gasto = int(input("Digite o gasto da empresa no mes:")) 
        balança = balança + (ganho - gasto)
        print("")
        mes = mes + 1

    if balança == 0 :
        print("A empresa",empresa,"Ficou indiferente(balança = R$ 0)")
    elif balança > 0:
        print("A empresa",empresa,"Fechou o lucro com R$",balança)
    else:
         print("A empresa",empresa,"Fechou o lucro com defict R$",balança)
    
    empresa = empresa + 1