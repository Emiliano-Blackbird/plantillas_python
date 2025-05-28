"""
LISTA DE TAREAS
Crea una clase "ListaTareas" que contenga una lista de tareas pendientes.
Implementa métodos para agregar una tarea,
marcar una tarea como completada y mostrar todas las tareas
"""


class ListaTareas:
    # Constructor de la clase, inicializa la lista de tareas vacía
    def __init__(self):
        self.tareas = []

    # Método para agregar una nueva tarea a la lista
    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})

    # Método para marcar una tarea como completada
    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True

    # Método para mostrar todas las tareas en la lista
    def mostrar_tareas(self):
        for indice, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{indice + 1}. {tarea['tarea']} - {estado}")


# Ejemplo de uso
lista_tareas = ListaTareas()  # Crear una instancia de ListaTareas
lista_tareas.agregar_tarea("Hacer la compra")  # Agregar una tarea a la lista
lista_tareas.agregar_tarea("Estudiar programación")  # Agregar otra tarea
lista_tareas.marcar_completada(1)  # Marcar la segunda tarea como completada
lista_tareas.mostrar_tareas()  # Mostrar todas las tareas con su estado
