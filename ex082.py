lista = list()
lista_pares = list()
lista_impares = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    if lista[-1] % 2 == 0:
        lista_pares.append(lista[-1])
    else:
        lista_impares.append(lista[-1])
    escolha = input('Deseja continuar? [S/N]').strip().upper()[0]
    if escolha in 'Ss':
        continue
    elif escolha in 'Nn':
        break
    else:
        print('Opção inválida. Tente novamente.')

        if lista[-1] % 2 == 0:
            lista_pares.pop(-1)
        else:
            lista_impares.pop(-1)
        lista.pop(-1)
print(f'Os número digitados foram: {lista}')
print(f'Os números pares digitados foram: {lista_pares}')
print(f'Os números ímpares digitados foram: {lista_impares}')
