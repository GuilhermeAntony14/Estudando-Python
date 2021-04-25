n = int(input('Escolha a tabuada: '))
print(f'A tabua de {n} é:')
print('=-' * 10)
for c in range(1, 11):
    print(f'{n:^4} * {c:^5} = {c * n:^5}')
print('=-' * 10)
