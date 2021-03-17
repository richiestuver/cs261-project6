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
        expected = [[0, 1, 4, 3, 2],
                    [1, 4, 0, 3, 2],
                    [2, 1, 4, 0, 3],
                    [3, 1, 4, 0, 2],
                    [4, 0, 1, 3, 2]]
        results = []

        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)
        for start in range(5):
            results.append(g.dfs(start))

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestBFS(unittest.TestCase):
    def test_something(self):
        expected = [[0, 1, 4, 3, 2],
                    [1, 4, 0, 3, 2],
                    [2, 1, 4, 0, 3],
                    [3, 1, 2, 4, 0],
                    [4, 0, 3, 1, 2]]
        results = []

        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)
        for start in range(5):
            results.append(g.bfs(start))

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestHasCycle(unittest.TestCase):
    def test_something(self):
        expected = [True, True, False, False, False, False, True]
        results = []
        labels = []

        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)

        edges_to_remove = [(3, 1), (4, 0), (3, 2)]
        for src, dst in edges_to_remove:
            g.remove_edge(src, dst)
            labels.append((src, dst))
            results.append(g.has_cycle())

        edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
        for src, dst in edges_to_add:
            g.add_edge(src, dst)
            labels.append((src, dst))
            results.append(g.has_cycle())

        for i in range(len(expected)):
            with self.subTest(labels[i]):
                self.assertEqual(expected[i], results[i])

    def test_gs1(self):
        expected = [False]
        results = []

        edges = [(0, 3, 19), (0, 10, 5), (1, 8, 17), (3, 12, 10),
                 (4, 0, 1), (4, 6, 14), (5, 6, 20), (6, 9, 18),
                 (6, 10, 14), (10, 8, 12), (10, 12, 15),
                 (11, 10, 5)]

        g = DirectedGraph(edges)
        results.append(g.has_cycle())
        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

class TestDijkstra(unittest.TestCase):
    def test_something(self):
        expected = [[0, 10, 35, 28, 25],
                    [27, 0, 25, 18, 15],
                    [50, 23, 0, 41, 38],
                    [32, 5, 7, 0, 20],
                    [12, 8, 10, 3, 0],
                    [0, 10, float('inf'), float('inf'), 25],
                    [27, 0, float('inf'), float('inf'), 15],
                    [50, 23, 0, float('inf'), 38],
                    [32, 5, 7, 0, 20],
                    [12, 22, float('inf'), float('inf'), 0]]
        results = []

        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)
        for i in range(5):
            results.append(g.dijkstra(i))

        g.remove_edge(4, 3)

        for i in range(5):
            results.append(g.dijkstra(i))

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

if __name__ == '__main__':
    unittest.main()
