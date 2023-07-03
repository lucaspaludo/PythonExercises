from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
valor = 0

while valor != 7:
    print('+=' * 10)
    print('''
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Maior
    6 - Novos números
    7 - Sair do programa
    ''')
    print('+=' * 10)
    valor = int(input('Qual operação você deseja? '))
    if valor == 1:
        print(f'Soma = {num1+num2}')
    elif valor == 2:
        print(f'Subtração = {num1 - num2}')
    elif valor == 3:
        print(f'Produto = {num1 * num2}')
    elif valor == 4:
        print(f'Razão = {num1 / num2}')
    elif valor == 5:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        elif num2 > num1:
            print(f'{num2} é maior que {num1}')
        else:
            print(f'{num1} é igual a {num2}')
    elif valor == 6:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    else:
        print('Opção inválida. Tente novamente.')
    print('+=' * 10)
    sleep(2)
sleep(1)


