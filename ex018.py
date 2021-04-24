from math import sin,cos,tan,radians
v = float(input('Coloque seu ângulo: '))
n = radians(v)
print(f' O ângulo de 30: \n Seno: {sin(n):^28.2f}\n Cosseno: {cos(n):^22.2f}\n Tangente: {tan(n):^20.2f}')
