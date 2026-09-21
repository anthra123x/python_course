#!/usr/bin/env python3
"""Runner de autoevaluación del curso "Python desde cero".

Ejecuta los tests de los módulos y muestra un resumen claro de qué
ejercicios pasan y cuáles aún necesitan trabajo.

USO
---
    python3 tools/verificar.py            # verifica TODO el curso
    python3 tools/verificar.py 01         # verifica solo el módulo 01
    python3 tools/verificar.py 04 2       # verifica el ejercicio 2 del módulo 04

Niveles de los mensajes:
    🟢 OK        → el ejercicio está resuelto correctamente.
    🔴 FAIL      → el ejercicio no cumple los requisitos.
    ⚠️ ERROR     → algo falló al cargar el ejercicio (sintaxis, TODO, etc.).
"""

from __future__ import annotations

import inspect
import re
import sys
import unittest
from pathlib import Path

# La raíz del curso: la carpeta padre del directorio "tools".
RAIZ = Path(__file__).resolve().parent.parent

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"


def encontrar_archivos_de_test() -> list[Path]:
    """Devuelve todos los archivos tests/test_modulo_*.py del curso, ordenados.

    Si el primer argumento es numérico, se interpreta como filtro de
    módulo (p. ej. "03").
    """
    filtro = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].isnumeric() else None

    archivos = sorted(RAIZ.glob("*/tests/test_modulo_*.py"))

    if filtro:
        archivos = [a for a in archivos if a.parent.parent.name.startswith(filtro)]

    return archivos


def construir_suite(archivos: list[Path]) -> unittest.TestSuite:
    """Carga cada archivo de test y agrega sus tests a una suite."""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for archivo in archivos:
        if archivo.exists():
            suite.addTests(loader.discover(str(archivo.parent),
                                           pattern=archivo.name,
                                           top_level_dir=str(archivo.parent)))
    return suite


def numero_de_ejercicio(test: unittest.TestCase) -> int | None:
    """Descubre a qué ejercicio corresponde un test.

    Los tests cargan su ejercicio en setUp() con una línea del tipo:
        self.ejercicio = cargar_modulo(BASE / "02_calculadora_de_edad.py")
    Extraemos el número inicial del nombre de archivo (02 → ejercicio 2).
    """
    try:
        fuente = inspect.getsource(test.__class__.setUp)
    except (OSError, TypeError):
        return None

    coincidencia = re.search(r'BASE\s*/\s*"(\d+)_', fuente)
    return int(coincidencia.group(1)) if coincidencia else None


def ejecutar_filtro_por_ejercicio(suite: unittest.TestSuite) -> unittest.TestSuite:
    """Si el usuario pidió un ejercicio concreto (p. ej. "04 2"), filtra la suite."""
    if len(sys.argv) < 3:
        return suite

    ejercicio_filtrado = int(sys.argv[2])
    suite_filtrada = unittest.TestSuite()

    def _recorrer(tests):
        for test in tests:
            if isinstance(test, unittest.TestSuite):
                _recorrer(test)
            elif numero_de_ejercicio(test) == ejercicio_filtrado:
                suite_filtrada.addTest(test)

    _recorrer(suite)
    return suite_filtrada


class ResultadoPersonalizado(unittest.TextTestResult):
    """TextTestResult que colorea el output y explica cada fallo."""

    def printErrors(self) -> None:
        """Solo imprimimos el traceback completo de ERROR (fallos de carga).

        Los FAIL ya muestran su mensaje en el output coloreado; el detalle
        completo de un ERROR (sintaxis, import) sí ayuda a corregir.
        """
        self.printErrorList("ERROR", self.errors)

    def startTest(self, test: unittest.TestCase) -> None:
        super().startTest(test)
        print(f"    → {test._testMethodName}")

    def addSuccess(self, test: unittest.TestCase) -> None:
        super().addSuccess(test)
        print(f"      {GREEN}✔ OK{RESET}")

    def addError(self, test: unittest.TestCase, err) -> None:
        super().addError(test, err)
        # err[1] es la excepción: para SyntaxError muestra la línea
        # problemática; para import errors, la causa real.
        detalle = self._detalle_de_error(err)
        print(f"      {YELLOW}⚠ ERROR: el ejercicio no se cargó correctamente{RESET}")
        print(f"        {detalle}")

    def addFailure(self, test: unittest.TestCase, err) -> None:
        super().addFailure(test, err)
        # La excepción de un assert: AssertionError con el mensaje.
        print(f"      {RED}✘ FAIL: la solución no cumple los requisitos{RESET}")
        print(f"        {self._detalle_de_error(err)}")

    @staticmethod
    def _detalle_de_error(err) -> str:
        """Convierte el error (type, exception, traceback) a texto útil."""
        excepcion = err[1] if len(err) > 1 else None
        if excepcion is None:
            return "(sin detalle)"
        mensaje = str(excepcion).strip()
        if not mensaje:
            return excepcion.__class__.__name__
        return mensaje.splitlines()[0]


def main() -> None:
    archivos = encontrar_archivos_de_test()

    if not archivos:
        print(f"{YELLOW}No se encontraron tests. Asegúrate de estar en la raíz del curso.{RESET}")
        sys.exit(1)

    print(f"\n{BOLD}{BLUE}=== Verificador del curso Python desde cero ==={RESET}\n")

    total_ok = 0
    total_fail = 0

    for archivo in archivos:
        nombre_modulo = archivo.parent.parent.name
        print(f"{BOLD}{BLUE}▸ Módulo {nombre_modulo}{RESET}")

        suite = construir_suite([archivo])
        suite = ejecutar_filtro_por_ejercicio(suite)

        if suite.countTestCases() == 0:
            print(f"    {YELLOW}(sin tests para este filtro){RESET}\n")
            continue

        runner = unittest.TextTestRunner(
            verbosity=0,
            resultclass=ResultadoPersonalizado,
            stream=sys.stdout,
        )
        resultado = runner.run(suite)

        total_ok += resultado.testsRun - len(resultado.failures) - len(resultado.errors)
        total_fail += len(resultado.failures) + len(resultado.errors)
        print()

    resumen = (
        f"{BOLD}TOTAL{RESET} "
        f"{GREEN}{total_ok} correctos{RESET} · "
        f"{RED}{total_fail} con errores{RESET}"
    )
    print(resumen)

    if total_fail == 0:
        print(f"\n{GREEN}{BOLD}🎉 ¡Todo en verde! Has completado todos los ejercicios verificados.{RESET}")
    else:
        print(f"\n{YELLOW}💪 Te faltan {total_fail} por resolver. ¡No te rindas!{RESET}")
        print(f"   Recuerda la regla de oro: intenta primero, mira la solución después.")
        print(f"   Si estás atascado, relee la teoría del README del módulo.")

    sys.exit(1 if total_fail else 0)


if __name__ == "__main__":
    main()