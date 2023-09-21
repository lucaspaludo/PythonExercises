from random import randint
from time import sleep


def sorteia(arg):
    print(f'Sorteando números: ', end='')
    sleep(0.5)
    arg.append(randint(1, 10))
    print(arg[0], end=', ')
    sleep(0.3)
    arg.append(randint(1, 10))
    print(arg[1], end=', ')
    sleep(0.3)
    arg.append(randint(1, 10))
    print(arg[2], end=', ')
    sleep(0.3)
    arg.append(randint(1, 10))
    print(arg[3], end=', ')
    sleep(0.3)
    arg.append(randint(1, 10))
    print(arg[4], end=', ')
    sleep(0.3)


def somaPar(x, y):
    for i in range(len(x)):
        if x[i] % 2 == 0:
            y.append(x[i])
    print(f'A soma dos valores pares é {sum(y)}')


numeros = list()
numPar = list()
sorteia(numeros)
print()
somaPar(numeros, numPar)
