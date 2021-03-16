import unittest
from d_graph import *


class TestAddVertex(unittest.TestCase):
    def test_something(self):
        expected = ['EMPTY GRAPH\n',
                    """GRAPH (5 vertices):
   | 0  1  2  3  4
------------------
 0 | 0  0  0  0  0
 1 | 0  0  0  0  0
 2 | 0  0  0  0  0
 3 | 0  0  0  0  0
 4 | 0  0  0  0  0
"""]
        results = []

        g = DirectedGraph()
        results.append(str(g))
        for _ in range(5):
            g.add_vertex()
        results.append(str(g))

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

class TestAddEdge(unittest.TestCase):
    def test_something(self):
        expected = ["""GRAPH (5 vertices):
   | 0  1  2  3  4
------------------
 0 | 0 10  0  0  0
 1 | 0  0  0  0 15
 2 | 0 23  0  0  0
 3 | 0  5  7  0  0
 4 |12  0  0  3  0
"""]
        results = []

        g = DirectedGraph()
        for _ in range(5):
            g.add_vertex()
        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        for src, dst, weight in edges:
            g.add_edge(src, dst, weight)
        results.append(str(g))
        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestRemoveEdge(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

        self.assertEqual(True, False)


class TestGetVertices(unittest.TestCase):
    def test_something(self):
        expected = [[],
                    [0, 1, 2, 3, 4]]
        results = []

        g = DirectedGraph()
        results.append(g.get_vertices())
        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)
        results.append(g.get_vertices())

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestGetEdges(unittest.TestCase):
    def test_something(self):
        expected = [[],
                    [(0, 1, 10), (1, 4, 15), (2, 1, 23), (3, 1, 5), (3, 2, 7), (4, 0, 12), (4, 3, 3)]]
        results = []

        g = DirectedGraph()
        results.append(g.get_edges())
        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)
        results.append(g.get_edges())

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestIsValidPath(unittest.TestCase):
    def test_something(self):
        expected = [True, False, False, True, True, True]
        results = []
        labels = []

        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)
        test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
        for path in test_cases:
            labels.append(path)
            results.append(g.is_valid_path(path))

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestDFS(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

        self.assertEqual(True, False)


class TestBFS(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

        self.assertEqual(True, False)


class TestHasCycle(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

        self.assertEqual(True, False)


class TestDijkstra(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
