n1 = int(input('Adicione um numero para a analise: '))
print('Escolha uma das bases para a conversão: ')
n = int(input('''\033[32m[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL\033[m
Qual e sua escolha: '''))
cor = {'am': '\033[33m', 'l': '\033[m'}
if n == 1:
    print('Seu valor convertido para {} BINARIO\033[m: {}'. format(cor['am'],bin(n1)))
elif n == 2:
    print('Seu valor convertido para {}OCTAL{}: {}'.format(cor['am'], cor['l'],oct(n1)))
elif n == 3:
    print('o numero convertido em {}HEXADECIMAL{}: {}'.format(cor['am'], cor['l'],hex(n1)))
else:
    print('Opção invalida, tente novamente.')
