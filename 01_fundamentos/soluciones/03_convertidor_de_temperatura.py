"""SOLUCIÓN 3: Convertidor de temperatura ⭐⭐

Aplica la fórmula tal cual. El orden de las operaciones hace que
(fahrenheit - 32) se calcule antes de multiplicar y dividir.
"""


def fahrenheit_a_celsius(fahrenheit: float) -> float:
    # Fórmula estándar de conversión °F → °C.
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    f = float(input("Temperatura en °F: "))
    c = fahrenheit_a_celsius(f)
    print(f"{f} °F son {c:.2f} °C")

    assert abs(fahrenheit_a_celsius(212) - 100.0) < 0.001
    assert abs(fahrenheit_a_celsius(32) - 0.0) < 0.001
    print("✔ ¡Tu función pasa las pruebas locales!")