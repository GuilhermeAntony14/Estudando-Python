casa = float(input('Valor da casa: R$'))
sa = float(input('Salário: R$'))
pa = float(input('Quantos anos vai pagar: '))
print(f'Valor da prestação é: {casa/(pa*12):.2f}\n'
      f'Valor maximo que você pode pagar: {sa * (30/100)}')
if casa/(pa*12) <= (30/100)*sa:
    print('Imprestimo \033[42maprovado\033[m\n')
else:
    print('\033[41mNão foi aprovado\033[m, pois superou 30% do seu salario.')
