from controladores import sistema, sugestao, calculadora
import os
from time import sleep

cont = True
vezes = 1

while cont:  # Equanto a variável cont for verdadeira ele rodará o programa.
    sistema.divisorias()
    print("Calculadora de IMC - Índice de massa corporal")
    sistema.divisorias()

    # Agora teremos unputs do teclado para atribuír as variáveis necessárias

    nome = input("Digite seu nome: ")
    while not nome.isalpha():
        sleep(2)
        print("\tAlgo está errado no seu nome, utilize apenas letras para isto.")
        nome = input("Digite seu primeiro nome: ")

    idade = sistema.verifica_idade()

    peso = sistema.verifica_peso()

    alt = sistema.verifica_altura()

    # Aqui chamaremos a função para calcular o IMc
    imc = calculadora.calcular(peso, alt)

    sleep(0.6)

    sistema.divisorias()

    # Aqui teremos uionformações básicas

    sistema.preparacao(nome, imc, idade)

    sleep(3)

    # Aqui sugerimos

    sugestao.sugerir(imc, idade)

    sleep(2)

    # perguntaremos se gostariam de fazer uma nova consulta atribuindo valor booleano a variável cont

    opcao = input("Deseja fazer outra consulta(S/N)? ")

    if opcao == "N" or opcao == "n":
        cont = False
    else:
        os.system('clear')
        sistema.divisorias()
        vezes += 1
        print("Começaremos novamente!!!")
        sistema.divisorias()
        sleep(1)
        os.system('clear')  # Esse código limpa a tela

# Se a variável cont for falsa chamará a função de encerramento

sistema.encerramento(1, vezes)

# Aqui é para mostrar a barra de carregamento

sistema.barraload()

# para paraar tudo pressione enter
tecla = input("\nPressione ENTER para sair...")
