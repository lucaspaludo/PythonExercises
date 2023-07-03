from random import choice
quant = 0
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor = choice(lista)
value = int(input('Digite um valor: '))
acertou = False
while not acertou:
    quant += 1
    value = int(input('Digite um valor: '))
    if value == valor:
        acertou = True
print(f'Acertou! Você precisou de {quant} tentativas')

