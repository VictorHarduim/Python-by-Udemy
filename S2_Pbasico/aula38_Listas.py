"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

"""
#ind.     0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#negat.   5    4    3    2    1

# lista[5] = 'Qualquer outra coisa'  (trocou o elemento 5)

print(lista[0::2])
print(lista[-1])
"""

l1 = [1, 2, 3]
l2 = [4, 5 ,6, 7, 8, 9]

# l3 = l1 + l2
# l2.pop()  - retira o ultimo elemento da lista
# l2.insert(0, 'br')  - 'br' passa a ser o indice 0 e os demais pulam uma casa
# l2.append('k')  - insere ao final da lista
# l1.extend(l2)  - A l2 se junta a l1, logo a l1 vai de 1 a 6
# del(l2[3:5])  - remove os itens de 3 a 5 (nã inclui o 5 item)

"""
print(l2)
l2.insert(0, 'br')
print(l2)
del(l2[0])
print(l2)
"""
print()
"""
print(max(l2))
print(min(l2))
"""
print()



"""
l4 = list(range(0,100,8))

soma = 0
for valor in l4:
    soma += valor

    print(soma)
"""
print()

"""
l5 = ['string', True, 10, -15.72]

for elem in l5:
    print(f'O tipo do elem é {type(elem)} e seu valor é {elem}.')
"""



secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break


    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print("Assim não vale!")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta.')
    else:
        print(f'A letra {letra} não existe na palcara secreta.')
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabens! A palavra era {secreto_temporario.title()}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario.title()}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()
