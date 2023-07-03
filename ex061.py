inicio = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimoPrimeiro = inicio + (11 - 1) * razao
while inicio != decimoPrimeiro:
    print(inicio, end='-> ')
    inicio += razao
print('FIM')




