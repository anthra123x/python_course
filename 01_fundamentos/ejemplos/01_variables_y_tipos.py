"""Ejemplo 01: Variables y tipos de datos.

Ejecuta este archivo y observa la salida en tu terminal:
    python3 01_fundamentos/ejemplos/01_variables_y_tipos.py

Presta atención a los comentarios: explican el PORQUÉ, no solo el qué.
"""

# --- Variables: cajas con nombre ---
nombre = "Ana"            # str: texto
edad = 30                 # int: número entero
altura = 1.65             # float: número decimal
es_estudiante = True      # bool: verdadero o falso

print(nombre, edad, altura, es_estudiante)

# --- Conocer el tipo de un valor ---
# type() te dice qué tipo de dato tienes. Útil para depurar.
print(type(nombre))       # <class 'str'>
print(type(edad))         # <class 'int'>
print(type(altura))       # <class 'float'>
print(type(es_estudiante))  # <class 'bool'>

# --- Strings: el tipo con superpoderes ---
# .upper() convierte a mayúsculas; len() da la longitud.
print(nombre.upper())     # ANA
print(len(nombre))        # 3

# --- f-strings: la forma moderna de armar texto ---
# El contenido dentro de {} se evalúa como expresión Python.
print(f"{nombre} tiene {edad} años y mide {altura} m")
print(f"El año que viene cumplirá {edad + 1} años")

# --- Operaciones con variables ---
# Python permite operar directamente con las variables como si fueran valores.
edad_doble = edad * 2
print(f"El doble de la edad es {edad_doble}")