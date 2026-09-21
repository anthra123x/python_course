"""Ejemplo 01: Manejo de errores con try/except.

Aprender a leer errores y a proteger tu programa de ellos es una
habilidad tan importante como la sintaxis. Aquí verás los patrones
clásicos.

Ejecuta: python3 06_avanzado/ejemplos/01_manejo_de_errores.py
"""

# --- 1. ValueError: convertir texto inválido ---
def pedir_entero(mensaje: str) -> int:
    """Pide un entero y NO se detiene hasta conseguirlo."""
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("⚠️  Eso no es un número entero. Intenta de nuevo.")


# --- 2. ZeroDivisionError: dividir entre cero ---
def dividir_seguro(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        print("⚠️  No se puede dividir entre cero.")
        return 0.0


# --- 3. KeyError: llave inexistente en un diccionario ---
def obtener_valor(datos: dict, llave: str):
    try:
        return datos[llave]
    except KeyError:
        return f"⚠️  La llave '{llave}' no existe en el diccionario."


# --- 4. FileNotFoundError: archivo inexistente ---
def leer_archivo(ruta: str) -> str:
    try:
        with open(ruta, "r") as archivo:
            return archivo.read()
    except FileNotFoundError:
        return f"⚠️  No encontré el archivo '{ruta}'."


# --- 5. except genérico: último recurso ---
def conversion_todo_terreno(texto: str) -> int:
    try:
        return int(texto)
    except (ValueError, TypeError) as error:
        # Capturamos varios errores en un solo except.
        print(f"⚠️  Error capturado: {error}")
        return 0


# --- Programa principal ---
if __name__ == "__main__":
    edad = pedir_entero("Tu edad: ")
    print(f"Tienes {edad} años.")

    print(dividir_seguro(10, 0))
    print(dividir_seguro(10, 2))

    persona = {"nombre": "Ana"}
    print(obtener_valor(persona, "email"))
    print(obtener_valor(persona, "nombre"))

    print(leer_archivo("archivo_que_no_existe.txt"))

    print(conversion_todo_terreno("123"))     # 123
    print(conversion_todo_terreno("abc"))     # 0 + mensaje
    print(conversion_todo_terreno(None))      # 0 + mensaje