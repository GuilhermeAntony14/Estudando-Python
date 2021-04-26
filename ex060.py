from time import sleep
f = 1
v = int(input('Digite seu numero para mostrar o factorial: '))
print('=-' * 20)
while v > 0:
     print(f'{v}', end=' ')
     print(' x ' if v > 1 else ' = ', end=' ')
     f *= v
     v -= 1
print(f)
print('=-' * 20)
sleep(1)
