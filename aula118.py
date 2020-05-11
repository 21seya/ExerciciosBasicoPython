class Pessoa():
    def __init__(self,nome,emprego,idade):
        self.nome = nome
        self.emprego = emprego
        self.idade = idade
    def ola(self):
        print('Ola meu nome e %s tenho %i anos e sou %s'%(self.nome,self.idade,self.emprego))
            