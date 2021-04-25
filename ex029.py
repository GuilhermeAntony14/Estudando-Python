from random import choice,sample
#l = choice(sample(range(100), k=1))
l = int(input('Qual sua velocidade: '))
print(f'A velocidade é: {l}km')
if l <= 80:
    print('Dirija com cuidado, continue abaixo de 80km!')
else:
    print(f'Você levou multa \nValor de: R${float((l-80)*7):.2f}')

