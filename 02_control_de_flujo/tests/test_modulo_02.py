"""Tests del Módulo 02 — Control de flujo."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "tools"))
from cargar import cargar_modulo

BASE = Path(__file__).resolve().parent.parent / "ejercicios"


class TestParOImpar(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "01_par_o_impar.py")

    def test_es_par_cuatro(self):
        self.assertTrue(self.ejercicio.es_par(4))

    def test_es_impar_siete(self):
        self.assertFalse(self.ejercicio.es_par(7))

    def test_cero_es_par(self):
        self.assertTrue(self.ejercicio.es_par(0))

    def test_negativo_par(self):
        self.assertTrue(self.ejercicio.es_par(-8))


class TestAccesoALaAtraccion(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "02_acceso_a_la_atraccion.py")

    def test_puede_subir_normal(self):
        self.assertEqual(self.ejercicio.puede_subir(20, 1.70, False), "Puedes subir.")

    def test_edad_muy_pequena(self):
        self.assertEqual(self.ejercicio.puede_subir(10, 1.70, False),
                         "No puedes subir: edad no permitida.")

    def test_edad_muy_grande(self):
        self.assertEqual(self.ejercicio.puede_subir(70, 1.70, False),
                         "No puedes subir: edad no permitida.")

    def test_estatura_insuficiente(self):
        self.assertEqual(self.ejercicio.puede_subir(20, 1.40, False),
                         "No puedes subir: estatura insuficiente.")

    def test_problemas_cardiacos(self):
        self.assertEqual(self.ejercicio.puede_subir(45, 1.70, True),
                         "No puedes subir: problemas cardiacos.")


class TestSumaDeNumeros(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "03_suma_de_numeros.py")

    def test_suma_5(self):
        self.assertEqual(self.ejercicio.suma_hasta(5), 15)

    def test_suma_10(self):
        self.assertEqual(self.ejercicio.suma_hasta(10), 55)

    def test_suma_1(self):
        self.assertEqual(self.ejercicio.suma_hasta(1), 1)

    def test_suma_100(self):
        self.assertEqual(self.ejercicio.suma_hasta(100), 5050)


class TestTablaDeMultiplicar(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "04_tabla_de_multiplicar.py")

    def test_tabla_3_limite_3(self):
        self.assertEqual(self.ejercicio.tabla_de_multiplicar(3, 3),
                         ["3 x 1 = 3", "3 x 2 = 6", "3 x 3 = 9"])

    def test_longitud_por_defecto(self):
        self.assertEqual(len(self.ejercicio.tabla_de_multiplicar(7)), 10)

    def test_primera_linea(self):
        self.assertEqual(self.ejercicio.tabla_de_multiplicar(5)[0], "5 x 1 = 5")


class TestBuscadorDeNumerosPares(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "05_buscador_de_numeros_pares.py")

    def test_pares_hasta_10(self):
        self.assertEqual(self.ejercicio.numeros_pares(10), [2, 4, 6, 8, 10])

    def test_sin_pares(self):
        self.assertEqual(self.ejercicio.numeros_pares(1), [])

    def test_pares_hasta_5(self):
        self.assertEqual(self.ejercicio.numeros_pares(5), [2, 4])

    def test_solo_pares_devueltos(self):
        for numero in self.ejercicio.numeros_pares(50):
            self.assertEqual(numero % 2, 0)


if __name__ == "__main__":
    unittest.main()