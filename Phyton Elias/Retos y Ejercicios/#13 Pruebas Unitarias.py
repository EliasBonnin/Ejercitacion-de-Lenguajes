# Ejercicio 13
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Pruebas Unitarias

import unittest
# from datetime import datetime, date


def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales")
    return a + b


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2, 3.4), 5.4)
        self.assertEqual(sum(5.4, 7), 12.4)
        self.assertEqual(sum(2.5, 2.5), 5)

    def test_sum_fail(self):
        with self.assertRaises(ValueError):
            sum("5", 7)

        with self.assertRaises(ValueError):
            sum(5, "7")

        with self.assertRaises(ValueError):
            sum("5", "7")

        with self.assertRaises(ValueError):
            sum("a", "7")


unittest.main()
