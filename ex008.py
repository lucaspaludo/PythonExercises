valorEmMetros = float(input('Digite o valor em metros: '))
cores = {
    "limpa": "\033[m",
    "vermelho": "\033[31m",
    "amarelo": "\033[33m",
}
if valorEmMetros == 1:
    print(f"{cores['vermelho']} {valorEmMetros} {cores['limpa']}metro equivale a {valorEmMetros*100} centímetros e {valorEmMetros*1000} milímetros")
else:
    print(f"{valorEmMetros} metros equivale a {valorEmMetros * 100:.2f} centimetros", end=' ')
    print(f"e {valorEmMetros * 1000:.2f} milimetros")
