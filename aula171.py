import subprocess, sys

print("Vamos ler os arquivos do direotrio")
if 'win' in sys.platform:
    subprocess.call(['dir'],shell=True)
else:
    subprocess.call(['ls','-l'])
input() 

print('O argumento shell tem de ser true no windows para')
print("Executar programas construidos internamente,como type,")
print("dir,entre outros.Um programa normal como python não")
print("possui necessidade deste argumento")
input()


