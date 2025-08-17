altura = float(input('Qual a altura?:'))
largura = float(input('Qual a largura?:'))
area = altura*largura
tinta = area/2
print('Com sua altura de {:.2f} e largura de {:.2f}, temos uma area de {:.2f}.'.format(altura, largura, area))
print('Tendo todas essas informações você vai precisa de {:.2f} litros de tinta.'.format(tinta))
