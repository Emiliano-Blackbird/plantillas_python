import functools  # guarda resultados (memoización).
import time  # medir duración o pausar ejecución.


@functools.lru_cache(maxsize=None)
def calcular_costo_envio(destino, distancia, peso):
    # Simulación de operación costosa
    time.sleep(1)

    costo_base = 5
    costo_por_km = 0.1
    costo_por_kg = 0.2

    # Distancia y peso
    costo_total = costo_base + (costo_por_km * distancia) + (costo_por_kg * peso)
    return costo_total


# Ejemplo de uso sin memoización (primera vez se calcula todo)
inicio = time.time()
destino1 = "Ciudad A"
distancia1 = 150
peso1 = 2.5
costo_sin_memo_1 = calcular_costo_envio(destino1, distancia1, peso1)

destino2 = "Ciudad B"
distancia2 = 100
peso2 = 4.5
costo_sin_memo_2 = calcular_costo_envio(destino2, distancia2, peso2)
final = time.time()


# Con memoización (la segunda llamada con mismos datos es inmediata)
inicio_2 = time.time()
costo_con_memo_1 = calcular_costo_envio(destino1, distancia1, peso1)  # ya está en cache
costo_con_memo_2 = calcular_costo_envio(destino2, distancia2, peso2)  # ya está en cache
final_2 = time.time()


print(f"Costo sin memoización para {destino1}: {costo_sin_memo_1}")
print(f"Costo sin memoización para {destino2}: {costo_sin_memo_2}")
print(f"Costo con memoización para {destino1}: {costo_con_memo_1}")
print(f"Costo con memoización para {destino2}: {costo_con_memo_2}")
print(f"Tiempo sin memoización: {final - inicio:.4f} segundos")
print(f"Tiempo con memoización: {final_2 - inicio_2:.4f} segundos")
