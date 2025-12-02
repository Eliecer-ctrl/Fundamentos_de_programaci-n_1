from parte1 import completar_dni


def matrícula(datos_academicos, dni):
    dic_asignaturas, dic_estudiantes = datos_academicos
    if dni[-1].isdigit():
        dni = completar_dni(dni)
    if dni not in dic_estudiantes:
        return []

    nombre_est, lista_codigos = dic_estudiantes[dni]
    if not lista_codigos:
        return []

    resultado = []
    for codigo in lista_codigos:
        nombre_asig, semestre, creditos = dic_asignaturas[codigo]
        linea = f"{nombre_asig:<35}{semestre:>2}{creditos:>3}"
        resultado.append(linea)

    return resultado