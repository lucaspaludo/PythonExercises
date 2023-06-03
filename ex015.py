dias = int(input('Quantidade de dias que utilizados: '))
km = float(input('Quantidade de Kilômetros percorridos pelo carro alugado: '))

print(f"Total a pagar: {(60*dias) + (0.15*km):.2f}")
