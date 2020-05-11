contato = {'Nome':'Wallace','Telefone':'991877123','Email':'wallacenevesk9@outlook.com',
'Endereco':'Rua Rosa Muller'}


def get(dic,key, valor=None):
    if key in dic:
        return dic[key]
    else:
        return valor

print(get(contato,'Nome'))
print(get(contato,'Telefone'))

