def qua(x): 
    return x**2

mapa = map(qua,[1,2,3,4,5])
listmap = list(map(qua,[1,2,3,4,5]))
ran = tuple(map(qua,range(10)))
lamb = list(map(lambda x: x**3,range(10))) 

print('map(...)=',mapa)
print()
print('list(map(...range())=',ran)
print()
print('map(funcao lambda,...)=',lamb)
