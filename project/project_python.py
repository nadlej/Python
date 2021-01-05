import copy
import unittest


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
        self.is_vector = [0] * self.n  # tablica istnienia danych wierzchołków
        self.e = 0  # liczba krawedzi
        self.v = 0  # liczba wierzchołków
        self.getDFS = []  # lista zwracająca DFS dla danego wierzchołka
        self.getBFS = []  # lista zwracająca BFS dla danego wierzchołka

    def v(self):  # zwraca liczbę wierzchołków
        return self.v

    def e(self):  # zwraca liczbę krawędzi
        return self.e

    def is_directed(self):  # bool, czy graf skierowany
        return self.directed

    def add_node(self, node):  # dodaje wierzchołek
        assert self.n != self.v, "max number of vectors"

        self.v += 1
        self.is_vector[node] = 1

    def has_node(self, node):  # bool
        if self.is_vector[node] == 1:
            return True
        else:
            return False

    def del_node(self, node):  # usuwa wierzchołek
        assert self.is_vector[node] == 1, "node is not exist"

        edges_list = []
        for k in self.adj:
            if len(k) != 0:
                edges_list.extend(k)

        if self.is_directed():
            for edge in edges_list:
                if edge.source == node:
                    self.e -= len(self.adj[node])
                    self.adj[node].clear()
                elif edge.target == node:
                    self.adj[edge.source].remove(edge)
                    self.e -= 1
        else:
            for edge in edges_list:
                if edge.source == node:
                    self.e -= len(self.adj[node])
                    self.adj[node].clear()
                elif edge.target == node:
                    self.adj[edge.source].remove(edge)

        self.v -= 1
        self.is_vector[node] = 0

    def add_edge(self, edge):  # wstawienie krawędzi
        assert edge.source < self.n and edge.target < self.n, "vector out of max"
        if self.is_directed():  # dodajemy krawedz do listy danego wierzcholka
            self.adj[edge.source].append(edge)
            self.e += 1
        else:  # dodajemy krawedz do listy danego wierzcholka i do jego celu
            if edge.source != edge.target:
                self.adj[edge.target].append(edge.__invert__())
                self.adj[edge.source].append(edge)
            else:
                self.adj[edge.source].append(edge)
            self.e += 1

    def has_edge(self, edge):  # bool
        if self.is_vector[edge.source] == 0:
            return False
        else:
            is_true = False
            for k in self.adj[edge.source]:
                if k.__cmp__(edge) == 0:
                    is_true = True
            return is_true

    def del_edge(self, edge):  # usunięcie krawędzi
        assert edge.source < self.n and edge.target < self.n, "vector out of max"

        if self.is_directed():  # iterujemy po wszystkich krawędziach wierzchołka źródłowego i porównujemy
            for iter_ in self.adj[edge.source]:
                if iter_.__cmp__(edge) == 0:
                    self.adj[edge.source].remove(iter_)
                    self.e -= 1
        else:  # iterujemy po wszystkich krawędziach wierzchołka źródłowego i docelowego i porównujemy
            for iter_ in self.adj[edge.source]:
                if iter_.__cmp__(edge) == 0:
                    self.adj[edge.source].remove(iter_)

            for iter_ in self.adj[edge.target]:
                if iter_.__cmp__(edge.__invert__()) == 0:
                    self.adj[edge.target].remove(iter_)
                    self.e -= 1

    def weight(self, edge):  # zwraca wagę krawędzi
        return edge.weight

    def iternodes(self):  # iterator po wierzchołkach
        nodes = []
        for k in range(0, self.n):
            if self.is_vector[k] == 1:
                nodes.append(k)
        return nodes

    def iteradjacent(self, node):  # iterator po wierzchołkach sąsiednich
        nodes = [k.target for k in self.adj[node]]
        return nodes

    def iteroutedges(self, node):  # iterator po krawędziach wychodzących
        edges = ""
        for i in self.adj[node]:
            edges += i.__repr__() + '\n'
        return edges

    def iterinedges(self, node):  # iterator po krawędziach przychodzących
        edges = ""
        edges_list = []
        for k in self.adj:
            if len(k) != 0:
                edges_list.extend(k)

        for k in edges_list:
            if k.target == node:
                edges += k.__repr__() + '\n'

        return edges

    def iteredges(self):  # iterator po krawędziach
        edges = ""
        for k in self.adj:
            if len(k) != 0:
                for l in k:
                    edges += l.__repr__() + '\n'

        return edges

    def copy(self):  # zwraca kopię grafu
        return copy.deepcopy(self)

    def transpose(self):  # zwraca graf transponowany
        new_graph = self.copy()

        if self.is_directed() is True:  # usuwamy wszystkie krawedzie z nowego grafu
            for k in new_graph.adj:
                k.clear()

            edges_list = []  # tworzymy listę wierzchołków "starego" grafu
            for k in self.adj:
                if len(k) != 0:
                    edges_list.extend(k)

            for k in edges_list:  # dodajemy "odwrócne" krawedzie do "nowego" grafu, wierzchołki się nie zmieniają
                new_graph.add_edge(k.__invert__())

            return new_graph
        else:  # jeżeli graf nie jest skierowany, graf transponowany zwróci to samo
            return new_graph

    def complement(self):  # zwraca dopełnienie grafu
        new_graph = self.copy()
        edges = []
        nodes = self.iternodes()
        subnodes = []

        for k in self.adj:  # tworzymy listę wszystkich krawędzi
            if len(k) != 0:
                edges.extend(k)

        for i in nodes:  # tworzymy listę aktywnych wierzchołków i czyścimy listy ich krawędzi w nowym grafie
            new_graph.adj[i].clear()

        if self.is_directed() is True:  # tworzymy wszystkie nowe połaczenia, ktore nie pojawiły się wcześniej
            for i in nodes:
                for edge in self.adj[i]:
                    subnodes.append(edge.target)
                for j in nodes:
                    if j not in subnodes:
                        new_graph.add_edge(Edge(i, j))
                subnodes.clear()
        else:
            for i in nodes:
                for edge in self.adj[i]:
                    subnodes.append(edge.target)
                for j in nodes:
                    if j not in subnodes and new_graph.has_edge(
                            Edge(i, j)) is False:  # "odwrócone" (1;1) to wciąż (1;1)
                        new_graph.add_edge(Edge(i, j))
                subnodes.clear()

        return new_graph

    def subgraph(self, nodes):  # zwraca podgraf indukowany
        new_graph = Graph(self.n, self.directed)

        for i in nodes:  # oznaczamy przeslane wierzchołki jako aktywne
            new_graph.is_vector[i] = 1

        if self.is_directed() is True:
            for k in self.adj:
                if len(k) != 0:
                    for l in k:  # sprawdzamy, czy wierzchołek źródłowy i jego cel znajdują się w liście
                        if l.source in nodes and l.target in nodes:
                            new_graph.add_edge(Edge(l.source, l.target, l.weight))
        else:
            for k in self.adj:
                if len(k) != 0:
                    for l in k:
                        if l.source in nodes \
                                and l.target in nodes and new_graph.has_edge(Edge(l.source, l.target,
                                                                                  l.weight)) is False:
                            new_graph.add_edge(Edge(l.source, l.target, l.weight))

        return new_graph

    def DFS(self, v):
        assert v >= 0 and self.is_vector[v] == 1 and self.is_directed() is True

        self.getDFS.clear()  # czyścimy, jeżeli wcześniej była używana
        visited = [False] * self.v  # tablica odwiedzonych wierzchołków
        self.DFSRecursion(v, visited)  # rozpoczynamy rekurencję

        return self.getDFS

    def DFSRecursion(self, v, visited):
        visited[v] = True
        self.getDFS.append(v)

        for edge in self.adj[v]:
            if not visited[edge.target]:
                self.DFSRecursion(edge.target, visited)

    def BFS(self, v):
        assert v >= 0 and self.is_vector[v] == 1 and self.is_directed() is True
        self.getBFS.clear()

        visited = [False] * self.v  # tablica odwiedzonych wierzchołków
        queue = []

        visited[v] = True
        queue.append(v)

        while len(queue) != 0:
            s = queue.pop(0)
            self.getBFS.append(s)

            for edge in self.adj[s]:
                if not visited[edge.target]:
                    visited[edge.target] = True
                    queue.append(edge.target)

        return self.getBFS


