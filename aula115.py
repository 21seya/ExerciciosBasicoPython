contato = {'Nome':'Wallace','Telefone':'991877123','Email':'wallacenevesk9@outlook.com',
'Endereco':'Rua Rosa Muller'}

def items(dic):
    lista= []
    for key in dic:
        lista.append((key,dic[key]))

    print(lista)

items(contato)

