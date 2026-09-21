"""SOLUCIÓN 4: ¿Qué hora es? ⭐⭐

datetime nos permite comparar horas directamente. Para medir cuánto
falta, comparamos la hora en formato entero (0-23).
"""

from datetime import datetime


def descanso_para(hora_limite: str) -> str:
    ahora = datetime.now().time()
    limite = datetime.strptime(hora_limite, "%H:%M").time()

    # Si ya pasó (o es) la hora límite: a descansar.
    if ahora >= limite:
        return "Es hora de descansar 🎉"

    # ¿Cuántas horas faltan aproximadamente?
    horas_faltantes = limite.hour - ahora.hour

    if horas_faltantes > 1:
        return "Aún falta un buen rato para descansar"
    else:
        return "Ya casi, aguanta un poquito más"


if __name__ == "__main__":
    print(descanso_para("14:00"))
    print(descanso_para("23:59"))

    assert isinstance(descanso_para("23:59"), str)
    assert descanso_para("23:59") in (
        "Es hora de descansar 🎉",
        "Aún falta un buen rato para descansar",
        "Ya casi, aguanta un poquito más",
    )
    print("✔ ¡Tu función pasa las pruebas locales!")