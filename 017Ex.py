from math import sqrt

co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))

hip = sqrt(co ** 2 + ca ** 2)

print('O valor da hipotenusa é {:.2f}'.format(hip))

'''hypot é a hipotenusa no math
from math import hypot
co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'O valor da hipotenusa é {hi:.2f}')'''


'''Essa versão é sem importação
co = float(input('Comprimento do cateto oposto: '))
ca= float(input("Comprimento do cateto adiacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')'''

