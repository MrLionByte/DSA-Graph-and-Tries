class Graph:
    def _init_(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                self.graph[neighbor].remove(vertex)
            del self.graph[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def dfs(self,start):
        if start not in self.graph:
            return set() 
        visited = set()
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(set(self.graph[vertex]) - visited)
        return visited

    def bfs(self, start):
        if start not in self.graph:
            return set() 
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(set(self.graph[vertex]) - visited)
        return visited 
    
    '''def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=' ')
                queue.extend(set(self.graph[vertex]) - visited)
        return visited'''
    
    def _str_(self):
        result = ""
        for vertex in self.graph:
            neighbors = ', '.join(map(str, self.graph[vertex]))  # This line
            result += f"{vertex} -> {neighbors}\n"
        return result


g = Graph()
vertices = [0, 1, 2, 3, 4, 5]
for v in vertices:
    g.add_vertex(v)

edges = [(0, 1), (0, 3), (1, 4), (1, 2), (2, 5), (3, 4), (4, 5)]
for edge in edges:
    g.add_edge(edge[0], edge[1])

print("Graph Representation:")
print(g)

print("BFS Traversal Starting from Vertex 0:")
print(g.bfs(0))