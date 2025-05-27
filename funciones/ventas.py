ventas = []


def agregar_venta(producto, precio, cantidad):
    venta = {
        'producto': producto,
        'precio': precio,
        'cantidad': cantidad
    }

    ventas.append(venta)


def mostrar_ventas():
    for venta in ventas:
        print("Productos", venta['producto'])
        print("Precio", venta['precio'])
        print("Cantidad", venta['cantidad'])


agregar_venta("Camisa", 20.5, 2)
agregar_venta("Pantalón", 35.0, 1)
agregar_venta("Zapatos", 50.0, 1)

mostrar_ventas()
