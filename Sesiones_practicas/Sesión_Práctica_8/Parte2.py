from Parte1 import mcd


def normalizar(tupla):
    if tupla[0] >= tupla[1]:
        m = mcd(tupla[0], tupla[1])
        a = tupla[0] // m
        b = tupla[1] // m
        return(a, b)
    else:
        m = mcd(tupla[1], tupla[0])
        a = tupla[0] // m
        b = tupla[1] // m
        return(a, b)
# Se desarrolla una función que tome como parametro una tupla con dos numeros que representa el numerador y el denominador
# Se comprueba que el numerador siempre sea el más grande 

