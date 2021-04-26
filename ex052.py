n = int(input('Adicione um numero: '))
t = 0
for n2 in range(1, n+1):
    if n % n2 == 0:
       print('\033[32m', end=' ')
       t += 1
    else:
       print('\033[31m', end=' ')
    print(f'{n2}', end=' ')
if t == 2:
      r = 'é primo.'
else:
      r = 'não e primo.'
print(f'\n\033[mSeu numero é {n}, foi divisivel {t}.\nO seu numero {r}.')
