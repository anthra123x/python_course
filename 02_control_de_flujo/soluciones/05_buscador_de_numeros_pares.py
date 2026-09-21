"""SOLUCIÓN 5: Buscador de números pares ⭐⭐

Combinamos un for con range y la prueba % 2 == 0.
El filtrado con una condición dentro de un bucle es un patrón
que verás por todas partes: "recorre y selecciona lo que cumpla".
"""


def numeros_pares(n: int) -> list:
    pares = []

    for numero in range(1, n + 1):
        if numero % 2 == 0:
            pares.append(numero)

    return pares


if __name__ == "__main__":
    limite = int(input("Buscar pares hasta: "))
    print(f"Números pares del 1 al {limite}: {numeros_pares(limite)}")

    assert numeros_pares(10) == [2, 4, 6, 8, 10]
    assert numeros_pares(1) == []
    assert numeros_pares(5) == [2, 4]
    print("✔ ¡Tu función pasa las pruebas locales!")