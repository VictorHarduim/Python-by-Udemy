"""
Desempacotamento de listas em Python
"""

lista = ["Jesus", "Alfa", "Omega", 0, 1, 2, 3, 4]

n1, n2, *outraLista, ultimoDaLista = lista  # outraLista = Omega, 0, 1 ...

print(outraLista)
