"""Tests del Módulo 03 — Estructuras de datos."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "tools"))
from cargar import cargar_modulo

BASE = Path(__file__).resolve().parent.parent / "ejercicios"


class TestListaDeCompras(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "01_lista_de_compras.py")

    def test_agregar_nuevo(self):
        self.assertEqual(self.ejercicio.agregar_articulo(["pan"], "leche"),
                         ["pan", "leche"])

    def test_agregar_duplicado(self):
        self.assertEqual(self.ejercicio.agregar_articulo(["pan"], "pan"), ["pan"])

    def test_quitar_existente(self):
        self.assertEqual(self.ejercicio.quitar_articulo(["pan", "leche"], "pan"),
                         ["leche"])

    def test_quitar_inexistente_no_falla(self):
        # No debe lanzar ValueError.
        self.assertEqual(self.ejercicio.quitar_articulo(["pan"], "leche"), ["pan"])


class TestConteoDePalabras(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "02_conteo_de_palabras.py")

    def test_frase_simple(self):
        self.assertEqual(self.ejercicio.contar_palabras("hola mundo hola"),
                         {"hola": 2, "mundo": 1})

    def test_texto_vacio(self):
        self.assertEqual(self.ejercicio.contar_palabras(""), {})

    def test_una_palabra(self):
        self.assertEqual(self.ejercicio.contar_palabras("python python python"),
                         {"python": 3})

    def test_devuelve_diccionario(self):
        self.assertIsInstance(self.ejercicio.contar_palabras("a b a"), dict)


class TestEliminarDuplicados(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "03_eliminar_duplicados.py")

    def test_duplicados_numericos(self):
        self.assertEqual(sorted(self.ejercicio.quitar_duplicados([1, 2, 2, 3, 3])),
                         [1, 2, 3])

    def test_lista_vacia(self):
        self.assertEqual(self.ejercicio.quitar_duplicados([]), [])

    def test_todos_iguales(self):
        self.assertEqual(len(self.ejercicio.quitar_duplicados([1, 1, 1, 1])), 1)

    def test_strings(self):
        resultado = self.ejercicio.quitar_duplicados(["a", "b", "a"])
        self.assertEqual(sorted(resultado), ["a", "b"])


class TestAgendaDeContactos(unittest.TestCase):
    def setUp(self):
        self.ejercicio = cargar_modulo(BASE / "04_agenda_de_contactos.py")

    def test_agregar_contacto_estructura(self):
        agenda = {}
        agenda = self.ejercicio.agregar_contacto(agenda, "ana", "+591 70012345")
        self.assertEqual(agenda["ana"]["telefono"], "+591 70012345")
        self.assertEqual(agenda["ana"]["llamadas"], 1)

    def test_registrar_llamada(self):
        agenda = {}
        agenda = self.ejercicio.agregar_contacto(agenda, "ana", "123")
        agenda = self.ejercicio.registrar_llamada(agenda, "ana")
        agenda = self.ejercicio.registrar_llamada(agenda, "ana")
        self.assertEqual(agenda["ana"]["llamadas"], 3)

    def test_registrar_llamada_contacto_inexistente(self):
        agenda = {"ana": {"telefono": "123", "llamadas": 1}}
        resultado = self.ejercicio.registrar_llamada(agenda, "luis")
        self.assertEqual(resultado["ana"]["llamadas"], 1)
        self.assertNotIn("luis", resultado)


if __name__ == "__main__":
    unittest.main()