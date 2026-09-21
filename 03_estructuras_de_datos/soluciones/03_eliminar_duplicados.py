"""SOLUCIÓN 3: Eliminar duplicados ⭐

Pasar por un conjunto (set) hace el trabajo pesado por nosotros.
list(set(...)) convierte de vuelta a lista.
"""


def quitar_duplicados(lista: list) -> list:
    # Un conjunto no admite duplicados: {1, 2, 2, 3} -> {1, 2, 3}
    return list(set(lista))


if __name__ == "__main__":
    original = [1, 2, 2, 3, 3, 3, 4]
    resultado = quitar_duplicados(original)
    print(f"Original: {original}")
    print(f"Sin duplicados: {resultado}")

    assert sorted(quitar_duplicados([1, 2, 2, 3, 3])) == [1, 2, 3]
    assert quitar_duplicados([]) == []
    assert len(quitar_duplicados([1, 1, 1, 1])) == 1
    print("✔ ¡Tu función pasa las pruebas locales!")