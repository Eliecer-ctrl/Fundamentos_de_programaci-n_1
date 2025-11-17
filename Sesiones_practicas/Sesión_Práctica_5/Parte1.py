def sumar_elementos(lista):
    suma = 0.0
    for elemento in lista:
        if type(elemento) is int:
            suma += elemento
        elif type(elemento) is float:
            suma += elemento
    return suma
# Se desarrolla una función que tome como parametro una lista
# Si los elemtos de la lista son de tipo int o float se suma a la variable suma
# Devuelve un valor de tipo float