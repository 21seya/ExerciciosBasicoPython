print("Primeiro importamos")
from collections import OrderedDict
input()

print("Podemos criar um OrderedDict a partir da seguinte sintaxe:")
print("1 - Comprehension")
print("d = OrderedDict ((value,str(value))) for value in range(10) if value>5)")
d = OrderedDict((value,str(value)) for value in range(10) if value>5)
print(d)
input()

print("2 - A partir der um objeto interável ")
print("d = OrderedDict.fromkeys('abcde')")
d = OrderedDict.fromkeys('abcde')
print(d)
input()

print("Podemos modificar o valor das chaves:")
print("d['a']=5")
d['a'] = 5
print(d)
input()

print("Podemos obter todas as chaves")
print("d['1']= 18")
d['1'] = 18
print(d)
input()

print("Podemos mover a chave de posição")
print("d.move_to_end('b')")
d.move_to_end('b')
print(d)
print("d.move_to_end('b',last = False)")
d.move_to_end('b',last=False)
print(d)
input()


