n = int(input('Digite um valor: '))
n2 = int(input('Adicione a razão da PA: '))
d = n + (11 - 1) * n2
print(f'Seu digito inicial {n}\nA razão é {n2}\nSua progressão é:')
for c in range(n, d + n2, n2):
    print(f'{c}', end=(','))
print('Fim')
