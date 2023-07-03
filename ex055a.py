maiorPeso = 0
menorPeso = 0
for c in range(1, 6):
    peso = int(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    elif peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso
print(f'A pessoa mais pesada tem {maiorPeso}Kg.')
print(f'A pessoa mais leve tem {menorPeso}Kg.')
