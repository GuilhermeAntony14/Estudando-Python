import random
n = [int(input('Escolha um numero de 1 a 10: '))]
n2 = random.sample(range(1, 11), k=1)
k = 1
while n != n2:
    if n >= n2:
        t = 'é menor'
    else:
        t = 'é maior'
    n = [int(input(f'Tente novamente, ele {t}: '))]
    k += 1
print(f'Você tentou a quantidade {k} de tentativas.')
