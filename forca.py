def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        print("jogando..")

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
        print("Voce perdeu!")

if(__name__ == "__main__"):
    jogar()