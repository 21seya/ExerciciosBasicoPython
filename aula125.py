def main():
    lista = []

    for i in range(3):
        num = int(input('Escolha um número:'))
        if num.isdigit():
            int(num)
        else:
            print('Digite apenas numeros')    

if __name__ == '__main__':
    main()

