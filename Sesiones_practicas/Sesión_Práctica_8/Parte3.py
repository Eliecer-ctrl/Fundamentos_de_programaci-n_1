from Parte2 import normalizar


def lista_normalizadas(lista):
    if lista == []:
        return []
    else:
        return ([normalizar(lista[0])] + lista_normalizadas(lista[1:]))
    


from Parte2 import normalizar


def lista_normalizadas(lista):
    if lista == []:
        return []
    else:
        primero = normalizar(lista[0])
        resto = lista_normalizadas(lista[1:])
        return ([primero] + resto)