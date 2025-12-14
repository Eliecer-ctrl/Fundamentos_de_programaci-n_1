from Parte1 import norm_mat

def check_car_data(texto):
    lista = texto.split(';')
    if len(lista) != 6:
        return texto
    normalizar = norm_mat(lista[0])
    if lista[3] != "combustión" or lista[3] != "híbrido" or lista[3] != "eléctrico":
        return texto
    return lista