"""
Funcoes (def) em Python - *args **kwargs -
"""


# def func(a1, a2, a3, a4, a5, nome=None):
#     print(a1, a2, a3, a4, a5, nome)
#     return nome, a5
#
# var = func(1,2,3,4,5, nome='Jesus')
# print(var)

"""
def func(*args):
    args = list(args)
    args[0] = 20
    print(args)

func(1, 2, 3, 4, 5)
"""

"""
def func(*args):
    for v in args:
        print(v)

func(1, 2, 3, 4, 5)
"""

"""
def func(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func(*lista, *lista2)  # as duas listas formam uma unica tupla
"""

def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print("Idade nao existe.")
        
lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func(*lista, *lista2, nome='Jesus', sobrenome = 'Cristo')