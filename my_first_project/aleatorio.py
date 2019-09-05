import random

def criarLista(tam):
    retorno = []
    for i in range(tam):
        retorno.append(random.randint(0,100))
    return retorno