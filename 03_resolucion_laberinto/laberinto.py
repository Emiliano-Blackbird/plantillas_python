# FUNCION PARA RESOLVER LABERINTO
def resolver_laberinto(laberinto, fila, columna, camino=None):
    """
    Busca un camino desde una posición inicial (fila, columna) hasta la salida (valor 9)
    en un laberinto representado como una matriz.

    Parámetros:
    - laberinto: lista de listas con enteros (0 = camino libre, 1 = pared, 9 = salida)
    - fila: posición inicial en filas
    - columna: posición inicial en columnas
    - camino: lista de coordenadas visitadas (opcional, se inicializa vacío en la primera llamada)

    Retorna:
    - Lista de coordenadas que forman el camino desde el inicio hasta la salida
    - None si no hay solución
    """

    # Crea el camino
    if camino is None:
        camino = []

    # Comprobamos si la posición es inválida:
    # 1. Está fuera de los límites del laberinto
    # 2. Es una pared (valor 1)
    # 3. Ya visitamos esa casilla (para evitar bucles infinitos)
    if not (0 <= fila < len(laberinto)) or not (0 <= columna < len(laberinto[0])) \
       or laberinto[fila][columna] == 1 or (fila, columna) in camino:
        return None  # Posición no válida → no seguimos por aquí

    # Marcamos la posición actual como parte del camino recorrido
    camino.append((fila, columna))

    # Caso base: si llegamos a la salida (valor 9), devuelve el camino encontrado
    if laberinto[fila][columna] == 9:
        return camino

    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Recorremos cada movimiento posible
    for mov in movimientos:
        nueva_fila = fila + mov[0]       # Calculamos la nueva fila
        nueva_columna = columna + mov[1] # Calculamos la nueva columna

        # Llamada recursiva para seguir explorando desde la nueva posición
        # Usamos camino.copy() para no modificar el camino original en otras ramas
        resultado = resolver_laberinto(laberinto, nueva_fila, nueva_columna, camino.copy())

        # Si encontramos un camino válido, lo devolvemos
        if resultado:
            return resultado

    # Si probamos todas las direcciones y no encontramos salida, devolvemos None
    return None


# FUNCION PARA IMPRIMIR LABERINTO
def imprimir_laberinto(laberinto, camino):
    """
    Muestra el laberinto por pantalla.
    - Las coordenadas que forman parte del camino se marcan con '*'.
    - Los valores originales se muestran para paredes y espacios libres.
    """
    for fila in range(len(laberinto)):  # Recorremos cada fila
        for columna in range(len(laberinto[0])):  # Recorremos cada columna
            if (fila, columna) in camino:  # Si la celda está en el camino
                print('*', end=' ')  # Imprimimos un asterisco
            else:
                print(laberinto[fila][columna], end=' ')  # Mostramos el valor original
        print()  # Salto de línea al final de cada fila


# LABERINTO GRANDE
# 0 = camino libre
# 1 = pared
# 9 = salida
laberinto = [
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 9],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# EJECUCIÓN DEL PROGRAMA
# Intentamos resolver el laberinto desde la posición inicial (0,0)
camino_solucion = resolver_laberinto(laberinto, 0, 0)

# Si encontramos un camino, lo mostramos
if camino_solucion:
    print("El camino para salir del laberinto es:")
    imprimir_laberinto(laberinto, camino_solucion)
else:
    print("No se encontró solución")
