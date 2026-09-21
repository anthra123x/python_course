"""Ejemplo 03: Operadores matemáticos.

Ejecuta este archivo y observa la diferencia entre cada operador.
"""

# --- Operadores básicos ---
print(7 + 3)   # 10   suma
print(7 - 3)   # 4    resta
print(7 * 3)   # 21   multiplicación
print(7 / 2)   # 3.5  división SIEMPRE devuelve float
print(7 // 2)  # 3    división entera (descarta el residuo)
print(7 % 2)   # 1    módulo / residuo
print(2 ** 3)  # 8    potencia

# --- ¿Para qué sirve el módulo (%)? ---
# Es la forma más común de saber si un número es par o impar:
# un número es par si su residuo al dividir entre 2 es 0.
numero = 10
print(f"{numero} es par: {numero % 2 == 0}")   # True

# --- Orden de operaciones ---
# Python respeta la jerarquía matemática: primero (), luego **,
# luego * / // %, y al final + -.
print(2 + 3 * 4)    # 14 (multiplicación primero)
print((2 + 3) * 4)  # 20 (los paréntesis mandan)

# --- Operadores de comparación (devuelven bool) ---
print(5 > 3)    # True
print(5 == 5)   # True  (== compara, = asigna: ¡no confundir!)
print(5 != 4)   # True
print(5 <= 5)   # True

# --- Operadores lógicos ---
print(True and False)  # False
print(True or False)   # True
print(not True)        # False