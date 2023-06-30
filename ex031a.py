from time import sleep
distancia = float(input('Digite a distância em Km: '))
print(f'Você está prestes a começar uma viagem de {distancia} Km.')
print('\n' + 'CALCULANDO O PREÇO DA SUA PASSAGEM...')
sleep(3)
print(f'O preço da passagem será de: R$: {(distancia * 0.45):.2f}') if distancia > 200 else print(f'O preço da passagem será de: R$: {(distancia * 0.5):.2f}')