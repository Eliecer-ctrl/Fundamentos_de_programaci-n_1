from Parte1 import make_list


# Escriba aquí la función solicitada
def expand(tupla1, tupla2):
    lista = []
    for x in tupla1:
        fila = make_list(tupla2, x)
        lista.append(fila)
    return lista