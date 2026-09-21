"""Ejemplo 01: Listas en acción — una agenda de actividades.

Este ejemplo es una versión mejorada y comentada de un script original
que manejaba una agenda con listas. Observa los comentarios: explican
el PORQUÉ de cada decisión.

Ejecuta: python3 03_estructuras_de_datos/ejemplos/01_listas.py
"""

# --- Crear una lista ---
# La lista crece en orden: primero "desayunar", luego "estudiar"...
actividades = ["desayunar", "estudiar", "leer"]
print("Agenda inicial:", actividades)

# --- Agregar elementos ---
# .append() agrega al final. Es la operación más común con listas.
nueva_actividad = "hacer ejercicio"
actividades.append(nueva_actividad)
print("Después de append:", actividades)

# .insert(posición, elemento) agrega en un lugar específico.
actividades.insert(0, "meditar")
print("Después de insert:", actividades)

# --- Eliminar elementos ---
# .remove(valor) elimina la primera aparición de ese valor.
# Primero verificamos con "in" para no provocar un ValueError.
actividad_completada = "estudiar"
if actividad_completada in actividades:
    actividades.remove(actividad_completada)
print("Después de remove:", actividades)

# .pop() elimina y devuelve el último. Útil para "deshacer".
ultima_actividad = actividades.pop()
print(f"Eliminé la última: '{ultima_actividad}'")
print("Después de pop:", actividades)

# --- Consultar información ---
print("¿Hay 'leer'?", "leer" in actividades)
print("Cantidad de actividades:", len(actividades))
print("Primera actividad:", actividades[0])
print("Última actividad:", actividades[-1])

# --- Recorrer con for ---
# El patrón clásico para hacer algo con cada elemento.
print("\nMi agenda de hoy:")
for actividad in actividades:
    print(f"  ✔ {actividad}")

# --- Ordenar ---
# sorted() devuelve una nueva lista ordenada (no modifica la original).
print("\nActividades ordenadas (a-z):", sorted(actividades))