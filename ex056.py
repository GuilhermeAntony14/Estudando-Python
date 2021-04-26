media = 0
velho = 0
idm = 0
nomev = ''
print('='*20)
for c in range(1, 6):
    nome = str(input('Qual seu nome: ')).strip()
    idade = int(input('Qual sua idade: '))
    sexo = str(input('''[ M ] Masculino.
[ F ] Feminino.
Qual e seu sexo: ''')).strip()
    print('='*20)
    if c == 1 and sexo in 'Mm':
        velho == idade
        if idade:
             nv = nome
    if sexo in 'Mm' and idade > velho:  # homem
        velho = idade
        nomev = nome
    if idade:
        media += idade
    if sexo in 'Ff' and idade < 20:  # mulher
        idm += 1
print(f' A media das idades é \033[31m{media/4:.1f}\033[m'
      f'\n Mais velho tem \033[31m{velho}\033[m anos e nome é \033[31m{nomev}\033[m '
      f'\n São \033[31m{idm}\033[m mulheres que tem menos que 20.')
