print('{:=^40}'.format('Lojas Gui'))
n = float(input('Coloque o valor do produto: R$ '))
print('''forma de pagamento. 
[1] Dinheiro/cheque. 
[2] Cartão. 
[3] 2x cartão. 
[4] 3x ou mais.''')
n2 = int(input('Coloque a opção: '))
print('===')
if n2 == 1:
    print(f'O valor a ser pago e R$ {n-(n*(10/100))}.')
elif n2 == 2:
    print(f'O valor a ser pago é R$ {n-(n*(5/100))}.')
elif n2 == 3:
    print(f'O valor a ser pago e R$ {n} \n2x de {n/2}.')
elif n2 == 4:
    print(f'O valor a ser pago é R$ {n+(n*(20/100))} \n3x de {(n+(n*(20/100)))/3}.')
else:
    print('Você fez algo errado.')
