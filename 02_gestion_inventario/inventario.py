def buscar_cantidad_producto(inventario, codigo_producto, inicio=0, fin=None):
    if fin is None:
        fin = len(inventario) - 1
    if inicio > fin:
        return 0
    medio = (inicio + fin) // 2
    if inventario[medio]['codigo'] == codigo_producto:
        return inventario[medio]['cantidad']
    elif inventario[medio]['codigo'] < codigo_producto:
        return buscar_cantidad_producto(inventario, codigo_producto, medio + 1, fin)
    else:
        return buscar_cantidad_producto(inventario, codigo_producto, inicio, medio - 1)


# Declarar inventario
inventario = [
    {'codigo': 101, 'cantidad': 10},
    {'codigo': 102, 'cantidad': 5},
    {'codigo': 103, 'cantidad': 15},
    {'codigo': 104, 'cantidad': 0},
    {'codigo': 105, 'cantidad': 20}
]

codigo_producto = 103
cantidad_disponible = buscar_cantidad_producto(inventario, codigo_producto)
print(f'Cantidad disponible del producto {codigo_producto}: {cantidad_disponible}')
