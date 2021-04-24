from random import shuffle,sample
a = str(input('1° nome: '))
a2 = str(input('2° nome: '))
a3 = str(input('3° nome: '))
a4 = str(input('4° nome: '))
lista = [a,a2,a3,a4]
shuffle(lista)
print(f'Ordem de apresentação: \n {lista}')
