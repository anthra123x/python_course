"""SOLUCIÓN 3: Suma de N números ⭐⭐

El patrón acumulador es la base de muchísimos programas:
    acumulador = 0
    mientras haya elementos:
        acumulador += elemento

Aquí el "elemento" es cada contador que avanza de 1 en 1.
"""


def suma_hasta(n: int) -> int:
    acumulador = 0
    contador = 1

    while contador <= n:
        acumulador += contador   # acumulador = acumulador + contador
        contador += 1            # ¡clave para que el bucle termine!

    return acumulador


if __name__ == "__main__":
    limite = int(input("¿Hasta qué número sumo? "))
    print(f"La suma de 1 a {limite} es {suma_hasta(limite)}")

    assert suma_hasta(5) == 15
    assert suma_hasta(10) == 55
    assert suma_hasta(1) == 1
    print("✔ ¡Tu función pasa las pruebas locales!")