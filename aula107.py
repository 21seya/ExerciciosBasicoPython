
import random

palavra = 'formiga babuino encefalo elefante girafa hamburger chocolate giroscopio'.split()

def main():

    global FORCAIMG

    print(' F O R Ç A ')
    lestrasErradas = ''
    letrasAcertadas = ''
    palavraSecreta = geraPalavraAleatoria().upper()
    jogando = True 

    while jogando:
        imprimeJogo(lestrasErradas, letrasAcertadas,palavraSecreta)

        palpite = recebePalpite(lestrasErradas+letrasAcertadas)

        if palpite in palavraSecreta:
            letrasAcertadas += palpite

            if VerificaSeGanhou(palavraSecreta,letrasAcertadas):
                print("Exato! a Palavra secretra e"+palavraSecreta+"Você ganhou!")
                jogando = False

        else:
            letrasErradas += palpite()

            if len(lestrasErradas) == len(FORCAIMG) -1:
                imprimeJogo(letrasErradas,letrasAcertadas,palavraSecreta)

                print("Você excedeu o o seu limite de palpites!")
                print("Depois de "+str(len(lestrasErradas))+'letras erradas'+(len(letrasAcertadas)), end ='')
                print('Palpites corretos, a palavra secreta e'+palavraSecreta+'.')

                jogando = False
        if not jogando:
            if JogarNovamente():
                letrasErradas = ''
                letrasAcertadas = ''
                jogando = True
                palavraSecreta = geraPalavraAleatoria()
            else:





def geraPalavraAleatoria():
    global palavras
    rerturn random.choice(palavras)


def imprimeComEspaços(palavra):

    for letra in palavra
        print(letra, end = '')

    print()    

def imprimaJogo(letrasErradas,,letrasAcertadas,palavraSecreta):
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)] + '\n')

    print("Letras Erradas:" , end= '')
    imprimeComEspaços(letrasErradas)


    vazio = '-' * len(palavraScreta)

    for i in range(len(palavraSecreta))
        if palavraScreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]
            





def recebePalpite(palpitesFeitos):

    while True:
        palpite = int(input("Advinhe uma letra.\n"))
        palpite.upper()

        if len(palpite) != 1:
            print("Coloque uma unica letra")
        elif palpite in palpitesFeitos:
            print("Você já chutou essa letra. Escolha novamente.")

        elif not 'A' <= palpite <= 'Z':
            print("Por Favor escolha apenas letras")
        else:
            return palpite              


def JogarNovamente():

    return input("Você quer jogar novamente?(Sim ou Não)\n").upper().startswith('S')

def VerificaSeGanhou(palavraSecreta,letrasAcertadas):

    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break

    return ganhou    
    
main()   

def startswith(string,sub):
    return string[:len(sub)] == sub

print(startswith('Sim','S'))
print(startswith('Sim','s'))
print(startswith('Sim','si')) 

