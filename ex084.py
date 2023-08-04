dados = []
nomes = []
pesados = []
leves = []
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    escolha = input('Quer continuar? [S/N] ').strip().upper()
    if escolha == 'N':
        break
    elif escolha == 'S':
        continue
    else:
        print('Opção inválida. Tente novamente.')
        dados.remove(dados[-1])
        dados.remove(dados[-1])

for i in range(0, len(dados), 2):
    nomes.append(dados[i])
    if dados[i+1] >= 100:
        pesados.append(dados[i])
    if dados[i+1] <= 70:
        leves.append(dados[i])

print('\n')
print('*=' * 30)
print(f'Foram cadastradas {len(nomes)} pessoas')
print(f'As pessoas mais pesadas são: {pesados}')
print(f'As pessoas mais leves são: {leves}')







