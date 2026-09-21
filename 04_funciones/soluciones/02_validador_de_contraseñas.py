"""SOLUCIÓN 2: Validador de contraseñas ⭐⭐⭐

El patrón es: barremos cada carácter con un for y prendemos banderas
(booleanos) cuando encontramos lo que buscamos. Al final, TODAS las
banderas deben estar encendidas.
"""


def validar_contrasena(contrasena: str) -> bool:
    # Condición 1: longitud mínima.
    if len(contrasena) < 8:
        return False

    # Banderas para las otras tres reglas.
    tiene_numero = False
    tiene_mayuscula = False
    tiene_minuscula = False

    for caracter in contrasena:
        if caracter.isdigit():
            tiene_numero = True
        elif caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True

    # Las tres deben ser True para aprobar.
    return tiene_numero and tiene_mayuscula and tiene_minuscula


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