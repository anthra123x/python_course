"""EJERCICIO 4: Tabla de multiplicar ⭐

Escribe una función `tabla_de_multiplicar(numero, limite)` que devuelva
una LISTA de strings con la tabla de multiplicar de `numero`, desde 1
hasta `limite`.

Cada elemento debe tener el formato:
    "3 x 1 = 3"

Uso un bucle `for` con `range(1, limite + 1)` y un f-string.

Ejemplo:
    tabla_de_multiplicar(3, 3)  ->  ["3 x 1 = 3", "3 x 2 = 6", "3 x 3 = 9"]
"""


def tabla_de_multiplicar(numero: int, limite: int = 10) -> list:
    # TODO: crea una lista vacía, recorre range(1, limite + 1)
    #       y agrega cada línea formateada.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    base = int(input("¿Qué tabla quieres? "))
    for linea in tabla_de_multiplicar(base, 5):
        print(linea)

    assert tabla_de_multiplicar(3, 3) == ["3 x 1 = 3", "3 x 2 = 6", "3 x 3 = 9"]
    assert len(tabla_de_multiplicar(7)) == 10
    print("✔ ¡Tu función pasa las pruebas locales!")