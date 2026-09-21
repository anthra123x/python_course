"""EJERCICIO 2: Validador de contraseñas ⭐⭐⭐

Escribe una función `validar_contrasena(contrasena)` que verifique
que una contraseña cumpla estas 4 reglas de seguridad:

    1. Tener al menos 8 caracteres.          (usa len())
    2. Contener al menos un número.          (digito)
    3. Contener al menos una letra mayúscula.
    4. Contener al menos una letra minúscula.

Devuelve True si cumple TODAS; False en caso contrario.

PISTAS:
    - Recorre la contraseña con `for char in contrasena` y lleva
      contadores booleanos (hay_numero, hay_mayuscula, hay_minuscula).
    - Para saber si un carácter es un dígito:  char.isdigit()
    - Para mayúscula:  char.isupper()
    - Para minúscula:  char.islower()

Ejemplo:
    validar_contrasena("Abc12345")      ->  True
    validar_contrasena("abcdefgh")      ->  False  (sin números ni mayúsculas)
    validar_contrasena("corta1A")       ->  False  (menos de 8)
"""


def validar_contrasena(contrasena: str) -> bool:
    # TODO: implementa las 4 reglas con un for y contadores.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    clave = input("Crea una contraseña: ")
    if validar_contrasena(clave):
        print("✅ Contraseña válida")
    else:
        print("❌ La contraseña no cumple los requisitos")

    assert validar_contrasena("Abc12345") is True
    assert validar_contrasena("abcdefgh") is False
    assert validar_contrasena("corta1A") is False
    print("✔ ¡Tu función pasa las pruebas locales!")