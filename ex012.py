nome = input('Qual é o seu nome: ')
preco = float(input('Digite o preço do produto: '))
descontoPercent = preco * 0.05

print(f"{nome}, você irá pagar {preco-descontoPercent:.2f} reais com 5% de desconto")
