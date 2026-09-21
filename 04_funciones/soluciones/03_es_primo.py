"""SOLUCIÓN 3: ¿Es primo? ⭐⭐⭐

Estrategia de fuerza bruta: probamos todos los divisores posibles
entre 2 y n-1. Si encontramos uno, sale con False.
"""


def es_primo(n: int) -> bool:
    # 0 y 1 no son primos (esto también descarta negativos).
    if n < 2:
        return False

    # Probamos todos los divisores entre 2 y n-1.
    for divisor in range(2, n):
        if n % divisor == 0:
            return False   # encontramos un divisor: no es primo

    return True            # ningún divisor encontrado: es primo


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