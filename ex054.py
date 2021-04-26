from datetime import date
n = date.today().year
t2 = 0
t = 0
for a in range(1, 8):
    d = int(input(f'Ano de nascimento da {a}° pessoa: '))
    if n - d >= 21:
        t += 1
    else:
        t2 += 1
print(f'Pessoas que chegaram a maioridade {t}.\nPessoas menores de idade {t2}.')
