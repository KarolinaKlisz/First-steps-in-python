class Graph:

    def __init__(self, graph=None):  # inicjalizacja grafu
        if graph is None:
            graph = {}
        self.graph = graph

    def print_graph(self):  # wydrukowanie grafu
        print("Graph: ", self.graph)

    def all_vertices(self):  # pokazuje tylko wierzchołki czyli klucze
        print("Vertices: ", set(self.graph.keys()))

    def add_vertex(self, vertex):  # dodajemy wierzchołek, jeśli go jeszcze nie ma
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print("Vertex already exists.")

    def remove_vertex(self, vertex):
        graf1 = []  # zmienna pomocnicza do przechowywania wartości
        for key, values in self.graph.items():
            graf1 = values
            if vertex in graf1:
                graf1.remove(vertex)
            self.graph[key] = graf1

        self.graph.pop(vertex)
        print("Vertex", vertex, "has been removed.")

    def add_edge(self, vertex1, vertex2):  # dodanie krawędzi między wierzchołkami/dodanie sąsiada
        if vertex1 not in self.graph:
            self.graph[vertex1] = []
        if vertex2 not in self.graph:
            self.graph[vertex2] = []
        if vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)

    def remove_edge(self, vertex1, vertex2):  # usuwa krawędzie między dwoma wierzchołkami
        for key, values in self.graph.items():
            graf1 = values
            if key == vertex1:
                graf1.remove(vertex2)
                self.graph[key] = graf1

            if key == vertex2:
                graf1.remove(vertex1)
                self.graph[key] = graf1

        # if self.graph[vertex1] == []:  //jeśli wierzchołek jest liściem to go usuwamy
        # self.graph.pop(vertex1)

        # if self.graph[vertex2] == []:
        #  self.graph.pop(vertex2)

        print("Edge between", vertex1, "and", vertex2, "has been removed.")

    def all_edges(self):  # wypisuje wszystkie krawędzie jakie już są w tym grafie
        edges = []
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        print("Edges: ", edges)

    def print_neighbours(self, vertex):
        neighbours = []
        for i in self.graph[vertex]:
            neighbours.append(i)
        print("Neighbours of vertex", vertex, ": ", neighbours)

    def bfs(self, root):
        queue = []
        visited = [root]
        queue.append(root)
        while queue:
            remove = queue.pop(0)
            for node in self.graph[remove]:
                if node not in visited:
                    visited.append(node)
                    queue.append(node)
        return visited

    def dfs(self, root, visited=None):
        if visited is None:
            visited = []
        visited.append(root)
        if root in self.graph:
            for node in self.graph[root]:
                if node not in visited:
                    self.dfs(node, visited)
            return visited


class GraphIteratorBFS:
    def __init__(self, graph):
        self.graph = graph

    def __next__(self):
        try:
            return self.graph
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


class GraphIteratorDFS:
    def __init__(self, graph):
        self.graph = graph

    def __next__(self):
        try:
            return self.graph
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    graf = Graph()
    graf.add_vertex(1)
    graf.add_vertex(2)
    graf.add_vertex(3)
    graf.add_vertex(4)
    graf.add_vertex(5)
    graf.add_vertex(6)
    graf.add_vertex(6) #próba ponownego dodania wierzchołka
    graf.print_graph()

    graf.add_edge(1, 3)
    graf.add_edge(1, 2)
    graf.add_edge(2, 4)
    graf.add_edge(2, 5)
    graf.add_edge(3, 4)
    graf.add_edge(4, 6)
    graf.print_graph()

    graf.all_vertices()
    graf.all_edges()

    graf.remove_edge(2, 5)
    graf.remove_vertex(5)

    graf.print_graph()
    graf.all_vertices()
    graf.all_edges()
    graf.print_neighbours(2)
    print("----BFS----")
    for vertex in graf.bfs(1):
        print(vertex)

    print("----DFS----")
    for vertex in graf.dfs(2):
        print(vertex)