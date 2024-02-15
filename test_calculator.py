# File: test_calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Initialisation des objets nécessaires pour les tests
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)
        print("Test addition réussi. Résultat :", result)

    def test_subtraction(self):
        result = self.calculator.subtract(8, 3)
        self.assertEqual(result, 5)
        print("Test soustraction réussi. Résultat :", result)

    def test_multiplication(self):
        result = self.calculator.multiply(4, 6)
        self.assertEqual(result, 24)
        print("Test multiplication réussi. Résultat :", result)

    def test_division(self):
        result = self.calculator.divide(8, 4)
        self.assertEqual(result, 2)
        print("Test division réussi. Résultat :", result)

        result = self.calculator.divide(5, 2)
        self.assertEqual(result, 2.5)
        print("Test division réussi. Résultat :", result)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)
        print("Test division par zéro réussi.")

if __name__ == '__main__':
    unittest.main()
