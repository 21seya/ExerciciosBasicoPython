turmas =int(input("Digite a quantidade de turmas:"))
soma = 0

for i in range(1,turmas+1):
    qtd = int(input("Digite o numero de alunos da turma %d:"%i))

    while qtd >40 and qtd <0:
        print("Numero de alunos invalido")
        qtd = int(input("Digite o numero de alunos da turma %d:"%i))

    soma += qtd

print(" A media dos alunos é %10.g alunos por turma. "%(soma/turmas))

