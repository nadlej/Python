import math
import unittest


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
        if isinstance(other, Circle):
            return self.x == other.pt.x and self.y == other.pt.y
        else:
            return self.x == other.x and self.y == other.y

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

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return 3.14 * self.radius**2

    def move(self, x, y):     # przesuniecie o (x, y)
        return self.pt + Point(x, y)

    def cover(self, other):   # najmniejszy okrąg pokrywający oba
        if self.pt == other.pt:
            return Circle(self.pt.x, self.pt.y, max(self.radius, other.radius))

        if self.radius <= other.radius:
            C1, C2 = self, other
        else:
            C1, C2 = other, self

        distance = (C1.pt - C2.pt).length()

        if distance + self.radius <= other.radius:
            return Circle(other.x, other.y, other.radius)
        else:
            R = (distance + self.radius + other.radius) / 2
            theta = 1 / 2 + (C2.radius - C1.radius) / (2 * distance)
            center_x = C1.pt.x + (C2.pt.x - C1.pt.x) * theta
            center_y = C1.pt.y + (C2.pt.y - C1.pt.y) * theta

            return Circle(center_x, center_y, R)


# Kod testujący moduł.


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(5, 5, 5)
        self.c2 = Circle(0, 0, 10)
        self.c3 = Circle(0, 0, 5)
        self.c4 = Circle(-2, 5, 8)

    def test_repr(self):
        self.assertEqual(self.c2.__repr__(), "Circle(0, 0, 10)")

    def test_equal(self):
        self.assertFalse(self.c1 == self.c2)
        self.assertTrue(self.c1 == Circle(5, 5, 5))

    def test_move(self):
        self.assertEqual(self.c4.move(2, -5), Circle(0, 0, 8))
        self.assertEqual(self.c3.move(5, 5), Circle(5, 5, 5))

    def test_area(self):
        self.assertEqual(self.c3.area(), 3.14 * 5**2)

    def test_cover(self):
        self.assertEqual(self.c2.cover(self.c3), Circle(0, 0, 10))
        self.assertEqual(self.c1.cover(self.c3), Circle(2.5, 2.5, 8.535533905932738))


if __name__ == '__main__':
    unittest.main()