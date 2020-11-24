import unittest
import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return '({},{})'.format(self.x, self.y)

    def __repr__(self):        # zwraca string "Point(x, y)"
        return 'Point({},{})'.format(self.x, self.y)

    def __eq__(self, other):   # obsługa point1 == point2
        return self.__repr__() == other.__repr__()

    def __ne__(self, other):        # obsługa point1 != point2
        return not self.__repr__() == other.__repr__()

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(self.x**2 + self.y**2)

# Kod testujący moduł.

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.f0 = Point(0, 1)
        self.f1 = Point(3, 6)
        self.f2 = Point(-1, 3)
        self.f3 = Point(7, 10)

    def test_str(self):
        self.assertEqual(self.f3.__str__(), '(7,10)')
        self.assertEqual(self.f0.__str__(), '(0,1)')

    def test_repr(self):
        self.assertEqual(self.f1.__repr__(), 'Point(3,6)')
        self.assertEqual(self.f2.__repr__(), 'Point(-1,3)')

    def test_eq(self):
        self.assertFalse(self.f0.__eq__(self.f1))
        self.assertTrue(self.f0.__eq__(self.f0))

    def test_ne(self):
        self.assertTrue(self.f0.__ne__(self.f1))
        self.assertFalse(self.f0.__ne__(self.f0))

    def test_add(self):
        self.assertEqual(self.f1.__add__(self.f0), Point(3, 7))
        self.assertEqual(self.f2.__add__(self.f3), Point(6, 13))
        self.assertEqual(self.f1.__add__(self.f2), Point(2, 9))

    def test_sub(self):
        self.assertEqual(self.f1.__sub__(self.f0), Point(3, 5))
        self.assertEqual(self.f2.__sub__(self.f3), Point(-8, -7))
        self.assertEqual(self.f1.__sub__(self.f2), Point(4, 3))

    def test_cross(self):
        self.assertEqual(self.f1.cross(self.f0), 3)
        self.assertEqual(self.f2.cross(self.f3), -31)

    def test_mul(self):
        self.assertEqual(self.f1.__mul__(self.f0), 6)
        self.assertEqual(self.f2.__mul__(self.f3), 23)
        self.assertEqual(self.f1.__mul__(self.f2), 15)

    def test_len(self):
        self.assertEqual(self.f1.length(), math.sqrt(self.f1.x**2 + self.f1.y**2))
        self.assertEqual(self.f2.length(), math.sqrt(self.f2.x**2 + self.f2.y**2))
        self.assertEqual(self.f3.length(), math.sqrt(self.f3.x**2 + self.f3.y**2))


if __name__ == '__main__':
    unittest.main()