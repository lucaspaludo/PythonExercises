num1 = float(input('Digite um número real: '))
num2 = float(input('Digite outro: '))
s = num1 + num2
cores = {
    "limpa": "\033[m",
    "branco": "\033[30m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "roxo": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
}
print(f'A soma entre {cores["vermelho"]} {num1} {cores["limpa"]} e {cores["vermelho"]} {num2} {cores["limpa"]} é {cores["verde"]} {s} {cores["limpa"]}!')
