def valores_en_rango(lista, num1, num2):
    conjunto = {}
    for elemento in lista:
        if num1 <= elemento <= num2:
            conjunto.add(elemento)
    return conjunto
# Se desarrolla una funcion que tome como parametro una lista y dos numeros
# Devuelve conjunto con los valores de la lista comprendidos entre el num1 y num2