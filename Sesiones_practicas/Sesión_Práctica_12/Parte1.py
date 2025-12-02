import re


def norm_mat(texto):
    condicion = r"(\d{4})[- ]?([A-Z]{3})$"
    match = re.fullmatch(condicion, texto)
    if match:
        digitos = match.group(1)
        letras = match.group(2)
        return f"{digitos}-{letras}"
    else:
        return False