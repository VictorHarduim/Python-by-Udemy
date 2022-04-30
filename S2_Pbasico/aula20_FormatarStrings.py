nome = 'victor'
idade = 23
altura = 1.75
e_maior = idade > 18
peso = 69
imc = peso / (altura**2)

print(nome, 'tem', idade , 'anos de idade e seu IMC é' , imc)

print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')

print('{} tem {} anos e seu imc é {:.3f}'.format(nome, idade, imc))  # respectiva ordem
print('{n} tem {i} anos e seu imc é {im:.3f}'.format(n = nome, i = idade, im = imc))
print('{0} tem {1} anos e seu imc é {2:.3f}'.format(nome, idade, imc))

