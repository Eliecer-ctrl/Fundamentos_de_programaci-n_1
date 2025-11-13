def transform_date(fecha):
    dia, mes, año = fecha.split('-')
    cadena = f"{mes}-{dia}-{año}"
    return cadena
# Se desarrolla una función que tome como parametro una string y se intercambia el dia por el mes separando en corcheetes dia, mes y año y luego devolver una cadena.