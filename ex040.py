print('vamos descobrir a sua nota!')
n = float(input('Digite sua primeira nota: '))
n1 = float(input('Digite o segundo valor: '))
n2 = float((n+n1)/2)
print(f'A media e {n2}!')
if n2 <= 4:
    print('Reprovado!')
elif n2 >= 5 and n2 < 7:
    print('Recuperação!')
elif n2 >= 7:
    print('\033[32mAprovado!\033[m')
