"""Tests del Módulo 04 — Funciones y módulos."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "tools"))
from cargar import cargar_modulo

BASE = Path(__file__).resolve().parent.parent / "ejercicios"


class TestCalculadoraDeNotas(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "01_calculadora_de_notas.py")

    def test_extremos_de_escala(self):
        self.assertEqual(self.ejercicio.calificar(100), "A")
        self.assertEqual(self.ejercicio.calificar(90), "A")
        self.assertEqual(self.ejercicio.calificar(89), "B")
        self.assertEqual(self.ejercicio.calificar(80), "B")
        self.assertEqual(self.ejercicio.calificar(79), "C")
        self.assertEqual(self.ejercicio.calificar(70), "C")
        self.assertEqual(self.ejercicio.calificar(69), "D")
        self.assertEqual(self.ejercicio.calificar(60), "D")

    def test_reprobado(self):
        self.assertEqual(self.ejercicio.calificar(59), "F")
        self.assertEqual(self.ejercicio.calificar(0), "F")

    def test_valor_medio(self):
        self.assertEqual(self.ejercicio.calificar(85), "B")
        self.assertEqual(self.ejercicio.calificar(72), "C")


class TestValidadorDeContrasena(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "02_validador_de_contraseñas.py")

    def test_valida_contraseña_completa(self):
        self.assertTrue(self.ejercicio.validar_contrasena("Abc12345"))

    def test_rechaza_sin_numero(self):
        self.assertFalse(self.ejercicio.validar_contrasena("Abcdefgh"))

    def test_rechaza_corta(self):
        self.assertFalse(self.ejercicio.validar_contrasena("corta1A"))

    def test_rechaza_sin_mayuscula(self):
        self.assertFalse(self.ejercicio.validar_contrasena("abc12345"))

    def test_rechaza_sin_minuscula(self):
        self.assertFalse(self.ejercicio.validar_contrasena("ABC12345"))


class TestEsPrimo(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "03_es_primo.py")

    def test_primos_conocidos(self):
        for primo in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            self.assertTrue(self.ejercicio.es_primo(primo), f"{primo} debería ser primo")

    def test_no_primos(self):
        for compuesto in (4, 6, 8, 9, 10, 12, 15, 21, 25, 49, 100):
            self.assertFalse(self.ejercicio.es_primo(compuesto),
                             f"{compuesto} no debería ser primo")

    def test_uno_y_cero_no_primos(self):
        self.assertFalse(self.ejercicio.es_primo(1))
        self.assertFalse(self.ejercicio.es_primo(0))

    def test_negativos_no_primos(self):
        self.assertFalse(self.ejercicio.es_primo(-7))


class TestQueHoraEs(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "04_que_hora_es.py")

    def test_devuelve_string(self):
        self.assertIsInstance(self.ejercicio.descanso_para("23:59"), str)

    def test_mensaje_esperado(self):
        mensajes = (
            "Es hora de descansar 🎉",
            "Aún falta un buen rato para descansar",
            "Ya casi, aguanta un poquito más",
        )
        self.assertIn(self.ejercicio.descanso_para("23:59"), mensajes)

    def test_cualquier_hora_valida(self):
        for hora in ("00:00", "08:30", "14:00", "18:45", "23:59"):
            self.assertIsInstance(self.ejercicio.descanso_para(hora), str)


if __name__ == "__main__":
    unittest.main()