pessoa = dict()
dados = list()
somaIdade = 0
listaMulheres = list()
listaIdadesAcimaMedia = list()

while True:
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['sexo'] = input('Digite o sexo: [M/F] ').strip().upper()[0]
    if pessoa['sexo'] == 'F':
        listaMulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Digite a idade: '))
    dados.append(pessoa)
    somaIdade += pessoa['idade']
    escolha = input('Deseja continuar? [S/N] ').strip().upper()
    if escolha == 'S' or escolha == 'SIM':
        continue
    elif escolha == 'N' or escolha == 'NÃO':
        break
    else:
        print('Opção inválida. Tente novamente')
        dados.pop()

print()
print(f'Foram cadastradas no total {len(dados)} pessoas')

print()
print(f'A média de idade das pessoas é {(somaIdade/len(dados)):.1f}')

print()
print(f'As mulheres cadastradas são:')
for i in listaMulheres:
    print(f'{"":<4}{i}')








