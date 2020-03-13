def perg_ok(perg,tentativas=3,lembrete='Por favor , responda sim ou não!'):
    while True:
        ok = input(perg)
        if ok in('S','S','Sim','SIM'):
            return True
        if ok in('n','N','Nao','NAO'):
            return False
        tentativas = tentativas - 1 
        if tentativas <0:
            raise ValueError('Resposta do usuário é invalida')
        print(lembrete)
if perg_ok('Quer continuar?') != True:
    print('Codigo não continuado')
else:
    print('Codigo continuado')             