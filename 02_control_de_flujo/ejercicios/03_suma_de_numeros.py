"""EJERCICIO 3: Suma de N números ⭐⭐

Escribe una función `suma_hasta` que reciba un número entero positivo `n`
y devuelva la suma de todos los enteros desde 1 hasta `n`.

Usa un bucle `while` (no la fórmula matemática 📐) para practicar
el patrón "acumulador":
    1. Declara una variable acumulador en 0.
    2. Declara un contador en 1.
    3. Mientras el contador sea <= n, suma el contador al acumulador
       y luego incrementa el contador.
    4. Devuelve el acumulador.

Ejemplo:
    suma_hasta(5)   ->   15   (1 + 2 + 3 + 4 + 5)
"""


def suma_hasta(n: int) -> int:
    # TODO: implementa el patrón acumulador con while.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    limite = int(input("¿Hasta qué número sumo? "))
    print(f"La suma de 1 a {limite} es {suma_hasta(limite)}")

    assert suma_hasta(5) == 15
    assert suma_hasta(10) == 55
    assert suma_hasta(1) == 1
    print("✔ ¡Tu función pasa las pruebas locales!")