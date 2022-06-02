"""
Funcoes - def em pyhton (parte1)
"""

def saudacao(msg, nome):
    # print('Jesus!')
    print(msg, nome)
    msg = msg.replace('a', '3')
    print(msg)

saudacao('Ola', 'Jesus')