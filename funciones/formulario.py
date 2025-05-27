# Este script valida un formulario simple
# con parametros de nombre, email y teléfono.

def validar_formulario(nombre, email, telefono):
    if len(nombre) < 3:
        return False

    if "@" not in email or "." not in email:
        return False

    if len(telefono) != 9 or not telefono.isdigit():
        return False

    return True


nombre = input("Ingrese su nombre: ")
email = input("Ingrese su correo electrónico: ")
telefono = input("Ingrese su número de teléfono: ")

valido = validar_formulario(nombre, email, telefono)

if valido:
    print("Formulario enviado correctamente.")
else:
    print("Error: El formulario contiene errores.")
