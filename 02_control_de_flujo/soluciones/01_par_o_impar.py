"""SOLUCIÓN 1: Par o impar ⭐

El operador % (módulo) devuelve el residuo de una división.
Si el residuo al dividir entre 2 es 0, el número es par.
"""


def es_par(numero: int) -> bool:
    # La expresión numero % 2 == 0 ya es True/False, se devuelve directo.
    return numero % 2 == 0


if __name__ == "__main__":
    num = int(input("Dame un número: "))
    if es_par(num):
        print(f"{num} es par")
    else:
        print(f"{num} es impar")

    assert es_par(4) is True
    assert es_par(7) is False
    assert es_par(0) is True
    print("✔ ¡Tu función pasa las pruebas locales!")