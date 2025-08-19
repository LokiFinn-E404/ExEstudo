salario = float(input('Qual seu salario base?:'))
aumento = salario*15/100
final = salario+aumento
print('Seu salario com o ajuste ficou em {:.2f} \nTendo um aumento de {:.2f}'.format(final, aumento))

