from random import choice
n = str(input('nome do 1° aluno: '))
n2 = str(input('nome do 2° aluno: '))
n3 = str(input('nome do 3° aluno: '))
n4 = str(input('nome do 4° aluno: '))
lista = (n,n2,n3,n4)
print(f'O aluno escolhido é: {choice(lista)}')