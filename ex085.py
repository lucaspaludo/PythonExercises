pares = []
impares = []
valores = [pares, impares]

for i in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('*=' * 30)
print('\n')
print(f'Os valores pares são {sorted(valores[0])}')
print(f'Os valores ímpares são {sorted(valores[1])}')
