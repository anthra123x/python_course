"""EJERCICIO 1: Saludo personalizado ⭐

Escribe una función `saludar` que reciba un nombre (str) y devuelva
el texto:  "Hola, {nombre}. ¡Bienvenido a Python!"

Ejemplo:
    saludar("Ana")  ->  "Hola, Ana. ¡Bienvenido a Python!"

TIP:
    Usa un f-string:  f"Hola, {nombre}. ¡Bienvenido a Python!"
"""


def saludar(nombre: str) -> str:
    # TODO: construye y devuelve el saludo con un f-string.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    nombre = input("¿Cómo te llamas? ")
    print(saludar(nombre))

    assert saludar("Ana") == "Hola, Ana. ¡Bienvenido a Python!"
    assert saludar("Luis") == "Hola, Luis. ¡Bienvenido a Python!"
    print("✔ ¡Tu función pasa las pruebas locales!")