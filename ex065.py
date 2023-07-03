num = int(input('Digite um número inteiro: '))
escolha = input('Você deseja continuar? [S/N] ').strip().upper()[0]
n = 1
alef = num
maior_numero = num
menor_numero = num
if escolha == 'S':
    while escolha == 'S':
        num = int(input('Digite um número inteiro: '))
        alef += num
        n += 1
        if num > maior_numero:
            maior_numero = num
        if num < menor_numero:
            menor_numero = num
        escolha = input('Você deseja continuar? [S/N] ').strip().upper()

media = alef / n
print(f'\nA média dos valores é: {media}')
print(f'O maior número é {maior_numero}')
print(f'O menor número é {menor_numero}')


