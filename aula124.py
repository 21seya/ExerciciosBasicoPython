try:
    a = int(input('Escolha um número entre 1 e 20:'))
    if not 1 <= a <=20:
        raise ValueError
    else:
        print('Obrigado por escolher',a)
except:
    print('Entrada invalida')    