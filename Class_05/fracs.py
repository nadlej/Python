from math import gcd
import unittest


def add_frac(frac1, frac2):  # frac1 + frac2
    nb = [frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]]
    mod = gcd(nb[0], nb[1])

    return [nb[0] / mod, nb[1] / mod]


def sub_frac(frac1, frac2):  # frac1 - frac2
    nb = [frac1[0] * frac2[1] - frac2[0] * frac1[1], frac1[1] * frac2[1]]
    mod = gcd(nb[0], nb[1])

    return [nb[0] / mod, nb[1] / mod]


def mul_frac(frac1, frac2):  # frac1 * frac2
    nb = [frac1[0] * frac2[0], frac1[1] * frac2[1]]

    assert nb[1] != 0, 'DIVIDING BY 0'

    mod = gcd(nb[0], nb[1])

    return [nb[0] / mod, nb[1] / mod]


def div_frac(frac1, frac2):  # frac1 / frac2
    nb = [frac1[0] * frac2[1], frac1[1] * frac2[0]]

    assert nb[1] != 0,'DIVIDING BY 0'

    mod = gcd(nb[0], nb[1])

    return [nb[0] / mod, nb[1] / mod]


def is_positive(frac):  # bool, czy dodatni
    return frac[0] * frac[1] > 0


def is_zero(frac):  # bool, typu [0, x]
    return frac[0] == 0


def cmp_frac(frac1, frac2):  # -1 | 0 | +1
    if frac2float(frac1) > frac2float(frac2):
        return -1
    elif frac2float(frac1) < frac2float(frac2):
        return 1
    else:
        return 0


def frac2float(frac):  # konwersja do float
    return frac[0] / frac[1]


f1 = [-1, 2]  # -1/2
f2 = [0, 1]  # zero
f3 = [3, 1]  # 3
f4 = [6, 2]  # 3 (niejednoznaczność)
f5 = [0, 2]  # zero (niejednoznaczność)


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([3, 6], [1, 3]), [5, 6])
        self.assertEqual(add_frac([0, 1], [1, 3]), [1, 3])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([3, 6], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([0, 1], [1, 3]), [-1, 3])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([-1, 2], [-1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertFalse(is_positive([-1, 2]))
        self.assertTrue(is_positive([1, 2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([2, 1]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), -1)
        self.assertEqual(cmp_frac([1,2], [5, 3]), 1)
        self.assertEqual(cmp_frac([5, 2], [5, 2]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 3]), 1 / 3)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
