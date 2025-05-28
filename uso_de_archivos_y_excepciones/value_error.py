while True:
    try:
        numero1 = int(input("Introduce un número entero: "))
        numero2 = int(input("Introduce otro número entero: "))
        resultado = numero1 + numero2
        print("El resultado de la suma es:", resultado)
        break
    except ValueError:
        print("Error: Debes introducir un número entero válido.")
