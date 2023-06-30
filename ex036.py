valor = float(input("Qual é o valor da casa? "))
salario = float(input("Qual é o seu salário? "))
anos = int(input("Em quantos anos irá pagar? "))

meses = 12*anos
prestacaoMensal = (valor/meses)
print(f"O valor da prestação mensal é de: \033[33m{prestacaoMensal:.2f}\033[m ")

salarioTrintaPorCento = salario * 0.3
print(f"30% do seu salário: {salarioTrintaPorCento}")
if prestacaoMensal > salarioTrintaPorCento:
    print(f"\033[31mO valor de {prestacaoMensal:.2f} da parcela mensal é maior do que 30% do seu salário\033[m")
else:
    print(f'\033[32mVocê pode comprar a casa sem problemas\033[m')
