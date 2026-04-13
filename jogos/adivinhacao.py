import random

def jogar():
    tentativas = 1
    errou = True
    sorteio_max = 10
    tentativas_max = 3
    numero = random.randint(0,sorteio_max)

    while (tentativas <= tentativas_max):
        print("Tentativa:", tentativas)
        chute = int(input("Digite o seu chute (0 a 10):"))
        if chute == numero:
            print("Parabéns, você acertouu!!!!! (˶˃ ᵕ ˂˶)")
            errou = False
            break
        else:
            print("Errou (╥﹏╥)")
        tentativas = tentativas + 1
        
    if errou == True:
        print("O número sorteado era:", numero)
    print("### FIM DO JOGO ###")

if __name__ == "__main__":
    jogar()