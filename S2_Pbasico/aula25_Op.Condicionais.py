"""
Operadores Relacionais
==  igualdade (pergunta)
>  maior que
>=  maior ou igual
<  menor que
<=  menor ou igual
!=  diferente
"""

"""
n1 = 2
n2 = 2

expressao = (n1 == n2)
print(expressao)

exp2 = (n1 > n2)
print(exp2)
"""

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
muitoJovem =20
muitoVelho = 30

if idade >= muitoJovem and idade <= muitoVelho:
    print(f'{nome} pode pegar um empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')