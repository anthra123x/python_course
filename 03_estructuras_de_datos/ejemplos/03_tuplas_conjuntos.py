"""Ejemplo 03: Tuplas y conjuntos.

Las tuplas son listas inmutables (no se pueden modificar). Los conjuntos
son colecciones sin duplicados con operaciones de teoría de conjuntos.

Ejecuta: python3 03_estructuras_de_datos/ejemplos/03_tuplas_conjuntos.py
"""

# ============================================================
# TUPLAS
# ============================================================
coordenadas = (16.5, -68.15)   # La Paz, Bolivia
print(coordenadas[0])          # 16.5
print(coordenadas[1])          # -68.15

# Intentar modificar lanza un TypeError (comenta la línea para seguir):
# coordenadas[0] = 10  # ❌ TypeError: 'tuple' object does not support item assignment

# Desempaquetado: asignar cada elemento a una variable.
latitud, longitud = coordenadas
print(f"Lat: {latitud}, Lon: {longitud}")

# Las tuplas son ideales para datos que no deben cambiar.
dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
print("¿El lunes es día laboral?", dias_semana[0] in ("lunes", "martes"))

# ============================================================
# CONJUNTOS (sets)
# ============================================================
# Eliminan duplicados automáticamente.
numeros = {1, 2, 2, 3, 3, 3, 4}
print("Conjunto:", numeros)        # {1, 2, 3, 4}

# El caso de uso clásico: quitar duplicados de una lista.
lista_con_repetidos = [1, 2, 2, 3, 3, 4]
sin_duplicados = list(set(lista_con_repetidos))
print("Sin duplicados:", sin_duplicados)

# Operaciones de conjuntos.
python_topics = {"variables", "bucles", "listas", "funciones"}
data_topics = {"listas", "sql", "funciones", "pandas"}

print("En ambos:", python_topics & data_topics)         # intersección
print("Solo Python:", python_topics - data_topics)      # diferencia
print("En alguno:", python_topics | data_topics)        # unión

# Agregar y eliminar.
python_topics.add("diccionarios")
python_topics.discard("bucles")    # discard no lanza error si no existe
print("Temas Python:", python_topics)