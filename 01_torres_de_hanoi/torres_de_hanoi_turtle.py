import turtle
import time


# ====== LÓGICA DEL ALGORITMO ======
def mover_disco_tuple(desde: int, hacia: int, disco: int) -> tuple:
    return (disco, desde, hacia)


def torres_de_hanoi_movimientos(n: int, origen: int, destino: int, auxiliar: int, movimientos=None):
    if movimientos is None:
        movimientos = []
    if n <= 0:
        return movimientos
    if n == 1:
        movimientos.append(mover_disco_tuple(origen, destino, 1))
        return movimientos
    torres_de_hanoi_movimientos(n - 1, origen, auxiliar, destino, movimientos)
    movimientos.append(mover_disco_tuple(origen, destino, n))
    torres_de_hanoi_movimientos(n - 1, auxiliar, destino, origen, movimientos)
    return movimientos


# ====== DIBUJO CON TURTLE ======
def dibujar_torre(x):
    turtle.penup()
    turtle.goto(x, -100)
    turtle.pendown()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)


def dibujar_disco(disco, x, y):
    ancho = 40 + disco * 20
    turtle.penup()
    turtle.goto(x - ancho // 2, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.end_fill()


def animar_hanoi(n):
    # Configuración de la pantalla
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.hideturtle()
    turtle.tracer(0, 0)  # Evita dibujar en tiempo real (mejor control)

    posiciones_torres = [-150, 0, 150]
    torres = [list(range(n, 0, -1)), [], []]

    # Dibujar las torres iniciales
    for pos in posiciones_torres:
        dibujar_torre(pos)

    # Dibujar discos iniciales
    colores = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i, disco in enumerate(torres[0]):
        turtle.fillcolor(colores[(disco-1) % len(colores)])
        dibujar_disco(disco, posiciones_torres[0], -100 + i*20)
    turtle.update()

    movimientos = torres_de_hanoi_movimientos(n, 0, 2, 1)

    for disco, desde, hacia in movimientos:
        # Sacar el disco de la torre de origen
        torres[desde].remove(disco)

        # Calcular posición nueva
        altura = len(torres[hacia])
        torres[hacia].append(disco)

        # Borrar pantalla y redibujar todo
        turtle.clear()
        for pos in posiciones_torres:
            dibujar_torre(pos)
        for torre_idx, torre in enumerate(torres):
            for i, d in enumerate(torre):
                turtle.fillcolor(colores[(d-1) % len(colores)])
                dibujar_disco(d, posiciones_torres[torre_idx], -100 + i*20)
        turtle.update()
        time.sleep(0.5)  # Pausa entre movimientos


if __name__ == "__main__":
    animar_hanoi(3)
    turtle.done()
