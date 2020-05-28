from socket import *

def main():
    host = ""
    port = 5000

    #Cria Socket
    server = socket(AF_INET,SOCK_DGRAM)

    #Indica que o servidor foi iniciado
    print("Servidor Iniciado")

    #Bloco infinito do servidor 
    while True:
        #Recebe a data e o endereço da conexao
        data,endereco = server.recvfrom(1024)

        #Imprime as informações da conexão

        print("Mensagem recebida de",str(endereco))
        print("Recebemos do cliente:",str(data))

        #Vamos mandar de volta a mensagem em eco 
        resposta = "Eco=>" + str(data)
        server.sendto(data,endereco)

    #Fechamos o servidor
    server.close()

if __name__ == '__main__':
    main()
    