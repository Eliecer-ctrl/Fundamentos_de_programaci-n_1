def filter_names(nombres, letra):
    if not nombres:
        return []

    primero = nombres[0]
    resto = filter_names(nombres[1:], letra)
    if primero.startswith(letra):
        return [primero] + resto
    else:
        return resto
# Se desarrolla una función que tome como parametro una lista de nombres una letra 
# El caso baso si no hay lista devuelve una lista vacía
# Cogemos como referencia el primer nombre y si empieza con la letra se crea una lista con este primer nombre + el recursivo