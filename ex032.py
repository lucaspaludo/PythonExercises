from datetime import date
ano = int(input('Digite o ano ou digite 0 para trabalhar com o ano atual: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bisexto!')
else:
    print(f'O ano {ano} não é bissexto')


