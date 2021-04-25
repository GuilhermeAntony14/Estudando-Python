from time import sleep
numero = int(input('Digite um numero inteiro: '))
print('Analisando...')
sleep(1)
if float(numero/2) == int(numero/2):
    print('E um numero par!')
else:
    print('numero é impar!')
