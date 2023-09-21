def ficha(n='<desconhecido>', g=0):
    return f'O jogador {n} fez {g} gols'


nome = input(f'Nome do jogador: ').strip()
gols = int(input('Número de gol(s): '))

if nome in '':
    print(ficha(g=gols))
elif nome in '' and (gols < 1 or type(gols) is not int):
    print(ficha())
elif gols < 1 or type(gols) is not int:
    print(ficha(n=nome))
else:
    print(ficha(nome, gols))
