total18 = totalH = totalM20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite o sexo: [M/F]').strip().upper()[0]
    if sexo == 'M':
        totalH += 1
    if idade > 18:
        total18 += 1
    if sexo == 'F' and idade < 20:
        totalM20 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
print(f'{total18} pessoas tem mais de 18 anos')
print(f'{totalH} são do sexo masculino')
print(f'{totalM20} mulheres tem menos de 20 anos')
