from time import sleep
alunos = list()
alunoPos = list()
notas = list()
numNota = list()

while True:
    alunoPos.append(input('Nome do aluno: '))
    notas.append(float(input('Digite a primeira nota: ')))
    notas.append(float(input('Digite a segunda nota: ')))
    alunoPos.append(notas[:])
    notas.clear()
    alunos.append(alunoPos[:])
    alunoPos.clear()
    escolha = input('Deseja continuar? [S/N] ').strip().upper()
    if escolha == 'S' or escolha == 'SIM':
        continue
    elif escolha == 'N' or escolha == 'NÃO':
        break
    else:
        print('Opção inválida. Tente novamente.')
        alunos.pop()

print('*=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-'*20)

for i in range(0, len(alunos)):
    numNota.append(i)
    media = (alunos[i][1][0] + alunos[i][1][1]) / 2
    print(f'{i:<4}{alunos[i][0]:<10}{media:>6.1f}')

while True:
    numAluno = int(input('Mostrar as notas de qual aluno? (999 para interromper) '))
    if numAluno in numNota:
        print(f'As notas de {alunos[numAluno][0]} são: {alunos[numAluno][1]}')
    elif numAluno == 999:
        print('FINALIZANDO.... ')
        sleep(0.5)
        print(f'<<< Volte sempre >>>')
        break
    else:
        print('Opção inválida. Tente Novamente')


