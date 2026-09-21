"""EJERCICIO 1: Lista de compras ⭐⭐

Vamos a construir el corazón de una app de compras: dos funciones.

1. `agregar_articulo(lista, articulo)` — agrega `articulo` a `lista`
   con .append() SOLO si no está ya en la lista (¿recuerdas `in`?).
   Devuelve la lista actualizada.

2. `quitar_articulo(lista, articulo)` — elimina `articulo` de `lista`
   con .remove() SOLO si existe (verifica con `in` para evitar un
   ValueError). Devuelve la lista actualizada.

Ejemplo:
    agregar_articulo(["pan"], "leche")      ->  ["pan", "leche"]
    agregar_articulo(["pan"], "pan")         ->  ["pan"]
    quitar_articulo(["pan", "leche"], "pan") ->  ["leche"]
"""


def agregar_articulo(lista: list, articulo: str) -> list:
    # TODO: si articulo no está en lista, haz append.
    pass  # Reemplaza esta línea


def quitar_articulo(lista: list, articulo: str) -> list:
    # TODO: si articulo está en lista, haz remove.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tus funciones ---
if __name__ == "__main__":
    compras = []
    compras = agregar_articulo(compras, "pan")
    compras = agregar_articulo(compras, "leche")
    compras = agregar_articulo(compras, "pan")   # no debería duplicarse
    print("Compras:", compras)
    compras = quitar_articulo(compras, "pan")
    print("Después de quitar:", compras)

    assert agregar_articulo(["pan"], "leche") == ["pan", "leche"]
    assert agregar_articulo(["pan"], "pan") == ["pan"]
    assert quitar_articulo(["pan", "leche"], "pan") == ["leche"]
    print("✔ ¡Tus funciones pasan las pruebas locales!")