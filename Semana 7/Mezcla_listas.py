def merge(lista1, lista2):
    if not lista1:
        return lista2
    if not lista2:
        return lista1
    if lista1[0] <= lista2[0]:
        return [lista1[0]] + merge(lista1[1:], lista2)
    else:
        return [lista2[0]] + merge(lista1, lista2[1:])
# Se desarrolla una funcion que tome como parametro dos listas 
# El caso base: si no hay lista1 devuelve lista2 y al revés
# Si el primer elemento de la lista1 es menor igual que el primer elemento de la lista2: ç
# Devuelve una lista con el primer elemento de la lista1 + el resto
