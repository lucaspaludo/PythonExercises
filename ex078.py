lista = []

for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

maior = max(lista)
menor = min(lista)

print(f'Você digitou os valores: {lista}')
print(f'O maior número digitado é {maior} nas posições ', end='')
for i, v in enumerate(lista):
   if v == maior:
       print(f'{i}...', end='')
print(f'\n')
print(f'O menor número digitado é {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')


