class Graph:
    def __init__(self):
        self.graphs = {}
       
    def add_vertex(self, vertex):
        if vertex not in self.graphs:
            self.graphs[vertex] = []
    
    def add_edges(self, vertex1, vertex2):
        if vertex1 in self.graphs and vertex2 in self.graphs:
            if vertex2 not in self.graphs[vertex1]:
                self.graphs[vertex1].append(vertex2)
            if vertex1 not in self.graphs[vertex2]:
                self.graphs[vertex2].append(vertex1)

    def delete_vertex(self, vertax):
        if vertax in self.graphs:
            for neighbour in self.graphs[vertax]:
                self.graphs[vertax].remove(neighbour)
            del self.graphs[vertax]

    def delete_edge(self, vertax1, vertax2):
        if vertax1 in self.graphs[vertax2]:
            self.graphs[vertax2].remove(vertax1)
        if vertax2 in self.graphs[vertax1]:
            self.graph[vertax1].remove(vertax2)
                
    def dfs(self, start):
        if start not in self.graphs:
            return set()
        visited = set()
        stack = [start]
        while stack:
            print('STACK', stack)
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print((self.graphs[vertex]),'Vrtex', vertex, 'Visited', visited)
                stack.extend(set(self.graphs[vertex])-visited)
                
        return visited
    
    def bfs(self, start):
        if start not in self.graphs:
            return set()
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(set(self.graphs[vertex]) - visited)
        return visited
    
    def graph_print(self):
        print (self.graphs)
        

graph = Graph()
arr = [1,2,3,4,5]
for i in arr:
    graph.add_vertex(i)

edges = [(0, 1), (0, 3), (1, 4), (1, 2), (2, 5), (3, 4), (4, 5)]
for i in edges:
    graph.add_edges(i[0],i[1])

graph.graph_print()
print(graph.dfs(5))
print(graph.bfs(5))
graph.graph_print()
