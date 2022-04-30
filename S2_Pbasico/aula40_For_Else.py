"""
For / Else em Python
"""

variavel = ['Victor', 'Brenda', 'Jesus']

for valor in variavel:
    if valor.lower().startswith('v'):
        print('Começa com V', valor)
    else:
        print('Não começa com V', valor)
