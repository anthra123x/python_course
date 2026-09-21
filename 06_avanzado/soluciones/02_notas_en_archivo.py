"""SOLUCIÓN 2: Notas en archivo ⭐⭐⭐

La ruta puede venir como Path o str; ambos funcionan con open().
El patrón with garantiza que el archivo se cierre solo.
"""


def guardar_notas(ruta: str, notas: dict) -> None:
    with open(ruta, "w") as archivo:
        for nombre, puntaje in notas.items():
            archivo.write(f"{nombre}: {puntaje}\n")


def leer_notas(ruta: str) -> dict:
    try:
        with open(ruta, "r") as archivo:
            resultado = {}
            for linea in archivo:
                # "Ana: 95\n" → strip → "Ana: 95" → split(": ") → ["Ana", "95"]
                nombre, puntaje = linea.strip().split(": ")
                resultado[nombre] = int(puntaje)
            return resultado
    except FileNotFoundError:
        return {}


if __name__ == "__main__":
    ARCHIVO_PRUEBA = "mis_notas.txt"
    notas = {"Ana": 95, "Luis": 82}

    guardar_notas(ARCHIVO_PRUEBA, notas)
    leidas = leer_notas(ARCHIVO_PRUEBA)

    print("Notas leídas:", leidas)
    import os
    os.remove(ARCHIVO_PRUEBA)

    assert leidas == {"Ana": 95, "Luis": 82}
    assert leer_notas("archivo_inexistente.txt") == {}
    print("✔ ¡Tus funciones pasan las pruebas locales!")