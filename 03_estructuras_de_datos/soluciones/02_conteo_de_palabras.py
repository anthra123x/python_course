"""SOLUCIÓN 2: Conteo de palabras ⭐⭐

El patrón contador con .get() es una joya: si la llave no existe,
.get(palabra, 0) devuelve 0 y la inicializamos en 1.
"""


def contar_palabras(texto: str) -> dict:
    contador = {}

    for palabra in texto.split():
        # Si "palabra" existía, sumamos 1 a su valor;
        # si no existía, .get devuelve 0 y empezamos en 1.
        contador[palabra] = contador.get(palabra, 0) + 1

    return contador


if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    print(contar_palabras(frase))

    assert contar_palabras("hola mundo hola") == {"hola": 2, "mundo": 1}
    assert contar_palabras("") == {}
    print("✔ ¡Tu función pasa las pruebas locales!")