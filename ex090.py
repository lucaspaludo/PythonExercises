situacao = ''
nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))

if media < 7:
    situacao = 'Reprovado'
elif 7 <= media <=10 :
    situacao = 'Aprovado'
else:
    situacao = 'Inválida'

aluno = {
    'nome' : nome,
    'media': media,
    'situacao' : situacao
}
print()
print(f'O nome é igual a {aluno["nome"]} ')
print(f'A média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situacao"]}')
