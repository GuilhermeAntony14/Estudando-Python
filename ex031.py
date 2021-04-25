# from random import choice, sample
from time import sleep
# numero = choice(sample(range(100), k=10))
numero = float(input('Distancia da viajem: '))
print(f'Distancia: {numero}Km')
print('Analisando sua passagem...')
sleep(1)
if numero <= 200:
    print(f'O valor cobrado para sua passagem é: R${numero * 0.50:.2f}')
else:
    print(f'O valor cobrado para sua passagem é: R${numero * 0.45:.2f}')
