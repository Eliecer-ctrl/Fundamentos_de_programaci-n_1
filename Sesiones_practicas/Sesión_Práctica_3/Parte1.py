def es_bisiesto(año):
    if año % 4 == 0 or año % 100 != 0:
        return 2
    elif año % 400 == 0:
        return 1
    else:
        return 0