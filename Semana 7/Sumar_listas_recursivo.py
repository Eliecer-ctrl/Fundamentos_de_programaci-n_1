def sum_lists(lista1, lista2):
    if not lista1:
        return []
    referencia = lista1[0]+ lista2[0]
    resto = sum_lists(lista1[1:], lista2[1:])
    return [referencia] + resto
# Se desarrolla una función que tome como parametro dos listas de numeros enteros
# Caso base sin no hay lista1 devuelve una lista vacía
# Se suma los primeros elementos de las listas y el resto con recursividad