inicio = int(input('Digite o primeiro da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = inicio + (10 - 1) * razao
for c in range(inicio, decimo + razao, razao):
    print(c, end=' -> ')
print('FIM')

