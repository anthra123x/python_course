"""EJERCICIO 2: Conteo de palabras ⭐⭐

Escribe una función `contar_palabras(texto)` que reciba un string y
devuelva un diccionario donde cada llave es una palabra y cada valor
es cuántas veces aparece.

TIP (el patrón contador que viste en el ejemplo 02):
    contador = {}
    for palabra in lista_de_palabras:
        contador[palabra] = contador.get(palabra, 0) + 1

Para separar el texto en palabras puedes usar .split():
    "hola mundo hola".split()  ->  ["hola", "mundo", "hola"]

Ejemplo:
    contar_palabras("hola mundo hola")  ->  {"hola": 2, "mundo": 1}
"""


def contar_palabras(texto: str) -> dict:
    # TODO: usa .split() y el patrón contador con .get().
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    print(contar_palabras(frase))

    assert contar_palabras("hola mundo hola") == {"hola": 2, "mundo": 1}
    assert contar_palabras("") == {}
    print("✔ ¡Tu función pasa las pruebas locales!")