"""
Operadores Lógicos
and, or, not
in e not in
"""

"""
# (Verdadeiro e False) = Falso
comparacao1 and comparacao

# Verdadeiro ou falso
Comparacao1 or comparacao
"""
""""
a = 2
b = 3
c = 0  # considerado booleano falso


if b > a :
    print('B é maior que A.')
else:
    print('A é maior que B.')

print()

if not c:
    print('Preencha o valor de C.')
"""
"""
nome = 'Victor'

if 'u' in nome:
    print('Existe a letra O no seu nome.')
else:
    print('Não existe.')

print()

if 'asd' not in nome:
    print('Executei.')
else:
    print('Existe o texto.')
"""

# Exemplo

user = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

user1 = 'victor'
senha1 = '123456'

if user1 == user and senha1 == senha:
    print('Você está logado.')
else:
    print('Dados inválidos.')