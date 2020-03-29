contas = []
depositos = []
saldo = 0

def main():
    opcao =bool(int(input("Deseja criar uma conta(1) deseja fechar o programa(0):")))
    while opcao:
        criaConta()
        VerSaldo()
        opcao =bool(int(input("Deseja criar uma conta(1) deseja fechar o programa(0):")))


def criaConta():
    global contas, depositos , saldo
    num_conta = int(input("Digite um número da conta:"))
    
    while num_conta in contas:
        print("Numero já existente. Digite Novamente.")
        num_conta = int(input("Digite um número de conta:"))

    contas.append(num_conta)

    deposito = float(input("Digite o valor do seu primeiro deposito:"))
    while deposito <= 0:
        print("Valor de deposito invalido.")
        deposito = float(input("Digite o valor do seu primeiro deposito:"))

    depositos.append(deposito)
    saldo += deposito    

def VerSaldo():
    global saldo
    opcao = bool(int(input("Deseja ver o saldo do banco (1- Sim/0 - Não):")))
    if opcao :
        print("O Saldo do banco R$",saldo)

main()



