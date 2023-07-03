total = contMil = menorPreco = cont = 0
produtoBarato = ' '
while True:
    nome = input('Digite o nome do produto: ')
    preco = int(input('Digite o preço do produto: '))
    total += preco
    cont += 1
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        produtoBarato = nome
    if preco > 1000:
        contMil += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
print(f'Total gasto de de R${total}')
print(f'{contMil} produtos custaram mais de R$1000')
print(f'Produto mais barato é um {produtoBarato} que custa R${menorPreco}')
