import chemistry
import re

def mol_weight(formula):
    total = 0.0

    # Patrón para extraer (elemento, número)
    pattern = r"([A-Z][a-z]?)([1-9][0-9]?)?"

    # findall devuelve lista de tuplas (elemento, numero)
    for elem, num in re.findall(pattern, formula):
        cantidad = int(num) if num else 1
        total += chemistry.atom_weight(elem) * cantidad

    return total
