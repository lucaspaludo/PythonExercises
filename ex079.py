lista = []
while True:
    num = lista.append(int(input('Digite um valor: ')))
    if lista.count(lista[-1]) > 1:
        print('Valor Reptido... Não vou adicionar')
        lista.pop(-1)
    else:
        print('Valor adicionado na lista.')

    escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if escolha in 'Nn':
        break
    elif escolha in 'Ss':
        continue
    else:
        print('Opção inválida. Tente novamente')
        lista.pop(-1)
print(sorted(lista))



