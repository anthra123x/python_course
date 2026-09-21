# Módulo 02 · Control de flujo

> **Objetivo:** que tus programas tomen decisiones (`if`), repitan tareas (`while`, `for`) y no se traben jamás.

| Sección | Contenido |
|---------|-----------|
| 📖 Teoría | Condicionales, comparaciones, bucles, `break`, `continue` |
| 👀 Ejemplos | `ejemplos/` (ejecútalos con `python3 ejemplos/01_condicionales.py`) |
| ✍️ Práctica | `ejercicios/` (5 ejercicios para resolver) |
| ✅ Verificación | `python3 ../tools/verificar.py 02` |
| 🔍 Soluciones | `soluciones/` |

---

## 1. Condicionales: el programa decide

Un programa sin condicionales ejecuta todo en orden, siempre igual. Con `if/elif/else` adquiere **inteligencia**:

```python
edad = int(input("Tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres un niño o niña")
```

Reglas de oro:
- `if` evalúa una condición. Si es `True`, ejecuta su bloque.
- `elif` (else-if): **otra** condición para probar si la anterior fue falsa.
- `else`: lo que pasa si **ninguna** condición anterior fue verdadera.
- El bloque se marca con **indentación (4 espacios)**. En Python, la indentación es **parte de la sintaxis**, no decoración.
- El orden importa: Python prueba las condiciones de arriba hacia abajo.

### Condiciones que suelen confundir

```python
# == compara valores, = asigna
if 5 == 5:      # ✅ correcto
if 5 = 5:       # ❌ SyntaxError

# Múltiples condiciones
if edad >= 18 and tiene_identificacion:
if edad < 12 or altura < 1.20:
if not es_vip:
```

## 2. Operadores de comparación y lógicos

| Operador | Significado |
|----------|-------------|
| `==` | igual a |
| `!=` | distinto de |
| `>` `<` | mayor/menor |
| `>=` `<=` | mayor/menor o igual |
| `and` | ambas condiciones verdaderas |
| `or` | al menos una verdadera |
| `not` | niega la condición |

## 3. El bucle `while`: repite mientras…

```python
respuesta = ""
while respuesta != "python":
    respuesta = input("¿Qué lenguaje estás aprendiendo? ")

print("¡Correcto!")
```

- El bloque se repite **mientras** la condición sea `True`.
- ⚠️ **Riesgo de bucle infinito:** si la condición nunca se vuelve falsa, el programa no termina nunca. Asegúrate de que algo dentro del bucle cambie la condición (como `respuesta` arriba).
- Tip: `Ctrl+C` detiene un programa atascado.

## 4. El bucle `for`: recorre colecciones

```python
# Recorrer una lista
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

# Repetir un número exacto de veces
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2): # 2, 4, 6, 8  (inicio, fin exclusivo, paso)
    print(i)
```

`range(inicio, fin, paso)` es la forma canónica de "repetir N veces":
`fin` es **exclusivo** (no incluye el último número).

## 5. `break` y `continue`: el control fino

```python
for numero in range(10):
    if numero == 5:
        break        # ⛔ detiene el bucle por completo
    print(numero)     # 0 1 2 3 4

for numero in range(5):
    if numero == 2:
        continue     # ⏭️ salta a la siguiente iteración
    print(numero)     # 0 1 3 4
```

> Usa `break` con moderación: un bucle `while` bien diseñado normalmente no lo necesita.

---

## ✍️ Ejercicios

| # | Ejercicio | Dificultad |
|---|-----------|------------|
| 1 | Par o impar — decide según el residuo | ⭐ |
| 2 | Acceso a la atracción — validación estilo parque de diversiones | ⭐⭐ |
| 3 | Suma de N números — acumulador con `while` | ⭐⭐ |
| 4 | Tabla de multiplicar — `for` + f-strings | ⭐ |
| 5 | Buscador de números pares — clásico con `for` y `%` | ⭐⭐ |

**Verifica:** `python3 ../tools/verificar.py 02`

---

## 🕳️ Errores comunes (léelos antes de empezar)

- `if edad = 18:` — usar `=` en lugar de `==`. **SyntaxError garantizado.**
- Olvidar la indentación: `IndentationError: expected an indented block`.
- Bucle infinito: olvidar actualizar la variable de la condición dentro del `while`.
- `for i in range(1, 10):` creer que imprime el 10. **No imprime**: `range` es exclusivo al final.

---

## ✅ Checklist de fin de módulo

- [ ] Tus programas toman decisiones con `if/elif/else`.
- [ ] Sabes cuándo usar `while` vs `for`.
- [ ] Evitas bucles infinitos actualizando la condición.
- [ ] Los 5 ejercicios pasan `python3 ../tools/verificar.py 02`.

¿Todo verde? ¡Al [Módulo 03 — Estructuras de datos](../03_estructuras_de_datos/README.md)! 🎉