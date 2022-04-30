"""
Formatando Valores com modificadores

:s - texto (strings)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:.(numero)f - quantida de casas decimais (float)
:(caractere)(> ou < ou ^)(quantidade)(tipo - s,d ou f)

> - Esquerda
< - direita
^ - centro
"""
nome = 'Victor'
n1 = 10
n2 = 3
divisao = n1 / n2

#print('{:.3f}'.format(divisao))
#print(f'{divisao:.3f}')

print(f'{n1:v^6}')
print(f'{n2:.3f}')

print(f'{nome:+^16}')

nome1 = nome.ljust(10, '*')  #leftJust, justificar a esquerda
print(nome1)

print(nome.upper())  #tudo minusculo
print(nome.lower())  #tudo maiusculo
print(nome.title())  #primeira letra maiuscula

