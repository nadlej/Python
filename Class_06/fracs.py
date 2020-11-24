from math import gcd
import unittest

#W pliku fracs.py zdefiniować klasę Frac wraz z potrzebnymi metodami.
#Ułamek jest reprezentowany przez parę liczb całkowitych. Napisać kod testujący moduł fracs.


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return "{}".format(self.x)
        else:
            return "{0} / {1}".format(self.x, self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return 'Frac({},{})'.format(self.x,self.y)

    def __eq__(self, other):
        return 1 if self.__sub__(other)[0] == 0 else 0

    def __ne__(self, other):
        return 1 if self.__sub__(other)[0] != 0 else 0

    def __lt__(self, other):
        nb = self.__sub__(other)
        return 1 if nb[0] < 0 else 0

    def __le__(self, other):
        nb = self.__sub__(other)
        return 1 if nb[0] > 0 else 0

    def __add__(self, other): # frac1 + frac2
        nb = [self.x * other.y + other.x * self.y, self.y * other.y]
        mod = gcd(nb[0], nb[1])

        return [nb[0] / mod, nb[1] / mod]

    def __sub__(self, other):  # frac1 - frac2
        nb = [self.x * other.y - other.x * self.y, self.y * other.y]
        mod = gcd(nb[0], nb[1])

        return [nb[0] / mod, nb[1] / mod]

    def __mul__(self, other):  # frac1 * frac2
        nb = [self.x * other.x, self.y * other.y]
        mod = gcd(nb[0], nb[1])

        return [nb[0] / mod, nb[1] / mod]

    def __div__(self, other):  # frac1 / frac2
        if other.x == 0:
            raise ZeroDivisionError
        nb = [self.x * other.y, self.y * other.x]
        mod = gcd(nb[0], nb[1])

        return [nb[0] / mod, nb[1] / mod]

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return self.x / self.y

# Kod testujący moduł.


class TestFrac(unittest.TestCase):
    def setUp(self):
        self.f0 = Frac(0, 1)
        self.f1 = Frac(3,6)
        self.f2 = Frac(-1,3)
        self.f3 = Frac(7,10)

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
        self.assertEqual(self.f1.__add__(self.f0), [1,2])
        self.assertEqual(self.f2.__add__(self.f3), [11,30])
        self.assertEqual(self.f1.__add__(self.f2), [1,6])

    def test_sub(self):
        self.assertEqual(self.f1.__sub__(self.f0), [1,2])
        self.assertEqual(self.f2.__sub__(self.f3), [-31,30])
        self.assertEqual(self.f1.__sub__(self.f2), [5,6])

    def test_mul(self):
        self.assertEqual(self.f1.__mul__(self.f0), [0,1])
        self.assertEqual(self.f2.__mul__(self.f3), [-7,30])
        self.assertEqual(self.f1.__mul__(self.f2), [-1,6])

    def test_div(self):
        self.assertRaises(ZeroDivisionError, self.f1.__div__, self.f0)
        self.assertEqual(self.f2.__div__(self.f3), [-10,21])
        self.assertEqual(self.f1.__div__(self.f2), [3,-2])

    def test_frac2float(self):
        self.assertEqual(self.f2.__float__(), -1 / 3)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()