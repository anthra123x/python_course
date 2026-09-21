"""SOLUCIÓN 1: Calculadora con validación ⭐⭐

El try captura el ZeroDivisionError y lo convertimos en un mensaje
amable. El segundo ejercicio valida tipos antes de sumar.
"""


def dividir(a: float, b: float):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división entre cero"


def sumar_lista(numeros: list):
    suma = 0

    for elemento in numeros:
        # type(elemento) *no* es int ni float → no es un número.
        if type(elemento) not in (int, float):
            return "Error: elementos no numéricos"
        suma += elemento

    return suma


if __name__ == "__main__":
    print(dividir(10, 2))
    print(dividir(10, 0))
    print(sumar_lista([1, 2, 3]))
    print(sumar_lista([1, "dos", 3]))

    assert dividir(10, 2) == 5.0
    assert dividir(10, 0) == "Error: división entre cero"
    assert sumar_lista([1, 2, 3]) == 6
    print("✔ ¡Tus funciones pasan las pruebas locales!")