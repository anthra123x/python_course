# Proyecto 02 · Quiz de computación

> Un cuestionario interactivo con puntaje, basado en un script original con dos bugs clásicos que ahora están resueltos.

## 🐛 Los bugs del original (aprende de ellos)

```python
# BUG 1: .lower es el MÉTODO, .lower() es la LLAMADA.
# El original comparaba el método contra "yes" → SIEMPRE False.
if playing.lower() != "yes":    # ✅ correcto
if playing.lower != "yes":      # ❌ bug (compara método, no resultado)

# BUG 2: la respuesta correcta solo aceptaba el texto EXACTO.
# "Central Processing Unit" se marcaba como incorrecta.
if respuesta.lower() == "central processing unit":   # ✅
if respuesta.lower == "central processing unit":     # ❌ bug
```

**Regla mental:** en Python, los métodos se *llaman* con `()`. `cadena.lower` es el método en sí (nunca se ejecuta); `cadena.lower()` es el resultado.

## 🎮 Requisitos

- Pregunta al inicio si quiere jugar (acepta "sí", "si", "s", "yes", "y"...).
- Bank de 5 preguntas con 4 opciones cada una.
- Cada pregunta vale 1 punto; al final muestra el puntaje y porcentaje.
- Recomienda "¡sigue practicando!" si el puntaje es bajo.

## ▶️ Ejecutar

```bash
python3 05_proyectos/02_quiz_game/quiz.py
```

## 🚀 Ideas de mejora

1. Mezcla las preguntas en cada partida: `random.shuffle(preguntas)`.
2. Agrega más preguntas o un segundo banco temático.
3. Haz las preguntas aleatorias: elige al azar entre varios bancos.
4. Agrega un temporizador... (spoiler: verás cómo en el módulo 06).
5. Muestra la pregunta correcta cuando el usuario falla.