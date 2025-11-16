def pack(lista1, lista2):
    lista3 = []
    for numero in range(len(lista1)):
        num1 = lista1[numero]
        num2 = lista2[numero]
        total = (num1, num2)
        lista3.append(total)
    return lista3
# Se desarrolla una función que tome como parametros dos listas.
# Y se quiere que devuelva una nueva lista de tuplascon los numero que se encuentre en la misma posición.