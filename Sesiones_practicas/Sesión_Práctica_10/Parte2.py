from Parte1 import completar_dni


def corregir_claves(diccionario):
    claves = list(diccionario.items())
    diccionario.clear()
    for dni, info in claves:
        letra = completar_dni(dni)
    diccionario[letra] = info
# Se tienen un diccionario que la claves del diccionario son números de DNI y los valores asociados son tuplas donde el primer elemento es el nombre del estudiante y el segundo una lista que contiene los códigos de las asignaturas en las que está matriculado.
# Los DNI estan sin letra