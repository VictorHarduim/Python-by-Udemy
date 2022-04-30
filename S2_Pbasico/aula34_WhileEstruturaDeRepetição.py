"""
While em Python
utilizado para realizar ações enquanto uma condição for verdadeira.
"""
"""  Loop infinito
while True:
    nome = input('Qual o seu nome: ')
    print(f'Olá {nome}.')
"""
####
"""
x = 0
while x < 5:
    print(x)
    x = x+1  # x += 1
print('Acabou!')
"""
####
"""
y = 0
while y < 10:
    if y == 3 or y == 6 or y == 9:
        pass  #break para quebrar o laço
    else:
        print(y)
    y = y +1
print("acabou!")
"""
###

"""
x = 0  #coluna

while x<10:
    y = 0  # linha

    while y<5:
        print(f'X vale {x} e Y vale {y}.')
        y += 1

    x+=1
print('Acabou')
"""

#####


while True:
    print()
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operador = input('Digite um operador matemático: ')  #+ - / *

    if not n1.isnumeric() or not n2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    n1 = float(n1)
    n2 = float(n2)



    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '/':
        print(n1 / n2)
    elif operador == '*':
        print(n1 * n2)

    else:
        print('Operador inválido!')