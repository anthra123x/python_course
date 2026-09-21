"""EJERCICIO 1: Calculadora de notas ⭐⭐

Una universidad califica con letras según el puntaje (0 a 100):

    90 - 100  ->  "A"   (excelente)
    80 -  89  ->  "B"   (notable)
    70 -  79  ->  "C"   (bien)
    60 -  69  ->  "D"   (suficiente)
        < 60  ->  "F"   (reprobado)

Escribe la función `calificar(puntaje)` que reciba el puntaje (int)
y devuelva la letra correspondiente.

PISTA:
    Evalúa de arriba hacia abajo (de la mejor nota a la peor).
    El PRIMER if que se cumpla gana, así que no necesitas escribir
    condiciones dobles tipo "80 <= puntaje <= 89".

Ejemplo:
    calificar(95)  ->  "A"
    calificar(72)  ->  "C"
    calificar(50)  ->  "F"
"""


def calificar(puntaje: int) -> str:
    # TODO: implementa la escala con if/elif/else descendente.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    puntos = int(input("Puntaje (0-100): "))
    print(f"Tu calificación es: {calificar(puntos)}")

    assert calificar(95) == "A"
    assert calificar(85) == "B"
    assert calificar(72) == "C"
    assert calificar(65) == "D"
    assert calificar(50) == "F"
    print("✔ ¡Tu función pasa las pruebas locales!")