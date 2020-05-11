
def find(frase,sub):
    for i in range(len(frase)+ 1 - len(sub)):
        if frase [i:i+len(sub)] ==sub:
            return i
    return None        

def index(frase,sub):
    for i in range(len(frase)+1 - len(sub)):
        if frase[i:i+len(sub)] == sub:
            return True
    return 'ERRO'

print(find('mississipi','ss'))
print(index('mississipi','ss'))                          

