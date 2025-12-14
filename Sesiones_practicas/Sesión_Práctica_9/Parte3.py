from Parte1 import escala_de_grises
from Parte2 import negativo


def procesar_imagen(matriz):
    dc = dict()
    grises = escala_de_grises(matriz)
    nega = negativo(matriz)
    dc["original"] = matriz
    dc["grises"] = grises
    dc["negativo"] = nega
    return dc


