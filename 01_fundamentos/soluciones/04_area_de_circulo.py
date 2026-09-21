"""SOLUCIÓN 4: Área de un círculo ⭐⭐

math.pi es la constante π con muchísima precisión, y ** eleva al cuadrado.
Una fórmula de una línea. ¡Eso es todo!
"""

import math


def area_circulo(radio: float) -> float:
    return math.pi * radio ** 2


if __name__ == "__main__":
    r = float(input("Radio del círculo: "))
    print(f"El área de un círculo de radio {r} es {area_circulo(r):.2f}")

    assert abs(area_circulo(1.0) - math.pi) < 0.001
    assert abs(area_circulo(2.0) - math.pi * 4) < 0.001
    print("✔ ¡Tu función pasa las pruebas locales!")