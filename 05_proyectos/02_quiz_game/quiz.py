"""Proyecto 02: Quiz de computación.

Versión corregida y mejorada del quiz original. Ahora cada pregunta es
un diccionario, las respuestas aceptan variaciones (mayúsculas, tildes)
y el puntaje se calcula en porcentaje.
"""

import random  # (lo usaremos en la mejora 1; ya está listo para ti)


def normalizar(texto: str) -> str:
    """Convierte la respuesta a minúsculas, sin espacios extra.

    Así "  SI " y "sí" y "Si" se comparan igual contra "si".
    """
    return texto.strip().lower()


def preguntar_si_jugar() -> bool:
    """Pregunta si quiere jugar; acepta varias formas de decir sí."""
    respuesta = normalizar(input("¿Quieres jugar al quiz de computación? (sí/no): "))

    # También aceptamos "yes"/"y" por si alguien responde en inglés.
    return respuesta in ("si", "sí", "s", "yes", "y")


def mostrar_pregunta(pregunta: dict, numero: int) -> bool:
    """Muestra la pregunta y las opciones; devuelve True si acierta."""
    print(f"\n📝 Pregunta {numero}: {pregunta['pregunta']}")

    # Las opciones están en una lista; recorremos con índice para
    # mostrarlas numeradas (a, b, c, d).
    letras = ["a", "b", "c", "d"]
    for letra, opcion in zip(letras, pregunta["opciones"]):
        print(f"   {letra}) {opcion}")

    respuesta = normalizar(input("Tu respuesta: "))

    # La respuesta correcta está guardada como letra: "b", "c"...
    return respuesta == pregunta["correcta"]


# Cada pregunta es un diccionario: pregunta / opciones / letra correcta.
PREGUNTAS = [
    {
        "pregunta": "¿Qué significa CPU?",
        "opciones": ["Unidad Central de Proceso", "Unidad de Cómputo Personalizada",
                     "Procesador de Cálculos Únicos", "Control de Procesos de Usuario"],
        "correcta": "a",
    },
    {
        "pregunta": "¿Qué significa GPU?",
        "opciones": ["Unidad de Generación de Programas", "Unidad de Procesamiento Gráfico",
                     "Procesador General de Usuario", "Generador de Procesos Únicos"],
        "correcta": "b",
    },
    {
        "pregunta": "¿Qué lenguaje se usa principalmente para crear páginas web?",
        "opciones": ["Python", "HTML", "SQL", "Ensamble"],
        "correcta": "b",
    },
    {
        "pregunta": "¿Cuál de estos es un sistema operativo?",
        "opciones": ["Microsoft Word", "Google Chrome", "Linux", "Python"],
        "correcta": "c",
    },
    {
        "pregunta": "¿Qué hace el operador % en Python?",
        "opciones": ["Divide", "Multiplica", "Calcula el porcentaje literal",
                     "Devuelve el residuo de la división"],
        "correcta": "d",
    },
]


def jugar() -> None:
    """Bucle principal del quiz."""
    print("💻 ¡Bienvenido al Quiz de Computación!")

    if not preguntar_si_jugar():
        print("👋 ¡Hasta la próxima!")
        return

    print("¡Vamos! Responde a, b, c o d.\n")

    puntaje = 0
    total = len(PREGUNTAS)

    for indice, pregunta in enumerate(PREGUNTAS, start=1):
        if mostrar_pregunta(pregunta, indice):
            print("   ✅ ¡Correcto!")
            puntaje += 1
        else:
            print(f"   ❌ Incorrecto. La correcta era: {pregunta['correcta']}")

    # Reporte final con porcentaje.
    porcentaje = puntaje / total * 100
    print("\n" + "=" * 40)
    print(f"🏆 Puntaje final: {puntaje}/{total}  ({porcentaje:.0f}%)")

    if porcentaje == 100:
        print("🌟 ¡PERFECTO! Eres todo un experto.")
    elif porcentaje >= 60:
        print("👍 ¡Buen trabajo! Sigue así.")
    else:
        print("📚 ¡Sigue practicando! Repasa los módulos 1 al 4.")


if __name__ == "__main__":
    # random.shuffle(PREGUNTAS)  ← descomenta esta línea para la mejora 1 😉
    jugar()