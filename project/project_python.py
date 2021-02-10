import copy
import unittest
from math import ceil


class Edge:
    """Klasa dla krawędzi skierowanej z wagą."""

    def __init__(self, source, target, weight=1):
        """Konstruktor krawędzi.."""
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """Zwraca reprezentacje napisowa krawędzi.."""
        if self.weight == 1:
            return "Edge(%s, %s)" % (
                repr(self.source), repr(self.target))
        else:
            return "Edge(%s, %s, %s)" % (
                repr(self.source), repr(self.target), repr(self.weight))

    def __cmp__(self, other):
        """Porównywanie krawędzi."""
        if self.weight > other.weight:
            return 1
        if self.weight < other.weight:
            return -1
        if self.source > other.source:
            return 1
        if self.source < other.source:
            return -1
        if self.target > other.target:
            return 1
        if self.target < other.target:
            return -1
        return 0

    def __hash__(self):
        """Krawędzie są hashowalne."""
        # return hash(repr(self))
        return hash((self.source, self.target, self.weight))

    def __invert__(self):
        """Zwraca krawędź o przeciwnym kierunku."""
        return Edge(self.target, self.source, self.weight)


class Graph:
    """Klasa dla grafu ważonego, skierowanego lub nieskierowanego."""

    def __init__(self, n, directed=False):
        self.n = n  # kompatybilność
        self.directed = directed  # bool, czy graf skierowany
        self.adj = [[] for i in range(self.n)]  # główna lista
        self.edges_count = 0  # liczba krawedzi
        self.getDFS = []  # lista zwracająca DFS dla danego wierzchołka
        self.getBFS = []  # lista zwracająca BFS dla danego wierzchołka

    def v(self):  # zwraca liczbę wierzchołków
        return self.n

    def e(self):  # zwraca liczbę krawędzi
        return self.edges_count

    def is_directed(self):  # bool, czy graf skierowany
        return self.directed

    def add_node(self, node):  # dodaje wierzchołek
        assert self.n >= node

    def has_node(self, node):  # bool
        return node < self.n

    def del_node(self, node):  # usuwa wierzchołek
        assert node < self.n, "node is not exist"

        if self.is_directed():
            self.edges_count -= len(self.adj[node])
            self.adj[node].clear()

            for vector in self.adj:
                if node in vector:
                    vector.remove(node)
                    self.edges_count -= 1

        else:
            self.edges_count -= len(self.adj[node])
            self.adj[node].clear()

            for vector in self.adj:
                if node in vector:
                    vector.remove(node)

    def add_edge(self, edge):  # wstawienie krawędzi
        assert (self.n > edge.source and self.n > edge.target) and edge.target != edge.source and edge.target not in self.adj[edge.source]
        if self.is_directed():  # dodajemy krawedz do listy danego wierzcholka
            self.adj[edge.source].append(edge.target)
            self.edges_count += 1
        else:  # dodajemy krawedz do listy danego wierzcholka i do jego celu
            if edge.source != edge.target:
                self.adj[edge.target].append(edge.source)
                self.adj[edge.source].append(edge.target)
            else:
                self.adj[edge.source].append(edge.target)
            self.edges_count += 1

    def has_edge(self, edge):  # bool
        return edge.target in self.adj[edge.source]

    def del_edge(self, edge):  # usunięcie krawędzi
        assert edge.source < self.n and edge.target < self.n, "vector out of max"
        assert edge.target in self.adj[edge.source]

        if self.is_directed():  # iterujemy po wszystkich krawędziach wierzchołka źródłowego i porównujemy
            self.adj[edge.source].remove(edge.target)
        else:  # iterujemy po wszystkich krawędziach wierzchołka źródłowego i docelowego i porównujemy
            self.adj[edge.source].remove(edge.target)
            self.adj[edge.target].remove(edge.source)
        self.edges_count -= 1

    def weight(self, edge):  # zwraca wagę krawędzi
        return edge.weight

    def iternodes(self):  # iterator po wierzchołkach
        for node in range(self.n):
            yield node

    def iteradjacent(self, node):  # iterator po wierzchołkach sąsiednich
        for node in self.adj[node]:
            yield node

    def iteroutedges(self, node):  # iterator po krawędziach wychodzących
        for i in self.adj[node]:
            yield Edge(node, i)

    def iterinedges(self, node):  # iterator po krawędziach przychodzących
        for k in self.adj:
            if node in k:
                yield Edge(self.adj.index(k), node)

    def iteredges(self):  # iterator po krawędziach
        if self.is_directed():
            for i in range(0, self.n):
                for k in self.adj[i]:
                    yield Edge(i, k)
        else:
            for i in range(0, self.n):
                for k in self.adj[i]:
                    if i < k:
                        yield Edge(i, k)

    def copy(self):  # zwraca kopię grafu
        return copy.deepcopy(self)

    def transpose(self):  # zwraca graf transponowany
        new_graph = self.copy()

        if self.is_directed():  # usuwamy wszystkie krawedzie z nowego grafu
            for k in new_graph.adj:
                k.clear()

            for i in range(0, self.n):  # dodajemy "odwrócne" krawedzie do "nowego" grafu, wierzchołki się nie zmieniają
                for k in self.adj[i]:
                    new_graph.add_edge(Edge(k, i))

            return new_graph
        else:  # jeżeli graf nie jest skierowany, graf transponowany zwróci to samo
            return new_graph

    def complement(self):  # zwraca dopełnienie grafu
        new_graph = Graph(self.n, directed=self.is_directed())

        if self.is_directed():  # tworzymy wszystkie nowe połaczenia, ktore nie pojawiły się wcześniej
            for i in range(0, self.n):
                for j in range(0, self.n):
                    if j not in self.adj[i] and i != j:
                        new_edge = Edge(i, j)
                        new_graph.add_edge(new_edge)
        else:
            for i in range(0, self.n):
                for j in range(i+1, self.n):
                    if j not in self.adj[i] and i not in self.adj[j] and i != j:
                        new_edge = Edge(i, j)
                        new_graph.add_edge(new_edge)

        return new_graph

    def subgraph(self, nodes):  # zwraca podgraf indukowany
        new_graph = Graph(self.n, self.directed)

        if self.is_directed():
            for i in nodes:
                for target in self.adj[i]:  # sprawdzamy, czy wierzchołek źródłowy i jego cel znajdują się w liście
                    if target in nodes:
                        new_edge = Edge(i, target)
                        new_graph.add_edge(new_edge)
        else:
            for i in nodes:
                for target in self.adj[i]:  # sprawdzamy, czy wierzchołek źródłowy i jego cel znajdują się w liście
                    if target in nodes and i not in new_graph.adj[target] and i != target:
                        new_edge = Edge(i, target)
                        new_graph.add_edge(new_edge)

        return new_graph

    def DFS(self, v):  # Przejście grafu DFS od podanego wierzchołka
        assert 0 <= v < self.n and self.is_directed()

        self.getDFS.clear()  # czyścimy, jeżeli wcześniej była używana
        visited = [False] * self.n  # tablica odwiedzonych wierzchołków
        self.DFSRecursion(v, visited)  # rozpoczynamy rekurencję

        return self.getDFS

    def DFSRecursion(self, v, visited):
        visited[v] = True
        self.getDFS.append(v)

        for target in self.adj[v]:
            if not visited[target]:
                self.DFSRecursion(target, visited)

    def BFS(self, v):  # przejście grafu BFS od podanego wierzchołka
        assert 0 <= v < self.n and self.is_directed()
        self.getBFS.clear()

        visited = [False] * self.n  # tablica odwiedzonych wierzchołków
        queue = []

        visited[v] = True
        queue.append(v)

        while len(queue) != 0:
            s = queue.pop(0)
            self.getBFS.append(s)

            for target in self.adj[s]:
                if not visited[target]:
                    visited[target] = True
                    queue.append(target)

        return self.getBFS


