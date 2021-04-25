a = int(input('Digite a 1° reta: '))
b = int(input('Digite a 2° reta: '))
c = int(input('Digite a 3° reta: '))
if ((b-c) < a < b + c) and ((a - c) < b < a + c) and ((a - b) < c < a + b):
    if a == b == c:
        print('E um triangulo equelátero.')
    elif a == b or b == c or a == c:
        print('E um triangulo isósceles.')
    else:
        print('E um triangulo escaleno.')
else:
    print('Não e um triangulo.')
    