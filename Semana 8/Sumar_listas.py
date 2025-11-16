def sum_lists(lista1, lista2):
    nueva = []
    lista_larga = max(len(lista1), len(lista2))
    for numero in range(lista_larga):
        if numero < len(lista1):
            num1 = lista1[numero]
        else:
            num1 = 0
        if numero < len(lista2):
            num2 = lista2[numero]
        else:
            num2 = 0
        nueva.append(num1 + num2)
    return nueva
# Se desarrolla una función que tome como parametro dos lista
# Se crea una nueva lista y una variable que se le asigne la longitud max de una de las dos listas
# Se inicia un bucle for que itera desde el indice 0 hasta la 

# Si llamas a la función con: sum_lists([10, 20], [5, 1, 4])
#    lista_larga se calcula como max(2, 3), por lo que es 3.
#    El bucle for itera con numero en 0, 1, 2.