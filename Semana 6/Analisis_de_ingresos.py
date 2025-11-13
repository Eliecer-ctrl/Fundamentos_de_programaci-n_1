def best_semester(lista1):
    semestre1 = lista1[:6]
    semestre2 = lista1[6:]
    if sum(semestre1) > sum(semestre2):
        return 1
    if sum(semestre1) < sum(semestre2):
        return 2
    else:
        return 0
# Se tienen listas conteniendo cada una 12 números que representan los beneficios mensuales de una cierta inversión durante un año natural.

#Desarrolle una función llamada best_semester, que tome por parámetro una lista como las descritas y devuelva un 1 si se han tenido más beneficios en la primera mitad del año y un 2 si se han tenido más beneficios en la segunda mitad del año. En caso de igualdad, debe devolver un cero