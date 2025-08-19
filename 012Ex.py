valor = float(input('Qual o valor do produto?:'))
desconto = valor*0.05
valorfinal = valor-desconto
print('O desconto ficou de R${:.2f}. \n Sendo assim o valor final ficou em R${:.2f}'.format(desconto, valorfinal))
