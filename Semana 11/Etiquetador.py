import re

def tagger(text: str, alphabet: str) -> str:
    # ADVERTENCIA: Esta implementación asume que 'alphabet' no contiene caracteres 
    # especiales de regex como '.', '*', '+', '?', '(', ')', etc.
    # Si 'alphabet' contuviera dichos caracteres, la expresión regular fallaría o se comportaría mal.

    # 1. Definir el conjunto de caracteres válidos usando el alfabeto.
    #    No se usa re.escape, asumiendo que el usuario garantiza la seguridad del input.
    alphabet_set = '[' + alphabet + ']+'
    
    # 2. Definir el conjunto de caracteres que NO están en el alfabeto.
    non_alphabet_set = '[^' + alphabet + ']'

    # 3. Construir el patrón usando Lookarounds para la delimitación.
    final_pattern = (
        r'(?<=^|' + non_alphabet_set + r')'  # Lookbehind: Inicio de string (^) o caracter no-alfabeto
        r'(' + alphabet_set + r')'         # Grupo 1: La PALABRA (una o más letras del alfabeto)
        r'(?=$|' + non_alphabet_set + r')'  # Lookahead: Final de string ($) o caracter no-alfabeto
    )
    
    # \1 hace referencia al Grupo 1 (la palabra) en la sustitución.
    return re.sub(final_pattern, r'[target]\1[endtarget]', text)