def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        print("jogando..")

        chute = input("Qual a letra?")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra):
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()