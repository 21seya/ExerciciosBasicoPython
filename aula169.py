import sys 

def interact():
    if "win" in sys.platform:
        print('Ola stream mundo! --> Termine pressionando ctrl+Z')
    else:
        print('Ola stream  mundo -->Termine pressionando ctrl+D')

    while True:
        try:
            reply = input('Entre um número')
        except EOFError:
            break
        else:
            num = int(reply)
            print("%d ao quadradro e %d" % (num,num**2))
    print('Tchau')

if __name__ == '__main__':
    interact()

    

