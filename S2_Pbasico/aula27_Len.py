"""
user = input('Digite seu usuário: ')
qtd_caracteres = len(user)

#  print(user, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você prescida de um nome maior.')
else:
    print('Voce foi cadastrado no sistema.')
"""


str1 = input('Digite alguma coisa: ')
str2 = input('Digite outra coisa: ')

# print(len(str1)) é o mesmo que print(str1.__len__())

print(f'A quantidade total de caracteres digitados foi {len(str1) + len(str2)}')
