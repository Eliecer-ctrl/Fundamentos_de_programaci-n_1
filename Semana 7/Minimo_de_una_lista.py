def list_min(lista):
    if len(lista) == 0:
        return lista[0]
    resto = list_min(lista[1:])
    if lista[0] < resto:
        return lista[0]
    else:
        return resto
# Se desarrolla una funcion que tome como parametro una lista, si la lista tiene un solo elemento devuelve ese elemento (Caso base)
# Lugo con recursividad se comprueba se comprueba el minimo de la lista