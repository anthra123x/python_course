"""Ejemplo 02: El bucle while.

El while repite un bloque MIENTRAS su condición sea True.
La clave está en que algo dentro del bloque modifique la condición;
si no, el bucle nunca termina (bucle infinito).

Ejecuta: python3 02_control_de_flujo/ejemplos/02_bucle_while.py
"""

# --- 1. Adivinar una contraseña ---
# La condición es "mientras no aciertes, sigue preguntando".
contrasena_correcta = "python"
intento = ""

while intento != contrasena_correcta:
    intento = input("Adivina la contraseña: ")

print("¡Acceso concedido!")

# --- 2. Contador con while ---
# Aquí la variable `contador` cambia dentro del bucle: +1 por vuelta.
contador = 0
while contador < 5:
    print(f"Vuelta número {contador}")
    contador += 1          # ¡CRUCIAL! Sin esto, bucle infinito.

print("¡El contador terminó!")

# --- 3. Validar entrada del usuario ---
# Patrón SUPER útil: pedir datos hasta que sean válidos.
numero_valido = None

while numero_valido is None:
    entrada = input("Dame un número par: ")
    if entrada.isdigit() and int(entrada) % 2 == 0:
        numero_valido = int(entrada)
    else:
        print("Eso no es un número par. Intenta de nuevo.")

print(f"¡Gracias! Me diste el número par {numero_valido}")

# --- 4. break: salir antes de tiempo ---
# El break detiene el bucle inmediatamente.
busqueda = 7
numero_de_vueltas = 0

while True:
    numero_de_vueltas += 1
    print(f"Intentando con {numero_de_vueltas}...")
    if numero_de_vueltas == busqueda:
        break

print(f"Encontré el número {busqueda} después de {numero_de_vueltas} intentos.")