'''

Trabajas en colegio y estas encargado de
mantener un seguimiento de las notas de
los estudiantes de un clase. En tu base de datos
tienes una lista con los nombres de los estudiantes
y para cada estudiante debes guardar sus notas provenientes
de deberes, exámenes y proyectos.

También necesitas calcular la nota media de cada
estudiante y la nota media de la clase al completo.

Pista: Para resolver este problema puedes usar una
lista anidada donde guardes las notas para cada
estudiante. Entonces puedes usar un bucle para recorrer
la lista de listas y calcular la nota media de cada
estudiante. También puedes usar otro bucle para calcular
la nota media de toda la clase.

'''

# SOLUCION USANDO DOS BUCLES FOR
# LA MEDIA INDIVIDUAL Y LA DE LA CLASE

# --- lista con los nombres de los alumnos
estudiantes = ["Juan", "María", "Pedro"]

# --- Creo la base de datos con las notas
database = []

# --- Pido los datos de las notas para cada estudiante
for estudiante in estudiantes:
    notas = []
    print(f"Ingrese las notas de {estudiante}")
    # pido la nota de deberes
    deberes = float(input("Notas de deberes: "))
    # la añado a la lista de notas
    notas.append(deberes)
    # pido la nota de examenes
    examenes = float(input("Notas de examenes: "))
    # la añado a la lista de notas
    notas.append(examenes)
    # pido la nota de proyectos
    proyectos = float(input("Notas de proyectos: "))
    # la añado a la lista de notas
    notas.append(proyectos)

    # añadir a la database el nombre y la lista de notas del alumno
    database.append([estudiante, notas])


'''
database = [["Juan", [6.4,7.0,9.1]],
            ["María", [8.2, 9.8, 6.5]],
            ["Pedro", [7.1, 8.4, 5.2]]
            ]
'''

print("  ")
print("  ")
print("Calculando medias individuales y totales...")
print("  ")
print("  ")

# --- Calcular la nota media de cada estudiante
sum_media = 0
for data in database:
    # extraemos el nombre del estudiante
    nombre = data[0]
    # extraemos la lista de notas del estudiante
    notas = data[1]
    # calculamos la media del estudiante
    media = sum(notas) / len(notas)
    # imprimimos por pantalla la media de cada estudiante
    print(f"La media de {nombre} es {media:.2f}")


# --- Calcular la nota media de toda la clase
total_notas = 0
num_notas = 0
for data in database:
    # extraemos la lista de notas del estudiante
    notas = data[1]
    # sumar todas las notas
    total_notas = total_notas + sum(notas)
    # numero de notas sumadas
    num_notas = num_notas + len(notas)

# calculamos la media de toda la clase
media_clase = total_notas/num_notas
# imprimimos la media de la clase
print("La media de la clase es {:.2f}".format(media_clase))
