# Lista inicial
lista_nombres = ["Pérez, Juan", "García, Ana", "López, Carlos", "Martínez, Luis", "Sánchez, Laura"]

# Transformo "Apellido, Nombre" -> "Nombre Apellido"
lista_nombres_transformados = [
    (lambda nombre_original: nombre_original.split(", ")[1] + " " + nombre_original.split(", ")[0])
    (nombre_original)
    for nombre_original in lista_nombres
]
print("Nombres transformados:", lista_nombres_transformados)


# Filtro la lista con una función para incluir solo nombres
# que contengan al menos dos vocales y una longitud mayor a 10 caracteres
def filtrar_nombres(lista_nombres_transformados):
    def nombre_valido(nombre):
        vocales = "aeiou"
        return sum(1 for letra in nombre if letra.lower() in vocales) >= 2 and len(nombre) > 10
    return [nombre for nombre in lista_nombres_transformados if nombre_valido(nombre)]


# Uso mi función directamente
lista_nombres_filtrados = filtrar_nombres(lista_nombres_transformados)
print("Nombres filtrados:", lista_nombres_filtrados)
