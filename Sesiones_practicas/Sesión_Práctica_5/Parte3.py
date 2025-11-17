from Parte1 import sumar_elementos
from Parte2 import acumular_precipitaciones


def mes_mas_lluvioso(lista_meses):
    acumuladas = acumular_precipitaciones(lista_meses)
    mesmax = acumuladas[0][0]
    valormax = acumuladas[0][1]
    mesmin = acumuladas[0][0]
    valormin = acumuladas[0][1]
    for mes, total in acumuladas[1:]:
        if total > valormax:
            valormax = total
            mesmax = mes
        elif total < valormin:
            valormin = total
            mesmin = mes
    return (mesmax, mesmin)
# Se tiene una lista de listas conteniendo las mediciones de las precipitaciones pluviométricas de la isla de Gran Canaria durante varios meses de un año. Las mediciones están agrupadas por meses, de forma que cada elemento (lista) contiene el nombre de un mes seguido de las mediciones realizadas cada día durante ese mes ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"). La lista global no está ordenada por meses.
# Escriba una función llamada mes_mas_lluvioso que reciba una lista como la descrita en el apartado anterior y, sin usar las funciones max() y min() de Python, devuelva una tupla con los nombres de los meses con mayor y menor precipitación del año. En caso de que varios meses tengan la misma precipitación (máxima o mínima), se devolverá el primero que aparezca en la lista. Para obtener las precipitaciones acumuladas de cada mes, deberá hacer uso de la función desarrollada en la PARTE 2.