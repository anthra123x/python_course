"""EJERCICIO 4: Área de un círculo ⭐⭐

Escribe una función `area_circulo` que reciba el radio (float) y
devuelva el área del círculo.

La fórmula es:   área = π × radio²

Usa el valor de π del módulo math:  import math  →  math.pi
Para elevar al cuadrado puedes usar el operador ** (radio ** 2).

Ejemplo:
    area_circulo(1.0)   ->   3.141592653589793

TIP:
    Un solo return:  return math.pi * radio ** 2
"""

import math


def area_circulo(radio: float) -> float:
    # TODO: calcula el área con math.pi y el operador **.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    r = float(input("Radio del círculo: "))
    print(f"El área de un círculo de radio {r} es {area_circulo(r):.2f}")

    assert abs(area_circulo(1.0) - math.pi) < 0.001
    assert abs(area_circulo(2.0) - math.pi * 4) < 0.001
    print("✔ ¡Tu función pasa las pruebas locales!")