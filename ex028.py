from random import choice,randint
from time import sleep
print('Vamos começar!')
print('Você consegue vencer?')
print('-=-=-' * 10)
print('vou pensar num valor de 0 a 5!')
print('-=-=-' * 10)
n = int(input('Qual você acha que é: '))
#escolha = choice([0,1,2,3,4,5])
escolha = randint(0,5)
print('Processando...')
sleep(1)
if n == escolha:
    print('Você venceu!')
else:
    print(f'Derrota! Eu pensei no {escolha} e não no {n}')
