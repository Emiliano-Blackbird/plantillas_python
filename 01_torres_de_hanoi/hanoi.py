"""
Este script resuelve el problema de las Torres de Hanoi usando recursión.
Devuelve la lista de movimientos paso a paso.
"""


def mover_disco_tuple(desde: str, hacia: str, disco: int) -> tuple:
    return (disco, desde, hacia)


def torres_de_hanoi_movimientos(n: int, origen: str, destino: str, auxiliar: str, movimientos=None):
    if movimientos is None:
        movimientos = []

    if n <= 0:
        return movimientos

    if n == 1:
        movimientos.append(mover_disco_tuple(origen, destino, 1))
        return movimientos

    # Mueve n-1 discos al auxiliar
    torres_de_hanoi_movimientos(n - 1, origen, auxiliar, destino, movimientos)

    # Mueve el disco más grande al destino
    movimientos.append(mover_disco_tuple(origen, destino, n))

    # Mueve los n-1 discos del auxiliar al destino
    torres_de_hanoi_movimientos(n - 1, auxiliar, destino, origen, movimientos)

    return movimientos


if __name__ == "__main__":
    # Número de discos
    discos = 3

    # Nombres de las torres
    torre1, torre2, torre3 = "Torre 1", "Torre 2", "Torre 3"

    # Obtener movimientos
    movs = torres_de_hanoi_movimientos(discos, torre1, torre3, torre2)

    # Imprimir movimientos
    for disco, desde, hacia in movs:
        print(f"Mover disco {disco} desde {desde} hacia {hacia}")
