"""Ejemplo 02: Parámetros y return en detalle.

La regla de oro: las funciones CALCULAN y DEVUELVEN con return;
los print van en el programa principal.

Ejecuta: python3 04_funciones/ejemplos/02_parametros_y_return.py
"""


# --- return devuelve un valor para usarlo después ---
def suma(a: int, b: int) -> int:
    return a + b


# --- sin return: la función devuelve None (¡trampa clásica!) ---
def suma_solo_imprime(a: int, b: int) -> None:
    print(a + b)


# --- Puedes llamar funciones dentro de otras funciones ---
def cuadrado(numero: int) -> int:
    return numero ** 2


def suma_de_cuadrados(x: int, y: int) -> int:
    return cuadrado(x) + cuadrado(y)


# --- return temprano: validar y salir ---
def dividir(a: float, b: float):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b


# --- Programa principal ---
resultado = suma(3, 4)
print(f"suma(3, 4) = {resultado}")

# Aquí está la trampa: la función imprime, pero su valor es None.
r = suma_solo_imprime(3, 4)      # # HUELLA: imprime 7
print(f"Pero el valor de r es: {r}")   # None

print(f"suma_de_cuadrados(2, 3) = {suma_de_cuadrados(2, 3)}")   # 4 + 9 = 13

print(dividir(10, 2))    # 5.0
print(dividir(10, 0))    # "No se puede dividir entre cero"

# --- Docstrings: documentación que se puede consultar ---
# help(suma) muestra el docstring + firma de la función.
print("\nDocumentación de suma():")
print(suma.__doc__)