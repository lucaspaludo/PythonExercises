s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print(f'Soma de todos os {cont} números ímpares e múltiplos de 3 no intervalo entre 1  e 500: {s}')



