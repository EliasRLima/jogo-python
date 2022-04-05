import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        print("jogando.. voce ainda pode errar: {} vezes.".format(6-erros))

        chute = input("Qual a letra?")
        chute = chute.strip()
        chute = chute.upper()
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        
        enforcou = (erros == 6)
        acertou = ("_" not in letras_acertadas)
        print(letras_acertadas)
    if(acertou):
        print("Voce ganhou!")
    else:
        print("Voce perdeu! A palavra era {}.".format(palavra_secreta))

if(__name__ == "__main__"):
    jogar()