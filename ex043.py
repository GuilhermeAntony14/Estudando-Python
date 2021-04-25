print('vamos calcular seu IMC')
a = float(input('Sua altura: '))
p = float(input('Seu peso: '))
n = (p/(a**2))
print(f'Seu IMC e: {n:.1f}')
if n < 18.5:
    print('Abaixo do peso.')
elif n <= 25 and n > 18.5:
    print('Peso ideal.')
elif n < 30 and n > 25:
    print('Sobrepeso.')
elif n <= 40 and 30 < n:
    print('obsidade.')
else:
    print('obsidade mórbida.')
    