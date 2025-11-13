def longest(lista):
    largo = 0
    for nombre in lista:
        if len(nombre) > largo:
            largo = len(nombre)
    return largo
# Se desarrolle una función que tome como parametro un lista de nombres 
# Y se compara las longitudes de los nombres y devuelve el mas largo