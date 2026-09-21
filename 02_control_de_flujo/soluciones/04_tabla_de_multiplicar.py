"""SOLUCIÓN 4: Tabla de multiplicar ⭐

Construimos una lista vacía, la llenamos con un for y la devolvemos.
El f-string formatea cada línea de la tabla.
"""


def tabla_de_multiplicar(numero: int, limite: int = 10) -> list:
    tabla = []  # la lista que irá creciendo

    for i in range(1, limite + 1):
        tabla.append(f"{numero} x {i} = {numero * i}")

    return tabla


if __name__ == "__main__":
    base = int(input("¿Qué tabla quieres? "))
    for linea in tabla_de_multiplicar(base, 5):
        print(linea)

    assert tabla_de_multiplicar(3, 3) == ["3 x 1 = 3", "3 x 2 = 6", "3 x 3 = 9"]
    assert len(tabla_de_multiplicar(7)) == 10
    print("✔ ¡Tu función pasa las pruebas locales!")