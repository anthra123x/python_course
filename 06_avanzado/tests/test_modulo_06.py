"""Tests del Módulo 06 — Avanzado."""

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "tools"))
from cargar import cargar_modulo

BASE = Path(__file__).resolve().parent.parent / "ejercicios"


class TestCalculadoraConValidacion(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "01_calculadora_con_validacion.py")

    def test_dividir_normal(self):
        self.assertEqual(self.ejercicio.dividir(10, 2), 5.0)

    def test_dividir_entre_cero(self):
        self.assertEqual(self.ejercicio.dividir(10, 0), "Error: división entre cero")

    def test_dividir_decimal(self):
        self.assertAlmostEqual(self.ejercicio.dividir(1, 3), 1 / 3)

    def test_sumar_lista_normal(self):
        self.assertEqual(self.ejercicio.sumar_lista([1, 2, 3]), 6)

    def test_sumar_lista_vacia(self):
        self.assertEqual(self.ejercicio.sumar_lista([]), 0)

    def test_sumar_lista_con_texto(self):
        self.assertEqual(self.ejercicio.sumar_lista([1, "dos", 3]),
                         "Error: elementos no numéricos")

    def test_sumar_lista_con_floats(self):
        self.assertAlmostEqual(self.ejercicio.sumar_lista([1.5, 2.5]), 4.0)


class TestNotasEnArchivo(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "02_notas_en_archivo.py")
        # Creamos un directorio temporal para los archivos de prueba.
        self.tmpdir = tempfile.mkdtemp()
        self.ruta_prueba = os.path.join(self.tmpdir, "notas.txt")

    def tearDown(self):
        # Limpiamos el archivo si aún existe.
        if os.path.exists(self.ruta_prueba):
            os.remove(self.ruta_prueba)

    def test_guardar_y_leer(self):
        notas = {"Ana": 95, "Luis": 82}
        self.ejercicio.guardar_notas(self.ruta_prueba, notas)
        leidas = self.ejercicio.leer_notas(self.ruta_prueba)
        self.assertEqual(leidas, notas)

    def test_leer_archivo_inexistente(self):
        self.assertEqual(self.ejercicio.leer_notas(os.path.join(self.tmpdir, "no.txt")), {})

    def test_valores_son_ints(self):
        self.ejercicio.guardar_notas(self.ruta_prueba, {"Ana": "95"})
        leidas = self.ejercicio.leer_notas(self.ruta_prueba)
        self.assertIsInstance(leidas.get("Ana"), int)

    def test_sobreescribe_archivo(self):
        self.ejercicio.guardar_notas(self.ruta_prueba, {"Ana": 95})
        self.ejercicio.guardar_notas(self.ruta_prueba, {"Luis": 82})
        self.assertEqual(self.ejercicio.leer_notas(self.ruta_prueba), {"Luis": 82})


if __name__ == "__main__":
    unittest.main()