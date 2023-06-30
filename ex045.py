from random import choice
from time import sleep

print('\033[33m--------------------------JOKENPÔ--------------------------\033[m')
escolha = input('Qual é a sua jogada? ').strip().upper()


jokenpo = ["PEDRA", "PAPEL", "TESOURA"]
jogo = choice(jokenpo)

if escolha != 'PEDRA' and escolha != 'PAPEL' and escolha != 'TESOURA':
    print('Jogada inválida')
else:
    print("\033[33mJO\033[m")
    sleep(1)
    print("\033[31mKEN\033[m")
    sleep(1)
    print("\033[34mPO!!!\033[m")

    print("\033[33m-------------\033[m")
    print(jogo)
    print("\033[33m-------------\033[m")

    if (escolha == 'PEDRA') and (jogo == 'PAPEL'):
        print("\033[31mParabéns! Você Perdeu\033[m")
    elif (escolha == 'PEDRA') and (jogo == 'TESOURA'):
        print("\033[32mParabéns! Você ganhou\033[m")
    elif (escolha == 'PEDRA') and (jogo == 'PEDRA'):
        print("Empatou")

    elif (escolha == 'TESOURA') and (jogo == 'PAPEL'):
        print("\033[32mParabéns! Você ganhou\033[m")
    elif (escolha == 'TESOURA') and (jogo == 'TESOURA'):
        print("Empatou")
    elif (escolha == 'TESOURA') and (jogo == 'PEDRA'):
        print("\033[31mParabéns! Você perdeu\033[m")

    elif (escolha == 'PAPEL') and (jogo == 'PAPEL'):
        print("Empatou")
    elif (escolha == 'PAPEL') and (jogo == 'TESOURA'):
        print("\033[31mParabéns! Você perdeu\033[m")
    elif (escolha == 'PAPEL') and (jogo == 'PEDRA'):
        print("\033[32mParabéns! Você ganhou\033[m")






