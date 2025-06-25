import random
n1 = (input('Primeiro nome: '))
n2 = (input('Segundo nome: '))
n3 = (input('Terceir nome: '))
n4 = (input('Quarto nome: '))

lista = [n1, n2, n3, n4]
res = random.choice(lista)
print(f'O aluno escolhido foi {res}')