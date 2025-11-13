def product(a, b):
    if b == 1:
        return a
    elif b % 2 == 0:
        return product(a + a, b // 2)
    else:
        return a + product(a + a, b // 2)
# Se desarrolla una función que toem como parametro dos numeros enteros 
# Y se multiplica usando recursividad