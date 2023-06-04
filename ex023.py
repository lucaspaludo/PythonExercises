num = int(input('Digite um número de 0 a 9999: '))
unidade = num // 1 % 10 #obtém unidade (divisão inteira por 1) e resto da divisão por 10
dezena = num // 10 % 10 #obtém dezena (divisão inteira por 10) e resto da divisão por 10
centena = num // 100 % 10 #obtém centena (divisão inteira por 100) e resto da divisão por 10
milhar = num // 1000 % 10 #obtém milhar (divisão inteira por 1000) e resto da divisão por 10
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
