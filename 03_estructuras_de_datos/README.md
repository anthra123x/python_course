# Módulo 03 · Estructuras de datos

> **Objetivo:** organizar colecciones de datos (listas, diccionarios, tuplas, conjuntos) y consultarlas como toda una experta.

| Sección | Contenido |
|---------|-----------|
| 📖 Teoría | Listas, tuplas, diccionarios, conjuntos, slicing |
| 👀 Ejemplos | `ejemplos/` |
| ✍️ Práctica | `ejercicios/` (4 ejercicios) |
| ✅ Verificación | `python3 ../tools/verificar.py 03` |
| 🔍 Soluciones | `soluciones/` |

---

## 1. Listas: colecciones ordenadas y modificables

Una lista guarda varios valores en orden. Imagínala como una fila de casilleros numerados.

```python
frutas = ["manzana", "pera", "uva"]
print(frutas[0])          # "manzana"  (¡se cuenta desde 0!)
print(frutas[-1])         # "uva"      (-1 es el último)
print(len(frutas))        # 3          (cantidad de elementos)
```

Operaciones esenciales:

```python
frutas = []
frutas.append("papaya")        # agregar al final
frutas.insert(0, "mango")      # agregar en una posición
frutas.remove("mango")         # eliminar por valor
frutas.pop()                   # eliminar y devolver el último
if "uva" in frutas:            # preguntar si existe
    print("¡hay uvas!")
```

La listas se recorren con `for`:

```python
for fruta in frutas:
    print(fruta)
```

## 2. Diccionarios: almacenes llave → valor

El diccionario es la estructura más útil de Python: asocia **llaves** con **valores**.

```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "La Paz"
}

print(persona["nombre"])        # Ana
print(persona.get("edad"))      # 30 (get no lanza error si falta)
persona["email"] = "ana@mail.com"   # agregar/actualizar una llave
persona["edad"] = 31            # actualizar

del persona["ciudad"]           # eliminar una llave
print("email" in persona)       # True (¿existe la llave?)
```

Recorrer un diccionario:

```python
for llave, valor in persona.items():
    print(f"{llave}: {valor}")

for llave in persona.keys():      # solo llaves
for valor in persona.values():    # solo valores
```

> 💡 Usa este mental model: una lista es una **fila ordenada**; un diccionario es un **directorio telefónico**.

## 3. Tuplas: listas inmutables

```python
coordenadas = (10, 20)
print(coordenadas[0])        # 10

# coordenadas[0] = 5         # ❌ TypeError: las tuplas no se modifican
```

Úsalas para datos que **no deben cambiar**: coordenadas, días de la semana, configuración fija.

Bonus: desempaquetado.

```python
x, y = coordenadas           # x=10, y=20
```

## 4. Conjuntos (sets): sin duplicados

```python
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)               # {1, 2, 3}  ← los duplicados desaparecen
```

| Operación | Símbolo | Ejemplo |
|-----------|---------|---------|
| Unión | `|` | `{1,2} \| {2,3} → {1,2,3}` |
| Intersección | `&` | `{1,2} & {2,3} → {2}` |
| Diferencia | `-` | `{1,2} - {2,3} → {1}` |

## 5. Slicing: cortar colecciones

```python
numeros = [0, 1, 2, 3, 4, 5]
print(numeros[1:4])    # [1, 2, 3]      (del índice 1 al 3)
print(numeros[:3])     # [0, 1, 2]      (hasta el 3, desde el inicio)
print(numeros[::2])    # [0, 2, 4]      (de 2 en 2)
print(numeros[::-1])   # [5, 4, 3, 2, 1, 0]  (al revés)
```

> El slicing funciona igual con strings: `"Python"[1:4]` → `"yth"`.

---

## ✍️ Ejercicios

| # | Ejercicio | Dificultad |
|---|-----------|------------|
| 1 | Lista de compras — agregar, eliminar y mostrar | ⭐⭐ |
| 2 | Conteo de palabras — diccionario como contador | ⭐⭐ |
| 3 | Eliminar duplicados — conjuntos al rescate | ⭐ |
| 4 | Agenda de contactos — diccionario de diccionarios | ⭐⭐⭐ |

**Verifica:** `python3 ../tools/verificar.py 03`

---

## 🕳️ Errores comunes

- `KeyError: 'ciudad'` — preguntar por una llave que no existe. Usa `.get()`.
- `IndexError: list index out of range` — acceder a un índice inexistente: `frutas[10]`.
- Confundir `append` (agrega un elemento) con `extend` (agrega varios).
- Modificar una lista mientras la recorres con `for` — causa saltos raros.

---

## ✅ Checklist de fin de módulo

- [ ] Sé crear y manipular listas con `append`, `remove`, `pop`, `in`.
- [ ] Sé usar diccionarios con `.get()`, `in` y `.items()`.
- [ ] Entiendo la diferencia entre lista, tupla, diccionario y conjunto.
- [ ] Los 4 ejercicios pasan `python3 ../tools/verificar.py 03`.

¿Todo verde? ¡Al [Módulo 04 — Funciones](../04_funciones/README.md)! 🎉