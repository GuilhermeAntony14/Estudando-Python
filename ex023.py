n = int(input('Digite um numero entre 0 e 9999: '))
print(f''' Unidade: {n // 1 % 10}
 Dezena: {n // 10 % 10}
 Centena: {n // 100 % 10}
 Milhar: {n // 1000 % 10}''')
