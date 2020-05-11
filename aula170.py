import sys
from io import StringIO
from io import BytesIO

print('Cria um buffer de strings')
buff = StringIO()
input()

print("Escreve 'span\\n' no buffer")
buff.write('span\n')
input()

print("Escreve 'ovos\\n' no buffer")
buff.write('ovos\\n')
input()

print("Pega o valor contido no buffer")
print(buff.getvalue())
input()

print("Cria um buffer já com um valor contido dentro dele")
buff = StringIO('presunto\\n')
input()

print("Le uma linha do buffer")
print(buff.readline())
input()

print("Lemos todas as linhas do buffer,se tentarmos ler novamente veremos")
print("'"+buff.readline()+"'")
input()

print("Recriamos o buffer vazio")
buff = sys.stdout
input()

print("Mandamos o sys.stdout=buff")
sys.stdout = buff
input()

print("Agora toda saida do print irá para o buff",file=temp)
print(42,'spam',3.141)
input()

print("Retornamos o sys.stdout ao padrao",file=temp)
sys.stdout = temp
input()

print("Pegamos o valor no buffer")
print(buff.getvalue())
input()

print("Podemos usar bytesIO de forma semelhante só que guardamos bytes ao invés de objetos strings")

