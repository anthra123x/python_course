"""Helper interno para cargar módulos de ejercicio por ruta.

Los archivos de ejercicio tienen nombres como ``01_saludo.py`` que no son
identificadores de módulo válidos en Python (empiezan con dígitos). Esta
función los carga usando importlib para que los tests puedan importar el
código DEMO de la persona estudiante sin problemas.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path


def cargar_modulo(ruta: str | Path) -> object:
    """Carga un archivo .py arbitrario y devuelve el módulo.

    Parámetros
    ----------
    ruta:
        Ruta (absoluta o relativa) hacia el archivo .py a cargar.

    Devuelve
    --------
    El módulo cargado, listo para acceder a sus funciones/variables.

    Lanza
    -----
    FileNotFoundError: si la ruta no existe.
    SyntaxError: si el archivo tiene errores de sintaxis (el estudiante
                 aún no terminó su código, por ejemplo).
    """
    ruta = Path(ruta).resolve()

    if not ruta.exists():
        raise FileNotFoundError(f"No existe el archivo: {ruta}")

    # El nombre del módulo debe ser un identificador válido: usamos una
    # clave única basada en la ruta.
    nombre_modulo = f"modulo_{abs(hash(str(ruta)))}"

    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta)
    if spec is None or spec.loader is None:
        raise ImportError(f"No se pudo crear la especificación para: {ruta}")

    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


# Aliasing cómodo para los archivos de test.
cargar_ejercicio = cargar_modulo