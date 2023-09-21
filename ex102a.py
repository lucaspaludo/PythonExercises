def fatorial(n, show=True):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f



num = int(input('Digite um número para cálcular o fatorial: '))
print(fatorial(num, show=False))