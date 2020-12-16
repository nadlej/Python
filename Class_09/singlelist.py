import unittest


class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(N)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1

    # klasy O(N)
    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.

    def remove_tail(self):
        if self.is_empty() is None:
            raise ValueError('pusta lista')
        elif self.count() == 1:
            node = self.tail
            self.head = None
            return node
        else:
            node = self.head
            while node.next.next is not None:
                node = node.next

            r_tail = node.next
            node.next = None
            self.tail = node
            self.length -= 1

        return r_tail

    # klasy O(1)
    # Węzły z listy other są przepinane do listy self na jej koniec.
    # Po zakończeniu operacji lista other ma być pusta.

    def merge(self, other):
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
            self.length = other.length
            other.head = None
        else:
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length
            other.head = None

    # czyszczenie listy

    def clear(self):
        while self.head != self.tail:
            self.remove_head()
            print(self.head)
        self.head = self.tail = None
        self.length = 0


class Test(unittest.TestCase):
    def setUp(self):
        self.alist = SingleList()
        self.alist.insert_head(Node(11))
        self.alist.insert_head(Node(22))
        self.alist.insert_tail(Node(33))
        self.blist = SingleList()
        self.blist.insert_head(Node(100))  # [11]
        self.blist.insert_head(Node(44))  # [11]
        self.clist = SingleList()

    def testLen(self):
        self.assertEqual(self.alist.length, 3)
        self.assertEqual(self.alist.count(), 3)
        self.assertEqual(self.blist.count(), 2)
        self.assertEqual(self.clist.count(), 0)

    def testMerge(self):
        self.alist.merge(self.blist)
        self.assertEqual(self.alist.count(), 5)
        self.assertEqual(self.alist.remove_tail().data, 100)
        self.clist.merge(self.alist)
        self.assertEqual(self.clist.count(), 4)
        self.assertEqual(self.clist.remove_tail().data, 44)

    def testClear(self):
        self.clist.clear()
        self.assertEqual(self.clist.count(), 0)


if __name__ == '__main__':
    unittest.main()
