n = 0
while n != 5:
    v = int(input('O 1° numero: '))
    v2 = int(input('O 2° numero: '))
    n = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] fechar
Adicione sua opição: '''))
    if n == 2 or n == 1:
        if n == 1:
            r = v + v2
            t = 'soma'
        elif n == 2:
            r = v * v2
            t = 'multiplicar'
        print(f'Você usou a operação de {t} e seu resultado é {r}.')
    elif n == 3:
        if v > v2:
            ma = v
        elif v2 > v:
            ma = v2
        print(f'O valor maior é {ma}')
    elif n == 4:
        print('Reiniciando os valores.')
    elif n == 5:
        print('Fechando programa.')
    else:
        print('Opção incorreta.')
