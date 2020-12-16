import unittest


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def btree_count(top):
    if top is None:
        return 0
    return btree_count(top.left) + 1 + btree_count(top.right)


def count_leafs(top):
    if top.data is None:
        return 0
    if top.left is None and top.right is None:
        return 1
    counter = count_leafs(top.left) + count_leafs(top.right)
    return counter


def count_total(top):
    if top.data is None:
        return 0
    return btree_count(top.left) + 1 + btree_count(top.right)


class Test(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
        self.root1 = Node(1)
        self.root2 = Node()

    def testLeafs(self):
        self.assertEqual(count_leafs(self.root), 4)
        self.assertEqual(count_leafs(self.root1), 1)
        self.assertEqual(count_leafs(self.root2), 0)

    def testTotal(self):
        self.assertEqual(count_total(self.root), 7)
        self.assertEqual(count_total(self.root1), 1)
        self.assertEqual(count_total(self.root2), 0)


if __name__ == '__main__':
    unittest.main()
