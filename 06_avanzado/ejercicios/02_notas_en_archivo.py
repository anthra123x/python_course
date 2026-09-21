"""EJERCICIO 2: Notas en archivo ⭐⭐⭐

Trabajar con archivos: guarda y lee calificaciones.

1. `guardar_notas(ruta, notas)` — recibe una ruta (str) y un
   diccionario {nombre: puntaje}. Escribe cada par como línea:
       "Ana: 95"
   con la ruta en modo "w" (sobreescribe).

2. `leer_notas(ruta)` — recibe una ruta, lee el archivo con modo "r"
   y devuelve un diccionario {nombre: puntaje} (convertido a int).
   Si el archivo no existe, devuelve {}.

PISTAS:
    - with open(ruta, "w") as archivo: ...
      for nombre, puntaje in notas.items():
          archivo.write(f"{nombre}: {puntaje}\n")
    - Para leer y construir el dict:
      for linea in archivo:
          nombre, puntaje = linea.strip().split(": ")
          resultado[nombre] = int(puntaje)
    - try/except FileNotFoundError para el caso del archivo inexistente.
"""


def guardar_notas(ruta: str, notas: dict) -> None:
    # TODO: escribe cada nombre y puntaje en el archivo.
    pass  # Reemplaza esta línea


def leer_notas(ruta: str) -> dict:
    # TODO: lee el archivo y devuelve el diccionario.
    #       Devuelve {} si el archivo no existe.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tus funciones ---
if __name__ == "__main__":
    ARCHIVO_PRUEBA = "mis_notas.txt"
    notas = {"Ana": 95, "Luis": 82}

    guardar_notas(ARCHIVO_PRUEBA, notas)
    leidas = leer_notas(ARCHIVO_PRUEBA)

    print("Notas leídas:", leidas)
    import os
    os.remove(ARCHIVO_PRUEBA)   # limpiamos el archivo de prueba

    assert leidas == {"Ana": 95, "Luis": 82}
    assert leer_notas("archivo_inexistente.txt") == {}
    print("✔ ¡Tus funciones pasan las pruebas locales!")