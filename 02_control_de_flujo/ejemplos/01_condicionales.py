"""Ejemplo 01: Condicionales — validación para subir a una atracción.

Este ejemplo es una versión corregida y comentada de un script clásico:
una montaña rusa con requisitos de edad, estatura y salud.

Observa el ORDEN de las condiciones: Python las evalúa de arriba hacia abajo,
y la primera que sea True ejecuta su bloque y se salta el resto.

Ejecuta: python3 02_control_de_flujo/ejemplos/01_condicionales.py
"""

# 1. Pedir datos (recuerda: input() devuelve texto, hay que convertirlo).
edad = int(input("Ingresa tu edad: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# 2. Reglas de seguridad del parque.
EDAD_MINIMA = 12
EDAD_MAXIMA = 65
ESTATURA_MINIMA = 1.55

# 3. Evaluación por capas: de la regla más general a la más específica.
#    Así el código es fácil de leer y de modificar.
if edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
    print("No puedes subir: tu edad está fuera del rango permitido.")

# elif: solo se evalúa si el if anterior fue falso.
elif estatura < ESTATURA_MINIMA:
    print("No puedes subir: no alcanzas la estatura mínima.")

# Para mayores de 40 se pregunta por problemas cardiacos (regla extra).
elif edad > 40:
    problema_cardiaco = input("¿Tienes algún problema cardiaco? (sí/no): ")

    # .lower() normaliza la respuesta para aceptar "SÍ", "Si", "sí"...
    if problema_cardiaco.lower() in ("si", "sí", "s"):
        print("No puedes subir por motivos de salud.")
    else:
        print("Puedes subir. ¡Disfruta!")

else:
    print("Puedes subir. ¡Disfruta!")

# Observación: "si" vs "sí". El código original usaba una sola "i" y un
# string truncado; aquí normalizamos y aceptamos ambas variantes para ser
# amables con quien escribe sin tilde. 🙂