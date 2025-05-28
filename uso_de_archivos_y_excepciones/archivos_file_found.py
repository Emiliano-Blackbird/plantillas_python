filenames = ["uso_de_archivos_y_excepciones/archivo1.txt",
             "uso_de_archivos_y_excepciones/archivo2.txt"]

for filename in filenames:
    try:
        with open(filename, 'r') as file:
            print(f"Contenido de {filename}:")
            contenido = file.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no fue encontrado.")