class Tests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(5, directed=True)
        self.graph.add_node(0)
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_node(3)
        self.graph.add_node(4)
        self.graph.add_edge(Edge(0, 1))
        self.graph.add_edge(Edge(0, 3))
        self.graph.add_edge(Edge(3, 1))
        self.graph.add_edge(Edge(1, 4))
        self.graph.add_edge(Edge(4, 2))
        self.graph.add_edge(Edge(2, 0))

        self.undirected_graph = Graph(3, directed=False)
        self.undirected_graph.add_node(0)
        self.undirected_graph.add_node(1)
        self.undirected_graph.add_node(2)
        self.undirected_graph.add_edge(Edge(0, 1))
        self.undirected_graph.add_edge(Edge(0, 2))
        self.undirected_graph.add_edge(Edge(1, 2))

    def testCount(self):
        self.assertEqual(self.graph.is_directed(), True)
        self.assertEqual(self.graph.v(), 5)
        self.assertEqual(self.graph.e(), 6)
        self.graph.del_node(3)
        self.assertEqual(self.graph.v(), 5)
        self.assertEqual(self.graph.e(), 4)
        self.assertEqual(self.graph.has_node(4), True)
        self.assertEqual(self.graph.has_node(3), True)
        self.assertEqual(self.graph.has_edge(Edge(4, 2)), True)
        self.assertEqual(self.graph.has_edge(Edge(3, 1)), False)
        self.graph.del_edge(Edge(0, 1))
        self.assertEqual(self.graph.has_edge(Edge(0, 1)), False)
        self.graph.add_node(3)
        self.graph.add_edge(Edge(0, 3))
        self.graph.add_edge(Edge(3, 1))
        self.graph.add_edge(Edge(0, 1))

    def testIterations(self):
        self.assertEqual(list(self.graph.iternodes()), [0, 1, 2, 3, 4])
        self.assertEqual(list(self.graph.iteradjacent(2)), [0])
        self.assertEqual([k.__repr__() for k in self.graph.iteroutedges(0)], [k.__repr__() for k in
                                                                              [Edge(0, 1), Edge(0, 3)]])
        self.assertEqual([k.__repr__() for k in self.graph.iterinedges(1)], [k.__repr__() for k in
                                                                             [Edge(0, 1), Edge(3, 1)]])
        self.assertEqual(self.graph.DFS(3), [3, 1, 4, 2, 0])
        self.assertEqual(self.graph.BFS(0), [0, 1, 3, 4, 2])

    def testOther(self):
        self.graph_b = self.graph.transpose()
        self.assertEqual(self.graph_b.has_edge(Edge(2, 4)), True)
        self.assertEqual(self.graph_b.has_edge(Edge(1, 3)), True)

        self.graph_c = self.graph.complement()
        self.assertEqual(self.graph_c.has_edge(Edge(0, 0)), False)
        self.assertEqual(self.graph_c.has_edge(Edge(1, 1)), False)
        self.assertEqual(self.graph_c.has_edge(Edge(0, 4)), True)
        self.assertEqual(self.graph_c.has_edge(Edge(0, 3)), False)

        self.graph_d = self.graph.subgraph([0, 1, 3])
        self.assertEqual([k.__repr__() for k in self.graph_d.iteredges()], [k.__repr__() for k in
                                                                            [Edge(0, 1), Edge(0, 3), Edge(3, 1)]])

    def testCount2(self):
        self.assertEqual(self.undirected_graph.is_directed(), False)
        self.assertEqual(self.undirected_graph.v(), 3)
        self.assertEqual(self.undirected_graph.e(), 3)
        self.undirected_graph.del_node(2)
        self.assertEqual(self.undirected_graph.v(), 3)
        self.assertEqual(self.undirected_graph.e(), 1)
        self.assertEqual(self.undirected_graph.has_node(5), False)
        self.assertEqual(self.undirected_graph.has_node(0), True)
        self.assertEqual(self.undirected_graph.has_edge(Edge(0, 1)), True)
        self.assertEqual(self.undirected_graph.has_edge(Edge(1, 2)), False)
        self.undirected_graph.del_edge(Edge(0, 1))
        self.assertEqual(self.undirected_graph.has_edge(Edge(0, 1)), False)
        self.assertEqual(self.undirected_graph.e(), 0)
        self.undirected_graph.add_node(2)
        self.undirected_graph.add_edge(Edge(0, 1))
        self.undirected_graph.add_edge(Edge(0, 2))
        self.undirected_graph.add_edge(Edge(1, 2))

    def testIterations2(self):
        self.assertEqual(list(self.undirected_graph.iternodes()), [0, 1, 2])
        self.assertEqual(list(self.undirected_graph.iteradjacent(2)), [0, 1])
        self.assertEqual([k.__repr__() for k in self.undirected_graph.iteroutedges(0)], [k.__repr__() for k in
                                                                                         [Edge(0, 1), Edge(0, 2)]])
        self.assertEqual([k.__repr__() for k in self.undirected_graph.iterinedges(1)], [k.__repr__() for k in
                                                                                        [Edge(0, 1), Edge(2, 1)]])

    def testOther2(self):
        self.undirected_graph_b = self.undirected_graph.transpose()
        self.assertEqual(self.undirected_graph_b.has_edge(Edge(0, 1)), True)
        self.assertEqual(self.undirected_graph_b.has_edge(Edge(2, 1)), True)
        self.assertRaises(AssertionError, self.undirected_graph.add_node, 4)

        self.undirected_graph_c = self.undirected_graph.complement()
        self.assertEqual(self.undirected_graph_c.has_edge(Edge(0, 4)), False)
        self.assertEqual(self.undirected_graph_c.has_edge(Edge(0, 1)), False)
        self.assertEqual(self.undirected_graph_c.has_edge(Edge(1, 2)), False)
        self.assertEqual(self.undirected_graph_c.has_edge(Edge(0, 2)), False)

        self.undirected_graph_d = self.undirected_graph.subgraph([0, 1])
        self.assertEqual([k.__repr__() for k in self.undirected_graph_d.iteredges()], [k.__repr__() for k in
                                                                                       [Edge(0, 1)]])


if __name__ == '__main__':
    unittest.main()
