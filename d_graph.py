# Course: CS261 - Data Structures
# Author: Richie Stuver
# Assignment: Project 6
# Description: Implement Directed Graph

import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Add a vertex to the graph and return the new number of vertices in the graph
        """

        self.adj_matrix.append([0 for _ in range(self.v_count)])
        for row in self.adj_matrix:
            row.append(0)

        self.v_count += 1
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        adds a new edge to the graph, connecting two vertices with provided indices. Do nothing if:
            - either (or both) vertex indices do not exist in the graph
            - the weight is not a positive integer
            - both vertices refer to the same vertex.
        If an edge already exists in the graph, the method will update its weight.
        """

        if src != dst and src in range(self.v_count) and dst in range(self.v_count):
            self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Remove edge between indicated nodes
        """

        self.add_edge(src, dst, 0)

    def get_vertices(self) -> []:
        """
        Return list of vertices
        """

        return [x for x in range(self.v_count)]

    def get_edges(self) -> []:
        """
        Return list of edges as tuples (src, dst, weight)
        """
        edges = []
        for src in range(len(self.adj_matrix)):
            for dst in range(len(self.adj_matrix[src])):
                edges.append((src, dst,self.adj_matrix[src][dst])) if self.adj_matrix[src][dst] != 0 else None

        return edges

    def is_valid_path(self, path: []) -> bool:
        """
        takes a list of vertex indices and returns True if the sequence of vertices represents a valid path in the graph
        """

        vertices = self.get_vertices()
        deq = deque(path)

        while len(deq) > 0:
            src = deq.popleft()
            if src not in vertices or (len(deq) > 0 and self.adj_matrix[src][deq[0]] == 0):
                return False

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        performs a depth-first search (DFS) in the graph and returns a list of vertices
        visited during the search, in the order they were visited
        """

        visited = []
        stack = deque()

        stack.append(v_start)

        while len(stack) > 0:
            v = stack.pop()
            if v == v_end:
                break

            if v not in visited:
                visited.append(v)
                for u in range(len(self.adj_matrix[v])-1, -1, -1):
                    if self.adj_matrix[v][u] != 0:
                        stack.append(u)

        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        performs a breadth-first search (BFS) in the graph and returns a list of vertices
        visited during the search, in the order they were visited
        """

        visited = []
        queue = deque()

        queue.append(v_start)

        while len(queue) > 0:
            v = queue.popleft()
            if v == v_end:
                break

            if v not in visited:
                visited.append(v)
                for u in range(len(self.adj_matrix[v])):
                    if self.adj_matrix[v][u] != 0:
                        queue.append(u)

        return visited

    def get_connected_components(self):
        """
        Return a list of connected components (sets)
        """

        visited = set()
        connected_components = []
        for src in range(len(self.adj_matrix)):
            if len(connected_components) == 0 or src not in visited:
                component = set(self.bfs(src))
                connected_components.append(component)
                visited = visited | component

        return connected_components

    def has_cycle(self):
        """
        returns True if there is at least one cycle in the graph. If the graph is acyclic,
        the method returns False
        """

        components = self.get_connected_components()

        for c in components:
            visited = []
            stack = deque()

            vertex = c.pop()
            c.add(vertex)

            stack.append(vertex)

            while len(stack) > 0:
                v = stack.pop()

                visited.append(v)
                for u in c:
                    if self.adj_matrix[v][u] != 0:
                        if u not in visited:
                            stack.append(u)
                        else:
                            for w in range(len(self.adj_matrix[u])):
                                if self.adj_matrix[u][w] != 0:
                                    if w in visited:
                                        return True

        return False

    def dijkstra(self, src: int) -> []:
        """
        Return list of shortest paths from src to each other node in the graph.
        """

        visited = {_: float('inf') for _ in range(self.v_count)}
        heap = []

        heapq.heappush(heap, [0, src])

        while len(heap) > 0:
            v = heapq.heappop(heap)
            dist = v[0]
            val = v[1]

            if dist < visited[val]:
                visited[val] = dist

                for u in range(len(self.adj_matrix[val])):
                    if u != src and self.adj_matrix[val][u] != 0:
                        heapq.heappush(heap, [dist + self.adj_matrix[val][u], u])

        shortest_paths = [_ for _ in visited.values()]
        return shortest_paths

if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
