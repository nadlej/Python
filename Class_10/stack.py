import unittest


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]  # utworzenie tablicy
        self.n = 0  # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.n == self.size:
            raise ValueError
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.n <= 0:
            raise ValueError
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None  # usuwam referencję
        return data


class MyTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(3)

    def testElements(self):
        self.assertRaises(ValueError, self.stack.pop)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertRaises(ValueError, self.stack.push, 4)
        self.assertEqual(self.stack.pop(), 3)
        self.stack.push(3)
        self.assertEqual(self.stack.is_empty(), False)
        self.assertEqual(self.stack.is_full(), True)


if __name__ == '__main__':
    unittest.main()
