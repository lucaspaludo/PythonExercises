frase = input('Digite uma frase: ').strip().upper()
fraseLista = frase.split()
fraseJunta = ''.join(fraseLista)
fraseInversa = ''
for c in range(len(fraseJunta) - 1, -1, -1):
    fraseInversa += fraseJunta[c]
print(fraseJunta, end=' ')
print(fraseInversa)

if fraseJunta == fraseInversa:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
