def count_values(lista1, lista2):
    nueva = []
    for numero in lista2:
        contar = lista1.count(numero)
        nueva.append(contar)
    return nueva
# Se desarrolla un función que tome como parametro dos listas
# Se crea una nueva lista y se agrega el numero de veces que aparecen los numeros de la lista2 en la lista1
# .count --> cuenta el numero en la lista