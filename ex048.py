x = 0
ct = 0
for c in range(1, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            x += c
            ct += 1
print(f'A soma dos {ct} numeros impares e multiplos de 3 e: {x}')
