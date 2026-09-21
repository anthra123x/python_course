"""Ejemplo 02: Diccionarios — directorio telefónico y contadores.

Los diccionarios asocian llaves con valores. Son la estructura más
versátil de Python: casi cualquier dato real se modela con diccionarios.

Ejecuta: python3 03_estructuras_de_datos/ejemplos/02_diccionarios.py
"""

# --- Crear y acceder ---
contacto = {
    "nombre": "Ana López",
    "telefono": "+591 70012345",
    "ciudad": "La Paz",
}

print(contacto["nombre"])            # Ana López

# .get() no lanza error si la llave no existe: devuelve None (o un default).
print(contacto.get("email"))                  # None
print(contacto.get("email", "sin email"))     # sin email

# --- Agregar / actualizar llaves ---
contacto["email"] = "ana@mail.com"    # nueva llave
contacto["ciudad"] = "El Alto"        # actualiza la existente
print(contacto)

# --- Eliminar ---
del contacto["ciudad"]
print("email" in contacto)            # True
print("ciudad" in contacto)           # False

# --- Recorrer ---
print("\nLos datos de mi contacto:")
for llave, valor in contacto.items():
    print(f"  {llave}: {valor}")

# --- ¡El patrón contador! ---
# Un problema clásico: contar cuántas veces aparece cada letra.
# El diccionario va de "letra" → "cantidad".

texto = "python es genial y piton es de la familia de las serpientes"

contador = {}
for letra in texto:
    # Si la letra aún no está, la inicializamos en 0, luego sumamos 1.
    contador[letra] = contador.get(letra, 0) + 1

print("\nFrecuencia de letras:", contador)

# --- Diccionario de diccionarios (modelo común de datos) ---
estudiantes = {
    "ana": {"edad": 20, "curso": "Python"},
    "luis": {"edad": 22, "curso": "Java"},
}

print("\nCurso de Ana:", estudiantes["ana"]["curso"])