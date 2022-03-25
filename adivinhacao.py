import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    total_de_tentativas = 0
    pontuacao = 1000
    rodada = 1
    numero_secreto = random.randrange(1, 101) #int(random.random() * 100) --pode gerar zeros entao melhor pelo range

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while (rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("\nVocê acertou!")
            break
        else:
            if (maior):
                print("\nVocê errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("\nVocê errou! O seu chute foi menor que o número secreto.")
            pontuacao_perdida = abs(numero_secreto - chute)
            pontuacao -= pontuacao_perdida
        rodada = rodada + 1

    print("Voce fez {} pontos. O numero secreto era {}.".format(pontuacao,numero_secreto))
    print("\nFim do jogo")

if (__name__ == "__main__"):
    jogar()