def posición(nombres, lon_min):
    for i, nombre in enumerate(nombres):
        if len(nombre) >= lon_min:
            return(i, len(nombre))

    return None
# Se desarrolla una funcion que tome como parametros una secuencia no vacía de nombres y un numero
# Y devuelve una tupla  una tupla con el índice de aparición y número de caracteres del primer nombre la secuencia de nombres pasado como primer parámetro cuyo número de caracteres sea igual o mayor que el del valor pasado como segundo parámetro