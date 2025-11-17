from Parte2 import expand
from utilities import row_to_str, mat_to_str


# Escriba aquí la función solicitada
def combine(tupla1, tupla2):
    matriz1 = expand(tupla1, tupla2)
    matriz2 = expand(tupla2, tupla1)
    corta = min(len(matriz1), len(matriz2))
    lista_final = []
    for i in range(corta):
        fila = []
        for j in range(corta):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        lista_final.append(fila)
    return lista_final
