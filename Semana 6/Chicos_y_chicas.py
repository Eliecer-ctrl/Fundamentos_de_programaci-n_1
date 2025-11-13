def filter_names(lista1, num):
    lista = []
    if num % 2 == 0:
        for nombre in range(0, len(lista1), 2):
            lista.append(lista1[nombre])
    else:
        for i in range(1, len(lista1), 2):
            lista.append(lista1[i])
    return lista
#Se tienen listas conteniendo nombres de chicos y chicas de forma que en los índices pares siempre hay nombres de chicas y, en los impares, de chicos.

#Desarrolle una función llamada filter_names, que tome por parámetro una lista como las descritas y un número entero.

#Si el número pasado como segundo parámetro es par, la función debe devolver una nueva lista con todos los nombres de chicas en el mismo orden que en la lista original.

#Si el número pasado como segundo parámetro es impar, la función debe devolver una nueva lista con todos los nombres de chicos en el mismo orden que en la lista original.