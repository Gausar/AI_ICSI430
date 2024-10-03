from collections import deque
import heapq
class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.adj[u].append(Edge(v, weight))
        self.adj[v].append(Edge(u, weight))

    def BFS(self, start, goal):
        visited = [False] * self.V
        queue = deque([(start, [start], 0)])

        while queue:
            s, path, cost = queue.popleft() 

            if s == goal: 
                path_cities = [index_to_city[i] for i in path]
                print(f"zam: {path_cities}")
                print(f"Niit zamiin urt: {cost}")
                return

            if not visited[s]:
                visited[s] = True

                for edge in self.adj[s]:
                    if not visited[edge.vertex]:
                        new_path = path + [edge.vertex]
                        new_cost = cost + edge.weight
                        queue.append((edge.vertex, new_path, new_cost))

        print("Zam oldsongui")

    def DFS(self, start, goal, index_to_city):
            stack = [(start, [start], 0)]
            visited = set()

            while stack:
                s, path, cost = stack.pop()

                if s == goal:
                    path_cities = [index_to_city[i] for i in path]
                    print(f"zam: {path_cities}")
                    print(f"Niit zamiin urt: {cost}")
                    return

                if s not in visited:
                    visited.add(s)

                    for edge in self.adj[s]:
                        if edge.vertex not in visited:
                            new_path = path + [edge.vertex]
                            new_cost = cost + edge.weight
                            stack.append((edge.vertex, new_path, new_cost))
            print("Zam oldsongui")
            
    def UCS(self, start, goal, index_to_city):
        visited = set()
        path = [start]
        total_cost = 0

        current = start

        while current != goal:
            visited.add(current)

            shortest_edge = None
            for edge in self.adj[current]:
                if edge.vertex not in visited:
                    if shortest_edge is None or edge.weight < shortest_edge.weight:
                        shortest_edge = edge

            if shortest_edge is None:
                print("Zam bhgui")
                return

            total_cost += shortest_edge.weight
            path.append(shortest_edge.vertex)
            current = shortest_edge.vertex

        path_in_cities = [index_to_city[i] for i in path]
        print(f"zam: {path_in_cities}")
        print(f"Niit zamiin urt: {total_cost}")


def city_index_map(cities):
    city_to_index = {}
    index_to_city = {}
    idx = 0
    for city1, city2, _ in cities:
        if city1 not in city_to_index:
            city_to_index[city1] = idx
            index_to_city[idx] = city1
            idx += 1
        if city2 not in city_to_index:
            city_to_index[city2] = idx
            index_to_city[idx] = city2
            idx += 1
    return city_to_index, index_to_city

city_data = [
    ('Arad', 'Zerind', 75),
    ('Arad', 'Sibiu', 140),
    ('Arad', 'Timisoara', 118),
    ('Zerind', 'Oradea', 71),
    ('Oradea', 'Sibiu', 151),
    ('Sibiu', 'Fagaras', 99),
    ('Sibiu', 'Rimnicu', 80),
    ('Timisoara', 'Lugoj', 111),
    ('Timisoara', 'Mehadia', 70),
    ('Fagaras', 'Bucharest', 211),
    ('Rimnicu', 'Pitesti', 97),
    ('Rimnicu', 'Craiova', 146),
    ('Lugoj', 'Mehadia', 70),
    ('Mehadia', 'Drobeta', 75),
    ('Bucharest', 'Urziceni', 85),
    ('Bucharest', 'Giurgiu', 90),
    ('Bucharest', 'Pitesti', 101),
    ('Pitesti', 'Craiova', 138),
    ('Craiova', 'Drobeta', 120),
    ('Urziceni', 'Vaslui', 142),
    ('Urziceni', 'Hirsova', 98),
    ('Vaslui', 'Iasi', 92),
    ('Hirsova', 'Eforie', 86),
    ('Iasi', 'Neamt', 87)
]

city_to_index, index_to_city = city_index_map(city_data)

g = Graph(len(city_to_index))

for city1, city2, weight in city_data:
    g.add_edge(city_to_index[city1], city_to_index[city2], weight)

start_city = 'Arad'
goal_city = 'Bucharest'
print('BFS : ')
g.BFS(city_to_index[start_city], city_to_index[goal_city])
print('DFS:')
g.DFS(city_to_index[start_city], city_to_index[goal_city], index_to_city)
print('UCS:')
g.UCS(city_to_index[start_city], city_to_index[goal_city], index_to_city)
