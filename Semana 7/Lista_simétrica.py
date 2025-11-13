def is_sym(lista):
    if len(lista) < 2:
        return True
    if lista[0] == lista[-1]:
        return is_sym(lista[1:-1])
    else:
        return False
# Sedesarrolla una función que toem como parametro una lista 
# Caso base si la longitud de la lista es menor que 2 devuelve True
# Se comprueba si la lista es simetrica o no, usando recursividad