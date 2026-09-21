"""SOLUCIÓN 1: Lista de compras ⭐⭐

La defensa contra duplicados y ValueError es la misma: verificar
con `in` antes de modificar. Eso se llama "validar antes de actuar".
"""


def agregar_articulo(lista: list, articulo: str) -> list:
    if articulo not in lista:
        lista.append(articulo)
    return lista


def quitar_articulo(lista: list, articulo: str) -> list:
    if articulo in lista:
        lista.remove(articulo)
    return lista


if __name__ == "__main__":
    compras = []
    compras = agregar_articulo(compras, "pan")
    compras = agregar_articulo(compras, "leche")
    compras = agregar_articulo(compras, "pan")
    print("Compras:", compras)
    compras = quitar_articulo(compras, "pan")
    print("Después de quitar:", compras)

    assert agregar_articulo(["pan"], "leche") == ["pan", "leche"]
    assert agregar_articulo(["pan"], "pan") == ["pan"]
    assert quitar_articulo(["pan", "leche"], "pan") == ["leche"]
    print("✔ ¡Tus funciones pasan las pruebas locales!")