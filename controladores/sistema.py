import os
from time import sleep

clones = 70


def divisorias():  # imprime as divisórias
    print("=" * clones)


def verifica_idade():  # verifica os dados da idade
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            return idade
        except ValueError:
            sleep(2)
            print("Há algo errado com tua idade!!")
            continue
        else:
            break


def verifica_peso():  # verifica os caracteres do peso
    while True:
        try:
            global peso
            peso = float(input("Digite seu peso: "))
            return peso
        except ValueError:
            sleep(2)
            print("Há algo errado com teu peso, utilize apenas os numéros.\n"
                  "Ex.: Digite seu peso: 77")
            continue
        else:
            break


def verifica_altura():  # verifica a formatação dos dados da altura
    while True:
        try:
            alt = float(input("Digite sua altura em metros: "))
            return alt
        except ValueError:
            sleep(2)
            print("Há algo errado com tua altura, utilize apenas os números.\n"
                  "(Ex.: Digite sua altura em metros: 1.83)")
            continue
        else:
            break


def preparacao(nome, imc, idade):  # imprime uma pre-informação do usuário
    nome = nome.title()  # aqui é para forçar a primeira letra maiúscula se o usuário não o fez.
    print(f"{nome}, o seu IMC é {imc:0.2f}. De acordo com sua\n"
          f"idade, {idade} anos, o que sugerimos é ...")
    divisorias()


def encerramento(n, vezes):  # função recursiva, tem como objetivo imprimir uma pequena contagem
    # usando o contador da variável global vezes.
    if n > 3:
        print("")
    else:
        if n == 1:
            print(f"\n...Apagando os", vezes, " registros...")
        elif n == 2:
            print("\n\t...Só mais um instante...")
        else:
            print("\n\t\t...Encerrando procedimentos...")
        sleep(1)
        return encerramento(n + 1, vezes)


def barraload(perc=10):  # Função para encerrar o programa utilizando o ciclo FOR
    for a in range(1, 20):
        os.system('clear')
        print("\n")
        if perc == 100:
            print("\tEncerrado!")
            print("\n\tAgradecemos a sua utilização!\n"
                  "\tMelhores cumprimentos e bons hábitos sempre!!\n")
        else:
            print("Fechando o programa...")
            print("#" * (a + 12), perc, end="%")
            a += 1
            perc += 5
            sleep(0.3)
