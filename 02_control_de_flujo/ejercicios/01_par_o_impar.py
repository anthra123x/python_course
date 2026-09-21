"""EJERCICIO 1: Par o impar ⭐

Escribe una función `es_par` que reciba un número entero y devuelva
`True` si es par, `False` si es impar.

TIP:
    Un número es par si su residuo al dividirlo entre 2 es 0.
    Recuerda el operador módulo:  %

Ejemplo:
    es_par(4)   ->  True
    es_par(7)   ->  False
"""


def es_par(numero: int) -> bool:
    # TODO: devuelve True si numero % 2 == 0
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
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