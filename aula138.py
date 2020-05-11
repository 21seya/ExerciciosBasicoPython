import pickle
arq = open('arquivo.pck','wb')
l1 = [1,2,3]
pickle.dump(l1,arq)
pickle.dumps(l1)
