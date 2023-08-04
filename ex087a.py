matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaCol = mai = 0
for i in range(0, 3):
    for j in range(0, 3):
        matrix[i][j] = int(input(f'Digite o valor para [{i},{j}]: '))
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matrix[i][j]:^5}]', end='')
        if matrix[i][j] % 2 == 0:
            somaPares += matrix[i][j]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {somaPares}')
for i in range(0, 3):
    somaCol += matrix[i][2]
print(f'A soma dos valores da terceira coluna é: {somaCol}')
for j in range(0, 3):
    if j == 0:
        mai = matrix[1][j]
    elif matrix[1][j] > mai:
        mai = matrix[1][j]
print(f'O maior valor da segunda linha é: {mai}')