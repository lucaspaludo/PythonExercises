quantidadeGols = list()
nome = input('Nome do jogador: ')
quantidadePartidas = int(input(f'Quantas partidas {nome} jogou: '))
for i in range(1, quantidadePartidas+1):
    quantidadeGols.append(int(input(f'Quantos gols {nome} fez na {i}ª partida: ')))

df = {
    'nome': nome,
    'quantidadePartidas': quantidadePartidas,
    'quantidadeGols': quantidadeGols,
    'soma': sum(quantidadeGols)
}

print()
for i, j in enumerate(quantidadeGols):
    print(f'Na {i+1}ª partida {nome} fez {j} gols')
print(f'{nome} fez {df["soma"]} gols no total')
