#versão com dot art୭ ᵎᵎ 🧁
#para a versão forca + adivinhação!!!
#update: arrumado o erro do jogo não terminar ao perder

import random

def jogar():
    temas = {
        "1": "doces.txt",
        "2": "MLP.txt",
        "3": "MH.txt"
    }

    print("Oi vamos jogar forca!!! ദ്ദി(˵ •̀ ᴗ - ˵ )✧")

    while True:
        print("1 - Doces e confeitaria!!")
        print("2 - My little Pony!!")
        print("3 - Monster High!!!")
        opcao = input("Digite a opção desejada (1 a 3): ")

        if opcao in temas:
            arquivo_nome = temas[opcao]
            break
        else:
            print("Opção inválida, tente novamente!")

    try:
        arquivo = open(arquivo_nome, "r")
        palavras = [linha.strip().upper() for linha in arquivo]
        arquivo.close()
    except FileNotFoundError:
        print("Arquivo não encontrado! Usando palavras padrão.")
        palavras = ["CHOCOLATE", "CUPcake", "PINKIEPIE", "FRANKIE"]

    palavra = random.choice(palavras)

    letras_acertadas = ["_" if letra != " " else " " for letra in palavra]

    acertou = False
    enforcou = False
    tentativa = 0
    limite_tentativa = len(palavra) + 6

    def mostrarPalavra():
        print(" ".join(letras_acertadas))
        print("")

    while(not acertou and not enforcou):
        mostrarPalavra()

        chute = input("Digite uma letra! (˶ˆᗜˆ˵)/").upper().strip()
        
        tentativa = tentativa + 1

        indice = 0
        acertou_nessa_rodada = False
        for letra in palavra:
            if (chute == letra):
                letras_acertadas[indice] = letra
                acertou_nessa_rodada = True
            indice = indice + 1

        # Feedback se acertou ou não na rodada
        if acertou_nessa_rodada:
            print("Letra encontrada!")
        else:
            print("Letra não encontrada.")

        if tentativa >= limite_tentativa:
            print("Você perdeu \nA palavra era: ", palavra)
            print("⡴⠒⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠉⠳⡆⠀\n⣇⠰⠉⢙⡄⠀⠀⣴⠖⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠁⠙⡆\n⠘⡇⢠⠞⠉⠙⣾⠃⢀⡼⠀⠀⠀⠀⠀⠀⠀⢀⣼⡀⠄⢷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠰⠒⠲⡄⠀⣏⣆⣀⡍\n ⢠⡏⠀⡤⠒⠃⠀⡜⠀⠀⠀⠀⠀⢀⣴⠾⠛⡁⠀⠀⢀⣈⡉⠙⠳⣤⡀⠀⠀⠀⠘⣆⠀⣇⡼⢋⠀⠀⢱\n⠀⠘⣇⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⡴⢋⡣⠊⡩⠋⠀⠀⠀⠣⡉⠲⣄⠀⠙⢆⠀⠀⠀⣸⠀⢉⠀⢀⠿⠀⢸\n⠀⠀⠸⡄⠀⠈⢳⣄⡇⠀⠀⢀⡞⠀⠈⠀⢀⣴⣾⣿⣿⣿⣿⣦⡀⠀⠀⠀⠈⢧⠀⠀⢳⣰⠁⠀⠀⠀⣠⠃\n⠀⠀⠀⠘⢄⣀⣸⠃⠀⠀⠀⡸⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠈⣇⠀⠀⠙⢄⣀⠤⠚⠁⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢰⣿⣿⣿⡿⠛⠁⠀⠉⠛⢿⣿⣿⣿⣧⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⣸⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠹⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣤⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⣀⣠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢤⣀⣀⠀⢀⣀⣀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            enforcou = True
            break

        if "_" not in letras_acertadas:
            print("Parabéns!!! você descobriu a palavra!!")
            mostrarPalavra()
            acertou = True
            break
