import os,sys

input('ID do programa e o diretorio de trabalho')
print(os.getpid(),os.getcwd())
input()

input('Vá na pasta e veja que o arquivo vai ser renomeado')
os.rename('arquivo','renomeado')
input()

input('Vamos remover também o arquivo')
os.remove('renomeado')
input()

input('Gera um stirng aleatoria e criptografada')
print(os.urandom(s))
input()

input('Constantes especiais para diretorios')
x = os.pathsep,os.sep,os.pardir,os.curdir,os.linesep
print(x)
input()

input('Dicionario com as configurações do sistemas')
print(list(os.environ.keys()))
input()

input('Valor de uma chave do dicionario')
if 'win' in sys.platform:
    print(os.environ['PYTHONPATH'])
    print(os.environ['TEMP'])

else:
    print(os.environ['LANGUAGE'])

print(os.environ['USER'])
input()


input('Modificação dos valores da chave')
os.environ['USER'] = 'wallace'
print(os.environ['USER'])
input()



