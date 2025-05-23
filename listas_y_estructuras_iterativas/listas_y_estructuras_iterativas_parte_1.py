# Total ventas de productos

precio_productos = [30.0, 9.8, 42.5, 32.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]
unidades_producto = [3, 1, 0, 0, 7, 2, 0, 0, 4, 0]

total_ventas = sum(unidades_producto)

# Bucle que recorre los productos
dinero_total = 0
for i in range(0, len(precio_productos)):
    dinero_por_producto = precio_productos[i] * unidades_producto[i]
    dinero_total = dinero_total + dinero_por_producto
    print(f"El dinero facturado por el producto {i + 1} es {dinero_por_producto} euros")


print("El número total de unidades vendidas es", total_ventas)
print("El dinero total facturado es", dinero_total, "euros")
