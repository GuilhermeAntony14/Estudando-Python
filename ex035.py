print('~#' * 20)
print('Analisar um triangulo')
print('~#' * 20)
a = float(input('Digite o valor 1°: '))
b = float(input('Digite o valor 2°: '))
c = float(input('Digite o valor 3°: '))
if (b-c) < a < b + c and (a-c) < b < a + c and (a-b) < c < a + b:
    print('\033[0;32mPode forma\033[m um triangulo!')
else:
    print('\033[0;31mNão forma\033[m um triangulo!')
print('~#' * 20)
