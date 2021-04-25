print('Qual valor sera maior?')
n1 = float(input('Escolha um valor: '))
n2 = float(input('Escolha outro valor: '))
co = {'rx': '\033[42m', 'l': '\033[m'}
if n1 > n2:
    print('O {}PRIMEIRO{} valor e maior.'.format(co['rx'], co['l']))
elif n2 > n1:
    print('O {}SEGUNDO{} valor e maior.'.format(co['rx'], co['l']))
else:
    print('{}Não existe{} valor maior, eles são iguais'.format(co['rx'], co['l']))
