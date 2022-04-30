lista = [
    #  0       1        2
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'joana'],  # 1
    ['Helena', 'Ed', 'Lu'],  # 2
]

"""
enumerada = list(enumerate(lista))  # Tupla, mostra o indice e o elemento
print(enumerada)
print()
print(enumerada[1][1][2])  # indiica 1 da lista mae, 1 da lista filha, 2 
"""
print()
"""
[<-- Enumerate
    0    1
    (0, ['Edu', 'João', 'Luiz']), 
    (1, ['Maria', 'Aline', 'joana']), 
    (2, ['Helena', 'Ed', 'Lu'])
]
"""

# for v1, v2 in enumerate(lista,53):
#     print(v1, v2)

for v1 in enumerate(lista, 53):
    valor_enumerado, minhaLista = v1
    nome1, nome2, nome3 = minhaLista
    print(nome1, nome3)