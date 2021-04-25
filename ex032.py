# import leapyear
# ano = int(input('Escolha um ano: '))
# print(f'E ano e bissexto: {leapyear.get(ano)}')

from datetime import date
ano = int(input('Que ano quer analisar?(Digite 0 se for o atual) '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano}, é Bissexto.')
else:
    print(f'O ano {ano}, Não e Bissexto.')
