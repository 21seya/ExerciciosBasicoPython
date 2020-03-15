import math 

dado_bruto = [56.7,float('NaN'),51.7,55.3,52.5,float('NaN'),47.8]
dado_filtrado = []

for valor in dado_bruto:
    if not math.isnan(valor):
        dado_filtrado.append(valor)

print(dado_filtrado)        