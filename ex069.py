cont_idade = 0
cont_homens = 0
cont_idade_mulheres = 0
while True:
    sexo = input('Digite o seu sexo: [M/F] ').strip().upper()[0]
    idade = int(input('Digite a sua idade: '))
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F' and idade < 20:
        cont_idade_mulheres += 1
    escolha = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
print(f'{cont_idade} pessoas são maiores de 18 anos.')
print(f'{cont_homens} homens.')
print(f'{cont_idade_mulheres} mulheres tem menos de 20 anos.')
