frase = input('Digite uma frase: ').replace(' ', '').upper()
fraseInversa = ''
for c in range(len(frase) - 1, -1, -1):
    fraseInversa += frase[c]
print(frase, end=' ')
print(fraseInversa)
if frase == fraseInversa:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo')
