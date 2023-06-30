salario = float(input('Digite o seu salário: '))
if salario > 1250:
    aumento = salario + (salario * 0.1)
    print(f'Com um aumento de 10% seu salário será de R$: {aumento}')
else:
    aumento = salario + (salario * 0.15)
    print(f'Com um aumento de 15% seu salário será de R$: {aumento}')
