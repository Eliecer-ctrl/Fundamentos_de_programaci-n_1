def filter_values(d, num1, num2):
    nuevo = {}
    for key, value in d.items():
        if num1 <= value <= num2:
            nuevo[key] = value
    return nuevo
# Se desarrolla una funcion que tome como parametro un diccionario y dos numeros enteros
# Devuelve un nuevo diccionario con los valores comprendido entre el num1 y num2