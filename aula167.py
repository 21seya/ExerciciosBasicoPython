import sys 

print(sys.argv)

def mais(text,numlinhas=15):
    linhas = text.splitlines()

    while linhas:
        chunk = linhas[:numlinhas]
        linhas = linhas[numlinhas:]
        for linha in chunk: print(linha)
        if linhas and input('Mais?') not in ['s','S']: break

if __name__ == '__main__':
    if len(sys.argv) >1:
        mais(open(sys.argv[1].read(),5))
                 