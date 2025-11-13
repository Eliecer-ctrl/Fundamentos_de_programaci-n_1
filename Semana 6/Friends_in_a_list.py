def is_friend(nombres, name):
    for nombre in nombres:
        if name == nombre:
            return True
    return False
# Se desarrolla una función que tome como parametro una lista de nombres y un nombre.
# Sie el nombre se encuentra dentro de la lista devuelve True sino False.