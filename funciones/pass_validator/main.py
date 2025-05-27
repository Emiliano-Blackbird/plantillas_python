# Solicitar una contraseña
# Validar la contraseña
# Si contraseña no es valida, solicitarla de nuevo

import validator
import generator


def solicitar_password():
    password = input("Introduce una contraseña: ")
    valida = validator.validar_password(password)

    if valida:
        print("Contraseña válida y segura.")
    else:
        print("La contraseña no es segura.")
        sugerencia = generator.generar_password_segura(9)
        print("Sugerencia de contraseña segura:", sugerencia)


# Ejemplo de uso
solicitar_password()
