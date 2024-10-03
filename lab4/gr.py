import heapq

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.f_n = 0

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.adj[u].append(Edge(v, weight))
        self.adj[v].append(Edge(u, weight))

    def a_star_search(self, start, goal, index_to_city, heuristic):
        visited = set()
        path = [start]
        total_cost = 0
        current = start

        while current != goal:
            visited.add(current)

            shortest = None
            for edge in self.adj[current]:
                if edge.vertex not in visited:
                    edge.f_n = edge.weight + heuristic[index_to_city[edge.vertex]]
                    if shortest is None or edge.f_n < shortest.f_n:
                        shortest = edge

            if shortest is None:
                print("Zam bhgui")
                return

            total_cost += shortest.weight
            path.append(shortest.vertex)
            current = shortest.vertex

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

def euclidean_distance():
    return {
        'Arad': 366,
        'Bucharest': 0,
        'Craiova': 160,
        'Drobeta': 242,
        'Eforie': 161,
        'Fagaras': 176,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 380,
        'Pitesti': 100,
        'Rimnicu': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374
    }
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
heuristic = euclidean_distance()

for city1, city2, weight in city_data:
    g.add_edge(city_to_index[city1], city_to_index[city2], weight)

start_city = 'Arad'
goal_city = 'Bucharest'

print('A* Search:')
g.a_star_search(city_to_index[start_city], city_to_index[goal_city], index_to_city, heuristic)
