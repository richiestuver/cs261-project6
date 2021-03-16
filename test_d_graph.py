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

        self.assertEqual(True, False)


class TestAddEdge(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

        self.assertEqual(True, False)


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
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

        self.assertEqual(True, False)


class TestGetEdges(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

        self.assertEqual(True, False)


class TestIsValidPath(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

        self.assertEqual(True, False)


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
