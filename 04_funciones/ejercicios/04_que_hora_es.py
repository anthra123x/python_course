"""EJERCICIO 4: ¿Qué hora es? ⭐⭐

(Este ejercicio rescata un script clásico y lo convierte en función.)

Escribe `descanso_para(hora_limite)` que reciba la hora límite como
string "HH:MM" y devuelva el mensaje adecuado según la hora ACTUAL:

    - Si la hora actual es >= hora_limite:
          "Es hora de descansar 🎉"
    - Si falta más de una hora:
          "Aún falta un buen rato para descansar"
    - En otro caso (falta 1 hora o menos):
          "Ya casi, aguanta un poquito más"

PISTAS:
    - Usa datetime:
          from datetime import datetime
          ahora = datetime.now().time()
          limite = datetime.strptime(hora_limite, "%H:%M").time()
    - Puedes comparar objetos .time() directamente con >=.
    - Para "falta más de una hora", compara horas:
          hora_actual = ahora.hour
          hora_limite_entero = limite.hour
"""

from datetime import datetime


def descanso_para(hora_limite: str) -> str:
    # TODO: calcula la hora actual y decide el mensaje.
    pass  # Reemplaza esta línea


# --- Código de prueba: ejecuta este archivo para probar tu función ---
if __name__ == "__main__":
    print(descanso_para("14:00"))
    print(descanso_para("23:59"))

    # Como este ejercicio depende de la hora actual, los tests verifican
    # manualmente: menor >= 14:00 devuelve el mensaje de descanso.
    assert isinstance(descanso_para("23:59"), str)
    assert descanso_para("23:59") in (
        "Es hora de descansar 🎉",
        "Aún falta un buen rato para descansar",
        "Ya casi, aguanta un poquito más",
    )
    print("✔ ¡Tu función pasa las pruebas locales!")