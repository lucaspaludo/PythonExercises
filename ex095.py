jogadores = list()
while True:
    quantidadeGols = list()
    nome = input('Nome do jogador: ')
    quantidadePartidas = int(input(f'Quantas partidas {nome} jogou: '))
    for i in range(1, quantidadePartidas + 1):
        quantidadeGols.append(int(input(f'Quantos gols {nome} fez na {i}ª partida: ')))

    df = {
        'nome': nome,
        'quantidadePartidas': quantidadePartidas,
        'quantidadeGols': quantidadeGols,
        'soma': sum(quantidadeGols)
    }

    jogadores.append(df)
    escolha = input('Quer continuar? [S/N] ').strip().upper()[0]

    if escolha == 'S' or escolha == 'SIM':
        print('=*' * 20)
        continue
    elif escolha == 'N' or escolha == 'NÃO':
        print('=*' * 20)
        break
    else:
        print('Opção inválida. Tente novamente.')
        print('=*' * 20)
        del df

print(f'{"cod.":<6}{"Nome":<10}{"Gols":>10}{"Total":>10}')

for i in range(len(jogadores)):
    print(f'{i:<4}{jogadores[i]["nome"]:<4}{jogadores[i]["quantidadeGols"]}{jogadores[i]["soma"]:>10}')

while True:
    detalhe = int(input('Mostrar dados de qual jogador? [999 p/ parar] '))
    if detalhe == 999:
        break
print('<< ENCERRADO >>')






