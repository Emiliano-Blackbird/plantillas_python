usuario_registrado = {
    "usuario1": {
        "nombre_completo": "Juan Pérez",
        "email": "juan.perez@example.com",
        "password": "password123"
    },
    "usuario2": {
        "nombre_completo": "María López",
        "email": "maria.lopez@example.com",
        "password": "password456"
    },
    "usuario3": {
        "nombre_completo": "Carlos García",
        "email": "carlos.garcia@example.com",
        "password": "password789"
    }
}


def verificar_inicio_sesion(funcion):
    def wrapper(nombre_usuario, password):
        if nombre_usuario in usuario_registrado and usuario_registrado[nombre_usuario] ["password"] == password:
            print(f"Bienvenido {nombre_usuario}!")
            usuario_info = usuario_registrado[nombre_usuario]
            return funcion(usuario_info)
    return wrapper


@verificar_inicio_sesion
def informacion_usuario(usuario_info):
    print("Información del usuario:")
    print("Nombre completo: ", usuario_info["nombre_completo"])
    print("Correo electrónico: ", usuario_info["email"])


informacion_usuario("usuario1", "password123")
informacion_usuario("usuario2", "password456")
