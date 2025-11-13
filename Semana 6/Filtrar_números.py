def filter_numbers(lista, num1, num2):
    lista2 = []
    for numero in lista:
        if num1 <= numero <= num2:
            lista2.append(numero)
    return lista2
# Se desarrolla una funcion que tome como parametro un lista de numeros enteros y dos numero enteros
#  Se comprueba si el numero de la lista esta en el rango entre el num1 y num2, si es así se añade el numero a la nueva lista