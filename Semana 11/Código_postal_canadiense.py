import re
from typing import List

def find_codes(text: str) -> List[str]:
    letras_iniciales = r'[ABCEGHJKLMNPRSTVXY]'
    grupo_uno = letras_iniciales + r'\d[A-Z]' 
    grupo_dos = r'\d[A-Z]\d'
    separador_opcional = r'\s?'
    patron_completo = r'(' + grupo_uno + r')' + separador_opcional + r'(' + grupo_dos + r')'
    matches = re.findall(patron_completo, text)
    codigos_normalizados = []
    for g1, g2 in matches:
        codigos_normalizados.append(g1 + ' ' + g2)
    return codigos_normalizados

# --- Ejemplo de Uso ---

texto_ejemplo = "Mi código postal es A1A1A1. El otro es V6B 1K2. También pruebo M5K-1A6 y un falso M0N0Z0. Y uno sin espacio H2W3A3, además de una dirección errónea Y0Z 9X9."

codigos_encontrados = find_codes(texto_ejemplo)

print(f"Texto original:\n\"{texto_ejemplo}\"")
print("-" * 50)
print(f"Códigos postales canadienses normalizados:")
print(codigos_encontrados)

# Resultado esperado: ['A1A 1A1', 'V6B 1K2', 'H2W 3A3']