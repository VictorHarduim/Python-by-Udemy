n1 = input("Digite um numero: ")
n2 = input("Digite outro numero: ")

"""
n1 = int(n1)
n2 = int(n2)
print(n1+n2)
"""

#isnumeric (true se for inteiro e positivo)
#isdigit
#isdecimal

#### Ver biblioteca Python ####

"""
if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)

    print(n1 + n2)
else:
    print('Não pude converter os números')
"""


try:
    n1 = float(n1)
    n2 = float(n2)

    print(n1 + n2)

except:
    print('Error')