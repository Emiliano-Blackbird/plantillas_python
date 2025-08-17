import time


def logger_con_tiempo_de_ejecucion(funcion):
    def wrapper():
        inicio = time.time()
        print(f"Inicio de la función: {funcion.__name__}")

        try:
            resultado = funcion()
        except Exception as e:
            print(f"Error en la función {funcion.__name__}: {e}")
            raise
        fin = time.time()
        print(f"La función {funcion.__name__} ha tardado {fin-inicio} ms en ejecutarse ")

        return resultado
    return wrapper


@logger_con_tiempo_de_ejecucion
def mi_funcion():
    fib_series = [0, 1]
    for i in range(2, 20):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series


print(mi_funcion())
