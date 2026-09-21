# Módulo 06 · Avanzado: errores, archivos y una pizca de GUI

> **Objetivo:** hacer tus programas a prueba de balas (manejo de errores), capaces de guardar datos en archivos, y con interfaz gráfica.

| Sección | Contenido |
|---------|-----------|
| 📖 Teoría | `try/except`, `with open`, tkinter |
| 👀 Ejemplos | `ejemplos/` (¡el 03 es un formulario gráfico que funciona!) |
| ✍️ Práctica | `ejercicios/` (2 ejercicios) |
| ✅ Verificación | `python3 ../tools/verificar.py 06` |
| 🔍 Soluciones | `soluciones/` |

---

## 1. Manejo de errores: `try` / `except`

Los programas reciben datos del mundo real, y el mundo real es caótico. En vez de que tu programa se estrelle, capturas el error y decides qué hacer:

```python
try:
    numero = int(input("Dame un número: "))
    print(10 / numero)
except ValueError:
    print("❌ Eso no era un número.")
except ZeroDivisionError:
    print("❌ No puedes dividir entre cero.")
```

- El código "peligroso" va dentro de `try`.
- Si lanza un error del tipo indicado, se ejecuta el `except` correspondiente.
- Sin `try/except`, un `ValueError` termina el programa con un traceback feo.

Los errores más comunes que verás:

| Error | Cuándo ocurre |
|-------|---------------|
| `ValueError` | Convertir `"abc"` a `int()` |
| `ZeroDivisionError` | Dividir entre 0 |
| `FileNotFoundError` | Abrir un archivo que no existe |
| `KeyError` | Preguntar por una llave inexistente en un dict |
| `TypeError` | Operar tipos incompatibles (`"5" + 5`) |

## 2. Archivos: guardar datos para siempre

Un programa que pierde sus datos al cerrar es un programa limitado. Con archivos, tu lista de compras sobrevive al cierre.

```python
# ESCRIBIR (sobreescribe si existe):
with open("datos.txt", "w") as archivo:    # "w" = write
    archivo.write("Hola, archivo!\n")       # \n es salto de línea

# LEER:
with open("datos.txt", "r") as archivo:    # "r" = read
    contenido = archivo.read()              # todo el texto

# AGREGAR al final sin borrar:
with open("datos.txt", "a") as archivo:    # "a" = append
    archivo.write("Otra línea\n")
```

> ✨ El bloque `with` cierra el archivo automáticamente (aunque haya errores). **No uses `archivo.close()` manualmente.**

## 3. Interfaz gráfica con tkinter

tkinter viene incluido en Python (Windows y Mac; en Linux quizá requiera `sudo apt install python3-tk`). Permite crear ventanas, botones y campos de texto.

Tiny ejemplo:

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
etiqueta = tk.Label(ventana, text="¡Hola, GUI!")
etiqueta.pack()
ventana.mainloop()   # mantiene la ventana abierta
```

> 💡 El ejemplo 03 del módulo es una **calculadora gráfica** reconstruida desde un script roto que intentaba `import thinker` (módulo que no existe). Ahora usa `tkinter` de verdad y funciona.

---

## ✍️ Ejercicios

| # | Ejercicio | Dificultad |
|---|-----------|------------|
| 1 | Calculadora con validación — envuelve operaciones en `try/except` | ⭐⭐ |
| 2 | Notas en archivo — guarda y lee calificaciones con `with open` | ⭐⭐⭐ |

**Verifica:** `python3 ../tools/verificar.py 06`

---

## ✅ Checklist de fin de módulo

- [ ] Uso `try/except` para proteger mi programa de entradas inválidas.
- [ ] Leo y escribo archivos con `with open`.
- [ ] Creé una ventana con tkinter (ejecutando el ejemplo 03).
- [ ] Los 2 ejercicios pasan `python3 ../tools/verificar.py 06`.

---

# 🎓 ¡FELICIDADES, GRADUADO/A!

Completaste el curso **Python desde cero — Aprende haciendo**. Ya puedes:
- ✅ Leer y entender código Python ajeno.
- ✅ Construir programas de consola completos.
- ✅ Validar entradas y manejar errores con gracia.
- ✅ Persistir datos en archivos.
- ✅ Incluso hacer pequeñas interfaces gráficas.

**¿Qué sigue?** El siguiente escalón natural es:
1. **Git y GitHub** — versiona tus proyectos (ya estás en un repo, ¡usa `git log`!).
2. **Programación orientada a objetos** — clases y objetos.
3. **Un framework web** — Flask o FastAPI para llevar tus programas a internet.

¡Nos vemos en el siguiente curso! 🚀