class Tests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(10, directed=True)
        self.graph.add_node(0)
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_node(3)
        self.graph.add_node(4)
        self.graph.add_edge(Edge(0, 1, 3))
        self.graph.add_edge(Edge(0, 3))
        self.graph.add_edge(Edge(3, 1, 2))
        self.graph.add_edge(Edge(1, 4, 1))
        self.graph.add_edge(Edge(4, 2, 8))
        self.graph.add_edge(Edge(2, 0, 2))

        self.undirected_graph = Graph(10, directed=False)
        self.undirected_graph.add_node(0)
        self.undirected_graph.add_node(1)
        self.undirected_graph.add_node(2)
        self.undirected_graph.add_edge(Edge(0, 1))
        self.undirected_graph.add_edge(Edge(0, 2))
        self.undirected_graph.add_edge(Edge(1, 2))

    def testCount(self):
        self.assertEqual(self.graph.is_directed(), True)
        self.assertEqual(self.graph.v, 5)
        self.assertEqual(self.graph.e, 6)
        self.graph.del_node(3)
        self.assertEqual(self.graph.v, 4)
        self.assertEqual(self.graph.e, 4)
        self.assertEqual(self.graph.has_node(4), True)
        self.assertEqual(self.graph.has_node(3), False)
        self.assertEqual(self.graph.has_edge(Edge(4, 2, 8)), True)
        self.assertEqual(self.graph.has_edge(Edge(3, 1, 2)), False)
        self.graph.del_edge(Edge(0, 1, 3))
        self.assertEqual(self.graph.has_edge(Edge(0, 1, 3)), False)
        self.graph.add_node(3)
        self.graph.add_edge(Edge(0, 3))
        self.graph.add_edge(Edge(3, 1, 2))
        self.graph.add_edge(Edge(0, 1, 3))

    def testIterations(self):
        self.assertEqual(self.graph.iternodes(), [0, 1, 2, 3, 4])
        self.assertEqual(self.graph.iteradjacent(2), [0])
        self.assertEqual(self.graph.iteroutedges(0), "Edge(0, 1, 3)\nEdge(0, 3)\n")
        self.assertEqual(self.graph.iterinedges(1), "Edge(0, 1, 3)\nEdge(3, 1, 2)\n")
        self.assertEqual(self.graph.DFS(3), [3, 1, 4, 2, 0])
        self.assertEqual(self.graph.BFS(0), [0, 1, 3, 4, 2])

    def testOther(self):
        self.graph_b = self.graph.transpose()
        self.assertEqual(self.graph_b.has_edge(Edge(2, 4, 8)), True)
        self.assertEqual(self.graph_b.has_edge(Edge(1, 3, 2)), True)

        self.graph_c = self.graph.complement()
        self.assertEqual(self.graph_c.has_edge(Edge(0, 0)), True)
        self.assertEqual(self.graph_c.has_edge(Edge(1, 1)), True)
        self.assertEqual(self.graph_c.has_edge(Edge(0, 4)), True)
        self.assertEqual(self.graph_c.has_edge(Edge(0, 3)), False)

        self.graph_d = self.graph.subgraph([0, 1, 3])
        self.assertEqual(self.graph_d.iteredges(), "Edge(0, 1, 3)\nEdge(0, 3)\nEdge(3, 1, 2)\n")

    def testCount2(self):
        self.assertEqual(self.undirected_graph.is_directed(), False)
        self.assertEqual(self.undirected_graph.v, 3)
        self.assertEqual(self.undirected_graph.e, 3)
        self.undirected_graph.del_node(2)
        self.assertEqual(self.undirected_graph.v, 2)
        self.assertEqual(self.undirected_graph.e, 1)
        self.assertEqual(self.undirected_graph.has_node(2), False)
        self.assertEqual(self.undirected_graph.has_node(0), True)
        self.assertEqual(self.undirected_graph.has_edge(Edge(0, 1)), True)
        self.assertEqual(self.undirected_graph.has_edge(Edge(1, 2)), False)
        self.undirected_graph.del_edge(Edge(0, 1))
        self.assertEqual(self.undirected_graph.has_edge(Edge(0, 1)), False)
        self.assertEqual(self.undirected_graph.e, 0)
        self.undirected_graph.add_node(2)
        self.undirected_graph.add_edge(Edge(0, 1))
        self.undirected_graph.add_edge(Edge(0, 2))
        self.undirected_graph.add_edge(Edge(1, 2))

    def testIterations2(self):
        self.assertEqual(self.undirected_graph.iternodes(), [0, 1, 2])
        self.assertEqual(self.undirected_graph.iteradjacent(2), [0, 1])
        self.assertEqual(self.undirected_graph.iteroutedges(0), "Edge(0, 1)\nEdge(0, 2)\n")
        self.assertEqual(self.undirected_graph.iterinedges(1), "Edge(0, 1)\nEdge(2, 1)\n")

    def testOther2(self):
        self.undirected_graph_b = self.undirected_graph.transpose()
        self.assertEqual(self.undirected_graph_b.has_edge(Edge(0, 1)), True)
        self.assertEqual(self.undirected_graph_b.has_edge(Edge(2, 1)), True)
        self.undirected_graph.add_node(4)

        self.undirected_graph_c = self.undirected_graph.complement()
        self.assertEqual(self.undirected_graph_c.has_edge(Edge(0, 4)), True)
        self.assertEqual(self.undirected_graph_c.has_edge(Edge(4, 1)), True)
        self.assertEqual(self.undirected_graph_c.has_edge(Edge(4, 2)), True)
        self.assertEqual(self.undirected_graph_c.has_edge(Edge(1, 2)), False)

        self.undirected_graph_d = self.undirected_graph.subgraph([0, 1])
        self.assertEqual(self.undirected_graph_d.iteredges(), "Edge(0, 1)\nEdge(1, 0)\n")


if __name__ == '__main__':
    unittest.main()
