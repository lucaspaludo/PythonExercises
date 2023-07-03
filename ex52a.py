num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
if cont == 2:
    print(f'\033[m\nO número {num} é primo, ele foi divisível {cont} vezes')
else:
    print(f'\033[m\nO número {num} não é primo, ele foi divisível {cont} vezes')
