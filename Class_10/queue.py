import unittest


class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data
    

class MyTest(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(3)

    def testElements(self):
        self.assertRaises(ValueError, self.queue.get)
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(3)
        self.assertEqual(self.queue.get(), 1)
        self.queue.put(1)
        self.assertRaises(ValueError, self.queue.put, 4)
        self.assertEqual(self.queue.is_full(), True)
        self.assertEqual(self.queue.is_empty(), False)


if __name__ == '__main__':
    unittest.main()
