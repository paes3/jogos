import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("******Escolha o seu jogo!********")
    print("*********************************")

    print("(1) Forca  (2) Adivinhação")

    jogo = int(input("Qual o Jogo?"))

    if(jogo == 1) :
        print("Jogando jogo da forca")
        forca.jogar()
    elif(jogo == 2) :
        print("Jogando jogo de adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
