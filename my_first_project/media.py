#media, mediana, moda

def media (lista):
    media = sum(lista)/float(len(lista))
    return media

def mediana (lista):
    list.sort(lista)
    if(len(lista)%2==0):
        return (lista[int(len(lista)/2)]+lista[int((len(lista)/2)+1)])/2
    else:
        return lista[int((len(lista)+1)/2)]

def moda (lista):
    list.sort(lista)
    mapa = {}
    for valor in lista:
        if(valor not in mapa):
            mapa[valor] = 1
        else:
            mapa[valor] +=1
    
    maior_lista = max(mapa.values())
    if(maior_lista>1):
        for i in mapa:
            if mapa[i] == maior_lista:
                moda = i
                break
        return moda
    else:
        return "Não tem moda"
