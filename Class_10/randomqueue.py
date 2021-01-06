import random
import unittest


class RandomQueue:

    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)

    def remove(self):   # zwraca losowy element
        pos = random.randint(0, len(self.queue)-1)
        self.queue[pos], self.queue[-1] = self.queue[-1], self.queue[pos]
        return self.queue.pop()

    def is_empty(self):
        return not self.queue

    def is_full(self):
        return False

    def clear(self):    # czyszczenie listy
        self.queue.clear()


class MyTest(unittest.TestCase):
    def setUp(self):
        self.queue = RandomQueue()
        self.queue.insert(1)
        self.queue.insert(2)
        self.queue.insert(3)
        self.queue.insert(4)

    def testElements(self):
        self.assertEqual(self.queue.is_full(), False)
        self.assertEqual(self.queue.is_empty(), False)
        print(self.queue.remove())
        print(self.queue.remove())


if __name__ == '__main__':
    unittest.main()