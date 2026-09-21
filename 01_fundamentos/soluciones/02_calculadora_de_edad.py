"""SOLUCIÓN 2: Calculadora de edad ⭐

El año de nacimiento aproximado es simplemente: año actual - edad.
Nada más. Las matemáticas simples también son programación. 🙂
"""


def ano_de_nacimiento(edad: int, ano_actual: int) -> int:
    return ano_actual - edad


if __name__ == "__main__":
    edad = int(input("¿Cuántos años tienes? "))
    resultado = ano_de_nacimiento(edad, 2026)
    print(f"Probablemente naciste alrededor del año {resultado}.")

    assert ano_de_nacimiento(30, 2026) == 1996
    assert ano_de_nacimiento(10, 2026) == 2016
    print("✔ ¡Tu función pasa las pruebas locales!")