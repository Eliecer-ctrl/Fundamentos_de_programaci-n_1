def seconds2hms(segundos2):
    horas = segundos2 // 3600
    segundos_restantes = segundos2 % 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    return horas, minutos, segundos
# Se desarrolla una función que tome como parametro un num que representa los segundos restantes
# Y se devuelve las horas, minutos y segundos