def caracteres_iguales(texto1, texto2):
    if not texto1 or not texto2:
        return []

    if texto1[0] == texto2[0]:
        comparacion = [1]
    else:
        comparacion = [0]

    resto = caracteres_iguales(texto1[1:], texto2[1:])
    return comparacion + resto
# Se desarrolla una funcion que tome como parametro dos listas
# Caso base si no hay lista1 o lista2 devuelve una lista vacía
# Si las letras de la misma posición coincide devuelve un 1 sino un 0 
# Se comprueba el resto con recursividad