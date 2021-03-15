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
    def test_add_edge(self):
        expected = ["""GRAPH: {
  A: ['B', 'C']
  B: ['A', 'C', 'D']
  C: ['A', 'B', 'D', 'E']
  D: ['B', 'C', 'E']
  E: ['C', 'D']}"""]
        results = []

        g = UndirectedGraph()

        for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
            g.add_edge(u, v)

        results.append(str(g))

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestRemoveEdge(unittest.TestCase):
    def test_something(self):
        expected = ["""GRAPH: {
  A: ['C']
  B: ['C', 'D']
  C: ['A', 'B', 'D', 'E']
  D: ['B', 'C', 'E']
  E: ['C', 'D']}"""]
        results = []

        g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
        g.remove_edge('A', 'B')
        g.remove_edge('X', 'B')
        results.append(str(g))

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestRemoveVertex(unittest.TestCase):
    def test_something(self):
        expected = ["""GRAPH: {
  A: ['C']
  B: ['C', 'D']
  C: ['A', 'B', 'D', 'E']
  D: ['B', 'C', 'E']
  E: ['C', 'D']}""",
                    "GRAPH: {A: ['C'], B: ['C'], C: ['A', 'B', 'E'], E: ['C']}"]
        results = []

        g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
        g.remove_vertex('DOES NOT EXIST')
        g.remove_edge('A', 'B')
        g.remove_edge('X', 'B')
        results.append(str(g))
        g.remove_vertex('D')
        results.append(str(g))

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestGetVertices(unittest.TestCase):
    def test_something(self):
        expected = [[],
                    sorted(['A', 'B', 'C', 'D', 'E'])]
        results = []

        g = UndirectedGraph()
        results.append(g.get_vertices())
        g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
        results.append(g.get_vertices())

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestGetEdges(unittest.TestCase):
    def test_something(self):
        expected = [[],
                    sorted([('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E')])]
        results = []

        g = UndirectedGraph()
        results.append(g.get_edges())
        g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
        results.append(g.get_edges())

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestIsValidPath(unittest.TestCase):
    def test_something(self):
        expected = [(['A', 'B', 'C'], True),
                    (['A', 'D', 'E'], False),
                    (['E', 'C', 'A', 'B', 'D', 'C', 'B', 'E'], False),
                    (['A', 'C', 'D', 'E', 'C', 'B'], True),
                    ([], True),
                    (['D'], True),
                    (['Z'], False)]
        results = []

        g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
        test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
        for path in test_cases:
            results.append(g.is_valid_path(list(path)))

        for i in range(len(expected)):
            with self.subTest(expected[i][0]):
                self.assertEqual(expected[i][1], results[i])


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
