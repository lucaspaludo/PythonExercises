num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha in 'Nn':
        break
for i in num:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'Os valores digitados são: {num}')
print(f'Os valores pares digitados são: {pares}')
print(f'Os valores ímpares digitados são: {impares}')
