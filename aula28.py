fun = [abs(x) for x in [-2,-1,0,1,2]]

tup = [(y,y**2) for y in range(1,11)]

lista1 = []
for a in range(4):
    for b in range(4):
        if a != b:
            lista1.append([a,b])

lista2 = [[a,b] for a in range(4)  for b in range(4) if a !=b]           