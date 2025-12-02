import re

def validate_formula(formula):
    pattern = r"^(([A-Z][a-z]?)([1-9]\d?)?)+$"
    if re.fullmatch(pattern, formula):
        return True
    else:
        return False
# ^ --> Inicio de lacadena    $ --> Final de línea
# (   )--> Grupo de captura   +--> una o más repeticiones del elemento anterior 
# [A-Z] -->  letras mayúsculas  [a-z] --> Letras en minúsculas que realmente no hace falta ya que las formulas van a estar en mayúsculas
# ? --> cero o una mas ocurrencias [1-9]--> primer dígito del subíndice