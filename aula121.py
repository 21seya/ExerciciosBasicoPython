class Conta(object):
    __total =1000
    reserva = 0.1
    def __init__(self,ID,saldo):
        self.ID = ID
        self.saldo = saldo
    def deposito(self,valor):
        self.saldo += valor
        Conta.__total += self.saldo
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo += valor
            Conta.__total += valor
    def imprimeReserva():
        print(Conta__total*Conta.reserva)
                
