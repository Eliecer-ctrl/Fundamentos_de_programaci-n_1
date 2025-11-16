def join_lists(lista1, lista2):
    corta = min(len(lista1), len((lista2)))
    d = {}
    for i in range(corta):
        clave = lista1[i]
        valor = lista2[i]
        d[clave] = valor
    return d
# Se desarrolla una función que tome como parametro dos listas 
# La primera lista representa las claves y la segunda los valores