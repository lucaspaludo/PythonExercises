num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))

tupla_num = (num1, num2, num3, num4)
print(f'O valor 9 apareceu {tupla_num.count(9)} vezes')

cont_tres = tupla_num.count(3)
if cont_tres == 0:
    print('O número 3 não foi digitado')
else:
    print(f'O valor 3 foi apareceu na posição {tupla_num.index(3) + 1}')

cont_pares = 0
for i in range(0, len(tupla_num)):
    if tupla_num[i] % 2 == 0:
        cont_pares += 1
print(f'Foram digitados {cont_pares} números pares')
