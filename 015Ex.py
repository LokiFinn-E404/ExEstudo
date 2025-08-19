dias = int(input('Quantos dias o carro foi usado?'))
kms = float(input('Quantos km o carro foi usado?'))
valorD = dias*60
kms = kms*0.15
valorf = valorD+kms
#Poderia ser também
# pago = (dias*60) + (kms*0.15)
print('O valor total é de R${:.2f}'.format(valorf))
