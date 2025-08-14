from datetime import datetime


# Función principal.
def analizar_ventas(ventas):
    # último trimestre del año
    ventas_filtradas = [venta for venta in ventas if datetime.strptime(venta['fecha_venta'], '%Y-%m-%d').month >= 10]

    # solo ventas mayores a $500
    ventas_filtradas = [venta for venta in ventas_filtradas if venta['monto'] > 500]

    # ventas por ubicación del comprador
    ventas_agrupadas = {}
    for venta in ventas_filtradas:
        ubicacion = venta['ubicacion_comprador']
        if ubicacion not in ventas_agrupadas:
            ventas_agrupadas[ubicacion] = []
        ventas_agrupadas[ubicacion].append(venta)

    # Promedio de monto de ventas por ubicación
    promedio_ventas = {}
    for ubicacion in ventas_agrupadas:
        ventas_por_ubicacion = ventas_agrupadas[ubicacion]
        promedio_ventas[ubicacion] = sum(venta['monto'] for venta in ventas_por_ubicacion) / len(ventas_por_ubicacion)

    # ubicaciones por promedio de ventas en forma descendente
    ubicaciones_ordenadas = sorted(promedio_ventas.items(), key=lambda ubicacion_ventas: ubicacion_ventas[1], reverse=True)

    # muestra la ubicación y sus promedios
    for ubicacion in ubicaciones_ordenadas:
        print(f"Ubicación: {ubicacion[0]}, Promedio de ventas: ${ubicacion[1]:.2f}")


ventas = [
    {'nombre_producto': 'Laptop', 'fecha_venta': '2023-10-15', 'monto': 1200, 'ubicacion_comprador': 'Madrid'},
    {'nombre_producto': 'Smartphone', 'fecha_venta': '2023-11-05', 'monto': 800, 'ubicacion_comprador': 'Barcelona'},
    {'nombre_producto': 'Tablet', 'fecha_venta': '2023-12-01', 'monto': 600, 'ubicacion_comprador': 'Madrid'},
    {'nombre_producto': 'Monitor', 'fecha_venta': '2023-10-20', 'monto': 300, 'ubicacion_comprador': 'Valencia'},
    {'nombre_producto': 'Teclado', 'fecha_venta': '2023-11-15', 'monto': 100, 'ubicacion_comprador': 'Madrid'},
]
analizar_ventas(ventas)
