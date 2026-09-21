"""SOLUCIÓN 1: Calculadora de notas ⭐⭐

El truco: evaluar en orden descendente. Como el if se cumple y sale,
nunca necesitas condiciones dobles.
"""


def calificar(puntaje: int) -> str:
    if puntaje >= 90:
        return "A"
    elif puntaje >= 80:
        return "B"
    elif puntaje >= 70:
        return "C"
    elif puntaje >= 60:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    puntos = int(input("Puntaje (0-100): "))
    print(f"Tu calificación es: {calificar(puntos)}")

    assert calificar(95) == "A"
    assert calificar(85) == "B"
    assert calificar(72) == "C"
    assert calificar(65) == "D"
    assert calificar(50) == "F"
    print("✔ ¡Tu función pasa las pruebas locales!")