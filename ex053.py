tx = str(input('Digite uma frase: ')).strip().lower()
tx2 = ''.join(tx.split())
i = tx2[::-1]
'''for c in range(len(tx2)-1, -1, -1):
    i += tx2[c]'''
if i == tx2:
    t = 'é palindromo'
else:
    t = 'não é palindromo'
print(f'A frase ({tx}) {t}')
