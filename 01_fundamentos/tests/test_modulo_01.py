"""Tests del Módulo 01 — Fundamentos.

Estos tests verifican TUS ejercicios (los archivos en ejercicios/).
Para verlos correr en conjunto:
    python3 tools/verificar.py 01
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "tools"))
from cargar import cargar_modulo

BASE = Path(__file__).resolve().parent.parent / "ejercicios"


class TestSaludoPersonalizado(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "01_saludo_personalizado.py")

    def test_saluda_con_nombre(self):
        self.assertEqual(self.ejercicio.saludar("Ana"), "Hola, Ana. ¡Bienvenido a Python!")

    def test_saluda_con_otro_nombre(self):
        self.assertEqual(self.ejercicio.saludar("Luis"), "Hola, Luis. ¡Bienvenido a Python!")

    def test_devuelve_string(self):
        self.assertIsInstance(self.ejercicio.saludar("x"), str)


class TestCalculadoraDeEdad(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "02_calculadora_de_edad.py")

    def test_edad_30(self):
        self.assertEqual(self.ejercicio.ano_de_nacimiento(30, 2026), 1996)

    def test_edad_10(self):
        self.assertEqual(self.ejercicio.ano_de_nacimiento(10, 2026), 2016)

    def test_edad_cero(self):
        self.assertEqual(self.ejercicio.ano_de_nacimiento(0, 2026), 2026)


class TestConvertidorDeTemperatura(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "03_convertidor_de_temperatura.py")

    def test_punto_de_ebullicion(self):
        self.assertAlmostEqual(self.ejercicio.fahrenheit_a_celsius(212), 100.0, places=6)

    def test_punto_de_congelacion(self):
        self.assertAlmostEqual(self.ejercicio.fahrenheit_a_celsius(32), 0.0, places=6)

    def test_valor_negativo(self):
        self.assertAlmostEqual(self.ejercicio.fahrenheit_a_celsius(-40), -40.0, places=6)


class TestAreaDeCirculo(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "04_area_de_circulo.py")

    def test_radio_unidad(self):
        self.assertAlmostEqual(self.ejercicio.area_circulo(1.0), 3.141592653589793, places=6)

    def test_radio_dos(self):
        self.assertAlmostEqual(self.ejercicio.area_circulo(2.0), 12.566370614359172, places=6)

    def test_radio_cero(self):
        self.assertEqual(self.ejercicio.area_circulo(0.0), 0.0)


if __name__ == "__main__":
    unittest.main()