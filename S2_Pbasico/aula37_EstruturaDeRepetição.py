"""
For in em Python
Iterando strings com for
função Range (start = 0, stop, step= 1)
"""

#continue - pula para o proximo laço
#break - termina o laço


""" Iteração com while e For
texto = 'Python'

c = 0
while c < len(texto):
    print(texto[c])
    c += 1

for letra in texto:
    print(letra)

print()

for n, letra in enumerate(texto):
    print(n, letra)
"""

print()

"""
for n in range(10):
    print(n)

for n in range(0, 10, 2):
    print(n)

for m in range(20, 10, -1):
    print(m)

print('#*#*#*#*#*#*#*#')

for k in range(100):
    if k % 8 == 00:
        print(k)
"""

print()

texto = 'Pyhton'
novaString = ''

for letra in texto:
    if letra == 't' or letra == 'h':
        novaString += letra.upper()
    else:
        novaString += letra
print(novaString)