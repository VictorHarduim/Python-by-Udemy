
# Atividade 1

def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')
saudacao('Bem vindo,', 'Jesus')

print('###')

# Atividade 2

def soma(a,b,c):
    print(a + b + c)
soma(1,2,3)
print('###')


# Atividade 3

def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual/100))

aumento_percentual(50, 10)
print('###')



# Atividade 4
def fizz_buzz(n):
    if (n % 3) == 0 and (n % 5)==0:
        print('FizzBuzz')
    elif (n % 3) == 0:
        print('Fizz')
    elif (n % 5)==0:
        print('Buzz')
    else:
        print(n)

fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(13)

print('###')

from random import randint
for i in range(100):
    aleatorio = randint(0,100)
    print(fizz_buzz(aleatorio))