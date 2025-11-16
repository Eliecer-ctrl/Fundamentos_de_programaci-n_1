def pass_highers(lista1, num1):
    nueva = []
    for lista in lista1:
        lista2 = []
        for elemento in lista:
            if elemento >= num1:
                lista2.append(elemento)
        nueva.append(lista2)
    return nueva
# Se desarrolla una función que tome como parametro una lista de listas y un número
# Devuelve una nueva lista de lista con los numero mayores que el nº pasado como segundo parametro