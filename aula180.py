import time

print("Para construir objetos indexáveis precisamos construir alguns")
print("Alguns métodos mágicos especificos dentro do nosso objeto")
print("São eles: __getitem__,__setitem__,__len__,__delitem__")
input()

print("__getitem__ -->Permite pegar o objeto contido no indice")
print("pedido. Exemplo:")

class MinhaLista(object):
    def __getitem__(self,index):
        return index **2

a = MinhaLista()

for i in range(5):
    print(a[i])

input()

print("O que acontece se eu tentar percorrer esse objeto com um for loop?")

t0 = time.time()
for i in a:
    print(i)
    tf = time.time()
    if tf - t0 > 5:
        break
input()

print("Veja que a lista não tem um limite por isso o for loop")
print("é infinito. Poderiamos corrigir isso fazendo:")

class MinhaLista(object):
    def __init__(self,tamanho):
        self.len = tamanho

    def __getitem__(self,index):
        if index < self.len:
            return index **2
        else:
            raise StopIteration

a = MinhaLista(5)

for i in a:
    print(i)

input()

print("ou")

class MinhaLista(object):
    def __init__(self,*args):
        self.data = []
        for arg in args:
            self.data.append(arg)

    def __getitem__(self,index):
        return self.data[index]**2

a = MinhaLista(0,1,2,3,4)

for i in a:
    print(i)

input()

print("É possível usar slices neles a partir desse método")
print("slice é um objeto em Python")
print("por exemplo slice(1,5,2) =",slice(1,5,2))
input()

print("Assim poderiamos obter o slice da seguinte forma:")

class MinhaLista:
    def __getitem__(self,index):
        if isinstance(index,int):
            print('indexing',index)
        else:
            print('slicing',index.start,index.stop,index.step)

a = MinhaLista()

a[1]
a[1:3]

input()


