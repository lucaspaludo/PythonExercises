lista_de_pesos = []

for i in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    lista_de_pesos.append(peso)

maior = lista_de_pesos[0]
menor = lista_de_pesos[0]

for i in lista_de_pesos:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f'Maior peso: {maior}')
print(f'Menor peso: {menor}')


