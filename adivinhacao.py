import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # CONSTANTES
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 250

    # SELEÇÃO DE DIFICULDADE
    print("Qual vai ser o nivel de dificuldade?")
    print("(1)Fácil  (2)Médio  (3)Difícil (666)HARDCORE" )

    nivel = int(input("Defina um nível: "))
        
    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 5
    elif (nivel == 3):
        total_de_tentativas = 3
    else :
        total_de_tentativas = 1

    # JOGO
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print(f"Você acertou e fez {pontos} pontos")
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    # PÓS JOGO
    print(f"O numero era {numero_secreto}")
    print("Fim do jogo")

if(__name__== "__main__"):
    jogar()