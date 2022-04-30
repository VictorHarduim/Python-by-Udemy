#  Indices
#        0123456..                        33

frase = 'o rato roeu a roupa do rei de roma'  # Iterável (percorrer cada elemento)
tamanho_frase = len(frase)

contador = 0
novaString = ''

inputDoUsuario = input('Qual letra deve ser maiúscula? ')

# while contador < tamanho_frase:
#     # print(frase[contador], contador)
#
#     novaString += frase[contador]
#     print(novaString)
#     contador += 1


while contador < tamanho_frase:
    letra = frase[contador]
    if letra == inputDoUsuario:
        novaString += inputDoUsuario.upper()
    else:
        novaString += letra
    contador += 1
print(novaString)
