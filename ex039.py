import datetime
a = int(input('''Você e:
[ 1 ] Homem
[ 2 ] Mulher
opção: '''))
co = {'v': '\033[31m', 'l': '\033[m', 'c': '\033[36m'}
if a == 1:
    n = int(input('Ano que você nasceu: '))
    d = datetime.date.today().year
    id = (d - n)
    print('Quem nasceu em {}{}{}, faz {}{}{} anos, no ano de {}{}{}'.format(co['v'], n, co['l'], co['v'], id, co['l'], co['v'], d, co['l']))
    print('-=' * 20)
    if id == 18:
        print('Você tem que se {}ALISTAR{} este ano.'.format(co['v'], co['l']))
    elif id > 18:
        print('{}Você esta atrasado no seu alistamento{}.\n'
         'Teria que ter se alistado a {}{} anos{}.'
          .format(co['c'], co['l'], co['v'], d-(id-18), co['l']))
    else:
        print('{}Você esta novo para se alistar ainda{}.\n'
            'Você so vai se alista em {}{} anos{}.'.format(co['c'], co['l'], co['v'], d+(18-id), co['l']))
    print('-=' * 20)
else:
    print('-=' * 20)
    print('{}Você e mulher não precisa se alistar{}.'.format(co['c'], co['l']))
    print('-=' * 20)
