nome = input('Digite seu nome: ')
salario = float(input('Digite o seu salário: '))

aumentoPercent = salario * 0.15
print(f"{nome}, seu salário agora é de {salario+aumentoPercent:.2f} com 15% de aumento")
