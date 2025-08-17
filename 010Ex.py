carteira = float(input('Quanto você tem em carteira?:'))
dolar = carteira/3.27
print('Você tem R${}, que é o equivalente a US${:.2f}'.format(carteira, dolar))
