"""EJERCICIO 2: Calculadora de edad ⭐

Escribe una función `ano_de_nacimiento` que reciba:
    - edad: int (la edad actual de la persona)
    - ano_actual: int (el año en curso)

y devuelva el año en que nació aproximadamente esa persona.

Ejemplo:
    ano_de_nacimiento(30, 2026)  ->  1996

TIP:
    Basta una resta. Si lo haces bien, los tests pasarán solos.
"""


def ano_de_nacimiento(edad: int, ano_actual: int) -> int:
    # TODO: calcula el año de nacimiento.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    edad = int(input("¿Cuántos años tienes? "))
    resultado = ano_de_nacimiento(edad, 2026)
    print(f"Probablemente naciste alrededor del año {resultado}.")

    assert ano_de_nacimiento(30, 2026) == 1996
    assert ano_de_nacimiento(10, 2026) == 2016
    print("✔ ¡Tu función pasa las pruebas locales!")