a = int(input('Digite o 1°: '))
b = int(input('Digite o 2°: '))
c = int(input('Digite o 3°: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'Menor valor é {menor}')
print(f'Maior valor é {maior}')
