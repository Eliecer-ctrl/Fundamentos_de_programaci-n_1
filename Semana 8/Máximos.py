def maxs(lista1, lista2):
    nueva = []
    lista_larga = max(len(lista1), len(lista2))
    for numero in range(lista_larga):
        if numero < len(lista1):
            num1 = lista1[numero]
        else:
            num1 = -1
        if numero < len(lista2):
            num2 = lista2[numero]
        else:
            num2 = -1
        nueva.append(max(num1, num2))
    return nueva
# Se desarrolla una funcion que tome como parametro dos listas
# se devuelve una nueva lista que compara que elemento es el mas grande que se encuentre en la misma posición
# Si no hay elemento se compara con el -1