def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols no campeonato')


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
