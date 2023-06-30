val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
val3 = int(input('Digite o terceiro valor: '))

menor = val1
if (val2 < val1) and (val2 < val3):
    menor = val2
if (val3 < val2) and (val3 < val1):
    menor = val3

maior = val1
if (val2 > val1) and (val2 > val3):
    maior = val2
if (val3 > val2) and (val3 > val1):
    maior = val3

print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')
