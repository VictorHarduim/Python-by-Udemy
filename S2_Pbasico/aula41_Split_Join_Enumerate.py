"""
Split, Join, Enumerate em Python
* Split -dividir uma strig #str
* Join - juntar uma lista #str
* Enumerate - enumerar elemento da lista #iteráveis
"""

"""
string = "O Brasil é o país do futebol, o Brasil é penta."

lista1 = string.split(' ')
lista2 = string.split(',')  # Vai dividir de acordo com o elemento interno escolhido

palavra = ''
contagem = 0

for valor in lista1:
    # print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase.')
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes foi {palavra} ({contagem}x)')
"""

print()

"""
string = 'O Brasil é penta.'
lista = string.split(' ')  #dividiu a str em lista com base nos espaçoes
string2 = ','.join(lista)  #uniu os elementos da lista usando virgula


print(string)
print(lista)
print(string2)
"""

print()

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)