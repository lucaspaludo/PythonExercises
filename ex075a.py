numeros = (int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')),
           int(input('Digite o quarto número: ')))

print(f'O número nove foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 aparece na {numeros.index(3) + 1}ª posição')
else:
    print(f'O número 3 não foi digitado.')
print('Os números pares digitados são: ', end='')
for i in numeros:
    if i % 2 == 0:
        print(i, end=', ')
