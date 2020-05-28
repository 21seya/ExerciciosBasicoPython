class Calculadora:
    def calcula(self,expressao):
        self.valor = eval(expressao)

class Falador:
    def fala(self):
        print('Ei,meu valor é',self.valor)

class CalculadoraFalante(Calculadora,Falador):
    pass

cf = CalculadoraFalante()
cf.calcula('1+2*3')
cf.fala()

input()

print("E se eu quiser usar um método de superclasse?")
print("Será que eu posso usar super?")

class Primeira(object):
    def __init__(self):
        self.p1 = 1
        print("primeira")

class Segunda(object):
    def __init__(self):
        self.p2 = 2
        print("Segunda")

class Terceira(Primeira,Segunda):
    def __init__(self):
        super(Terceira,self).__init__()
        try:
            print("Acabou!",self.p1,self.p2)
        except Exception as E:
            print(E)

t = Terceira()

input()

print('Corrigindo.....')

class Primeira(object):
    def __init__(self):
        self.p1 = 1
        print("primeira")

class Segunda(object):
    def __init__(self):
        self.p2 = 2
        print("segunda")

class Terceira(object):
    def __init__(self):
        Primeira.__init__(self)
        Segunda.__init__(self)
        print('Acabou!',self.p1,self.p2)
        

