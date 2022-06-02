
variavel = 'valor'

def func():
    print(variavel)

# def func2():
#     global variavel
#     variavel = 'Outro valor'
#     print(variavel)

def func2(arg = None):
    arg = arg.replace('v', 'k')
    return arg


func()
outra_variavel = func2(arg=variavel)

print(variavel)