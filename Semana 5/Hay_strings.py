def contains_strs(tupla):
    for elemento in tupla:
        if type(elemento) == str:
            return True
    return False
# Se desarrolla una tupla con elemnetos de diferentes tipos y se comprueba si algun elemento de tipo str y devuelve True si no hay devuelve False
