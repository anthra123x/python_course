# Proyecto 01 · Adivina el número

> Un clásico de iniciación: la computadora elige un número secreto y tú debes adivinarlo con pistas.

## 🎮 Requisitos

- El programa elige un número aleatorio entre 1 y 100 (`random.randint`).
- Pide al usuario que adivine.
- Si el intento es **menor** al secreto → pista: *"Demasiado bajo"*.
- Si el intento es **mayor** → pista: *"Demasiado alto"*.
- Contador de intentos: al final, muestra cuántos intentos necesitó.
- Si el usuario escribe algo que no es un número → mensaje amable y sigue.

## ▶️ Ejecutar

```bash
python3 05_proyectos/01_adivina_el_numero/juego.py
```

## 🧩 Conceptos que practicas

| Concepto | Dónde lo ves |
|----------|--------------|
| `import random` | Elegir el número secreto |
| `while` | Repetir hasta acertar |
| `if/elif/else` | Dar la pista correcta (bajo/alto) |
| Validación de entrada | `try/except ValueError` para texto no numérico |
| Acumulador | Contar intentos |

## 🚀 Ideas de mejora

1. Permite que el usuario elija el rango (mínimo y máximo).
2. Agrega dificultades: fácil (1–50), media (1–100), difícil (1–1000).
3. Lleva el récord y muestra "¡Nuevo récord!" cuando se supere.
4. Limita los intentos: si los agota, muestra el número secreto.
5. ¿Solo 3 pistas? "Frío", "tibio", "caliente" según la cercanía al número.