"""SOLUCIÓN 4: Agenda de contactos ⭐⭐⭐

La agenda es un diccionario de diccionarios. Cada operación trabaja
una "ficha" (el diccionario interno) del contacto elegido.
"""


def agregar_contacto(agenda: dict, nombre: str, telefono: str) -> dict:
    # Cada contacto empieza con su teléfono y un contador de llamadas.
    agenda[nombre] = {"telefono": telefono, "llamadas": 1}
    return agenda


def registrar_llamada(agenda: dict, nombre: str) -> dict:
    # Solo registramos si el contacto existe; .get() evita el KeyError.
    if nombre in agenda:
        agenda[nombre]["llamadas"] += 1
    return agenda


if __name__ == "__main__":
    agenda = {}
    agenda = agregar_contacto(agenda, "ana", "+591 70012345")
    agenda = agregar_contacto(agenda, "luis", "+591 71054321")
    agenda = registrar_llamada(agenda, "ana")
    agenda = registrar_llamada(agenda, "ana")

    for nombre, datos in agenda.items():
        print(f"{nombre}: {datos}")

    assert agenda["ana"]["llamadas"] == 3
    assert agenda["luis"]["llamadas"] == 1
    print("✔ ¡Tus funciones pasan las pruebas locales!")