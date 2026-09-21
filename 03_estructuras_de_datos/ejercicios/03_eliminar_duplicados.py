"""EJERCICIO 3: Eliminar duplicados ⭐

Escribe una función `quitar_duplicados(lista)` que devuelva una NUEVA
lista (sin modificar la original) pero sin elementos repetidos.

TIP de oro:
    Pasar por un conjunto (set) elimina los duplicados automáticamente,
    y list(...) convierte de vuelta a lista. Dos líneas bastan:
        sin_duplicados = list(set(lista))

Ejemplo:
    quitar_duplicados([1, 2, 2, 3, 3])  ->  [1, 2, 3]  (el orden puede variar)
"""


def quitar_duplicados(lista: list) -> list:
    # TODO: conviértela a set y de vuelta a lista.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    original = [1, 2, 2, 3, 3, 3, 4]
    resultado = quitar_duplicados(original)
    print(f"Original: {original}")
    print(f"Sin duplicados: {resultado}")

    assert sorted(quitar_duplicados([1, 2, 2, 3, 3])) == [1, 2, 3]
    assert quitar_duplicados([]) == []
    assert len(quitar_duplicados([1, 1, 1, 1])) == 1
    print("✔ ¡Tu función pasa las pruebas locales!")