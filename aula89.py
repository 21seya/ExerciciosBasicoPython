#importa o modulo random 
import random 

#Armazena a vida do player 
player_vida = 500

#Armazena o sp do player 
player_sp = 100

#Vida padrao de um inimigo 
inimigo_vida = 50

#determina o número de inimigos 
n = int(input("Digite o numero de inimigos:"))

#vetor que armazena todos os inimigos
inimigos = []

#Adicionado ao vetor um vetor com 2 componentes : o número do inimigo e sua vida
for i in range(n):
    inimigos.append([i+1,inimigo_vida])

#Enquanto essa variável for True estamos rodando o jogo

jogando = True 

while jogando : #Loop do jogo
    #Imprimimos na tela a vida

    print("Vida:",player_vida)

    #e o sp do player 
    print("SP:",player_sp)

    #pedimos para o player escolher o que fazer 

    atk = int(input("Deseja atacar (1) ou curar (2) :"))

    #se ele escolher atacar, devemos:

    if atk == 1:
        #escolher aleatoriamente um inimigo para ser atacado

        selecionado = random.choice(inimigos)
        #determinar o dano causado

        dano = random.randint(10,15)
        #imprimir essas informações para o usuário 
        print("Causou %i de dano ao inimigo  %i! "%(dano,selecionado[0]))
        #diminuir da vida do inimigo o dano

        selecionado[1] -= dano 

        #se a vida do inimigo for zerada,devemos:

        if selecionado[1] <= 0:
            #dizer que o inimigo morreu 

            print("Inimigo %i morreu! "%selecionado[0])
            #e remover esse inimigo da lista de inimigos

            inimigos.remove(selecionado)

    #caso contrario ele escolheu curar
    else:
        #só podemos curar se o sp do player for maior do que 10
        if player_sp >= 10:
            #escolhemos um valor aleatorio para a cura

            cura = random.randint(10,15)
            #imprimos quanto o player recebeu a cura 
            print("Você recebeu %i de vida "%cura)
            #adicionamos isso a vida do player 

            player_vida += cura
            #e diminuimos em 10 o sp do player 
        else:
            #imprimimos que o player não pode se curar 

            print("Sp insuficiente")
    
    #depois disso é a vez dos inimigos atacaram 
    for inimigo in inimigos:
        #escolhemos se o inimigo var acertar ou errar 
        # o inimigo tem 75% de chance de acertar 

        acertou = bool(random.choice([1,1,1,0]))
        #se ele acertar,devemos 
        if acertou:
            #escolher um dano causado ao player 
            dano = random.randint(1,3)
            #imprimir a msg do dano

            print("Inimigo %i causou  %i de dano! "%(inimigo[0],dano))
            #diminuir a vida do player
            player_vida  -= dano
        #caso contrário
        else:
            #devemos informar que o inimigo errou 
            print("Inimigo %i errou o ataque "%inimigo[0])

    #depois devemos aumentar o sp do player 
    if player_sp < 100:
        #aumentar em 3 toda rodada
        player_sp += 3

    #mas o player nunca pode ter mais que 100 de sp
    if player_sp > 100:
        player_sp = 100

    #se a vida do player for < 0 ele perdeu 
    if player_vida <= 0:
        print("Perdeu o jogo!")
        jogando = False
                 
