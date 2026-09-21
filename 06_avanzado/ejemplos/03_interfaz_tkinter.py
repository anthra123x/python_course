"""Ejemplo 03: Interfaz gráfica con tkinter — Calculadora GUI.

Este archivo RESCATA un script original roto que decía:
    import thinker as tk        # ❌ no existe ningún módulo "thinker"

El módulo correcto es tkinter (sin "h"). Esta versión construye una
calculadora funcional con botones y una pantalla.

⚠️  REQUISITO: tkinter viene con Python en Windows y Mac. En Linux:
    sudo apt install python3-tk      (Debian/Ubuntu)

Ejecuta: python3 06_avanzado/ejemplos/03_interfaz_tkinter.py
"""

import tkinter as tk


def crear_pantalla(ventana: tk.Tk) -> tk.Entry:
    """Crea el campo de texto donde se ve el número y el resultado."""
    pantalla = tk.Entry(ventana, font=("Arial", 18), justify="right", width=20)
    pantalla.grid(row=0, column=0, columnspan=4, padx=8, pady=8)
    pantalla.insert(0, "0")
    return pantalla


def presionar_tecla(pantalla: tk.Entry, tecla: str) -> None:
    """Agrega el dígito/operador presionado a la pantalla."""
    actual = pantalla.get()

    # Si el marcador está en "0", lo reemplazamos (excepto si es un punto).
    if actual == "0" and tecla not in ("+", "-", "*", "/"):
        actual = ""

    pantalla.delete(0, tk.END)
    pantalla.insert(0, actual + tecla)


def calcular(pantalla: tk.Entry) -> None:
    """Evalúa la expresión de la pantalla y muestra el resultado.

    eval() interpreta el texto como código Python. ¡Cuidado!
    En producción no se usa eval con datos de usuario; aquí es un
    ejemplo educativo de GUI simple.
    """
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")


def limpiar(pantalla: tk.Entry) -> None:
    """Reinicia la pantalla a 0."""
    pantalla.delete(0, tk.END)
    pantalla.insert(0, "0")


def main() -> None:
    ventana = tk.Tk()
    ventana.title("Calculadora")
    ventana.resizable(False, False)

    pantalla = crear_pantalla(ventana)

    # Distribución de los botones (3 filas x 4 columnas).
    botones = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
    ]

    for fila, linea in enumerate(botones, start=1):
        for columna, texto in enumerate(linea):
            if texto == "=":
                boton = tk.Button(ventana, text=texto, width=6, height=2,
                                  command=lambda p=pantalla: calcular(p))
            elif texto == "C":
                boton = tk.Button(ventana, text=texto, width=6, height=2,
                                  command=lambda p=pantalla: limpiar(p))
            else:
                boton = tk.Button(ventana, text=texto, width=6, height=2,
                                  command=lambda t=texto, p=pantalla: presionar_tecla(p, t))
            boton.grid(row=fila, column=columna, padx=2, pady=2)

    ventana.mainloop()


if __name__ == "__main__":
    main()