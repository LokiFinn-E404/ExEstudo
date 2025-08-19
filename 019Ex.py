import random

a1 = str(input('Qual nome do primeiro aluno?: '))
a2 = str(input('Qual nome do segundo aluno?: '))
a3 = str(input('Qual nome do terceiro aluno?: '))
a4 = str(input('Qual nome do quarto aluno?: '))
lista = [a1, a2, a3, a4]
escolha = random.choice(lista)
print(escolha)

'''from random import choice

a1 = str(input('Qual nome do primeiro aluno?: '))
a2 = str(input('Qual nome do segundo aluno?: '))
a3 = str(input('Qual nome do terceiro aluno?: '))
a4 = str(input('Qual nome do quarto aluno?: '))
lista = [a1, a2, a3, a4]
escolha = choice(lista)
print(escolha)'''