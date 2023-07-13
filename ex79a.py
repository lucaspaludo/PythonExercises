numeros = list()
while True:
    n = int(input('Digite um número para adicionar na lista: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado')
    else:
        print('Número duplicado. Não vou adicionar')
    escolha = input('Deseja continuar? [S/N] ')
    if escolha in 'Nn':
        break
print('*=' * 30)
numeros.sort()
print(f'Os números digitados foram {numeros}')
