# 🐍 Python desde cero — Aprende haciendo

> Un curso práctico, progresivo y autoevaluable. Clona el repositorio y empieza a aprender hoy mismo.

Este repositorio es un **curso completo de Python** organizado en módulos progresivos. No es un montón de ejercicios sueltos: es un camino de aprendizaje diseñado con la mejor metodología para que **programes desde el primer minuto**.

---

## 🎯 ¿Qué aprenderás?

Al terminar el curso serás capaz de:

- ✅ Escribir programas en Python con sintaxis limpia y comentarios útiles.
- ✅ Usar variables, tipos de datos, operadores, condicionales y bucles con soltura.
- ✅ Manipular listas, diccionarios, tuplas y conjuntos.
- ✅ Diseñar funciones reutilizables y organizar tu código en módulos.
- ✅ Leer y manejar errores como una persona programadora (no como quien los teme).
- ✅ Construir **4 proyectos completos** desde cero: un juego de adivinanza, un quiz, un gestor de compras y una calculadora.

> **No necesitas experiencia previa.** Solo Python instalado y ganas de practicar.

---

## 📥 Instalación (menos de 2 minutos)

### 1. Clona el repositorio

```bash
git clone https://github.com/TU_USUARIO/python_course.git
cd python_course
```

### 2. Verifica que tienes Python (3.10 o superior)

```bash
python3 --version
```

