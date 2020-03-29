import random 

testes = int(input("Digite o numero de testes:"))

trocar = 0


for i in range(testes):
    porta = random.randrange(1,4)
    premio = random.randint(1,3)

    if porta != premio:
        trocar += 1

print("é vantajoso trocar em %.3g %% das vezes "%(trocar*100/testes))
print(" Não é vantajoso trocar em %.3g %% das vezes "%((1 - trocar/testes)*100))

