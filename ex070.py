nome = input('Digite o nome do produto: ').strip()
preco = float(input('Digite o preço do produto: '))
menor_preco = preco
total = preco
menor_prod = nome
cont_preco = 0
if preco < 1000:
    cont_preco = 1
escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]
if escolha == 'S':
    while True:
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        total += preco
        if preco < 1000:
            cont_preco += 1
        if preco < menor_preco:
            menor_preco = preco
            menor_prod = nome
        escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if escolha == 'N':
            break
print(f'Temos {cont_preco} produtos com menos de 1000 reais')
print(f'Total: {total}')
print(f'{menor_prod} é o produto mais barato e custa {menor_preco:.2f} reais')

