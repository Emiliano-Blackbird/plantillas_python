import functools
import re
import time


@functools.lru_cache(maxsize=None)
def calcular_frecuencia_palabras(texto):
    # Preprocesamiento del texto
    texto = texto.lower()
    texto = re.sub(r'\W+', ' ', texto)  # Eliminar caracteres no alfanuméricos
    palabras = texto.split()

    # Excluir palabras comunes
    palabras_comunes = set(['y', 'la', 'el', 'en', 'de', 'que', 'a', 'los', 'las'])

    palabras = [palabra for palabra in palabras if palabra not in palabras_comunes]

    # Conteo de frecuencia
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


# Ejemplo de uso
texto_1 = "El gato juega con la pelota, el gato corre y el gato duerme"
texto_2 = "La pelota rueda y el perro corre, pero el gato mira la pelota"

inicio_1 = time.time()
frecuencia_sin_memo_1 = calcular_frecuencia_palabras(texto_1)
frecuencia_sin_memo_2 = calcular_frecuencia_palabras(texto_2)
fin_1 = time.time()

inicio_2 = time.time()
frecuencia_con_memo_1 = calcular_frecuencia_palabras(texto_1)
frecuencia_con_memo_2 = calcular_frecuencia_palabras(texto_2)
fin_2 = time.time()

print("Frecuencia sin memoización (texto 1):", frecuencia_sin_memo_1)
print("Frecuencia sin memoización (texto 2):", frecuencia_sin_memo_2)
print("Frecuencia con memoización (texto 1):", frecuencia_con_memo_1)
print("Frecuencia con memoización (texto 2):", frecuencia_con_memo_2)
print("Tiempo sin memoización:", fin_1 - inicio_1)
print("Tiempo con memoización:", fin_2 - inicio_2)
