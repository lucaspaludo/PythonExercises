matrix = []
for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        linha.append(int(input(f'Digite o valor na posição [{i}][{j}]: ')))
    matrix.append(linha)

print('*=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matrix[i][j]:^5} ]', end=' ')
    print()

