listagem = ('Iogurte', 10.99, 'Granola', 17.99, 'Ovo', 20.99, 'Pão Francês', 110.21)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<30}', end='')
    print(f'R$: {listagem[i + 1]}')
print('-' * 40)

