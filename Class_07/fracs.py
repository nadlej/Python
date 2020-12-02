from math import gcd
import unittest


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        try:
            assert y != 0
            self.x = x
            self.y = y
        except AssertionError:
            raise ValueError

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return "{}".format(self.x)
        else:
            return "{0} / {1}".format(self.x, self.y)

    def __repr__(self):  # zwraca "Frac(x, y)"
        return 'Frac({},{})'.format(self.x, self.y)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        return 1 if self.x * other.y == other.x * self.y else 0

    def __ne__(self, other):
        return 1 if self.x * other.y != other.x * self.y else 0

    def __lt__(self, other):
        return 1 if self.x * other.y < other.x * self.y else 0

    def __le__(self, other):
        return 1 if self.x * other.y > other.x * self.y else 0

    def __add__(self, other):  # frac1+frac2, frac+int
        other = self._normalize(other)
        nb = [self.x * other.y + other.x * self.y, self.y * other.y]
        mod = gcd(nb[0], nb[1])

        return Frac(nb[0] / mod, nb[1] / mod)

    __radd__ = __add__  # int+frac

    def __sub__(self, other):  # frac1-frac2, frac-int
        other = self._normalize(other)
        nb = [self.x * other.y - other.x * self.y, self.y * other.y]
        mod = gcd(nb[0], nb[1])

        return Frac(nb[0] / mod, nb[1] / mod)

    def __rsub__(self, other):  # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):  # frac1*frac2, frac*int
        other = self._normalize(other)
        nb = [self.x * other.x, self.y * other.y]
        mod = gcd(nb[0], nb[1])

        return Frac(nb[0] / mod, nb[1] / mod)

    __rmul__ = __mul__  # int*frac

    def __div__(self, other):  # frac1/frac2, frac/int, Python 2
        other = self._normalize(other)
        nb = [self.x * other.y, self.y * other.x]
        mod = gcd(nb[0], nb[1])

        return Frac(nb[0] / mod, nb[1] / mod)

    def __rdiv__(self, other):  # int/frac, Python 2
        return Frac(self.x, self.y * other)

    def __truediv__(self, other):  # frac1/frac2, frac/int, Python 3
        other = self._normalize(other)
        return float(self) / float(other)

    def __rtruediv__(self, other):  # int/frac, Python 3
        return other / float(self)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):  # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))  # immutable fracs
        # assert set([2]) == set([2.0])

    @staticmethod
    def _normalize(other):
        if isinstance(other, int):
            other = Frac(other)
        elif isinstance(other, float):
            m, n = other.as_integer_ratio()
            other = Frac(m, n)
        return other


# Kod testujący moduł.


class TestFrac(unittest.TestCase):
    def setUp(self):
        self.f0 = Frac(0, 1)
        self.f1 = Frac(3, 6)
        self.f2 = Frac(-1, 3)
        self.f3 = Frac(7, 10)

    def test_str(self):
        self.assertEqual(self.f3.__str__(), "7 / 10")
        self.assertEqual(self.f0.__str__(), "0")

    def test_repr(self):
        self.assertEqual(self.f1.__repr__(), "Frac(3,6)")
        self.assertEqual(self.f2.__repr__(), "Frac(-1,3)")

    def test_eq(self):
        self.assertFalse(self.f0.__eq__(self.f1))
        self.assertTrue(self.f0.__eq__(self.f0))

    def test_ne(self):
        self.assertTrue(self.f0.__ne__(self.f1))
        self.assertFalse(self.f0.__ne__(self.f0))

    def test_lt(self):
        self.assertTrue(self.f2.__lt__(self.f3))
        self.assertFalse(self.f1.__lt__(self.f0))

    def test_le(self):
        self.assertFalse(self.f2.__le__(self.f3))
        self.assertTrue(self.f1.__le__(self.f0))

    def test_add(self):
        self.assertEqual(self.f0.__add__(2), Frac(2, 1))
        self.assertEqual(self.f2.__add__(self.f3), Frac(11, 30))
        self.assertEqual(self.f1.__add__(0.5), Frac(1, 1))

    def test_sub(self):
        self.assertEqual(self.f1.__sub__(0.5), Frac(0, 1))
        self.assertEqual(self.f2.__sub__(self.f3), Frac(-31, 30))
        self.assertEqual(self.f3.__sub__(0.2), Frac(1, 2))

    def test_mul(self):
        self.assertEqual(self.f1.__mul__(2), Frac(1, 1))
        self.assertEqual(self.f2.__mul__(self.f3), Frac(-7, 30))
        self.assertEqual(self.f1.__mul__(0.2), Frac(1, 10))

    def test_div(self):
        self.assertRaises(ValueError, self.f1.__div__, self.f0)
        self.assertEqual(self.f2.__div__(self.f3), Frac(-10, 21))
        self.assertEqual(self.f1.__div__(self.f2), Frac(3, -2))

    def test_frac2float(self):
        self.assertEqual(self.f2.__float__(), -1 / 3)

    def test_truediv(self):
        self.assertEqual(self.f2.__truediv__(2), (-1 / 3) / 2)
        self.assertEqual(self.f3.__truediv__(10 / 7), (7 / 10) / (10 / 7))

    def test_cmp_frac(self):
        self.assertTrue(self.f1 > self.f0)
        self.assertTrue(self.f1 > self.f2)
        self.assertTrue(self.f3 > self.f1)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()