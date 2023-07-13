classificacao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético Mineiro', 'Atlético Paranaense', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'América MG', 'Sport','Vitória', 'Paraná')

print(f'Os 5 primeiros colocados são: {classificacao[0:5]}')

#for i in range(0, 4):
    #print(classificacao[i])

#print('\n')
#print('Os últimos 4 colocados são: ')
#for i in range(16, 20):
#    print(classificacao[i])
#print('\n')

print(f'Os últimos 4 colocados são: {classificacao[-4:]}')

print('Classificação em ordem alfabética:')
print(sorted(classificacao))

print('\n')
print(f'A Chapecoense está na {classificacao.index("Chapecoense")+1}ª posição. ')

