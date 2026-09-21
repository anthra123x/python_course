"""EJERCICIO 1: Calculadora con validación ⭐⭐

Escribe una función `dividir(a, b)` que:
    1. Devuelva "Error: división entre cero" si `b` es 0.
       (USA try/except con ZeroDivisionError, no un if.)
    2. Devuelva el resultado de a / b en cualquier otro caso.

Escribe también `sumar_lista(numeros)` que sume una lista de números,
pero devuelva "Error: elementos no numéricos" si algún elemento no es
un número (int o float).

PISTAS:
    - El try captura el error; el except lo maneja con un mensaje.
    - suma = 0 y for elemento in numeros: suma += elemento.
    - Para el tipo: type(elemento) not in (int, float)

Ejemplo:
    dividir(10, 2)         ->  5.0
    dividir(10, 0)         ->  "Error: división entre cero"
    sumar_lista([1, 2, 3]) ->  6
"""


def dividir(a: float, b: float):
    # TODO: envuelve a / b en try/except ZeroDivisionError.
    pass  # Reemplaza esta línea


def sumar_lista(numeros: list):
    # TODO: suma los números; si hay un elemento no numérico,
    #       devuelve el mensaje de error.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tus funciones ---
if __name__ == "__main__":
    print(dividir(10, 2))
    print(dividir(10, 0))
    print(sumar_lista([1, 2, 3]))
    print(sumar_lista([1, "dos", 3]))

    assert dividir(10, 2) == 5.0
    assert dividir(10, 0) == "Error: división entre cero"
    assert sumar_lista([1, 2, 3]) == 6
    print("✔ ¡Tus funciones pasan las pruebas locales!")