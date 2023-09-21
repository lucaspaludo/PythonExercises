def maior(*args):
    print(f'Analisando os valores passados {args}', sep=', ')

    print(f'Ao todo recebi {len(args)} valores e o maior deles é {max(args)}')


maior(2, 3, 4, 12, 5)
print('-*' * 30)
print()
maior(4, 3, 6, 1, 2)
print('-*' * 30)
