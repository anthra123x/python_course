"""Proyecto 04: Calculadora.

Una calculadora con menú que usa un diccionario de funciones.
Si la ejecutas y algo se rompe por una entrada rara, el try/except
se encarga de avisar sin cerrar el programa.
"""


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    # La división entre cero lanza ZeroDivisionError.
    # Lo PREVENIMOS aquí para dar un mensaje amigable.
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def potencia(a: float, b: float) -> float:
    return a ** b


# Diccionario: la llave es la opción del menú, el valor es la función.
OPERACIONES = {
    "1": sumar,
    "2": restar,
    "3": multiplicar,
    "4": dividir,
    "5": potencia,
}


def pedir_numero(mensaje: str) -> float:
    """Pide un número y lo valida con try/except.

    int() y float() lanzan ValueError cuando el texto no es un número.
    """
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("⚠️ Eso no es un número. Intenta de nuevo.")


def mostrar_menu() -> None:
    print("\n" + "=" * 30)
    print("🧮 CALCULADORA")
    print("=" * 30)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Salir")


def main() -> None:
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == "6":
            print("👋 ¡Hasta la próxima!")
            break

        if opcion not in OPERACIONES:
            print("⚠️ Opción inválida.")
            continue

        # Pedimos los dos números y ejecutamos la operación del diccionario.
        a = pedir_numero("Primer número: ")
        b = pedir_numero("Segundo número: ")

        try:
            resultado = OPERACIONES[opcion](a, b)
            # :.2f formatea con 2 decimales.
            print(f"→ Resultado: {resultado:.2f}")
        except ValueError as error:
            # Capturamos el error de división entre cero y cualquier otro.
            print(f"❌ {error}")


if __name__ == "__main__":
    main()