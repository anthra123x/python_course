# Changelog

## [1.0.0] - 2026-09-21

### Reestructuración total como curso guiado

El repositorio pasó de ser una colección suelta de scripts a un **curso completo "Python desde cero — Aprende haciendo"** con metodología pedagógica.

#### Nuevo
- Estructura en 6 módulos progresivos con patrón `Teoría → Ejemplos → Ejercicios → Soluciones → Verificación`.
- Sistema de autoevaluación `tools/verificar.py` basado en `unittest` (sin dependencias externas).
- Módulo 01 **Fundamentos**: variables, tipos, I/O, operadores, strings.
- Módulo 02 **Control de flujo**: condicionales, bucles, `break`/`continue`.
- Módulo 03 **Estructuras de datos**: listas, tuplas, diccionarios, conjuntos.
- Módulo 04 **Funciones y módulos**: `def`, parámetros, `return`, `datetime`, `random`.
- Módulo 05 **Proyectos**: juego de adivinanza, quiz, lista de compras y calculadora.
- Módulo 06 **Avanzado**: manejo de errores, archivos, interfaz gráfica tkinter.
- README principal con metodología de estudio, mapa del curso y guía de instalación.

#### Correcciones de bugs en el código original
- `quiz_game.py`: `playing.lower` y `answer.lower` llamaban al método sin `()` → ahora `lower()`.
- `adivina_el_numero.py`: la pista siempre decía "Demasiado pequeño" → ahora compara y da la pista correcta.
- `condicionales.py`: string truncado `"(sino"` y lógica de validación incompleta → reescrito y completado.
- `calculadoraiterfaz.py`: `import thinker as tk` (módulo inexistente) → `import tkinter as tk`, reconstruido como proyecto GUI en el módulo 06.
- Archivos vacíos (`buscador_de_numeros_pares.py`, `calculadora_de_notas.py`, `lista_de_compras.py`, `validador_de_contraseñas.py`) → convertidos en ejercicios y soluciones completos.
- `listas.py` → reescrito como ejemplo didáctico con comentarios de *porqué*.
- `que_hora__es.py` → reescrito con funciones y explicación de `datetime`.

#### Eliminado
- Scripts planos en la raíz del repositorio (su contenido ya vive, corregido y explicado, dentro de los módulos).