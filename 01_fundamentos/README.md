# Módulo 01 · Fundamentos

> **Objetivo:** escribir tu primer programa en Python: pedir datos, hacer cálculos y mostrar resultados.

| Sección | Contenido |
|---------|-----------|
| 📖 Teoría | Variables, tipos de datos, `input`, `print`, operadores, strings |
| 👀 Ejemplos | `ejemplos/` (ejecútalos con `python3 ejemplos/01_variables_y_tipos.py`) |
| ✍️ Práctica | `ejercicios/` (4 ejercicios para resolver) |
| ✅ Verificación | `python3 ../tools/verificar.py 01` |
| 🔍 Soluciones | `soluciones/` (solo después de intentarlo) |

---

## 1. Variables: las cajas donde guardas cosas

Una variable es una **caja con nombre** donde guardas un valor para usarlo después.

```python
nombre = "Ana"     # guarda texto
edad = 30          # guarda un número entero
altura = 1.65      # guarda un número decimal
```

- El `=` asigna el valor de la derecha al nombre de la izquierda (**no** significa "igual a").
- Los nombres son libres, pero usa **minúsculas con guion bajo**: `mi_edad`, `total_compra`.
  Nunca uses espacios ni empieces con un número: `3edad` ❌, `edad_3` ✅.
- Los nombres describen su contenido: `precio_cafe` es mucho mejor que `x`.

## 2. Tipos de datos básicos

Python reconoce distintos tipos de valores; conocerlos evita el error #1 de principiantes:

| Tipo | Ejemplo | Para qué sirve |
|------|---------|----------------|
| `int` | `42`, `-7` | Números enteros |
| `float` | `3.14`, `1.5` | Números decimales |
| `str` (string) | `"hola"`, `'mundo'`, `"42"` | Texto (¡ojo! `"42"` es texto, no número) |
| `bool` | `True`, `False` | Verdadero o falso |

Puedes saber el tipo de cualquier valor con `type(...)`:

```python
print(type(42))      # <class 'int'>
print(type("42"))    # <class 'str'>
```

## 3. Mostrar y pedir datos: `print()` e `input()`

```python
print("Hola desde Python")              # muestra texto
nombre = input("¿Cómo te llamas? ")     # pide texto y lo guarda en nombre
print("Mucho gusto,", nombre)           # imprime con una coma (agrega espacio)
```

> ⚠️ **Trampa clásica:** `input()` **siempre devuelve texto** (`str`). Si pides la edad con `input()` y quieres sumarla, debes convertirla: `int(input("Tu edad: "))`. Olvidarlo provoca `TypeError: unsupported operand type(s)`.

## 4. Operadores matemáticos

| Operador | Operación | Ejemplo |
|----------|-----------|---------|
| `+` | Suma | `7 + 3 → 10` |
| `-` | Resta | `7 - 3 → 4` |
| `*` | Multiplicación | `7 * 3 → 21` |
| `/` | División (siempre decimal) | `7 / 2 → 3.5` |
| `//` | División entera | `7 // 2 → 3` |
| `%` | Módulo (residuo) | `7 % 2 → 1` |
| `**` | Potencia | `2 ** 3 → 8` |

## 5. Strings: tu primer "tipo con superpoderes"

```python
nombre = "Ana"
apellido = "López"

nombre_completo = nombre + " " + apellido   # concatenación con +
print(nombre_completo)                      # Ana López

print(nombre.upper())                       # ANA  (métodos de strings)
print(len(nombre))                          # 3    (longitud)
```

### Los f-strings: la forma moderna de formatear

```python
edad = 30
print(f"{nombre} tiene {edad} años")        # Ana tiene 30 años
print(f"El doble de {edad} es {edad * 2}")  # puedes poner expresiones dentro de {}
```

Usar f-strings evita errores de tipos y deja el código legible. **Adopta este estilo desde el día 1.**

## 6. Comentarios: tu yo del futuro te lo agradecerá

```python
# Esto es un comentario: Python lo ignora.
precio = 19.99  # comentario al final de la línea
```

Un buen comentario explica el **porqué**, no el qué. `precio = 19.99` ya dice qué hace; no escribas `# asignar precio`.

---

## ✍️ Ejercicios (nivel: ⭐ fácil / ⭐⭐ medio)

| # | Ejercicio | Dificultad |
|---|-----------|------------|
| 1 | Saludo personalizado — pregunta el nombre y saluda | ⭐ |
| 2 | Calculadora de edad — calcula en qué año naciste | ⭐ |
| 3 | Convertidor de temperatura — de °F a °C | ⭐⭐ |
| 4 | Área de un círculo — usa `float`, `**` y f-strings | ⭐⭐ |

**Cómo trabajar:** abre cada archivo de `ejercicios/`, lee las instrucciones en su docstring, reemplaza el `pass`/`TODO` y ejecútalo. Después verifica con:

```bash
python3 ../tools/verificar.py 01
```

> 📌 **Recuerda:** intenta primero. La solución está en `soluciones/`, pero el aprendizaje real ocurre cuando te equivocas y entiendes por qué.

---

## ✅ Checklist de fin de módulo

- [ ] Sé que `input()` devuelve texto y sé convertirlo con `int()`/`float()`.
- [ ] Uso f-strings en lugar de concatenar con `+`.
- [ ] Distingo `int`, `float`, `str` y `bool`.
- [ ] Mis 4 ejercicios pasan `python3 ../tools/verificar.py 01`.

¿Todo verde? ¡Al [Módulo 02 — Control de flujo](../02_control_de_flujo/README.md)! 🎉