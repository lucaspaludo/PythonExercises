valor = i = soma = 0
while valor != 999:
    valor = int(input('Digite um número: '))
    if valor != 999:
        i += valor
        soma += 1
print(f'A soma dos números digitados é {i}')
print(f'Você digitou {soma} valores')
