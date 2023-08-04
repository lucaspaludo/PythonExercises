from random import randint
from time import sleep

listaAtual = list()
listaJogos = list()
print('-=' * 30)
print('     APOSTAS DA LOTERIA      ')
print('-=' * 30)
quant = int(input('Quantos jogos você quer jogar? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in listaAtual:
            listaAtual.append(num)
            cont += 1
        if cont >= 6:
            break
    listaAtual.sort()
    listaJogos.append(listaAtual[:])
    listaAtual.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(listaJogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
