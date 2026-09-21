"""Ejemplo 02: Trabajar con archivos.

Tu lista de compras no debería desaparecer al cerrar el programa.
Con archivos, los datos sobreviven. Tres modos básicos:
    "w" = write  (sobreescribe)
    "r" = read   (lee)
    "a" = append (agrega al final)

Ejecuta: python3 06_avanzado/ejemplos/02_trabajar_con_archivos.py
"""

from pathlib import Path

# Nombre del archivo donde guardaremos (relativo a la carpeta del ejemplo).
ARCHIVO = Path(__file__).parent / "notas.txt"


def escribir_notas() -> None:
    """Sobreescribe el archivo con tres líneas."""
    with open(ARCHIVO, "w") as archivo:
        archivo.write("Ana: 95\n")
        archivo.write("Luis: 82\n")
        archivo.write("María: 78\n")
    print(f"✍️  Notas escritas en {ARCHIVO.name}")


def leer_notas() -> None:
    """Lee todo el archivo línea por línea."""
    try:
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                # .strip() quita el salto de línea final.
                print(f"   {linea.strip()}")
    except FileNotFoundError:
        print("⚠️  El archivo aún no existe. Escribe primero.")


def agregar_nota(nombre: str, puntaje: int) -> None:
    """Agrega una línea al final del archivo (sin borrar lo demás)."""
    with open(ARCHIVO, "a") as archivo:
        archivo.write(f"{nombre}: {puntaje}\n")
    print(f"➕ Nota de {nombre} agregada.")


if __name__ == "__main__":
    # 1. Escribimos desde cero.
    escribir_notas()

    # 2. Leemos lo que acabamos de escribir.
    print("\nContenido actual:")
    leer_notas()

    # 3. Agregamos una línea.
    print()
    agregar_nota("Pedro", 88)

    # 4. Leemos de nuevo: ahora tiene 4 líneas.
    print("\nContenido después de agregar:")
    leer_notas()

    # Si quieres empezar limpio la próxima vez, borra el archivo:
    # ARCHIVO.unlink()