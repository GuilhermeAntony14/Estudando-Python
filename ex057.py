n = ''
while n != 'M' and n != 'F':
    n = str(input('sexo(M/F): ')).strip().upper()[0]
if n == 'M':
    t = 'Homem'
else:
    t = 'Mulher'
print(f'Você e {t}.')

# sexo = str(input('sexo[M/F]: '))
# while sexo not in 'MF':
#     sexo = str(input('Dados invalidos. Favor adicionar um dado valido: '))
# print(f'Dado adicionado com sucesso sexo [{sexo}].')
