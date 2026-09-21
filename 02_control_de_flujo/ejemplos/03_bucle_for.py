"""Ejemplo 03: El bucle for.

El for recorre colecciones (listas, strings, rangos...) de forma natural.
Es el bucle más usado en Python: "para cada elemento, haz esto".

Ejecuta: python3 02_control_de_flujo/ejemplos/03_bucle_for.py
"""

# --- 1. Recorrer una lista ---
frutas = ["manzana", "pera", "uva", "mango"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")

# --- 2. range(n): repetir n veces ---
for i in range(3):
    print(f"Vuelta {i}")          # 0, 1, 2 (empieza en 0)

# --- 3. range(inicio, fin, paso) ---
print("Pares del 0 al 10:")
for i in range(0, 11, 2):
    print(i)

print("Cuenta regresiva:")
for i in range(10, 0, -1):        # paso negativo: hacia atrás
    print(i)

# --- 4. Recorrer los caracteres de un string ---
for letra in "Python":
    print(f"Letra: {letra}")

# --- 5. Acumulador: la suma de 1 a 100 ---
suma = 0                          # el acumulador empieza en 0
for numero in range(1, 101):
    suma += numero                # suma = suma + numero

print(f"La suma de 1 a 100 es {suma}")   # 5050

# --- 6. continue y break dentro de for ---
print("Números 1-5 saltando el 3:")
for numero in range(1, 6):
    if numero == 3:
        continue                  # salta el 3
    print(numero)

print("Deteniéndose en el 4:")
for numero in range(1, 10):
    if numero == 4:
        break                     # se detiene en el 4
    print(numero)