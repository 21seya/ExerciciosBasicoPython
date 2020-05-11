lista = [326,300,100,320,310,301,311,111,25,20,10,21,11,1,7,16]

for num in lista:
    centenas = num//100
    dezenas = (num%100)//10
    unidades = num%10

    saida = str(num) + '='

    if centenas > 0:
        saida += str(centenas)
        if centenas > 1:
            saida += 'centenas'
        else:
            saida += 'centena'

        if dezenas > 0:
            saida += ','
        else:
            if unidades > 0:
                saida += 'e' 

    if dezenas > 0:
        saida += str(dezenas)
        if dezenas > 1:
            saida += 'dezenas'
        else:
            saida += 'dezena'
                
