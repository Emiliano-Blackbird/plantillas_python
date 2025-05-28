def contar_apariciones(filename, palabras_comunes):
    """ Cuenta las apariciones de palabras
    comunes en un archivo de texto."""

    with open(filename, 'r') as file:
        texto = file.read()
        count = texto.count(palabras_comunes)
        return count


filename = "uso_de_archivos_y_excepciones/texto.txt"
palabra_a_contar = "Python"

ocurrencias = contar_apariciones(filename, palabra_a_contar)

print(f"La palabra '{palabra_a_contar}' aparece {ocurrencias} veces en el archivo de texto.")
