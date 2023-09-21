listaGols = list()
jogador = dict()
jogador['nome'] = input('Nome do jogador: ')
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    listaGols.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
jogador['gols'] = listaGols[:]
jogador['total'] = sum(listaGols)
print('-*' * 30)
print()
print('Primeira visualização:')
print(jogador)
print()
print('-*' * 30)
print()
print('Segunda visualização:')
for k, v in jogador.items():
    print(f'{"":<4} - O campo {k} tem valor {v}')
print()
print('-*' * 30)
print()
print('Terceira visualização:')
if len(jogador["gols"]) == 1:
    print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partida')
    print(f'Na partida em que ele jogou ele fez {jogador["gols"][0]} gols')
else:
    for i,v in enumerate(jogador['gols']):
        print(f'Na {i+1}ª partida fez {v} gols')
    print(f'{jogador["nome"]} fez {jogador["total"]} gols no total')
print('-*' * 30)
