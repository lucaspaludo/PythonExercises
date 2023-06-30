preco = float(input('Qual é o preço do produto? '))
print("\033[33m---------------------------------------------------\033[m")
print('\t 1. À Vista no dinheiro/cheque.')
print('\t 2. À Vista no cartão.')
print('\t 3. Em até 2x no cartão.')
print('\t 4. Em até 3x ou mais no cartão.')
print("\033[33m---------------------------------------------------\033[m")

formaPagamento = int(input('Digite o número correspondente a forma de pagamento: '))

if formaPagamento == 1:
    pagamento = preco - (0.1 * preco)
    print(f'Voce irá pagar {pagamento:.2f} sem juros')
elif formaPagamento == 2:
    pagamento = preco - (0.05 * preco)
    print(f'Você irá pagar {pagamento:.2f} sem juros')
elif formaPagamento == 3:
    valorParcela = preco / 2
    print(f'Sua parcela será de {valorParcela:.2f} e o preço é de {preco} sem juros.')
elif formaPagamento == 4:
    pagamento = preco + (0.2 * preco)
    totalDeParcelas = int(input('Quantas parcelas? '))
    valorParcela = pagamento / totalDeParcelas
    print(f'Sua parcela é de {valorParcela:.2f} e o preço é de {pagamento} com juros.')
else:
    print('\033[31mOpção inválida! Tente novamente.\033[m')

