tupla0_20 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
             'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número: '))
    if num > 20 or num < 0:
        print('Opção inválida. Tente novamente.')
    if num >=0 and num <= 20:
        numero_mostrado = tupla0_20[num]
        print(f'O número equivalente é {numero_mostrado}')
        escolha = input('Quer continuar? [S/N] ').strip()
        if escolha in 'Ss':
            continue
        if escolha not in 'Ss':
            break


