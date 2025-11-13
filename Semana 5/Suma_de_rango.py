def sum_numbers(num1, num2):
    sumador = 0
    for numero in range(num1 + 1, num2):
        if num1 > num2:
            return 0
        else:
            sumador += numero
    return sumador
# Se desarrolla una función que tome como paramtro dos numeros 
# y se devuelve la suma en el rango (num1 + 1, num2)