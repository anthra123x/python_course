# Módulo 04 · Funciones y módulos

> **Objetivo:** dividir tus programas en piezas reutilizables con funciones, y usar los módulos de la biblioteca estándar.

| Sección | Contenido |
|---------|-----------|
| 📖 Teoría | `def`, parámetros, `return`, alcance, módulos (`random`, `datetime`) |
| 👀 Ejemplos | `ejemplos/` |
| ✍️ Práctica | `ejercicios/` (4 ejercicios) |
| ✅ Verificación | `python3 ../tools/verificar.py 04` |
| 🔍 Soluciones | `soluciones/` |

---

## 1. ¿Por qué funciones?

Un programa grande escrito todo en línea es ilegible. Las funciones:

- **Dividen** el problema en piezas pequeñas y nombradas.
- **Evitan repetir** código (escribe una vez, usa mil veces).
- **Aíslan errores**: cada función se prueba sola.

```python
def saludar(nombre):
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}!"

mensaje = saludar("Ana")
print(mensaje)          # Hola, Ana!
```

Anatomía de una función:

```
def  nombre(parametros):
    """docstring: explica qué hace"""
    ... cuerpo ...
    return valor        # opcional
```

- `def` la define; el cuerpo se marca con indentación.
- `parametros` son los datos de entrada (pueden ser cero: `def menu():`).
- `return` devuelve un valor. Sin `return`, la función devuelve `None`.

## 2. Parámetros: con valores por defecto y varios argumentos

```python
def presentar(nombre, edad=18):
    return f"{nombre} tiene {edad} años"

presentar("Ana")            # Ana tiene 18 años  (usa el default)
presentar("Ana", 30)        # Ana tiene 30 años
```

- Parámetros con valor por defecto son opcionales y van **al final**.
- Orden respetado: `presentar("Ana", 30)` → `nombre="Ana"`, `edad=30`.

## 3. `return` vs `print`

Diferencia sutil y crítiva:

```python
def suma(a, b):
    return a + b        # devuelve el resultado para usarlo después

def muestra_suma(a, b):
    print(a + b)        # solo imprime, devuelve None
```

```
resultado = suma(2, 3)        # resultado vale 5
resultado = muestra_suma(2,3) # imprime 5, pero resultado vale None
```

Regla de oro: **las funciones calculan y devuelven (`return`); los `print` van en el programa principal.**

## 4. Alcance (scope): lo de adentro es de adentro

```python
def funcion():
    variable_local = 10    # solo existe DENTRO de la función
    return variable_local

# print(variable_local)    # ❌ NameError: no existe fuera
```

- Las variables creadas dentro de una función son **locales**.
- Para leer valores globales dentro de una función, puedes pasar como parámetro (preferible) o usar `global` (evítalo).

## 5. Módulos: bibliotecas listas para usar

Python trae cientos de módulos de regalo (no hay que instalar nada).

```python
import random             # números aleatorios (¡clave para juegos!)
import datetime           # fechas y horas
from math import pi, sqrt # importar cosas específicas
```

```python
import random
print(random.randint(1, 10))     # entero aleatorio entre 1 y 10
print(random.choice(["a", "b"])) # elige un elemento al azar

from datetime import datetime
ahora = datetime.now()
print(ahora.hour)                # la hora actual (0-23)
```

> 💡 Usa `from modulo import cosa` cuando solo necesites una o dos cosas.

---

## ✍️ Ejercicios

| # | Ejercicio | Dificultad |
|---|-----------|------------|
| 1 | Calculadora de notas — convierte puntaje a calificación | ⭐⭐ |
| 2 | Validador de contraseñas — aplicación de reglas de seguridad | ⭐⭐⭐ |
| 3 | ¿Es primo? — clásico de entrevistas técnicas | ⭐⭐⭐ |
| 4 | ¿Qué hora es? — `datetime` + funciones | ⭐⭐ |

**Verifica:** `python3 ../tools/verificar.py 04`

---

## 🕳️ Errores comunes

- `NameError: name 'x' is not defined` — usaste una variable antes de crearla, o una local fuera de su función.
- Olvidar `return` y luego preguntarte por qué la función devuelve `None`.
- `TypeError: suma() missing 1 required positional argument` — llamaste con menos argumentos de los definidos.
- Confundir parámetro (lo que define la función) con argumento (lo que le pasas al llamarla).

---

## ✅ Checklist de fin de módulo

- [ ] Defino funciones con `def`, parámetros y `return`.
- [ ] Uso parámetros con valor por defecto.
- [ ] Entiendo la diferencia entre `return` y `print`.
- [ ] Importo módulos con `import` y `from ... import`.
- [ ] Los 4 ejercicios pasan `python3 ../tools/verificar.py 04`.

¿Todo verde? ¡Llegó el momento de **crear**! Al [Módulo 05 — Proyectos](../05_proyectos/README.md) 🎉