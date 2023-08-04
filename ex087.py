matrix = []
soma_pares = 0
soma_terceira_coluna = 0
soma_segunda_linha = 0
for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        linha.append(int(input('Digite um valor: ')))
    matrix.append(linha)

print('*=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matrix[i][j]} ]', end='')
    print('\r')

for i in range(0, 3):
    for j in range(0, 3):
        if matrix[i][j] % 2 == 0:
            soma_pares += matrix[i][j]
        if j == 2:
            soma_terceira_coluna += matrix[i][j]
        if i == 1:
            soma_segunda_linha += matrix[i][j]


print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'A soma dos valores da segunda linha é: {soma_segunda_linha}')
