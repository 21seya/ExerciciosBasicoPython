from socket import *

#Cria o nome do host
meuHost = ''

#Utiliza este número de port

minhaPort = 50007

sockobj = socket(AF_INET,SOCK_STREAM)

sockobj.bind((meuHost,minhaPort))

sockobj.listen(5)

while True:

    conexao,endereco = sockobj.accept()
    print('Server Conectado por',endereco)

    while True:

        data = conexao.recv(1024)

        if not data : break

        conexao.send(b'Eco=>'+data)
        

