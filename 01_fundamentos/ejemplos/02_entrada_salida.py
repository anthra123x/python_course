"""Ejemplo 02: Entrada y salida de datos: print() e input().

Ejecuta este archivo y contesta las preguntas en la terminal.

El flujo de un programa casi siempre es:
    1. Pedir datos con input()
    2. Procesarlos
    3. Mostrar resultados con print()
"""

# --- input() SIEMPRE devuelve texto (str) ---
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}")

# --- Convertir lo que entra: int() y float() ---
# Sin conversión, "10" + "5" sería "105" (concatena). Con int(), es 15.
edad = int(input("¿Cuántos años tienes? "))
print(f"En 10 años tendrás {edad + 10}")

precio = float(input("¿Cuánto cuesta el café que compras? $"))
print(f"El café cuesta {precio} y con 10% de propina pagas {precio * 1.10:.2f}")

# --- Detalle: {precio * 1.10:.2f} formatea el número con 2 decimales.
#     El ": .2f" significa "float con 2 decimales". ¡Muy útil!

# --- print() puede recibir varios valores separados por comas ---
print("Python", "es", "genial")
print("Los valores se separan con espacios por defecto")

# --- sep y end: personalizar la impresión ---
print("uno", "dos", "tres", sep=" - ")   # uno - dos - tres
print("primera línea", end=" ")
print("misma línea")                      # primera línea misma línea