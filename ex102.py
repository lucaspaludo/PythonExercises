def fatorial(num, conta=True):
    """
    :param num: número a ser calculado o fatorial
    :param conta: mostral cálculo na tela (opcional)
    :return: fatorial calculado
    """
    f = 1
    if not conta:
        for c in range(num, 0, -1):
            f *= c
        return f'\nO fatorial de {num} é {f}'
    else:
        for c in range(num, 0, -1):
            print(f'{c} X', end=' ')
            f *= c
        return f'\nO fatorial de {num} é {f}'


fat = fatorial(5)
print(fat)
help(fatorial)
