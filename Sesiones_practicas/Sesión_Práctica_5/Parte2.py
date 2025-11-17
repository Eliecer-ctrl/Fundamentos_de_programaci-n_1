from Parte1 import sumar_elementos


def acumular_precipitaciones(listas_de_listas):
    resultado = []
    for mes_datos in listas_de_listas:
        mes = mes_datos[0]
        mediciones = mes_datos[1:]
        total = sumar_elementos(mediciones)
        resultado.append((mes, total))
    return resultado
# Se tiene una lista de listas conteniendo las mediciones de las precipitaciones pluviométricas de la isla de Gran Canaria durante varios meses de un año. Las mediciones están agrupadas por meses, de forma que cada elemento (lista) contiene el nombre de un mes seguido de las mediciones realizadas cada día durante ese mes ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"). La lista global no está ordenada por meses.
# Escriba una función llamada acumular_precipitaciones a al que se le pase una lista de listas como la descrita en el apartado anterior y devuelva una lista de tuplas con el mismo número de elementos. Cada tupla tendrá como primer elemento el nombre del mes de la lista que ocupa la misma posición en la lista original y como segundo elemento la suma de las precipitaciones correspondientes a ese mes. Para calcular la suma de las precipitaciones se usará la función desarrollada en la PARTE 1.