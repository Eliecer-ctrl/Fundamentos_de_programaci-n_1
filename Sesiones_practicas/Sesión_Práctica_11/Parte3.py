from parte1 import validate_formula
from parte2 import mol_weight

def find_formulas(text):
    tokens = text.split()
    results = []

    for tok in tokens:
        if validate_formula(tok):
            pm = mol_weight(tok)

            # rellenar con puntos hasta 8 caracteres
            puntos = 8 - len(tok)
            if puntos < 0:
                puntos = 0
            left = tok + "." * puntos

            # convertir pm a string con exactamente 2 decimales
            pm_int = int(pm)
            pm_dec = int(round((pm - pm_int) * 100))
            if pm_dec == 100:
                pm_int += 1
                pm_dec = 0
            # formar string con dos decimales
            pm_str = str(pm_int) + "." + (str(pm_dec) if pm_dec >= 10 else "0" + str(pm_dec))

            # agregar espacios a la izquierda si es menor que 6 caracteres
            while len(pm_str) < 6:
                pm_str = " " + pm_str

            results.append(left + "PM: " + pm_str)

    return results
