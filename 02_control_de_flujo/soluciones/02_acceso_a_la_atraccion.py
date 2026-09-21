"""SOLUCIÓN 2: Acceso a la atracción ⭐⭐

El patrón "validar y salir temprano" (early return) hace el código
lineal y fácil de leer: cada regla fallida termina la función de inmediato.
"""


def puede_subir(edad: int, estatura: float, problemas_cardiacos: bool) -> str:
    # Regla 1: rango de edad
    if edad < 12 or edad > 65:
        return "No puedes subir: edad no permitida."

    # Regla 2: estatura mínima
    if estatura < 1.50:
        return "No puedes subir: estatura insuficiente."

    # Regla 3: salud (solo aplica si llegamos aquí)
    if problemas_cardiacos:
        return "No puedes subir: problemas cardiacos."

    # Si ninguna regla falló, puede subir.
    return "Puedes subir."


if __name__ == "__main__":
    e = int(input("Edad: "))
    es = float(input("Estatura (m): "))
    pc = input("¿Problemas cardiacos? (sí/no): ").lower() in ("si", "sí", "s")
    print(puede_subir(e, es, pc))

    assert puede_subir(20, 1.70, False) == "Puedes subir."
    assert puede_subir(10, 1.70, False) == "No puedes subir: edad no permitida."
    print("✔ ¡Tu función pasa las pruebas locales!")