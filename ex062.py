inicio = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimoPrimeiro = inicio + 10 * razao
cont = 10
while inicio != decimoPrimeiro:
    print(inicio, end=' -> ')
    inicio += razao
print('FIM')
escolha = int(input('\nDeseja mostrar mais quantos termos? '))
cont += escolha
while escolha != 0:
    adicionado = decimoPrimeiro + escolha * razao
    while decimoPrimeiro != adicionado:
        print(decimoPrimeiro, end=' -> ')
        decimoPrimeiro += razao
    print('FIM')
    escolha = int(input('\nDeseja mostrar mais quantos termos? '))
    cont += escolha
print(f'Processo finalizado com {cont} termos')
print('Finished.')
