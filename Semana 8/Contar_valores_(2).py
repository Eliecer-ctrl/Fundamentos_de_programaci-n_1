def count_values(lista1, lista2):
    for i in range(len(lista2)):
        contar = lista1.count(lista2[i])
        lista2[i] = (lista2[i], contar)
    return lista2
# Se desarrolla una funcion que tome como parametro dos listas
# Y devuelve la lista2 modificada. Cada elemento de la lista2 se sustituye por una tupla donde se esncuentra el numero de la lista2 y el nº de veces que aparece en la lista1        