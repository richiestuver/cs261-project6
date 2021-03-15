import unittest
from ud_graph import *


class TestAddVertex(unittest.TestCase):
    def test_something(self):
        expected = ['GRAPH: {}',
                    'GRAPH: {A: [], B: [], C: [], D: [], E: []}',
                    'GRAPH: {A: [], B: [], C: [], D: [], E: []}']
        results = []

        g = UndirectedGraph()
        results.append(str(g))

        for v in 'ABCDE':
            g.add_vertex(v)
        results.append(str(g))

        g.add_vertex('A')
        results.append(str(g))

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestAddEdge(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestRemoveVertex(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

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
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestGetEdges(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestIsValidPath(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

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


class TestBFS(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestCountConnected(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestHasCycle(unittest.TestCase):
    def test_something(self):
        expected = []
        results = []

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

if __name__ == '__main__':
    unittest.main()
