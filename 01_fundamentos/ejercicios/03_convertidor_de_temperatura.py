"""EJERCICIO 3: Convertidor de temperatura ⭐⭐

Escribe una función `fahrenheit_a_celsius` que reciba una temperatura
en grados Fahrenheit (float) y devuelva su equivalente en Celsius.

La fórmula es:   °C = (°F − 32) × 5 / 9

Ejemplo:
    fahrenheit_a_celsius(212)   ->  100.0
    fahrenheit_a_celsius(32)    ->  0.0

TIP:
    Puedes devolver el resultado directo de la fórmula; por ejemplo
    (fahrenheit - 32) * 5 / 9. El valor será float, como esperan los tests.
"""


def fahrenheit_a_celsius(fahrenheit: float) -> float:
    # TODO: aplica la fórmula y devuelve el resultado.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    f = float(input("Temperatura en °F: "))
    c = fahrenheit_a_celsius(f)
    print(f"{f} °F son {c:.2f} °C")

    assert abs(fahrenheit_a_celsius(212) - 100.0) < 0.001
    assert abs(fahrenheit_a_celsius(32) - 0.0) < 0.001
    print("✔ ¡Tu función pasa las pruebas locales!")