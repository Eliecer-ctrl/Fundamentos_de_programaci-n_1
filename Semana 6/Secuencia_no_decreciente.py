def no_decreasing(lista1):
    if len(lista1) == 1:
        return True

    for elemento in range(1, len(lista1)):
        if lista1[elemento] < lista1[elemento - 1]:
            return False
    return True
#Desarrolle una función llamada no_decreasing, que tome como parámetro una lista de números enteros y devuelva True si es una lista no decreciente y False si no lo es. Una lista no decreciente es una en la que cada valor, excepto el primero, es mayor o igual que el valor que está en la posición anterior. Una lista con un solo elemento es no decreciente.