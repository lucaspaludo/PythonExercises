num = int(input('Digite o número: '))
print(f'Tabuada do {num}')

for c in range(1, 11):
    res = c * num
    print(f'{num} X {c:2} = \033[32m{res}\033[m')
