from Parte1 import es_bisiesto


def días(mes, año):
    if mes > 12 or mes < 1 or año <= 0:
        return -1
    if mes == 2:
        if es_bisiesto(año) == 1 or es_bisiesto(año) == 2:
            return 29
        elif es_bisiesto(año) == 0:
            return 28
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7:
        return 31
    elif mes == 8 or mes == 10 or mes == 12:
        return 31
    else:
        return 30
