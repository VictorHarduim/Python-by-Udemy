# Exercicio 1

"""
num = input("Digite um número: ")

if num.isdigit():
    num = int(num)

    if num == 0:
        print(f'O número {num} é neutro.')
    elif (num % 2) == 0:
        print(f'O númeor {num} é par!')
    else:
        print(f'O núemro {num} é ímpar.')

else:
    print('Isso não é um número.')

"""

# Exercicio 2

"""
hora = input('Que horas são? ')

if hora.isdigit():
    hora = float(hora)

    if hora >= 0 and hora <=11:
        print(f'Bom dia!')
    elif hora >= 12 and hora <= 17:
        print(f'Boa tarde!')
    elif hora >= 18 and hora <=23:
        print(f'Boa noite!')
    else:
        print(f'Digite um horário válido.')
else:
    print(f'Digite um horário válido.')
"""

# Exercicio 3

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print(f'Seu nome é muito curto.')
elif tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
