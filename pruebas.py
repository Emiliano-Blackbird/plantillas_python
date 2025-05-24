a = float(input("Introduce un número: "))
b = float(input("Introduce otro número: "))
c = float(input("Introduce un tercer número: "))
d = float(input("Introduce un cuarto número: "))

# imprimir el mayor de los 4 números

if a > b and a > c and a > d:
    print("El mayor es:", a)
elif b > a and b > c and b > d:
    print("El mayor es:", b)
elif c > a and c > b and c > d:
    print("El mayor es:", c)
elif d > a and d > b and d > c:
    print("El mayor es:", d)
else:
    print("Hay números iguales")

# imprimir el menor de los 4 números
if a < b and a < c and a < d:
    print("El menor es:", a)
elif b < a and b < c and b < d:
    print("El menor es:", b)
elif c < a and c < b and c < d:
    print("El menor es:", c)
elif d < a and d < b and d < c:
    print("El menor es:", d)
else:
    print("Hay números iguales")

# imprimir la suma de los 4 números
suma = a + b + c + d
print("La suma es:", suma)

# imprimir el promedio de los 4 números
promedio = suma / 4
print("El promedio es:", promedio)
