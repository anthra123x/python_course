"""EJERCICIO 4: Agenda de contactos ⭐⭐⭐

Crea una mini agenda. Cada contacto es un diccionario, y la agenda es
un diccionario que asocia el NOMBRE del contacto a su diccionario.

Escribe dos funciones:

1. `agregar_contacto(agenda, nombre, telefono)`:
   Agrega a la agenda un contacto con su teléfono. Los contactos nuevos
   empiezan con 1 llamada registrada.

   Estructura esperada:
       agenda["ana"]  ->  {"telefono": "+591 70012345", "llamadas": 1}

2. `registrar_llamada(agenda, nombre)`:
   Suma 1 al contador "llamadas" del contacto. Si el contacto no existe,
   no hace nada (usa .get() para preguntar).

Ejemplo:
    agenda = {}
    agenda = agregar_contacto(agenda, "ana", "+591 70012345")
    agenda = registrar_llamada(agenda, "ana")
    agenda["ana"]["llamadas"]  ->  2
"""


def agregar_contacto(agenda: dict, nombre: str, telefono: str) -> dict:
    # TODO: agenda[nombre] = {"telefono": telefono, "llamadas": 1}
    pass  # Reemplaza esta línea


def registrar_llamada(agenda: dict, nombre: str) -> dict:
    # TODO: si nombre está en agenda, suma 1 a agenda[nombre]["llamadas"].
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tus funciones ---
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