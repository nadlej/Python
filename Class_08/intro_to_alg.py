import random
from math import sqrt
import unittest

"""Rozwiązywanie równania liniowego a x + b y + c = 0."""


def solve1(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "NIESKONCZENIE WIELE ROZWIAZAN"
            else:
                return "ROWNANIE SPRZECZNE"
        else:
            return "y = {}".format(-c / b)
    else:
        if b == 0:
            return "x = {}".format(-c / a)
        else:
            if c != 0:
                return "y = {}x{:+}".format(-a / b, -c / b)
            else:
                return "y = {}x".format(-a / b)


"""Obliczanie liczby pi metodą Monte Carlo.
n oznacza liczbę losowanych punktów."""


def calc_pi(n=100):
    circle = 0
    for i in range(n):
        x = random.random()
        y = random.random()

        if x ** 2 + y ** 2 <= 1:
            circle += 1

    return 4 * circle / n


"""
Obliczanie pola powierzchni trójkąta za pomocą wzoru
Herona. Długości boków trójkąta wynoszą a, b, c.
"""


def heron(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        raise ValueError


# Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j). Porównać
# z wersją rekurencyjną programu. Wskazówka: Wykorzystać tablicę
# dwuwymiarową (np. słownik) do przechowywania wartości funkcji. Wartości w tablicy wypełniać kolejno wierszami.


def P_recursion(i, j):
    if i == 0 and j == 0:
        return 0.5
    if i > 0 and j == 0:
        return 0.0
    if i == 0 and j > 0:
        return 1.0
    if i > 0 and j > 0:
        return 0.5 * (P_recursion(i - 1, j) + P_recursion(i, j - 1))


def P_dynamic(i, j):
    D = {}
    D[(0, 0)] = 0.5
    for k in range(max(i, j) + 1):
        D[(k, 0)] = 0
        D[(0, k)] = 1

    for x in range(1, max(i, j) + 1):
        for y in range(1, max(i, j) + 1):
            D[(x, y)] = 0.5 * (D[(x - 1, y)] + D[(x, y - 1)])

    return D[(i, j)]


class Test(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual(solve1(0, 0, 0), "NIESKONCZENIE WIELE ROZWIAZAN")
        self.assertEqual(solve1(0, 0, 1), "ROWNANIE SPRZECZNE")
        self.assertEqual(solve1(-4, 2, -4), "y = 2.0x+2.0")
        self.assertEqual(solve1(1, 1, 0), "y = -1.0x")
        self.assertEqual(solve1(0, 1, 1), "y = -1.0")
        self.assertEqual(solve1(0, 1, 0), "y = 0.0")
        self.assertEqual(solve1(1, 0, 0), "x = 0.0")
        self.assertEqual(solve1(1, 1, 1), "y = -1.0x-1.0")

    def test_pi(self):
        self.assertTrue(abs(calc_pi(10000) - 3.14) < 0.1, True)

    def test_heron(self):
        self.assertEqual(heron(4, 13, 15), 24)
        self.assertEqual(heron(3, 4, 5), 6)
        self.assertRaises(ValueError, heron, 50, 1, 2)

    def test_P_recursion(self):
        self.assertEqual(P_recursion(2, 3), 0.6875)

    def test_P_dynamic(self):
        self.assertEqual(P_dynamic(2, 3), 0.6875)


if __name__ == '__main__':
    unittest.main()
