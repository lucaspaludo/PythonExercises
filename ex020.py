from random import shuffle
nome1 = input('Digite um nome: ')
nome2 = input('Digite um nome: ')
nome3 = input('Digite um nome: ')
nome4 = input('Digite um nome: ')
seq = [nome1, nome2, nome3, nome4]
shuffle(seq)
print(seq)
