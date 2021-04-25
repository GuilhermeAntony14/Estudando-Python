from time import sleep
l = int(input('Digite um numero inteiro: '))
print('Analisando...')
sleep(1)
if float(l/2) == int(l/2):
    print('E um numero par!')
else:
    print('numero é impar!')
