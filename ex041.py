import time
co = {'verde': '\033[32m', 'l': '\033[m', 'amarelo': '\033[33m'}
n = int(input('Qual a sua idade: '))
print('{}Vamos falar sua categoria{}!'.format(co['amarelo'], co['l']))
time.sleep(2)
print('O atleta tem {}{}{}\n'
      f'Sua classificação é:'.format(co['verde'], n, co['l']))
if n <= 9:
    print('{}Mirim{}'.format(co['verde'], co['l']))
elif n > 9 and n <= 14:
    print('{}Infantil{}'.format(co['verde'], co['l']))
elif n  > 14 and n <= 19:
    print('{}Junior{}'.format(co['verde'], co['l']))
elif n > 19 and n <= 20:
    print('{}Sênior{}'.format(co['verde'], co['l']))
elif n > 20:
    print('{}Master{}'.format(co['verde'], co['l']))
