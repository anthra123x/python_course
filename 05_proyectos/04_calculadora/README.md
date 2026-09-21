# Proyecto 04 · Calculadora

> Una calculadora de consola con sumar, restar, multiplicar, dividir y potencias, con validación de errores.

## 🎮 Requisitos

- Menú con las 5 operaciones + salir.
- Pide los dos números y muestra el resultado con 2 decimales.
- Detecta división entre cero: en lugar de estrellarse, muestra un mensaje claro.
- Después de cada operación, pregunta si continuar.
- Resiste entradas inválidas (`try/except ValueError`).

## ▶️ Ejecutar

```bash
python3 05_proyectos/04_calculadora/calculadora.py
```

## 🧩 Conceptos que practicas

| Concepto | Dónde lo ves |
|----------|--------------|
| Diccionario de funciones | Las operaciones viven en un `dict` |
| `try/except` | Validar números y división entre cero |
| `while True` + `break` | El menú principal |
| `f"{resultado:.2f}"` | Formato con 2 decimales |
| Composición de funciones | `pedir_numero` se reutiliza dos veces |

## 💡 El truco del diccionario de funciones

En vez de 5 `elif` enormes, guardamos las operaciones en un diccionario donde la **llave es el texto del menú** y el **valor es la función**:

```python
operaciones = {
    "1": sumar,
    "2": restar,
    "3": multiplicar,
    ...
}
operacion = operaciones[opcion]   # obtenemos la función
resultado = operacion(a, b)       # y la llamamos
```

Poder tratar funciones como valores es uno de los superpoderes de Python.

## 🚀 Ideas de mejora

1. Agrega más operaciones: raíz cuadrada, módulo (%), promedio.
2. Guarda el historial de cálculos en una lista y muéstralo con una opción.
3. Convierte la calculadora a la interfaz gráfica del módulo 06 (van de la mano 😉).
4. Permite encadenar resultados: usar el último resultado como primer número.
5. Valida que el usuario no ingrese cero en el divisor ANTES de llamar a la operación.