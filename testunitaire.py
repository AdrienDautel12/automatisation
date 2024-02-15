import unittest
from programmepython import addition, soustraction, multiplication, division

class TestMonProgramme(unittest.TestCase):
    def test_addition(self):
        result = addition(3, 5)
        self.assertEqual(result, 8)
        print("Test addition réussi. Résultat:", result)

    def test_soustraction(self):
        result = soustraction(8, 3)
        self.assertEqual(result, 5)
        print("Test soustraction réussi. Résultat:", result)

    def test_multiplication(self):
        result = multiplication(4, 6)
        self.assertEqual(result, 24)
        print("Test multiplication réussi. Résultat:", result)

    def test_division(self):
        result = division(8, 4)
        self.assertEqual(result, 2)
        print("Test division réussi. Résultat:", result)

        result = division(5, 2)
        self.assertEqual(result, 2.5)
        print("Test division réussi. Résultat:", result)

    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            division(10, 0)
        print("Test division par zéro réussi.")

if __name__ == '__main__':
    unittest.main()
