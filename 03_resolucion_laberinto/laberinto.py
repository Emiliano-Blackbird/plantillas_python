def resolver_laberinto(laberinto, fila, columna, camino=None):
    if camino is None:
        camino = []

    # Validar posición fuera de límites o pared o ya visitada
    if not (0 <= fila < len(laberinto)) or not (0 <= columna < len(laberinto[0])) or laberinto[fila][columna] == 1 or (fila, columna) in camino:
        return None

    # Agregar posición actual al camino
    camino.append((fila, columna))

    # Caso base: si encontramos la salida
    if laberinto[fila][columna] == 9:
        return camino

    # Movimientos: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for mov in movimientos:
        nueva_fila = fila + mov[0]
        nueva_columna = columna + mov[1]
        resultado = resolver_laberinto(laberinto, nueva_fila, nueva_columna, camino.copy())
        if resultado:
            return resultado

    return None  # No se encontró solución


def imprimir_laberinto(laberinto, camino):
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if (fila, columna) in camino:
                print('*', end=' ')
            else:
                print(laberinto[fila][columna], end=' ')
        print()  # Salto de línea por cada fila


# Ejemplo
laberinto = [
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 9, 0],
    [0, 0, 0, 0, 0]
]

camino_solucion = resolver_laberinto(laberinto, 0, 0)
if camino_solucion:
    print("El camino para salir del laberinto es:")
    imprimir_laberinto(laberinto, camino_solucion)
else:
    print("No se encontró solución")
