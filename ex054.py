from datetime import date
somaMaior = 0
somaMenor = 0
for c in range(0, 6):
    ano = int(input('Em que ano você nasce? '))
    idade = date.today().year - ano
    if idade >= 21:
        somaMaior += 1
    else:
        somaMenor += 1

print(f'\n{somaMaior} pessoas são maiores de idade')
print(f'{somaMenor} pessoas são menores de idade')
