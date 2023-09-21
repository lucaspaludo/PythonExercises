from random import randint
from time import sleep

jogador1 = randint(1, 6)
jogador2 = randint(1, 6)
jogador3 = randint(1, 6)
jogador4 = randint(1, 6)

sleep(0.5)
print('Valores sorteados: ')
sleep(1)
print(f'{"":<4}Jogador um tirou {jogador1}')
sleep(1)
print(f'{"":<4}Jogador dois tirou {jogador2}')
sleep(1)
print(f'{"":<4}Jogador três tirou {jogador3}')
sleep(1)
print(f'{"":<4}Jogador quatro tirou {jogador4}')

jogo = {
    'jogador1' : jogador1,
    'jogador2' : jogador2,
    'jogador3' : jogador3,
    'jogador4' : jogador4,
}

for i in sorted(jogo, key=jogo.get, reverse=True):
    print(f'O {i} que tirou {jogo[i]}')
    sleep(0.5)



