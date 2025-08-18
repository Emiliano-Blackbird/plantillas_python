def verificar_acceso_entorno(funcion):
    def wrapper(*args, **kwargs):
        entorno = obtener_entorno()
        if entorno == "produccion":
            print("Acceso permitido en entorno de producción.")
            return funcion(*args, **kwargs)
        else:
            print("Acceso denegado. Entorno no permitido.")
    return wrapper


@verificar_acceso_entorno
def subir_archivo(documento):
    print(f"Subiendo archivo {documento}")


@verificar_acceso_entorno
def eliminar_archivo(documento):
    print(f"Eliminando archivo {documento}")


# Entorno de producción
print("Entorno de producción:")


def obtener_entorno():
    return "produccion"


subir_archivo("documento A")
eliminar_archivo("documento B")


# Entorno de desarrollo
print("\nEntorno de desarrollo:")


def obtener_entorno():
    return "desarrollo"


subir_archivo("documento A")
eliminar_archivo("documento B")
