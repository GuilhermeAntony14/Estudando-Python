'''v = float(input('O valor do cateto op: '))
v2 = float(input('O valor do cateto ad: '))
n = ((v**2)+(v2**2))**(1/2)
print(f'{n:.2f}')'''
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
print(f' A hipotenusa mede: {hypot(co,ca):.2f}')