- **No lo tienes →** descárgalo gratis de [python.org/downloads](https://www.python.org/downloads/) (Windows/Mac/Linux).
  - En Windows, al instalar, **marca la casilla "Add Python to PATH"**.
  - En Ubuntu/Debian: `sudo apt install python3`
- Todos los scripts del curso usan **solo la biblioteca estándar**: no hay que instalar nada más. 🎉

### 3. (Opcional, recomendado) Crea un entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate    # Linux/Mac
# .venv\Scripts\activate     # Windows
```

### 4. Ejecuta tu primera verificación

```bash
python3 tools/verificar.py 01
```

¿Ves `OK` en verde? Ya estás listo para empezar. 🚀

---

## 🧭 Cómo usar el curso (la metodología)

Cada módulo sigue el mismo patrón, que es el que la ciencia del aprendizaje recomienda:

```
┌─────────────────────────────────────────────────────────────┐
│  1. 📖 TEORÍA      → README.md del módulo                    │
│  2. 👀 EJEMPLOS    → ejemplos/  (código ejecutable)          │
│  3. ✍️ PRÁCTICA    → ejercicios/ (programa tú)               │
│  4. ✅ VERIFICACIÓN → python3 tools/verificar.py <módulo>    │
│  5. 🔍 SOLUCIONES  → soluciones/ (solo después de intentar)  │
└─────────────────────────────────────────────────────────────┘
```

### ⚠️ La regla de oro del curso

> **Intenta el ejercicio ANTES de mirar la solución.**

Aprender a programar es como aprender un deporte: **leer de la técnica no te hace mejor, practicar sí**.
Mira la solución únicamente cuando:
1. Lleves al menos **15–20 minutos** intentándolo de verdad, o
2. Tu ejercicio pase los tests y quieras comparar enfoques.

Cuando mires una solución, **no la copies**: entiéndela, ciérrala y vuelve a escribirla con tus propias palabras.

---

## 🗺️ Mapa del curso

| Módulo | Tema | Qué sabrás hacer al terminar |
|--------|------|------------------------------|
| [`01_fundamentos`](01_fundamentos/) | Variables, tipos, entrada/salida, operadores, strings | Pedir datos, hacer cálculos y mostrar resultados con f-strings |
| [`02_control_de_flujo`](02_control_de_flujo/) | `if/elif/else`, `while`, `for`, `break/continue` | Programas que toman decisiones y repiten tareas |
| [`03_estructuras_de_datos`](03_estructuras_de_datos/) | Listas, tuplas, diccionarios, conjuntos | Organizar colecciones de datos y consultarlas |
| [`04_funciones`](04_funciones/) | `def`, parámetros, `return`, alcance, módulos | Dividir programas en piezas reutilizables |
| [`05_proyectos`](05_proyectos/) | Proyectos integradores | **4 programas completos** de principio a fin |
| [`06_avanzado`](06_avanzado/) | Errores, archivos, interfaz gráfica (tkinter) | Programas robustos y con interfaz visual |

**Orden recomendado:** 01 → 02 → 03 → 04 → 05. El módulo `06` es opcional y puedes hincarle el diente en cualquier momento después del 03.

> 💡 **Consejo de estudio:** avanza de a un módulo por sesión. La repetición espaciada (repasar ejercicios viejos días después) consolida mucho más que las maratones de un día.

---

## ▶️ Cómo ejecutar cada cosa

```bash
# Un ejemplo (código que ya está hecho, solo ejecútalo y obsérvalo):
python3 01_fundamentos/ejemplos/01_variables_y_tipos.py

# Un ejercicio tuyo:
python3 03_estructuras_de_datos/ejercicios/01_lista_de_compras.py

# Un proyecto completo:
python3 05_proyectos/01_adivina_el_numero/juego.py
```

### ✅ El sistema de verificación automática

Cada módulo tiene tests que comprueban **tus** ejercicios (no las soluciones). Esto te da retroalimentación inmediata —como en un curso con profesor que corrige al instante—:

```bash
# Verificar TODO el curso:
python3 tools/verificar.py

# Verificar un módulo:
python3 tools/verificar.py 03

# Verificar un solo ejercicio (el 2 del módulo 04):
python3 tools/verificar.py 04 2
```

Qué significa cada resultado:

| Resultado | Significado |
|-----------|-------------|
| 🟢 `OK` | Tu solución cumple los requisitos. ¡Sigue así! |
| 🔴 `ERROR` / `FAIL` | Tu solución no cumple algo. Lee el mensaje: te dice qué se esperaba. |
| ⚠️ `ERROR de importación` | El módulo falla al cargarse (sintaxis, `TODO` sin resolver, etc.). |

---

## 📂 Estructura del repositorio

```
python_course/
├── README.md                      ← Estás aquí
├── requirements.txt               ← Sin dependencias externas (stdlib)
├── CHANGELOG.md                   ← Historial de cambios
├── tools/
│   ├── verificar.py               ← Runner de autoevaluación
│   └── cargar.py                  ← Helper interno para cargar ejercicios
├── 01_fundamentos/
│   ├── README.md                  ← Teoría del módulo
│   ├── ejemplos/                  ← Código ejecutable comentado
│   ├── ejercicios/                ← Tu campo de práctica (archivos incompletos)
│   ├── soluciones/                ← Soluciones explicadas
│   └── tests/                     ← Tests que comprueban tus ejercicios
├── 02_control_de_flujo/           ← (misma estructura)
├── 03_estructuras_de_datos/       ← (misma estructura)
├── 04_funciones/                  ← (misma estructura)
├── 05_proyectos/
│   ├── 01_adivina_el_numero/
│   ├── 02_quiz_game/
│   ├── 03_lista_de_compras/
│   └── 04_calculadora/
└── 06_avanzado/                   ← (misma estructura)
```

---

## 🛠️ Para contribuir o extender el curso

¿Quieres mejorar el curso? ¡Genial! Revisa [CONTRIBUTING](CONTRIBUTING.md) (si existe) o simplemente:
1. Haz *fork* del repositorio.
2. Agrega ejemplos, ejercicios o módulos siguiendo la misma estructura.
3. Asegúrate de que `python3 tools/verificar.py` siga pasando en verde.
4. Abre un *pull request*.

Reglas de estilo:
- Código en inglés (nombres de variables/funciones), explicaciones en español.
- Sin dependencias externas: solo `import` de la biblioteca estándar.
- Todo código comentado con `#` explicando el **porqué**, no solo el qué.

---

## 🙌 Créditos y contexto

Este curso nació de una colección de ejercicios de práctica. Se reestructuró como un **programa guiado** con teoría, ejemplos, ejercicios autoevaluables y proyectos, para que cualquier persona pueda clonarlo y aprender de forma autónoma.

> Hecho con ❤️ para quien quiere aprender Python. ¡Disfruta el camino y no te rindas! 🚀