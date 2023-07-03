from random import choice
cont = 0
while True:
    escolha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    computador = choice(escolha)
    num = int(input('Digite um valor: '))
    jogada = ' '
    while jogada not in 'PI':
        jogada = input('Par ou ímpar: [P/I] ').strip().upper()[0]
        soma = computador + num
    if jogada == 'P' and soma % 2 == 0:
        print('PARABÉNS! VOCÊ VENCEU')
        cont += 1
    if jogada == 'P' and soma % 2 != 0:
        print('\nVOCÊ PERDEU')
        break
    if jogada == 'I' and soma % 2 == 0:
        print('\nVOCÊ PERDEU')
        break
    if jogada == 'I' and soma % 2 != 0:
        print('PARABÉNS! VOCÊ VENCEU')
        cont += 1
print(f'VOCÊ CONSEGUIU ME VENCER {cont} vezes')
