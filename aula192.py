import csv 

print("O modulo csv permite lidar com tabelas")
print("desse tipo de uma maneira bastante")
print("simples")

input()

f = open('tabelas.csv','w')
try:
    writer = csv.writer(f)
    writer.writerow(('Nome','Idade','Sexo'))
    writer.writerow(('Luan',23,'M'))
    writer.writerow(('Luana',17,'F'))
    writer.writerow(('Joao',27,'M'))
finally:
    f.close()

print(open('tabelas.csv','rt').read())

input()

f = open('tabelas.csv','r')
try:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)
finally:
    f.close()        

input()

##f = open('tabela.csv','a')
##try:

