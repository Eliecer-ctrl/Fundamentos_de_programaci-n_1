from Parte2 import días


def validar_fecha(fecha):
    día = int(fecha[0:2])
    mes = int(fecha[3:5])
    año = int(fecha[6:])
    if días(mes, año) == -1 or día <= 0:
        return False
    elif días(mes, año) >= día:
        return True
    else:
        return False
