'''from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você desejar'))
seno = sin(radians (ângulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians (ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians (ângulo))
print('O ângulo de () tem a TANGENTE de (:.2f}'.format(ângulo, tangente))

print(f'Seno é {seno:.2f}')
print(f'Cosseno {cosseno:.2f}')
print(f'Tangente {tangente:.2f}')'''

import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O angulo {angulo} tem o seno de {seno:.2f}, cosseno de {cosseno:.2f}, tangente de {tangente:.2f}')