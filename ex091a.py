from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1' : randint(1, 6),
    'jogador2' : randint(1, 6),
    'jogador3' : randint(1, 6),
    'jogador4' : randint(1, 6)
}
ranking = list()
print('Valores Sorteados')
for k, v in jogo.items():
    sleep(1)
    print(f'{k} tirou {v}')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=*' * 30)
print(' == Ranking dos Jogadores == ')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'  {i+1}º lugar {v[0]} que tirou {v[1]}')
