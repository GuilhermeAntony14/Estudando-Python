from random import choice
from time import sleep
co = {'l': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'roxo': '\033[35m', 'azul claro': '\033[36m', 'cinza': '\033[37m'}
n = 0
while n != 4:
    sleep(1)
    print('Bora para o jogo.')
    print('''Escolha sua jogada. 
        [1] Pedra.
        [2] Papel.
        [3] Tesoura.
        [4] Exit''')
    n = int(input('Sua escolha: '))
    n2 = [1, 2, 3]
    n3 = choice(n2)
    if n != 4:
        if n3 == 1:
            t = 'Pedra'
        elif n3 == 2:
            t = 'Papel'
        elif n3 == 3:
            t = 'Tesoura'
        if n == 1:
            t2 = 'Pedra'
        elif n == 2:
            t2 = 'Papel'
        elif n == 3:
            t2 = 'Tesoura'
        print('+-'*20)
        print('Você jogou {}{}{}, o maquina jogou {}{}{}.'
            .format(co['amarelo'], t2, co['l'], co['amarelo'], t, co['l']))
        print('+-'*20)
        if t == t2:
            print('Desta vez foi {}Empate{}.'.format(co['azul'], co['l']))
        if t != t2:
            if n == 1:
                if t == 'Tesoura':
                    print('Você {}Venceu{} parabens.'.format(co['verde'], co['l']))
                else:
                    print('Você {}Perdeu{} não foi desta vez.'.format(co['vermelho'], co['l']))
            if n == 2:
                if t == 'Pedra':
                    print('Você {}Venceu{} parabens.'.format(co['verde'], co['l']))
                else:
                    print('Você {}Perdeu{} não foi desta vez.'.format(co['vermelho'], co['l']))
            if n == 3:
                if t == 'Papel':
                    print('Você {}Venceu{} parabens.'.format(co['verde'], co['l']))
                else:
                    print('Você {}Perdeu{} não foi desta vez.'.format(co['vermelho'], co['l']))
        print('+-'*20)
