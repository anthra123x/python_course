"""Proyecto 01: Adivina el número.

Versión corregida y ampliada de un script original. Los problemas del
original: (1) el rango era solo 1-10, (2) la pista SIEMPRE decía
"Demasiado pequeño" aunque el intento fuera mayor, y (3) si escribías
texto en vez de número, el programa se estrellaba con ValueError.

Aquí cada uno de esos problemas tiene solución comentada.
"""

import random


def pedir_intento(minimo: int, maximo: int) -> int:
    """Pide un número al usuario y lo valida.

    El try/except captura el ValueError que lanza int() cuando el
    usuario escribe texto ("abc") en vez de un número.
    """
    while True:
        entrada = input(f"Adivina un número entre {minimo} y {maximo}: ")
        try:
            intento = int(entrada)
            if minimo <= intento <= maximo:
                return intento
            print(f"⚠️ El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            # int("abc") lanza ValueError; aquí avisamos y seguimos.
            print("⚠️ Eso no parece un número. Intenta de nuevo.")


def jugar(minimo: int = 1, maximo: int = 100) -> None:
    """Bucle principal del juego."""
    print("🎲 ¡Bienvenido a Adivina el número!")
    print(f"Estoy pensando en un número entre {minimo} y {maximo}...")

    # random.randint(inicio, fin) incluye ambos extremos.
    secreto = random.randint(minimo, maximo)
    intentos = 0

    while True:
        intento = pedir_intento(minimo, maximo)
        intentos += 1                      # acumulador de intentos

        if intento < secreto:
            print("📉 Demasiado BAJO. Intenta con un número mayor.")
        elif intento > secreto:
            print("📈 Demasiado ALTO. Intenta con un número menor.")
        else:
            # ¡Acierto! La única forma de salir del while.
            print(f"🎉 ¡Correcto! El número era {secreto}.")
            print(f"🏆 Lo lograste en {intentos} intento(s).")
            return


# El famoso "if __name__": este bloque SOLO se ejecuta si corres este
# archivo directamente (no si lo importas desde otro programa).
if __name__ == "__main__":
    jugar()