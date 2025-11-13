def sum_ints(tupla):
    suma = 0
    for elemento in tupla:
        if type(elemento) == int:
            suma += elemento
    return suma
# Se desarrolla una tupla con diferentes valores y se devuelve la suma de los valores de tipo int