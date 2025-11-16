def emparejados(conj1, conj2, conj3):
    en_dos = (conj1 & conj2) | (conj1 & conj3) | (conj2 & conj3)
    en_tres = conj1 & conj2 & conj3
    diferencia = en_dos - en_tres
    return diferencia
# Se desarrolla una funcion que tome como parametro tres conjuntos {}{}{}
# Primero se calcula la intersección en dos y la unión
# Luego se calcula la intersección en lostres 
# Por último la diferencia