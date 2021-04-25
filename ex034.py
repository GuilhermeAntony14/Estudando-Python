# from random import sample, choice
# n = choice(sample(range(10000), k=1))
n = float(input('Digite seu salario: '))
print(f'Seu salario é: R$ {n:.2f}')
if n <= 1250:
    s = (n*(15/100))+n
else:
    s = (n*(10/100))+n
print(f'Seu novo salario é: R${s:.2f}')
