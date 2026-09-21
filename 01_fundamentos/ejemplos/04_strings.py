"""Ejemplo 04: Strings en acción.

Los strings (texto) son el tipo de dato más usado en programación.
Aquí verás las operaciones más comunes.

Ejecuta:  python3 01_fundamentos/ejemplos/04_strings.py
"""

# --- Comillas simples o dobles: equivalentes ---
a = 'Hola'
b = "Hola"
print(a == b)   # True

# --- Concatenación (unir) con + ---
nombre = "Ada"
apellido = "Lovelace"
nombre_completo = nombre + " " + apellido
print(nombre_completo)                    # Ada Lovelace

# --- Multiplicar strings (¡sí, se puede!) ---
print("ja" * 3)                           # jajaja

# --- Métodos útiles ---
texto = "  Programar en Python  "
print(texto.strip())        # quita espacios de los extremos
print(texto.lower())        # todo en minúsculas
print(texto.upper())        # todo en mayúsculas
print(texto.title())        # Primera Letra De Cada Palabra En Mayúscula

mensaje = "Hola, mundo"
print(mensaje.replace("mundo", "Python"))  # Hola, Python
print(len(mensaje))                        # 11 (longitud incluyendo espacios)

# --- Acceder a caracteres por posición (índice) ---
# Python cuenta desde 0:  H(0) o(1) l(2) a(3) ,(4) ...
print(mensaje[0])     # H
print(mensaje[-1])    # o  (el -1 es el ÚLTIMO carácter)
print(mensaje[0:4])   # Hola  (slicing: del índice 0 al 3)

# --- Pertenencia (in) ---
print("mundo" in mensaje)     # True
print("Python" in mensaje)    # False

# --- f-strings con formato numérico ---
precio = 19.995
print(f"Precio: {precio:.2f}")   # Precio: 20.00  (redondea a 2 decimales)
print(f"Porcentaje: {0.8532:.1%}")  # Porcentaje: 85.3%