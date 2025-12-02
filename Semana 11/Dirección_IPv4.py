import re


# Escriba aquí su código
def validate_ips(lista):
    octeto = r'(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)'
    ipv4 = r'^' + octeto + r'\.' + octeto + r'\.' + octeto + r'\.' + octeto + r'$'
    validas = []
    invalidas = []
    for ip in lista:
        if re.fullmatch(ipv4, ip):
            validas.append(ip)
        else:
            invalidas.append(ip)
    return validas, invalidas
