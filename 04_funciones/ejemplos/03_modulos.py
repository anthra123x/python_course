"""Ejemplo 03: Módulos — random y datetime.

La biblioteca estándar trae módulos listos para usar. Dos de los más
útiles: random (aleatoriedad) y datetime (fechas y horas).

Este ejemplo es una versión corregida y ampliada de un script original
llamado "que_hora__es.py".

Ejecuta: python3 04_funciones/ejemplos/03_modulos.py
"""

import datetime
import random

# ============================================================
# MÓDULO DATETIME: fechas y horas
# ============================================================
# Estrategia original del curso: una persona estudiante quería saber
# si ya era hora de descansar (14:00). Lo refactorizamos como función.
def es_hora_de_descansar(hora_descanso: str = "14:00") -> bool:
    """Devuelve True si la hora actual es >= hora_descanso.

    Parámetro:
        hora_descanso: string "HH:MM" con el momento objetivo.
    """
    ahora = datetime.datetime.now().time()
    objetivo = datetime.datetime.strptime(hora_descanso, "%H:%M").time()
    return ahora >= objetivo


if es_hora_de_descansar():
    print("✔ Es hora de descansar")
else:
    print("✖ Aún no es hora de descansar")

# Otras operaciones con datetime:
ahora = datetime.datetime.now()
print("Hoy es:", ahora.strftime("%A, %d de %B de %Y"))   # formato bonito
print("Son las:", ahora.strftime("%H:%M"))
print("Año:", ahora.year)

# ============================================================
# MÓDULO RANDOM: aleatoriedad
# ============================================================
print("\nNúmero aleatorio entre 1 y 10:", random.randint(1, 10))
print("Elegir un elemento al azar:", random.choice(["piedra", "papel", "tijera"]))
print("Mezclar una lista:", random.sample([1, 2, 3, 4, 5], k=3))

# ============================================================
# TU PROPIO MÓDULO
# ============================================================
# Cualquier archivo .py es un módulo importable. Aquí creamos uno
# en memoria con dos funciones y lo "importamos" desde este archivo.
# En un proyecto real, importarías:  from mi_modulo import funcion
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}!"

print(saludar("mundo"))