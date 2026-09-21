"""EJERCICIO 5: Buscador de números pares ⭐⭐

Escribe una función `numeros_pares(n)` que devuelva una LISTA con todos
los números pares entre 1 y `n` (incluyendo `n` si es par).

Pistas:
    - Recorre range(1, n + 1).
    - Pregunta con % si el número es par y, si lo es, agrégalo
      a una lista con .append().

Ejemplo:
    numeros_pares(10)  ->  [2, 4, 6, 8, 10]
    numeros_pares(1)   ->  []
"""


def numeros_pares(n: int) -> list:
    # TODO: construye la lista de números pares.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    limite = int(input("Buscar pares hasta: "))
    print(f"Números pares del 1 al {limite}: {numeros_pares(limite)}")

    assert numeros_pares(10) == [2, 4, 6, 8, 10]
    assert numeros_pares(1) == []
    assert numeros_pares(5) == [2, 4]
    print("✔ ¡Tu función pasa las pruebas locales!")