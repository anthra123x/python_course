"""EJERCICIO 2: Acceso a la atracción ⭐⭐

Un parque de diversiones tiene estas reglas para una montaña rusa:
    1. Debes tener entre 12 y 65 años (incluidos).
    2. Estatura mínima: 1.50 m.
    3. Si tienes más de 40 años, se pregunta por problemas cardiacos.

Escribe la función `puede_subir(edad, estatura, problemas_cardiacos)` que
reciba:
    - edad: int
    - estatura: float (en metros)
    - problemas_cardiacos: bool (True si la persona los tiene)

y devuelva:
    - "No puedes subir: edad no permitida."       si falla la regla 1
    - "No puedes subir: estatura insuficiente."   si falla la regla 2
    - "No puedes subir: problemas cardiacos."     si tiene problemas cardiacos
    - "Puedes subir."                             si cumple todo

TIP:
    Evalúa primero la regla más general y devuelve temprano.
    El orden de los `if` importa: la edad se evalúa primero.
"""


def puede_subir(edad: int, estatura: float, problemas_cardiacos: bool) -> str:
    # TODO: implementa las 4 reglas con if/elif/else (o if + return).
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    e = int(input("Edad: "))
    es = float(input("Estatura (m): "))
    pc = input("¿Problemas cardiacos? (sí/no): ").lower() in ("si", "sí", "s")
    print(puede_subir(e, es, pc))

    assert puede_subir(20, 1.70, False) == "Puedes subir."
    assert puede_subir(10, 1.70, False) == "No puedes subir: edad no permitida."
    print("✔ ¡Tu función pasa las pruebas locales!")