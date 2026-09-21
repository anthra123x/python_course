"""EJERCICIO 3: ¿Es primo? ⭐⭐⭐

Un número primo solo es divisible entre 1 y sí mismo.
Escribe la función `es_primo(n)` que devuelva True si `n` es primo.

Estrategia simple (no la más óptima, sí la más clara):
    1. Si n < 2, no es primo (0 y 1 NO son primos).
    2. Recorre con un for: `for divisor in range(2, n)`
    3. Si n % divisor == 0, encontramos un divisor: NO es primo → return False.
    4. Si terminaste el for sin encontrar divisores, es primo → return True.

Ejemplo:
    es_primo(7)   ->  True
    es_primo(10)  ->  False
    es_primo(1)   ->  False
"""


def es_primo(n: int) -> bool:
    # TODO: implementa la estrategia de arriba.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    numero = int(input("¿Qué número quieres evaluar? "))
    if es_primo(numero):
        print(f"{numero} SÍ es primo")
    else:
        print(f"{numero} NO es primo")

    assert es_primo(7) is True
    assert es_primo(10) is False
    assert es_primo(1) is False
    assert es_primo(2) is True
    print("✔ ¡Tu función pasa las pruebas locales!")