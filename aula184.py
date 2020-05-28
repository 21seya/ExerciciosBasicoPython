class Pessoa:
    def __init__(self,prim_nome,ult_nome):
        self.prim_nome = prim_nome
        self.ult_nome = ult_nome

    @property
    def nome(self):
        return '%s,%s' % (self.ult_nome,self.prim_nome)

    @nome.setter
    def nome(self,valor):
        self.prim_nome = valor

    @nome.deleter
    def nome(self):
        del self.prim_nome
        del self.ult_nome

p = Pessoa('luiz','Mario')
print(p.nome)
p.nome = 'Martin','Souza'
print(p.nome)
del p.nome

input()
