num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    print(f'\033[33m{num1}\033[m é maior que \033[33m{num2}\033[m')
    print('O primeiro valor é o maior.')
elif num2 > num1:
    print(f'\033[33m{num2}\033[m é maior que \033[33m{num1}\033[m')
    print('O segundo valor é o maior.')
else:
    print('Os valores são iguais')
