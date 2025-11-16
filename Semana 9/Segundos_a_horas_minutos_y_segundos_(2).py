def seconds2hms(num1):
    horas = num1 // 3600
    segundos_restantes = num1 % 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    d = {'Horas': horas, 'Minutos': minutos, 'Segundos': segundos}
    return d
# Se desarrolla una funcion que tome como parametro un numero que representa una cantidad de segundos
# Se calcula las horas, minutos y segundos y lo devuelve en un diccionario