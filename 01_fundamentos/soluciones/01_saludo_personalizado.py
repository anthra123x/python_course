"""SOLUCIÓN 1: Saludo personalizado ⭐

La clave está en usar un f-string para interpolar la variable `nombre`
dentro del texto. Compara con tu intento antes de seguir adelante.
"""


def saludar(nombre: str) -> str:
    # f-string: todo lo que va entre {} se evalúa como expresión.
    return f"Hola, {nombre}. ¡Bienvenido a Python!"


if __name__ == "__main__":
    nombre = input("¿Cómo te llamas? ")
    print(saludar(nombre))

    assert saludar("Ana") == "Hola, Ana. ¡Bienvenido a Python!"
    assert saludar("Luis") == "Hola, Luis. ¡Bienvenido a Python!"
    print("✔ ¡Tu función pasa las pruebas locales!")