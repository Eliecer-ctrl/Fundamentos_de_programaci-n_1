def contar_mayores(tupla, valor_float):
    contador = 0
    for elemento in tupla:
        if elemento > valor_float:
            contador += 1
    return contador
# Se desarrolla una función que tome como parametro una tupla con valores de tipo float y un valor de tipo float
# Se comprueba cuantos valores son mayores al valor pasado como segundo parametro