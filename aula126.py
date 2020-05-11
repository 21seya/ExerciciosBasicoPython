def main():
    lista = []

    for i in range(3):
        while True:
            try:
                num = int(input('Escolha um número:'))
                break
            except:    
                print('Digite apenas numeros') 
        if num not in lista:
            lista.append(num)
                      
if __name__ == '__main__':
    main()
