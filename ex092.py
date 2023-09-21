from datetime import date

nome = input('Nome: ')
anoNascimento = int(input('Ano de Nascimento: '))
data = date.today()
anoAtual = data.strftime("%Y")
idade = int(anoAtual) - anoNascimento
ctps = int(input('Carteira de trabalho: '))

df = {
    'nome' : nome,
    'idade' : idade,
    'ctps' : ctps
}

if df['ctps'] == 0:
    print('=*' * 20)
    print(f'O nome é {df["nome"]}')
    print(f'A idade é {df["idade"]}')
    print(f'Não possui carteira de trabalho')
else:
    df['anoContratacao'] = int(input('Digite o ano de contratação: '))
    df['salario'] = float(input('Digite o salário: '))
    anoAposentadoria = df['anoContratacao'] + 35
    df['idadeAposentadoria'] = anoAposentadoria - anoNascimento

    print('=*' * 20)
    print(f'{"":<3} - O nome é {df["nome"]}')
    print(f'{"":<3} - A idade é {df["idade"]}')
    print(f'{"":<3} - O número da carteira de trabalho é {df["ctps"]}')
    print(f'{"":<3} - O ano de contratação é {df["anoContratacao"]}')
    print(f'{"":<3} - O salário é {df["salario"]}')
    print(f'{"":<3} - Irá se aposentar com {df["idadeAposentadoria"]} anos')




