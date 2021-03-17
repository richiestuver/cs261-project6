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

    def test_gs1(self):
        expected = ["GRAPH: {C: ['J'], J: ['C']}"]
        results = []

        g = UndirectedGraph()
        for u, v in ['CJ', 'JC']:
            g.add_edge(u, v)

        g.add_edge('B', 'B')
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
        expected = [['B', 'C', 'A', 'E', 'D', 'H'],
                    ['C', 'A', 'E'],
                    ['D'],
                    ['E', 'A', 'C'],
                    ['G', 'F', 'Q'],
                    ['H', 'B', 'C', 'A']]
        results = []
        labels = []

        edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
        g = UndirectedGraph(edges)
        test_cases = 'ABCDEGH'
        for case in test_cases:
            labels.append(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')

        for i in range(1, len(test_cases)):
            v1, v2 = test_cases[i], test_cases[-1 - i]
            results.append(g.dfs(v1, v2))

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestBFS(unittest.TestCase):
    def test_something(self):
        expected = [['B', 'C', 'D', 'E', 'H', 'A'],
                    ['C', 'A', 'B', 'D', 'E'],
                    ['D'],
                    ['E', 'A', 'B', 'C'],
                    ['G', 'F', 'Q'],
                    ['H', 'B', 'C', 'D', 'E', 'A']]
        results = []
        labels = []

        edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
        g = UndirectedGraph(edges)
        test_cases = 'ABCDEGH'

        for case in test_cases:
            labels.append(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')

        for i in range(1, len(test_cases)):
            v1, v2 = test_cases[i], test_cases[-1 - i]
            results.append(g.bfs(v1, v2))

        for i in range(len(expected)):
            with self.subTest(labels[i]):
                self.assertEqual(expected[i], results[i])

    def test_gs1(self):
        expected = [[]]
        results = []

        graph = UndirectedGraph()
        g = {
  'E': ['D', 'F', 'J'],
  "D": ['E', 'H'],
  'H': ['A', 'D'],
  'A': ['H', 'J'],
  'F': ['E'],
  'K': ['B'],
  'B': ['K', 'G'],
  'J': ['E', 'A'],
  'G': ['B']}


        for v in g:
            for u in g[v]:
                graph.add_edge(v, u)
        print(graph)
        results.append(graph.bfs('I'))
        print(graph)

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])

class TestCountConnected(unittest.TestCase):
    def test_something(self):
        expected = [1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 2]
        results = []

        edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
        g = UndirectedGraph(edges)
        test_cases = (
            'add QH', 'remove FG', 'remove GQ', 'remove HQ',
            'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
            'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
            'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
        for case in test_cases:
            command, edge = case.split()
            u, v = edge
            g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
            results.append(g.count_connected_components())

        for i in range(len(expected)):
            with self.subTest(expected[i]):
                self.assertEqual(expected[i], results[i])


class TestHasCycle(unittest.TestCase):
    def test_something(self):
        expected = [True, True, True, True, True, True, True, True, True,
                    False, False, False, False, False, False,
                    True, True, True,
                    False, False,
                    True, False]
        results = []
        labels = []

        edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
        g = UndirectedGraph(edges)
        test_cases = (
            'add QH', 'remove FG', 'remove GQ', 'remove HQ',
            'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
            'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
            'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
            'add FG', 'remove GE')
        for case in test_cases:
            command, edge = case.split()
            u, v = edge
            g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
            labels.append('{:<10}'.format(case))
            results.append(g.has_cycle())

        for i in range(len(expected)):
            with self.subTest(labels[i]):
                self.assertEqual(expected[i], results[i])

if __name__ == '__main__':
    unittest.main()
