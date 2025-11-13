def capital(capital_inicial, interes, numero_de_periodos):
    final = capital_inicial * (1 + interes) ** numero_de_periodos
    return final
# Se desarrolla una función que tome como parametro tres numero y se calcula la capital final.