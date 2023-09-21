from datetime import datetime
from time import sleep
dados = dict()
dados['nome'] = input('Nome: ')
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('CTPS (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print()
print(f'{"":^10} Dados de {dados["nome"]} ')
for k,v in dados.items():
    sleep(1)
    print(f'{"":<4} - {k} tem o valor {v}')
