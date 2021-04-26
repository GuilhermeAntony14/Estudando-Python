maior = 0
menor = 0
for p in range(1, 6):
    p2 = float(input(f'Digite o peso da {p}° pessoa: '))
    if p == 1:
        maior = p2
        menor = p2
    else:
        if p2 > maior:
            maior = p2
        if p2 < menor:
            menor = p2
print('='*20)
print(f'Maior peso é {maior}Kg\nMenor peso é {menor}Kg')
print('='*20)
