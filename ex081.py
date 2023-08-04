lista = list()
while True:
    num = lista.append(int(input('Digite um valor: ')))
    escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if escolha in 'Nn':
        break
    elif escolha in 'Ss':
        continue
    else:
        print('Opção inválida. Tente novamente.')
        lista.pop(-1)

print('*=' * 20)
print(f'Foram digitador {len(lista)} valores')
print(f'Valores na forma decrescente {sorted(lista, reverse=True)}')

if 5 in lista:
    print(f'O número 5 aparece {lista.count(5)} vezes')
else:
    print('O número 5 não aparece na lista')
