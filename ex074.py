from random import randint
tupla_num = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('Os números sorteados foram: ', end='')
for i in tupla_num:
    print(f'{i} ', end='')
print(f'\nO maior valor é {max(tupla_num)} e o menor valor é {min(tupla_num)} ')
