print("Metaclasses")
input()

print("TUDO EM PYTHON  É OBJETO")
print("essa frase se extende até mesmo para classes")
print("classes são objetos de uma classe")

input()

print("type usando 3 argumentos ")
print("Podemos usar a função type com 3 argumentos para")
print("construir novas classes. Por exemplo")

def criaClasse(**argumentos):
    return type("MinhaClasse",(object,),argumentos)

a = criaClasse(idade=13,olhos=2)
print(a)
print(a.idade,a.olhos)

print("Veja que criamos a classe MinhaClasse equivalente a")
class MinhaClasse(object):
    idade = 13
    olhos = 2

print("Porém de forma dinâmica")

input()

print("Se uma classe é um objeto de outra classe,que classe é essa?")
print("Vamos usar o atributo __class__ para determinar isso")
class UmaClasse: pass
a = UmaClasse()
print(a.__class__)
print(UmaClasse.__class__)

input()

print("Então como funciona a definição de uma classe em Python?")
print("1 - Python ve a definição da classe")
print("2 - Python armazena a definição de métodos e atributos em um dicionário")
print("3 - Python chama Meta(nome_da_classe,pais_da_classe,dicionário) para determinar a Metaclasse da classe")
print("4- Ao determinar a metaclasse ela é chamada para construir a classe")

input()

print("Como determinar a metaclasse de uma classe?")
print("Procura-se ver se o atributo __metaclasse__ está definido")
print("Se estiver essa será a metaclasse,senão será type.")

input()

print("Como definir minha própria metaclasse?")
print("Utilizar métodos __new__ e __init__")
class MinhaClasse(type):
    def __new__(meta,name,bases,dct):
        print('...........................')
        print("Alocando memória para a classe",name)
        print(meta)
        print(bases)
        print(dct)
        return super(MinhaClasse,meta).__new__(meta,name,bases,dct)
    def __init__(cls,name,bases,dct):
        print('.....................')
        print("Inicializando a classe",name)
        print(cls)
        print(bases)
        print(dct)
        super(MinhaClasse,cls).__init__(name,bases,dct)

class MinhaClasse(object,metaclass=MinhaMeta):

    def teste(self,param):
        pass

    atributo = 2

a = MinhaClasse()

input()

print("É util construir um método __call__ no lugar do par __init__ e __new__")
print("para definir uma metaclasse")

class MinhaClasse(type):
    def __call__(cls,*args,**kwds):
        print('__call__ de ',str(cls))
        print('__call__ *args=',str(args))
        return tyepe.__call__(cls,*args,**kwds)

class MinhaClasse(object,metaclass =MinhaMeta):

    def __init__(self,a,b):
        print('MinhaClasse objeto com a=%s, b=%s'%(a,b))

print('Vou criar agora...')
a = MinhaClasse(1,2)

input()





