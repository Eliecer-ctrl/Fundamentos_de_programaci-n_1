def factorial(num1):
    factorial = 1
    for numero in range(num1 + 1):
        if numero == 0:
            return 1
        else:
            factorial *= numero
    return factorial
# Se desarrolla una funcón que tome como parametro un numero 
# Y se calcula el factorial de es numero es por ello que se usa el rango 
