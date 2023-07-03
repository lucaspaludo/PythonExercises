n = int(input('Digite a quantidade de elementos da sequência de Fibonacci: '))
lista = [None]*n
lista[0] = 1
lista[1] = 1
i = 2
while i != n:
    lista[i] = lista[i-1] + lista[i-2]
    i += 1
print(lista)

