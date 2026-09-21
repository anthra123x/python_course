# Proyecto 03 · Lista de compras

> Una app de consola completa: agrega, quita, ve y vacía tus compras. Es el proyecto más completo del módulo.

## 🎮 Requisitos

- Menú interactivo con 5 opciones: ver, agregar, quitar, vaciar y salir.
- Al agregar: evita duplicados (lo practicaste en el ejercicio 01 del módulo 03).
- Al quitar: avisa si el artículo no está.
- El menú se muestra en un bucle `while` hasta que el usuario elige salir (`break`).
- Todo el programa se apoya en **funciones pequeñas** — la señal de un código profesional.

## ▶️ Ejecutar

```bash
python3 05_proyectos/03_lista_de_compras/lista_de_compras.py
```

## 🧩 Conceptos que practicas

| Concepto | Dónde lo ves |
|----------|--------------|
| Funciones pequeñas | Cada acción del menú es una función |
| `while True` + `break` | El menú infinito que termina con la opción 5 |
| `if/elif/else` | Enrutar la opción elegida |
| Listas + `in` | Evitar duplicados y verificar existencia |
| `enumerate` | Numerar los artículos al mostrarlos |

## 🚀 Ideas de mejora

1. Agrega cantidad a cada artículo: guarda diccionarios `{articulo: cantidad}` en vez de strings.
2. Marca artículos como "✓ comprado" con una opción más del menú.
3. Guarda la lista en un archivo de texto para no perderla al cerrar (spoiler: eso se ve en el módulo 06).
4. Ordena la lista alfabéticamente al mostrarla: `sorted(lista)`.
5. Calcula el costo total si cada artículo tiene precio.