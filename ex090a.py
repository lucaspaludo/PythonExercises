df = dict()
df['nome'] = input('Digite o nome do aluno: ')
df['media'] = float(input(f'Média de {df["nome"]}: '))
if df['media'] >= 7:
    df['situacao'] = 'Aprovado'
elif df['media'] < 5:
    df['situacao'] = 'Reprovado'
else:
    df['situacao'] = 'Recuperação'
print('*='*15)
print(f'O nome do aluno é {df["nome"]}')
print(f'A média de {df["nome"]} é {df["media"]}')
print(f'A situação de {df["nome"]} é {df["situacao"]}')

