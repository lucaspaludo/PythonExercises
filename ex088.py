from time import sleep
from random import randint

listaJogos = []
jogoAtual = []
cont = 0
print('=*' * 10, 'APOSTAS LOTERIA', '=*' * 10)
numJogos = int(input('Quantos jogos deseja jogar? '))

for i in range(0, numJogos):
    for j in range(0, 6):
        num = randint(1, 60)
        jogoAtual.append(num)

    listaJogos.append(jogoAtual[:])
    jogoAtual.clear()

for i in range(1, numJogos+1):
    print(f'Jogo {i}: {listaJogos[i-1]}')
    sleep(1)


