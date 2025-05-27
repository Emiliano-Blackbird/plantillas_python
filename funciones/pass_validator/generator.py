import random
import string


def generar_password_segura(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_caracteres_especiales=True):
    """
    Genera una contraseña segura basada en los parámetros especificados.
    """
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    password = ''.join(random.choice(caracteres) for i in range(longitud))
    return password
