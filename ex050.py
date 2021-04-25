x = 0
n = 0
n2 = 0
for s in range(1, 7):
    s2 = int(input('Digite um valor: '))
    n += 1
    if s2 % 2 == 0:
        x += s2
        n2 += 1
print(f'A soma Pares: {x}\nTinha cerca de: {n}\nImpares: {n-n2}\nPares: {n2}')
