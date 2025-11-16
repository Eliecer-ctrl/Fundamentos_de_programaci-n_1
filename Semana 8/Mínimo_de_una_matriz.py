def min_of_matrix(matriz_tuplas):
    minimo_actual = matriz_tuplas[0][0]
    for fila in matriz_tuplas:
        for numero in fila:
            if numero < minimo_actual:
                minimo_actual = numero
    return minimo_actual
# Se desarrolla una funcion que tome como parametro una matriz (tupla)
# Devuelve el minimo de una matriz