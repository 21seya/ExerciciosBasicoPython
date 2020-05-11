import os,sys

input('ID do programa e do diretorio de trabalho')
print(os.getpid(),os.getcwd())
input()

input('Vá na pasta e veja que o arquivo vai ser renomeado')
os.rename('arquivo','renomeado')
input()

input('Vamos também remover o arquivo')
os.remove('renomeado')
input()

input('Gera uma stirng aleatoria e criptografada')
print(os.urandom(5))
input()
