"""
Operação Ternária em Python
"""
"""
loggedUser = False

if loggedUser:
    msg = 'Usário Logado'
else:
    msg = 'Usuário precisa logar.'

print(msg)
"""

print()

"""
loggedUser = True
msg = 'Usuário logado.' if loggedUser else 'Usuário precisa logar.'
print(msg)
"""



idade = input('Qual a sua idade? ')

# if idade >= 18:
#     print('Pode acessar.')
# else:
#     print('Não pode acessar.')

if not idade.isnumeric():
    print('Você precisa digitar apenas números.')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar.' if e_de_maior else 'Não pode acessar.'
    print(msg)
