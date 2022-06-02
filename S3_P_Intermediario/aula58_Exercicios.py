# Atividade 1

def funcao1():
    return 'Jesus!'


def funcao2(funcao):
    return funcao()

executando = funcao2(funcao1)
print(executando)



# Atividade 2

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando2 = mestre(fala_oi, 'Jesus')
executando3 = mestre(saudacao, 'Victor', saudacao = 'Bom dia')
print(executando2)
print(executando3)