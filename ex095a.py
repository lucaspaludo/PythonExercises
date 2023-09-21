time = list()
listaGols = list()
jogador = dict()
#coleta de dados
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    listaGols.clear()
    for c in range(0, tot):
        listaGols.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
    jogador['gols'] = listaGols[:]
    jogador['total'] = sum(listaGols)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

print('-*' * 30)

#exibição dos dados
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

#análise de dados
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 p/ parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com código {busca}')
    else:
        print(f'---- Levantamento do jogador {time[busca]["nome"]} ----')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')


