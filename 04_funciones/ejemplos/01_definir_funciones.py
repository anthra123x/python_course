"""Ejemplo 01: Definir funciones.

Las funciones agrupan lógica con un nombre. Cuando programas algo
de más de 5 líneas, pregúntate: "¿esto debería ser una función?"

Ejecuta: python3 04_funciones/ejemplos/01_definir_funciones.py
"""


def saludar() -> None:
    """Función sin parámetros ni retorno: solo imprime."""
    print("¡Hola desde una función!")


def saludar_a(nombre: str) -> str:
    """Función con parámetro y retorno: devuelve un string."""
    return f"Hola, {nombre}!"


def presentar(nombre: str, edad: int = 18) -> str:
    """Parámetro con valor por defecto: edad es opcional."""
    return f"{nombre} tiene {edad} años"


def operaciones(a: int, b: int) -> tuple:
    """Devuelve varios valores en una tupla (desempaquetado después)."""
    suma = a + b
    producto = a * b
    return suma, producto


# --- Usar las funciones ---
saludar()

mensaje = saludar_a("Ana")
print(mensaje)

print(presentar("Ana"))           # usa el default de edad
print(presentar("Ana", 30))       # sobreescribe la edad

suma, producto = operaciones(4, 5)   # desempaquetado de la tupla
print(f"Suma: {suma}, Producto: {producto}")


# --- El problema que resuelven las funciones: repetir código ---
# SIN funciones tendríamos que copiar/pegar. CON funciones, una línea:
def area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo."""
    return base * altura


for base, altura in [(2, 3), (5, 2), (10, 10)]:
    print(f"Área de {base}x{altura}: {area_rectangulo(base, altura)}")